#!/usr/bin/env python3

#imports
import pwd
import os
import shutil
import subprocess

#function to check if user exists
def user_exists(uName):
    
    #try statement to check if user exists
    try:
        
        #runs a command to check if user exists
        subprocess.check_output(["id", uName])
        
        #returns true if user exists
        return True
    
    #runs a process if user does not exist
    except subprocess.CalledProcessError:
        
        #returns false if user does not exist
        return False

#function to create a new user
def create_user(fName, uName):
    
    #checks if user exists
    if user_exists(uName):
        
        #prints message if user exists
        print(f"The username '{uName}' already exists.")
        
        #returns false if user exists
        return False
    
    #else statement
    else:
        
        #try statement
        try:
            
            #runs subprocess to create a new user that calls for full name and then password
            subprocess.check_call(["useradd", "-c", fName, "-m", uName])
            
            #prints message if user is created
            print(f"The user '{uName}' has been created successfully.")
            
            #returns true if user is created
            return True
        
        #runs another process if user is not created
        except subprocess.CalledProcessError:
            
            #prints message if user is failed to be created
            print(f"Failed to create the user '{uName}'.")
            
            #returns false if user is failed to be created
            return False

#function to remove a user
def remove_user(uName):
    
    # Check if user exists
    if not user_exists(uName):
        
        #prints message if user does not exist
        print(f"Error: User {uName} does not exist")
        
        #returns false if user does not exist
        return False
    
    #sets h_dir to the home directory of the user 
    h_dir = f"/home/{uName}"
    
    #checks if home directory exists
    if os.path.exists(h_dir):
        
        #shutil.rmtree removes the home directory
        shutil.rmtree(h_dir)
    
    # Delete user account
    os.system(f"sudo userdel -r {uName}")
    
    #prints message if user is deleted
    print(f"User {uName} has been successfully deleted")
    
    #returns true if user is deleted
    return True

#function to modify a user
def modify_user_account(uName):

    # Check if the user account exists
    if not user_exists(uName):
        
        #prints message if user does not exist
        print(f"The user account '{uName}' does not exist.")
        
        #returns false if user does not exist
        return False

    # Prompt the user for the modification option
    while True:
        
        #prints message for user to select an option with the username
        print(f"What do you want to modify for the user account '{uName}'?")
        
        #prints message for user to select option 1
        print(f"1. Lock the account")
        
        #prints message for user to select option 2
        print(f"2. Change the real name")
        
        #sets option to the user input
        option = input("Enter an option number (1 or 2): ")
        
        #checks if option is not 1 or 2
        if option not in ["1", "2"]:
            
            #prints message if option is not 1 or 2
            print("Invalid option. Please try again.")
            
        #else statement
        else:
            
            #break statement
            break

    # Lock the account if option is 1
    if option == "1":
        
        #try statement
        try:
            
            #subprocess.run runs a command to lock the account
            subprocess.run(["sudo", "usermod", "--lock", uName], check=True)
            
            #prints message if account is locked
            print(f"The account '{uName}' has been locked.")
            
            #returns true if account is locked
            return True
        
        #subprocess.CalledProcessError runs a process if account is not locked
        except subprocess.CalledProcessError as e:
            
            #prints message error occurs if account is not locked
            print(f"An error occurred while locking the account '{uName}': {e}")
            
            #returns false
            return False

    #Change the real name if option is 2
    elif option == "2":
        
        #new_rName is set to the user input for the new real name
        new_rName = input(f"Enter the new real name for the user '{uName}': ")
        
        #try statement
        try:
            
            #subprocess.run runs a command to change the real name
            subprocess.run(["sudo", "chfn", "-f", new_rName, uName], check=True)
            
            #prints message if real name is changed
            print(f"The real name of the account '{uName}' has been changed to '{new_rName}'.")
            
            #returns true if real name is changed
            return True
        
        #subprocess.CalledProcessError runs a process if real name is not changed
        except subprocess.CalledProcessError as e:
            
            #prints message if error occurs if real name is not changed
            print(f"An error occurred while changing the real name of the account '{uName}': {e}")
            
            #returns false
            return False

#function to check if username exists
def username_exists(uName):
    
    #try statement
    try:
        
        #pwd.getpwnam gets username
        pwd.getpwnam(uName)
        
        #returns true if username exists
        return True
    
    #key error runs a process if username does not exist
    except KeyError:
        
        #returns false if username does not exist
        return False

#function to create a user for menu
def create_user():
    
    #gets user input for new user's full name
    full_name = input("Enter full name: ")
    
    #gets user input for new user's username
    username = input("Enter username: ")

    #checks if username exists
    if username_exists(username):
        
        #prints message if username exists
        print("Error: username already exists")
        
        #returns false if username exists
        return False

    #creates the new user account
    cmd = f"useradd -m -s /bin/bash -c '{full_name}' {username}"
    
    #system runs a command
    os.system(cmd)
    
    #prints message if user is created
    print(f"New user '{username}' created successfully")
    
    #returns true if user is created
    return True

#function to remove a user for menu
def delete_user():
    
    #sets username to the user input for the username to be deleted
    username = input("Enter username to be deleted: ")

    #checks if username exists
    if not username_exists(username):
        
        #prints message if username does not exist
        print("Error: username does not exist")
        
        #returns false if username does not exist
        return False

    #removes the user account
    cmd = f"userdel -r {username}"
    
    #system runs a command
    os.system(cmd)
    
    #prints message if user is deleted
    print(f"User '{username}' deleted successfully")
    
    #retuen true if user is deleted
    return True

#function to modify a user for menu
def modify_user():
    
    #sets username to the user input for the username to be modified
    username = input("Enter username to be modified: ")

    #checks if username exists
    if not username_exists(username):
        
        #prints message if username does not exist
        print("Error: username does not exist")
        
        #returns false if username does not exist
        return False

    #prints message for user to select an option with the username
    print("Select an option:")
    
    #prints message for user to select option 1
    print("1. Lock the account")
    
    #prints message for user to select option 2
    print("2. Change the real name")

    #sets choice to the user input for the selected option
    choice = input("Enter your choice: ")
    
    #while loop to check if choice is not 1 or 2
    while choice not in ['1', '2']:
        
        #prints message if choice is not 1 or 2
        print("Invalid choice, please select a valid option")
        
        #prompts user to select an option
        choice = input("Enter your choice: ")

    #checks if choice is 1
    if choice == '1':
        
        #cmd is set to the command to lock the account
        cmd = f"passwd -l {username}"
        
        #system runs a command
        os.system(cmd)
        
        #prints message if account is locked
        print(f"User '{username}' locked successfully")
        
    #checks if choice is 2
    elif choice == '2':
        
        #new_full_name is set to the user input for the new full name
        new_full_name = input("Enter new full name: ")
        
        #cmd is set to the command to change the real name
        cmd = f"usermod -c '{new_full_name}' {username}"
        
        #system runs a command
        os.system(cmd)
        
        #prints message if real name is changed
        print(f"Real name for user '{username}' changed to '{new_full_name}' successfully")
        
    #returns true if account is locked or real name is changed
    return True

#function to display menu
def menu():
    
    #while loop to display menu
    while True:
        #prints message for user to select an option
        print("\nSelect an option:")
        
        #prints message for user to select option 1
        print("1. Create a new user")
        
        #prints message for user to select option 2
        print("2. Remove an existing user")
        
        #prints message for user to select option 3
        print("3. Modify an existing user account")
        
        #prints message for user to select option 4
        print("4. Quit")

        #sets choice to the user input for the selected option
        choice = input("Enter your choice: ")
        
        #while loop to check if choice is not 1, 2, 3, or 4
        while choice not in ['1', '2', '3', '4']:
            
            #prints message if choice is not 1, 2, 3, or 4
            print("Invalid choice, please select a valid option")
            
            #choice is set to the user input for the selected option
            choice = input("Enter your choice: ")

        #checks if choice is 1
        if choice == '1':
            
            #calls create_user function
            create_user()
            
        #checks if choice is 2
        elif choice == '2':
            
            #calls delete_user function
            delete_user()
            
        #checks if choice is 3
        elif choice == '3':
            
            #calls modify_user function
            modify_user()
            
        #checks if choice is 4
        elif choice == '4':
            
            #exits the program
            break

#checks if the program is being run directly
if __name__ == "__main__":
    
    #launches menu
    menu()
