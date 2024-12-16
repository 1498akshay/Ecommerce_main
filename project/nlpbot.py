import spacy
import re
import sqlite3

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define the default table
DEFAULT_TABLE = "ORDER_TABLE"

# Function to process user input and extract conditions
def extract_condition(user_input):
    """Extract conditions like 'price less than 5000' or 'quantity equals 5'."""
    doc = nlp(user_input.lower())  # Process the input with SpaCy

    condition = []
    
    # Define key condition phrases and their SQL equivalents
    condition_keywords = {
        "is": "=",
        "equals": "=",
        "equal to": "=",
        "less than": "<",
        "greater than": ">",
        "greater": ">",
        "below": "<",
        "above": ">",
        "and": "AND",
        "or": "OR"
    }
    Column_headings = {
    'orderid':'OrderID',
    'customername':'CustomerName' ,
    'productid':'ProductID',
    'category':'Category',
    'price':'Price',
    'quantity':'Quantity',
    'productname':'ProductName',
    'price':'Price',
    'stock':'Stock' }

    for token in doc:
        # Check for condition keywords
        if token.text in condition_keywords:
            condition.append(condition_keywords[token.text])
        # Extract numeric values and column names
        elif token.text in Column_headings:
            condition.append(f"LOWER({Column_headings[token.text]})")
        elif token.pos_ == "NUM" or token.pos_ == "ADJ":
            condition.append(f"'{token.text}'")
        elif token.pos_ == "NOUN":
            condition.append(f"'{token.text}'")
        print(condition)

    return " ".join(condition)

# Function to generate SQL query
def generate_sql_query(user_input):
    """Generate a SELECT query based on the user's input."""
    condition = extract_condition(user_input)  # Extract condition from input
    
    # Construct SQL query
    if condition:
        query = f"SELECT * FROM {DEFAULT_TABLE} WHERE {condition};"
    else:
        query = None  # If no condition is extracted, return None

    return query

# # Function to execute SQL query
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error: {e}")
        return None

# # Fallback pipeline
# def fallback_pipeline(user_input):
#     """Handle cases where user input doesn't work in the primary pipeline."""
#     return "Sorry, I couldn't process your request. Please try rephrasing or provide more details."

# # Main chatbot logic
# def main_pipeline(user_input, db="ECOMMERCE.db"):
#     # Generate SQL query
#     sql_query = generate_sql_query(user_input)
    
#     if not sql_query:
#         # If SQL query is None, use fallback
#         return fallback_pipeline(user_input)

#     print(f"Generated SQL Query: {sql_query}")
#     result = read_sql_query(sql_query, db)
#     if result:
#         return result
#     else:
#         return fallback_pipeline(user_input)

# # Example interaction

# # user_input = "skjknskj"

# # response = main_pipeline(user_input)
# # print(f"Chatbot: {response}")


