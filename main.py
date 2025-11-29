import logging
from pathlib import Path
from flask import Flask, render_template
from flask_cors import CORS

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

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    logger.info("Starting server...")
    app.run(host="0.0.0.0", port=8001, debug=False)
