# <img src="https://cdn-icons-png.flaticon.com/512/2954/2954885.png" width="45" alt="SentimentSleuth"> SentimentSleuth

Welcome to the **SentimentSleuth** repository! This project is a Python-based sentiment analysis tool that classifies text as positive, negative, or neutral. Using NLP techniques and machine learning, it processes data, extracts features, trains models, and evaluates performance. Ideal for analyzing feedback and social media sentiment.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/) [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![TextBlob](https://img.shields.io/badge/TextBlob-0277BD?style=for-the-badge&logo=data:image/png;base64)](https://textblob.readthedocs.io/en/dev/)

---

## Table of Contents
- [About The Project](#about-the-project)
  - [User Interface](#user-interface)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## About The Project

SentimentSleuth is designed to analyze textual data and classify it into three categories - positive, negative, or neutral. It leverages **Natural Language Processing (NLP)** using **TextBlob** and provides an intuitive interface for user interaction, allowing seamless analysis of user-provided text.

### User Interface

<br>
<p align="center">
  <img src="/assets/sentimentsleuth-readme-preview.png" alt="SentimentSleuth Demo" width="700">
</p>

- Intuitive web interface powered by **Flask**.
- Clean, minimal design styled with custom CSS.
- Real-time analysis for quick insights.

---

### Built With
- **[Python](https://www.python.org/)** - Core language.
- **[Flask](https://flask.palletsprojects.com/)** - Web framework for serving the application.
- **[TextBlob](https://textblob.readthedocs.io/en/dev/)** - NLP library for sentiment analysis.
- **HTML5/CSS3** - Frontend structure and styling.

---

## Getting Started

Follow the steps below to set up SentimentSleuth on your local machine.

### Prerequisites
Ensure you have the following installed:
- **Python 3.12+** ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gayanukabulegoda/SentimentSleuth.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd SentimentSleuth
   ```

3. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\\Scripts\\activate'
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Visit the app in your browser**
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Enter text in the input field on the homepage.
2. Click "Analyze Sentiment" to get an instant analysis.
3. View the classification (Positive, Negative, Neutral) and re-analyze as needed.
4. Use the "Back" button to analyze another text.

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

<p align="center">
  &copy; 2025 Gayanuka Bulegoda
</p>

