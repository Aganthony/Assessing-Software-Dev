import csv
import sqlite3

# Open the csv file and read its contents into a list of tuples
with open('customers.csv', newline='', encoding='ISO-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    customers = [tuple(row) for row in reader]

# Connect to the chinook.db database and insert the data into the customers table
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()
cursor.executemany(
    "INSERT INTO customers (Company, FirstName, LastName, Address, City, PostalCode, Country, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", customers)
conn.commit()
conn.close()
