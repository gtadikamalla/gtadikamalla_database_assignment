#modify this module to include the function definitions
#Developed by :   Enter your name here
import sqlite3
import os
def create_database_file(file_name):
    try:
        conn = sqlite3.connect(file_name)
    except sqlite3.Error as e:
        print(e)
    else:
        print('Created the database file.')
        return conn
    
def create_rep_table(database_connectiion):
    #use the connection object to create the database table
    #Create a function that will create the rep table and add data to it. 
    #Use the data in sql_commands.txt to help you with it.
    pass
def create_customer_table(database_connectiion):
    #use the connection object to create the database table
    #Create a function that will create the customer table and add the data to it.
    # Use the data in sql_commands.txt to help you with it.
    pass
def insert_a_customer_record(database_connectiion):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    pass
def query_rep_table(database_connection):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    pass
def update_rep_table(database_connection):
    #Create a function that prompts the user for a rep number.  
    # Then use the rep number to update the rep commission if it is in the [0.0 to 0.20]  range
    pass
def delete_customer_record(database_connection):
    # Create a function that prompts the user for a customer number.  
    # if the customer number exists, confirm for deletion and 
    # then and delete then delete that customer 
    pass
def delete_database(file_name, database_connection):
    # Create a function that deletes the database.  Verify that the file exists. 
    # Close the connection.  Then confirm the user really wants to delete the file,  Then delete the file.
    pass
