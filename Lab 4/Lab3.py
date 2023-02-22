#!/usr/bin/env python3

# importing to read and work with csv files
import csv

#suspicious user login limit
login_limit = 250

#setup the csv file names
input_f = 'employee-logins.csv'
output_f = 'suspicious-users.txt'



#opening the csv file as a variable labeled csv_file
def read_csv(input_f):
    #create lists to store the data from the csv file
    first_name = []
    last_name = []
    login_attempts = []
    
    #opens input_f as csv_file
    with open(input_f) as csv_file:
    
        #make an object out of csv_file with a delimiter(separator) of commas
        read = csv.reader(csv_file, delimiter=',')
    
        #get contents from columns 2,3, and 5
        #enumerate the rows in the csv file to not get the first row as it is only the column names
        for i, row in enumerate(read):
            if i  == 0:
                continue 
            #skip the first row of the csv file
            
            #create a list of first names
            first_name.append(row[1])

            #create a list of last names
            last_name.append(row[2])

            #create a list of login attempts
            login_attempts.append(int(row[4]))
            
    #returning the names and login attempts from the csv file to be used in the suspicious_users function
    return first_name, last_name, login_attempts

#finding the suspicious users
def suspicious_users(first_name, last_name, login_attempts, login_limit):
    
    #create a list to store the suspicious users
    sus_users = []
    
    #Loops through the login attempts
    for i in range(len(login_attempts)):
        
        #checks if the current login attempt is greater than or equal to the login limit
        if login_attempts[i] >= login_limit:
            
            #if the login attempt is greater than or equal to the login limit, add the user to the list of suspicious users by the index number
            sus_users.append((first_name[i], last_name[i], login_attempts[i]))
    
    #return the list of suspicious users
    return sus_users

#creates a file with the suspicious user information and writes it to the file called output_f
def write_file(sus_users, output_f):
    
    #opens the file output_f as f 
    with open(output_f, 'w') as f:
        
        #loops the users in the list of sus_users 
        for users in sus_users:
            
            #writes the first name, last name, and login attempts to the file output_f
            f.write(f'{users[0]} {users[1]} {str(users[2])}\n')

#main execution of the program
def main():
    
    #calls the read_csv function and stores the returned values in the variables first_name, last_name, and login_attempts to inout_f
    first_name, last_name, login_attempts = read_csv(input_f)
    
    #calls the suspicious_users function and stores the returned values in the variable sus_users
    sus_users = suspicious_users(first_name, last_name, login_attempts, login_limit)
    
    #calls the write_file function and passes the variables sus_users and output_f
    write_file(sus_users, output_f)
    
    #loops through users in sus_users
    for users in sus_users:
        
        #prints the first name, last name, and login attempts of the suspicious users to the console
        print(f'{users[0]} {users[1]} - Login attempts: {[users[2]]}\n')
        
#calls the main function
main()