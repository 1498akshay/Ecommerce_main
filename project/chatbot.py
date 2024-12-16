from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

# def read_sql_query(sql,db):
#     conn=sqlite3.connect(db)
#     cur=conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows
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
        return []
## Define Your Prompt
ORDER_TABLE_prompt=[
    """
You are an expert in converting English questions to SQL query!
The SQL database has the name ORDER_TABLE and has the following columns - OrderID, CustomerName, ProductID, Category, Price, Quantity.

For example:
Example 1 - How many orders are present?
The SQL command will be something like this:
SELECT COUNT(*) FROM ORDER_TABLE;

Example 2 - Show all orders in the Electronics category.
The SQL command will be something like this:
SELECT * FROM ORDER_TABLE WHERE LOWER(Category) = 'electronics';

Note: Ensure that the queries are case-insensitive by using functions like LOWER() where applicable. Do not include ``` or the word "SQL" in the output.


    """


]

PRODUCT_TABLE_prompt = [
    """
You are an expert in converting English questions to SQL query!
The SQL database has the name PRODUCT_TABLE and has the following columns - ProductID, ProductName, Category, Price, Stock.

For example:
Example 1 - How many products are in the database?
The SQL command will be something like this:
SELECT COUNT(*) FROM PRODUCT_TABLE;

Example 2 - Show all products in the Electronics category.
The SQL command will be something like this:
SELECT * FROM PRODUCT_TABLE WHERE LOWER(Category) = 'electronics';

Note: Ensure that the queries are case-insensitive by using functions like LOWER() where applicable. Do not include ``` or the word "SQL" in the output.
    """
]


# question="give me section books"

# response=get_gemini_response(question,prompt)


# response=read_sql_query(response,"ECOMMERCE.db")

# print(response)