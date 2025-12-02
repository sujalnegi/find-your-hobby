import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
import numpy as np
from flask import Flask, render_template
from flask_cors import CORS
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("server.log"),
    logging.StreamHandler()
])
logger = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve().parent
HOBBIES_PATH = BASE_DIR / "hobbies.json"
EMB_PATH = BASE_DIR / "hobby_emb.npy"
DOCS_PATH = BASE_DIR / "hobby_docs.json"
MODEL_NAME = "all-MiniLM-L6-v2"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


class Answers(BaseModel):
    interest: Optional[str] = ""
    environment: Optional[str] = "both"
    physical: Optional[str] = "low"
    creative: Optional[str] = "no"
    social: Optional[str] = "either"
    budget: Optional[str] = "low"
    time: Optional[str] = "medium"

class AppState:
    def __init__(self):
        self.hobbies: List[Dict[str, Any]] = []
        self.model = None
        self.hobby_embeddings: Optional[np.ndarray] = None
        self.hobby_docs: List[str] = []

    def load_hobbies(self):
        try:
            if not HOBBIES_PATH.exists():
                logger.error(f"Hobbies file not found at {HOBBIES_PATH}")
                self.hobbies = []
                return

            with open(HOBBIES_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)

            self.hobbies = []
            if isinstance(raw, list):
                for item in raw:
                    if isinstance(item, dict):
                        self.hobbies.append(item)
                    elif isinstance(item, list):
                        for sub in item:
                            if isinstance(sub, dict):
                                self.hobbies.append(sub)
            elif isinstance(raw, dict):
                self.hobbies = [raw]
            
            logger.info(f"Loaded {len(self.hobbies)} hobbies.")

        except Exception as e:
            logger.error(f"Failed to load hobbies: {e}")
            self.hobbies = []

    def build_docs(self) -> List[str]:
        out = []
        for h in self.hobbies:
            parts = [h.get("name", ""), h.get("short", "")] + h.get("interests", [])
            txt = " | ".join([str(x) for x in parts if x])
            out.append(txt)
        return out

    def load_or_build_embeddings(self):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(MODEL_NAME)
            
            if EMB_PATH.exists() and DOCS_PATH.exists():
                try:
                    mats = np.load(str(EMB_PATH))
                    with open(DOCS_PATH, "r", encoding="utf-8") as f:
                        docs = json.load(f)
                    
                    if len(docs) == len(self.hobbies) and mats.shape[0] == len(self.hobbies):
                        self.hobby_embeddings = mats
                        self.hobby_docs = docs
                        logger.info("Loaded cached embeddings.")
                        return
                except Exception as e:
                    logger.warning(f"Failed to load cached embeddings, rebuilding: {e}")

            logger.info("Building new embeddings...")
            self.hobby_docs = self.build_docs()
            if not self.hobby_docs:
                 logger.warning("No documents to embed.")
                 self.hobby_embeddings = None
                 return

            self.hobby_embeddings = self.model.encode(self.hobby_docs, convert_to_numpy=True, show_progress_bar=False)
            
            np.save(str(EMB_PATH), self.hobby_embeddings)
            with open(DOCS_PATH, "w", encoding="utf-8") as f:
                json.dump(self.hobby_docs, f, ensure_ascii=False, indent=2)
            logger.info("Embeddings built and saved.")

        except Exception as e:
            logger.error(f"Failed to initialize embeddings: {e}")
            self.hobby_embeddings = None
            self.hobby_docs = []

state = AppState()

def safe_float(x: Any, default: float = 0.0) -> float:
    try:
        if x is None:
            return default
        return float(x)
    except (ValueError, TypeError):
        return default

@app.route("/")
def index():
    return render_template("index.html")

state.load_hobbies()
state.load_or_build_embeddings()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=False)
