🍛 ML Food Recommendation System

A machine learning-based food recommendation system that suggests food items based on customer order patterns using the Apriori algorithm. Built with Python and Flask, it features a full restaurant menu interface with a smart recommendation engine.
🧠 ML Features

Uses Apriori Algorithm for association rule mining
Analyzes 300 real restaurant transactions to find patterns
Recommends food items that are frequently ordered together

🌟 Features

🍽️ Interactive Menu — Browse food items with images
🤖 Smart Recommendations — Get AI-powered food suggestions
🛒 Cart System — Add items and place orders
📊 Transaction Dataset — Trained on real restaurant data

🛠️ Tech Stack

Language: Python
Backend: Flask
ML Algorithm: Apriori (Association Rule Mining)
Frontend: HTML, CSS
Dataset: CSV (300 restaurant transactions)

▶️ How to Run

Install dependencies:

   pip install flask mlxtend pandas

Run the app:

   python app.py

Open your browser and go to:

   http://localhost:5000
📁 Project Structure
ML_FOODRECOMMEND/
│
├── app.py                          # Main Flask application
├── apriori_module.py               # ML recommendation logic
├── menu.html                       # Menu page
├── dataset/
│   └── restaurant_transactions_300.csv   # Training data
└── static/
    └── images/                     # Food item images
