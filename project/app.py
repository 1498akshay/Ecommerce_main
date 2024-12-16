from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import chatbot
import pipeline

app = Flask(__name__)

def get_students():
    """Fetch all students from the SQLite database."""
    connection = sqlite3.connect('ECOMMERCE.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ORDER_TABLE")
    students = cursor.fetchall()
    connection.close()
    return students

@app.route('/')
def index():
    """Route to display students on the web page."""
    students = get_students()
    print(students)
    return render_template('index.html', students=students)

@app.route('/product_info', methods=['GET', 'POST'])
def product_info():
    if request.method == 'POST':
        product_id = request.form.get('title')  # Fetching the input value
        search_type = request.form.get('search_type')  # Determines the search criteria
        
        connection = sqlite3.connect('ECOMMERCE.db')
        cursor = connection.cursor()
        
        # Query based on the search type
        if search_type == 'marks':
            cursor.execute("SELECT * FROM PRODUCT_TABLE WHERE ProductID = ?", (product_id,))
            students = cursor.fetchall()
            print(students)
            connection.close()


        elif search_type == 'section':
            students = pipeline.main_pipeline(product_id,chatbot.PRODUCT_TABLE_prompt,  "ECOMMERCE.db")
            # response = chatbot.get_gemini_response(product_id,chatbot.PRODUCT_TABLE_prompt)
            # print(response)
            # students= chatbot.read_sql_query(response,"ECOMMERCE.db")
            connection.close()

        
        # Displaying the results on the template

        return render_template('product.html', students=students)
    
    # Default GET response
    return render_template('product.html')





@app.route('/show', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        product_id = request.form.get('title')  # Fetching the input value
        search_type = request.form.get('search_type')  # Determines the search criteria
        
        connection = sqlite3.connect('ECOMMERCE.db')
        cursor = connection.cursor()
        
        # Query based on the search type
        if search_type == 'marks':
            cursor.execute("SELECT * FROM ORDER_TABLE WHERE OrderID = ?", (product_id,))
            students = cursor.fetchall()
            print(students)
            connection.close()


        elif search_type == 'section':
            students = pipeline.main_pipeline(product_id,chatbot.ORDER_TABLE_prompt,  "ECOMMERCE.db")
            # response = chatbot.get_gemini_response(product_id,chatbot.ORDER_TABLE_prompt)
            
            # students= chatbot.read_sql_query(response,"ECOMMERCE.db")
            connection.close()

        
        # Displaying the results on the template

        return render_template('order.html', students=students)
    
    # Default GET response
    return render_template('order.html')

@app.route('/other')
def other():
    return render_template('other.html')

@app.route('/offer')
def offer():
    return "this is offer page"

@app.route('/highestsold')
def highestsold():
    product_id = request.form.get('title')  # Fetching the input value
    search_type = request.form.get('search_type')  # Determines the search criteria
    connection = sqlite3.connect('ECOMMERCE.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ORDER_TABLE WHERE quantity = ( SELECT MAX(quantity)FROM ORDER_TABLE)")
    students = cursor.fetchall()
    connection.close()

    return f"{students}"

@app.route('/highestprice')
def highestprice():
    product_id = request.form.get('title')  # Fetching the input value
    search_type = request.form.get('search_type')  # Determines the search criteria
    connection = sqlite3.connect('ECOMMERCE.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM PRODUCT_TABLE WHERE Price = (SELECT MAX(Price)FROM PRODUCT_TABLE)")
    students = cursor.fetchall()
    connection.close()

    return f"{students}"


if __name__ == "__main__":
    app.run(debug=True, port=8000)