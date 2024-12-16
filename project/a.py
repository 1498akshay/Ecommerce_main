# # create_tables.py
# from app import app, db

# # Initialize app context and create tables
# with app.app_context():
#     db.create_all()
# Start the chatbot
import sqlite3
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows
response = 'SELECT * FROM products WHERE red colour'
read_sql_query(response,"ECOMMERCE.db")