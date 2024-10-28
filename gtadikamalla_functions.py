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
    create_sql="""create table rep (rep_num char(2) primary key, last_name char(15), first_name char(15), street char(15), city char(15), state char(2),zip char(5), commission decimal(7,2), rate decimal(3,2))"""
    try:
        cursor=database_connectiion.cursor()
        cursor.execute(create_sql)
    except sqlite3.Error as e:
        print(e)
    else:
        print('Rep table is created')

    try:
        insert_sql=["insert into rep values ('20','Tadikamalla','Gangadhar','624 Randall','Grove','FL','33321',20542.50,0.05);",
"insert into rep values ('35','Hull','Richard','532 Jackson','Sheldon','FL','33553',39216.00,0.07);",
"insert into rep values ('65','Perez','Juan','1626 Taylor','Fillmore','FL','33336',23487.00,0.05);"]
        for query in insert_sql:
            cursor.execute(query)
            database_connectiion.commit()
    except sqlite3.Error as e:
        print(e)
    else:
        print('Alls rows are updated to rep table.')
    pass

def create_customer_table(database_connectiion):
    #use the connection object to create the database table
    #Create a function that will create the customer table and add the data to it.
    # Use the data in sql_commands.txt to help you with it.
    create_sql="""create table customer (customer_num char(3) primary key, customer_name char(35) not null, street char(15), city char(15), state char(2),
zip char(5), balance decimal(8,2), credit_limit decimal(8,2), rep_num char(2),FOREIGN KEY (rep_num) REFERENCES rep(rep_num));"""
    try:
        cursor=database_connectiion.cursor()
        cursor.execute(create_sql)
    except sqlite3.Error as e:
        print(e)
    else:
        print('Customer table is created')

    try:
        insert_sql=["insert into customer values ('148','Al''s Appliance and Sport','2837 Greenway','Fillmore','FL','33336',6550.00,7500.00,'20');",
"insert into customer values ('282','Brookings Direct','3827 Devon','Grove','FL','33321',431.50,10000.00,'35');",
"insert into customer values ('356','Ferguson''s','382  Wildwood','Northfield','FL','33146',5785.00,7500.00,'65');",
"insert into customer values ('408','The Everything Shop','1828 Raven','Crystal','FL','33503',5285.25,5000.00,'35');",
"insert into customer values ('462','Bargains Galore','3829  Central','Grove','FL','33321',3412.00,10000.00,'65');",
"insert into customer values ('524','Kline''s','838 Ridgeland','Fillmore','FL','33336',12762.00,15000.00,'20');",
"insert into customer values ('608','Johnson''s Department Store','372  Oxford','Sheldon','FL','33553',2106.00,10000.00,'65');",
"insert into customer values ('687','Lee''s Sport and Appliance','282 Evergreen','Altonville','FL','32543',2851.00,5000.00,'35');",
"insert into customer values ('725','Deerfield''s Four Seasons','282 Columbia','Sheldon','FL','33553',248.00,7500.00,'35');"]
        for query in insert_sql:
            cursor.execute(query)
            database_connectiion.commit()
    except sqlite3.Error as e:
        print(e)
    else:
        print('Alls rows are updated to customer table.')
    pass
def insert_a_customer_record(database_connectiion):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    while True:
        try:
            cursor=database_connectiion.cursor()
            customer_num = input("Enter customer number: ")

            if customer_num.isdigit():
                select_query = """SELECT * FROM customer WHERE customer_num = ?"""
                cursor.execute(select_query, (customer_num,))
                result = cursor.fetchone()
                if result:
                        print("Customer already exists with details:")
                        print("Customer Details are:", result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])
                else:
                        print("Customer not found. Enter new customer details:")
                        customer_name = input("Customer Name: ")
                        street = input("Street: ")
                        city = input("City: ")
                        state = input("State: ")
                        zip_code = input("ZIP Code: ")
                        balance = float(input("Balance: "))
                        credit_limit = float(input("Credit Limit: "))
                        rep_num = input("Rep Number: ")

                        insert_query = """
                        INSERT INTO customer (customer_num, customer_name, street, city, state, zip, balance, credit_limit, rep_num)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """
                    
                        cursor.execute(insert_query, (customer_num, customer_name, street, city, state, zip_code, balance, credit_limit, rep_num))
                        
                        # Commit the changes
                        database_connectiion.commit()
                        print("New customer record inserted successfully.")
                        break
            else:
                print('Invalid input.')
        
        except sqlite3.Error as e:
            print(e)
        pass

def query_rep_table(database_connection):
    #Create a function that prompts the user for a rep number. 
    # If the result is not empty, display the first record.
    while True:
        rep_num=input('Enter your rep number:')
        if rep_num:
            try:
                cursor=database_connection.cursor()
                select_query="""select * from rep where rep_num=?"""
                cursor.execute(select_query,(rep_num,))
                result=cursor.fetchone()
                if result:
                    print(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])
                    break
                else:
                    print(f'Given rep number is not found in table.')
                    break
            except sqlite3.Error as e:
                print(e)
        else:
            print('Invalid input. Please enter valid input.')
    pass
def update_rep_table(database_connection):
    #Create a function that prompts the user for a rep number.  
    #Then use the rep number to update the rep commission if it is in the [0.0 to 0.20]  range
    try:
        cursor = database_connection.cursor()
        
        rep_num = input("Enter the representative number (rep_num): ")
        select_query = "SELECT * FROM rep WHERE rep_num = ?"
        cursor.execute(select_query, (rep_num,))
        result = cursor.fetchone()
        
        if result:
            print("Current details for rep:", result)
            
            try:
                new_commission = float(input("Enter new commission rate (between 0.0 and 0.20): "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                return

            if 0.0 <= new_commission <= 0.20:
                update_query = "UPDATE rep SET rate = ? WHERE rep_num = ?"
                cursor.execute(update_query, (new_commission, rep_num))
                database_connection.commit()
                print(f"Commission rate for rep {rep_num} updated to {new_commission}.")
            else:
                print("Error: Commission rate must be between 0.0 and 0.20.")
        
        else:
            print("Error: No representative found with the provided rep number.")

    except sqlite3.Error as e:
        print("Database error:", e)

    pass
def delete_customer_record(database_connection):
    # Create a function that prompts the user for a customer number.  
    # if the customer number exists, confirm for deletion and 
    # then and delete then delete that customer 
    while True:
        try:
            cursor = database_connection.cursor()
            customer_num = input("Enter the customer number to delete: ")
            if customer_num.isdigit():
                select_query = "SELECT * FROM customer WHERE customer_num = ?"
                cursor.execute(select_query, (customer_num,))
                result = cursor.fetchone()
                
                if result:
                    print("Customer Details:", result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])
                
                    confirm = input("Are you sure you want to delete this customer? (yes/no): ")
                    if confirm.lower() == 'yes':

                        delete_query = "DELETE FROM customer WHERE customer_num = ?"
                        cursor.execute(delete_query, (customer_num,))
                        database_connection.commit()
                        print(f"Customer {customer_num} has been deleted.")
                        break
                    else:
                        print("Deletion canceled.")
                else:
                    print("No customer found with the provided customer number.")
            else:
                print('Invalid input, valid input')

        except sqlite3.Error as e:
            print("Database error:", e)
    pass
def delete_database(file_name, database_connection):
    # Create a function that deletes the database.  Verify that the file exists. 
    # Close the connection.  Then confirm the user really wants to delete the file,  Then delete the file.
    if os.path.exists(file_name):
        print(f"Database '{file_name}' found.")
        database_connection.close()
        print("Database connection closed successfully.")
        print('-----------------------------------------')
        
        confirm = input("Are you sure you want to delete this database file? (yes/no): ")
        if confirm.lower() == 'yes':
            try:
                os.remove(file_name)
                print(f"Database '{file_name}' has been deleted.")
            except Exception as e:
                print(f"An error occurred while deleting the database: {e}")
        else:
            print("Deletion canceled.")
    else:
        print(f"No database found at '{file_name}'.")

    
    pass
