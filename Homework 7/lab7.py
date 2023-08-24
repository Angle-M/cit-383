#!/usr/bin/env python3

#imports csv
import csv

#sets filename to the name of the csv file
filename = 'empdata-2.csv'

#sets output_filename to the name of the output csv file
output_filename = 'compromised.csv'

# function to print the names of employees with compromised computers
def check_compromised_computers(filename):
    
    compromised_subnet = '250.30.8'
    
    #opens the file as a file object
    with open(filename, 'r') as file:
        
        #sets reader to a csv.DictReader object
        reader = csv.DictReader(file)
        
        # opens empdata-2.csv with a newline character as out_file
        with open('empdata-2.csv', 'r') as input_file, open(output_filename,'w',newline='') as output_file:
            
            #sets reader to a csv.DictReader object
            reader = csv.DictReader(input_file)
            
            #sets writer to a csv.writer object
            writer = csv.writer(output_file)
            
            #writer writes the headers
            writer.writerow(['name', 'department', 'email'])
            
            for row in reader:
                
                #sets ip_address to the value of the IP Address key
                ip_address = row['ip_address']
                
                #checks if the ip_address starts with 250.30.8
                if ip_address.startswith(compromised_subnet):
                    
                    #writes the name, department, and email of the employee to compromised.csv
                    writer.writerow([row['first_name']+' '+row['last_name'], row['department'], row['email']])

# function to print the names of employees with weak passwords
def check_weak_passwords(filename):
    
    #opens the file as a file object
    with open(filename, 'r') as file:
        
        #sets reader to a csv.DictReader object
        reader = csv.DictReader(file)
        
        #loops through the rows in the file in reader
        for row in reader:
            
            #sets password to the value of the Password key
            password = row['Password']
            
            #checks if the password is less than 8 or greater than 12 characters
            if len(password) < 8 or len(password) > 12:
                
                #prints the name of the employee with a weak password
                print(f"{row['first_name']} {row['last_name']} has a weak password: password length should be between 8 and 12 characters.\n")
                
            #checks if the password does not have a combination of upper- and lower-case characters
            elif not any(char.isupper() for char in password) or not any(char.islower() for char in password):
                
                #prints the name of the employee with a weak password
                print(f"{row['first_name']} {row['last_name']} has a weak password: password must have a combination of upper- and lower-case characters.\n")
                
            #checks if the password does not have at least 1 digit
            elif not any(char.isdigit() for char in password):
                
                #prints the name of the employee with a weak password
                print(f"{row['first_name']} {row['last_name']} has a weak password: password must have at least 1 digit.\n")
            
            #checks if the password does not have at least 1 non-alphanumeric character
            elif not any(not char.isalnum() for char in password):
                
                #prints the name of the employee with a weak password
                print(f"{row['first_name']} {row['last_name']} has a weak password: password must have at least 1 non-alphanumeric character./n")
                
            #checks if the password contains the @ character
            elif "@" in password:
                
                #prints the name of the employee with a weak password
                print(f"{row['first_name']} {row['last_name']} has a weak password: password must not contain the @ character.\n")

# function to print the names of employees with threat emails
def check_threat_emails(filename):
    
    #opens the file as a file object
    with open(filename, 'r') as file:
        
        #sets reader to a csv.DictReader object
        reader = csv.DictReader(file)
        
        #loops through the rows in the file in reader
        for row in reader:
            
            #sets email to the value of the Email key
            email = row['email']
            
            #checks if the email contains the @ character or the .ru or .jp domain
            if len(email.split('@')[0]) > 10 or email.endswith('.ru') or email.endswith('.jp'):
                
                #prints the name of the employee with a threat email
                print(f"{row['first_name']} {row['last_name']}, {row['email']}, {row['department']}")

# function to display the menu
def display_menu():
    
    #prints the menu
    print("Menu:")
    
    #prints the menu options
    print("1. Check compromised computers")
    
    #prints the menu options
    print("2. Check weak passwords")
    
    #prints the menu options
    print("3. Check threat emails")
    
    #prints the menu options
    print("4. Exit")

# function to run the program
def main():
    
    #while loop to run the program
    while True:
        
        #calls the display_menu function
        display_menu()
        
        #sets choice to user input
        choice = input("Enter your choice: ")
        
        #checks if the user's choice is 1
        if choice == '1':
            
            #calls the check_compromised_computers function and checks the file
            check_compromised_computers(filename)
            
        #checks if the user's choice is 2
        elif choice == '2':
            
            #calls the check_weak_passwords function and checks the file
            check_weak_passwords(filename)
            
        #checks if the user's choice is 3
        elif choice == '3':
            
            #calls the check_threat_emails function and checks the file
            check_threat_emails(filename)
            
        #checks if the user's choice is 4
        elif choice == '4':
            
            #prints the exit message
            print("Exiting...")
            
            #leaves the while loop
            break
        
        #else statement
        else:
            
            #prints the invalid choice message
            print("Invalid choice, please try again.")

#checks if the program is being run directly
if __name__ == '__main__':
    
    #calls the main function
    main()
