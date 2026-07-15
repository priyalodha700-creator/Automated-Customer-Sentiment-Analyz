mport pandas as pd
import sqlite3

# --- STEP 1: Raw Customer Review Data ---
data = {
    'Review_ID': [1, 2, 3],
    'Review_Text': [
        "This product is amazing and beautiful!",
        "Horrible experience, completely waste of money.",
        "It is okay, nothing special but works fine."
    ]
}
df = pd.DataFrame(data)

# --- STEP 2: AI Automation (Sentiment Classification) ---
# This function acts as our AI tool to read text and decide the mood
def ai_mood_analyzer(text):
    text_lower = text.lower()
    if "amazing" in text_lower or "beautiful" in text_lower or "good" in text_lower:
        return "Positive"
    elif "horrible" in text_lower or "waste" in text_lower or "bad" in text_lower:
        return "Negative"
    else:
        return "Neutral"

# AI automatically runs on all reviews and creates a new column
df['AI_Analysis'] = df['Review_Text'].apply(ai_mood_analyzer)
print("--- AI has successfully analyzed and classified all reviews! ---\n")


# --- STEP 3: Database Storage (SQL Load) ---
# Creating and connecting to SQLite database 'ai_database.db'
conn = sqlite3.connect('ai_database.db')
df.to_sql('customer_insights', conn, if_exists='replace', index=False)


# --- STEP 4: SQL Query (Filtering Negative Feedback) ---
# Querying the database to fetch only the unhappy customers
sql_query = "SELECT * FROM customer_insights WHERE AI_Analysis = 'Negative'"

# Extracting the results
unhappy_customers = pd.read_sql_query(sql_query, conn)

print("=== SQL Result: Unhappy Customer List for Support Team ===")
print(unhappy_customers)

# Closing the database connection
conn.close()
