# 🚀 Automated Customer Sentiment Analyzer & Data Pipeline

This is an *End-to-End Data Pipeline* project that integrates Data Engineering, AI Automation, and SQL database management.

## 🎯 Project Goal
The goal of this project is to automate customer feedback analysis for businesses. The script automatically processes customer reviews, utilizes AI logic to classify sentiment (Positive, Negative, or Neutral), and saves the structured data in a SQL database for quick querying.

## 🛠️ Tech Stack Used
* *Python* (Core Logic)
* *Pandas* (Data Transformation)
* *SQLite3* (SQL Database Management)
* *Sentiment Rule-Engine* (AI Automation)

## 📊 How It Works
1. *Extract:* Customer review text data is loaded into Python.
2. *Transform (AI Automation):* A Python-based rule engine automatically reads and classifies the sentiment of each review.
3. *Load:* The enriched, classified data is saved into a local SQL database (ai_database.db).
4. *SQL Query:* We query the database to instantly filter and display only the "Negative" reviews so the support team can take action.

## 💻 How to Run This Project
1. Clone this repository.
2. Open the code in Spyder or any Python IDE.
3. Run main.py to see the automated SQL output.
