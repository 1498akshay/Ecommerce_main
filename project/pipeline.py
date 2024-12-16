import chatbot
import nlpbot

# Main chatbot logic
def main_pipeline(user_input, prompt, db="ECOMMERCE.db" ):
    # Generate SQL query
    sql_query = nlpbot.generate_sql_query(user_input)
    
    if not sql_query:
        # If SQL query is None, use fallback
        response = chatbot.get_gemini_response(user_input,prompt)
        students= chatbot.read_sql_query(response,"ECOMMERCE.db")
        return students


    print(f"Generated SQL Query: {sql_query}")
    result = nlpbot.read_sql_query(sql_query, db)
    if result:
        return result
    else:
        response = chatbot.get_gemini_response(user_input,prompt)
        print(response)
        students= chatbot.read_sql_query(response,"ECOMMERCE.db")
        return students

# Example interaction

# user_input = "Category is Books"

# response = main_pipeline(user_input)
# print(f"Chatbot: {response}")
# response = "SELECT * FROM ORDER_TABLE WHERE LOWER(category) = 'books'"
# print(chatbot.read_sql_query(response,"ECOMMERCE.db"))