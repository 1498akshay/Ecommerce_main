
# import sqlite3

# # Connect to SQLite database
# connection = sqlite3.connect('ECOMMERCE.db')
# cursor = connection.cursor()

# # Create table for e-commerce data
# table_info = """
# CREATE TABLE ORDER_TABLE (
#     OrderID VARCHAR(10),
#     CustomerName VARCHAR(25),
#     ProductID VARCHAR(10),
#     Category VARCHAR(25),
#     Price REAL,
#     Quantity INT
# );
# """
# cursor.execute(table_info)

# # Insert 25 rows of e-commerce data
# records = [
#     ('O001', 'Alice', 'P001', 'Electronics', 199.99, 1),
#     ('O002', 'Bob', 'P002', 'Clothing', 29.99, 2),
#     ('O003', 'Charlie', 'P003', 'Books', 15.99, 3),
#     ('O004', 'Diana', 'P004', 'Electronics', 499.99, 1),
#     ('O005', 'Eve', 'P005', 'Home', 89.99, 2),
#     ('O006', 'Frank', 'P006', 'Beauty', 19.99, 5),
#     ('O007', 'Grace', 'P007', 'Clothing', 49.99, 1),
#     ('O008', 'Hank', 'P008', 'Books', 9.99, 4),
#     ('O009', 'Ivy', 'P009', 'Electronics', 299.99, 1),
#     ('O010', 'Jack', 'P010', 'Home', 59.99, 3),
#     ('O011', 'Karen', 'P011', 'Beauty', 25.99, 2),
#     ('O012', 'Leo', 'P012', 'Clothing', 39.99, 1),
#     ('O013', 'Mia', 'P013', 'Books', 12.99, 5),
#     ('O014', 'Nina', 'P014', 'Electronics', 149.99, 2),
#     ('O015', 'Oscar', 'P015', 'Home', 79.99, 1),
#     ('O016', 'Paul', 'P016', 'Beauty', 29.99, 3),
#     ('O017', 'Quincy', 'P017', 'Clothing', 59.99, 2),
#     ('O018', 'Rachel', 'P018', 'Books', 8.99, 6),
#     ('O019', 'Steve', 'P019', 'Electronics', 399.99, 1),
#     ('O020', 'Tina', 'P020', 'Home', 99.99, 2),
#     ('O021', 'Uma', 'P021', 'Beauty', 22.99, 4),
#     ('O022', 'Victor', 'P022', 'Clothing', 44.99, 1),
#     ('O023', 'Wendy', 'P023', 'Books', 10.99, 3),
#     ('O024', 'Xander', 'P024', 'Electronics', 249.99, 1),
#     ('O025', 'Yara', 'P025', 'Home', 69.99, 2)
# ]

# # Insert records into the table
# cursor.executemany('INSERT INTO ORDER_TABLE VALUES (?, ?, ?, ?, ?, ?)', records)

# # Commit the transaction
# connection.commit()

# # Verify the data
# cursor.execute('SELECT * FROM ORDER_TABLE')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Close the connection
# connection.close()

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('ECOMMERCE.db')
cursor = connection.cursor()

# Create table for product data
product_table_info = """
CREATE TABLE PRODUCT_TABLE (
    ProductID VARCHAR(10) PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(25),
    Price REAL,
    Stock INT
);
"""
cursor.execute(product_table_info)

# Insert data into PRODUCT_TABLE
product_records = [
    ('P001', 'Smartphone', 'Electronics', 199.99, 50),
    ('P002', 'T-Shirt', 'Clothing', 29.99, 100),
    ('P003', 'Novel', 'Books', 15.99, 200),
    ('P004', 'Laptop', 'Electronics', 499.99, 30),
    ('P005', 'Vacuum Cleaner', 'Home', 89.99, 40),
    ('P006', 'Lipstick', 'Beauty', 19.99, 150),
    ('P007', 'Jacket', 'Clothing', 49.99, 60),
    ('P008', 'Notebook', 'Books', 9.99, 300),
    ('P009', 'Tablet', 'Electronics', 299.99, 25),
    ('P010', 'Lamp', 'Home', 59.99, 50),
    ('P011', 'Moisturizer', 'Beauty', 25.99, 80),
    ('P012', 'Jeans', 'Clothing', 39.99, 70),
    ('P013', 'Magazine', 'Books', 12.99, 120),
    ('P014', 'Camera', 'Electronics', 149.99, 15),
    ('P015', 'Cookware Set', 'Home', 79.99, 35),
    ('P016', 'Shampoo', 'Beauty', 29.99, 110),
    ('P017', 'Sweater', 'Clothing', 59.99, 45),
    ('P018', 'Comic Book', 'Books', 8.99, 250),
    ('P019', 'Monitor', 'Electronics', 399.99, 20),
    ('P020', 'Chair', 'Home', 99.99, 30),
    ('P021', 'Perfume', 'Beauty', 22.99, 90),
    ('P022', 'Hat', 'Clothing', 44.99, 75),
    ('P023', 'Guide Book', 'Books', 10.99, 180),
    ('P024', 'Headphones', 'Electronics', 249.99, 40),
    ('P025', 'Blanket', 'Home', 69.99, 50)
]

# Insert records into PRODUCT_TABLE
cursor.executemany('INSERT INTO PRODUCT_TABLE VALUES (?, ?, ?, ?, ?)', product_records)

# Commit the transaction
connection.commit()

# Verify the data
cursor.execute('SELECT * FROM PRODUCT_TABLE')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()
