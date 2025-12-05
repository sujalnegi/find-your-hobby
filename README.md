# Find Your Hobby 
<div align="center">
  <img src="static/logo.svg" alt="Find Your Hobby Logo" width="600"/>

**Find Your Hobby is an intelligent web application built with Flask and synthetic dataset that helps users discover their perfect hobby based on their interests, personality, and lifestyle preferences.**

</div>

## Features

* **Smart Recommendation Engine:**
    * **Vector-Based Matching:** Utilizes advanced vector similarity algorithms to match user inputs against a comprehensive synthetic dataset of hobbies.
    * **Hybrid Scoring System:** Combines semantic similarity with rule-based filtering (budget, time, social preference) for highly accurate suggestions.
* **Comprehensive Filtering:**
    * **Interest Analysis:** Analyzes free-text interest inputs (e.g., "Space", "Art", "Outdoor") to find relevant activities.
    * **Lifestyle Alignment:** Filters hobbies based on:
        * **Environment:** Indoor vs. Outdoor
        * **Intensity:** Physical exertion levels
        * **Social Mode:** Solo vs. Group activities
        * **Budget:** Low to High cost requirements
        * **Time Commitment:** Weekly hour availability
* **User-Friendly Interface:**
    * A modern, responsive UI with glassmorphism effects and particle animations.
    * Real-time "Initiate Scan" feedback.
    * Detailed hobby cards showing "Why it Fits", "How to Start", and a compatibility score.

## Demo & Deployment

* **Live Deployment:** [Click Here to Visit](https://fyb-api.onrender.com/)
* **Demo Video:** [Watch on Google Drive](https://drive.google.com/file/d/1zetQSRrrh_wsWW7xvd4t9x3C2mohl-JC/view?usp=drive_link)

## Technologies Used

* **Backend:** Python, Flask
* **ML & Data:** Sentence Transformers, NumPy, SciPy (Cosine Distance)
* **Data Validation:** Pydantic
* **Frontend:** HTML5, CSS3 (Animations, Glassmorphism), JavaScript (Vanilla)
* **Deployment:** Render (Gunicorn)

## Local Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### 2. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/find-your-hobby.git
cd find-your-hobby
```

### 3. Create a Virtual Environment

just to look cool add a virtual environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install all the required Python libraries using `pip`.

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Once the setup is complete, start the Flask server:

```bash
python main.py
```

Now, open your web browser and navigate to the following address:

```
http://127.0.0.1:8001/
```

You should see the **Find Your Hobby** application running!

## How to Use

1. **Enter Your Interest:** Type a keyword like "Travel", "Coding", or "Music".
2. **Set Preferences:** Adjust the dropdowns for Environment, Intensity, Creativity, Social Mode, Budget, and Time.
3. **Initiate Scan:** Click the **"INITIATE SCAN"** button to let the AI analyze your profile.
4. **View Results:** The app will display the top 3 matching hobbies with a match score and personalized reasons why they fit you.
5. **Browse All:** Click **"BROWSE DATABASE"** to explore the full list of available hobbies.

## Author

- **Sujal Negi**

## Credits

* **Background Effects:** Inspired by [Prismic Blog - CSS Background Effects](https://prismic.io/blog/css-background-effects)
