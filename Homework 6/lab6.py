#imports

import os
import argparse

#function checks if the directory exists
def val_dir(path):
    
    #if the path is not a directory
    if not os.path.isdir(path):
        
        #raise an error of the path is not a valid directory
        raise argparse.ArgumentTypeError("{0} is not a valid directory".format(path))
    
    #return the path
    return path

#function to list the contents of the directory
def list_directory_contents(directory, logfile=None):
    
    #if the directory does not exist
    if not os.path.exists(directory):
        
        #print an error message
        print(f"Error: Directory '{directory}' does not exist.")
        
        #statement return
        return
    
    #setting the entries to the list of the directory
    entries = os.listdir(directory)
    
    #if the logfile is not empty
    if logfile:
        
        #open the logfile in write mode
        with open(logfile, 'w') as f:
            
            #format the directory and write it to the file
            f.write(f"Directory contents: {directory}\n")
            
            #format the line and write it to the file
            f.write("********************************\n")
            
            #loops through the entries
            for entry in entries:
                
                #checks if the entry contains . or ..
                if entry not in ['.', '..']:
                    
                    #writes  the entry stored in the variable with a new line following
                    f.write(entry + '\n')
                    
    #else statement
    else:
        
        #prints the directory contents
        print(f"Directory contents: {directory}")
        
        #pritns the line
        print("********************************")
        
        #loops through the entries
        for entry in entries:
            
            #checks if the entry contains . or ..
            if entry not in ['.', '..']:
                
                #prints the entry
                print(entry)

#function to create directories
def create_directories(path, n):
    
    #for loop to create the directories
    for i in range(1, n+1):
        
        #uses the os module to create the directories
        os.mkdir(os.path.join(path, f"dir_{i}"))

#checks if the file is being run as the main file
if __name__ == '__main__':
    
    #sets par to the argument parser
    par = argparse.ArgumentParser(description='List contents of a directory')
    
    #calls par.add_argument to add the directory argument of help
    par.add_argument('directory', type=val_dir, help='Path to directory')
    
    #calls par.add_argument to add the logfile argument
    par.add_argument('-l', '--logfile', help='Name of log file')
    
    #calls par.add_argument to add the create argument
    par.add_argument('-c', '--create', type=int, help='Number of directories to create')
    
    #sets args to the parse_args method
    args = par.parse_args()

    #checks if the create argument is called
    if args.create:
        
        #calls the create_directories function
        create_directories(args.directory, args.create)
        
    #calls the list_directory_contents function
    list_directory_contents(args.directory, args.logfile)
