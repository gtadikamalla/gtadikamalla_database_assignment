#modify this module to write code for the user interface
import your_name_functions as functions 
connection = None 
while True:
    prompt = """
            B to create the database file
            P to create rep table
            S to create customer table
            I to insert a customer record
            R to query the Rep table
            U to update the rep table
            D to delete a customer record
            X to delete the database
            Q to quit the application
            """
    choice = input(prompt)
    if choice in 'Bb':
        file_name = input('Enter the database file name: ')
        connection = functions.create_database_file(file_name)
    elif choice in 'Pp':
        #check if the connection exists 
        #call functions.create_rep_table with the connection
        pass
    elif choice in 'Ss':
        #check if the connection exists 
        #call functions.create_customer_table with the connection
        pass
    elif choice in 'Ii':
        #check if the connection exists 
        #call functions.insert_customer with the connection
        #in that function, prompt the user for 
        pass
    elif choice in 'Rr':
        #check if the connection exists 
        #call functions.query_rep with the connection
        pass
    elif choice in 'Uu':
       #check if the connection exists 
        #call functions.update_rep with the connection
        pass
    elif choice in 'Dd':
        #check if the connection exists 
        #call functions.delete_a_customer with the connection
        pass
    elif choice in 'Xx':
        #check if the connection exists t
        #call functions.delete_the_database with the connection
        pass

    elif choice in 'Qq':
       #check if the connection exists 
        #call functions.queries
        pass
    else:
        #process the other choices
        break


    
