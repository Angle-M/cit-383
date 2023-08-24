#!/usr/bin/env python3

#imports
import re
from collections import Counter

#function to get file data from file name
def getFileData(file_name):
    
    #try statement
    try:
        
        #opens file in read mode
        with open(file_name, 'r') as file:
            
            #sets file data variable to readlines
            file_data = file.readlines()
            
            #returns file data
            return file_data
    
    #file not found error
    except FileNotFoundError:
        
        #prints error message
        print("File not found!")
        
        #returns empty list
        return []

#function to generate client ip from file data
def genClientIP(file_data):
    
    #sets client ip list to an empty list
    client_ips = []
    
    #loops through each line in file data
    for line in file_data:
        
        #sets match variable to regex search for ip address
        match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        
        #checks if match is true
        if match:
            
            #adds match to client ip list
            client_ips.append(match.group(0))
            
    #sets client ip counter to counter object with client ip list
    client_ip_counter = Counter(client_ips)
    
    #returns client ip counter
    return client_ip_counter

#function to generate status code from file data
def genStatusCode(file_data):
    
    #sets status code list to an empty list
    status_codes = []
    
    #loops through each line in file data
    for line in file_data:
        
        #searches for status code in line
        match = re.search(r"\s(\d{3})\s", line)
        
        #checks if match is true
        if match:
            
            #adds match to status code list
            status_codes.append(match.group(1))
            
    #sets status code counter to counter object with status code list
    status_code_counter = Counter(status_codes)
    
    #returns status code counter
    return status_code_counter

#function to print report from client ip and status code dictionaries
def printReport(client_ip_dict, status_code_dict):
    
    #sets file name variable to appache-access_log
    file_name = "appache-access_log"
    
    #prints line
    print("----------------------------------------------------")
    
    #prints statistics for file name
    print(f"Statistics for the Apache log file {file_name}")
    
    #prints line
    print("----------------------------------------------------\n")

    #prints frequency of client ip addresses
    print("Frequency of Client IP Addresses:")
    
    #loops through each ip and count in client ip dictionary
    for ip, count in client_ip_dict.items():
        
        #formats ip and count and prints
        print(f"{ip:<20s}{'*' * count}")

    #sets total_lines variable to sum of status code dictionary values
    total_lines = sum(status_code_dict.values())
    
    #prints new line with http status codes summary
    print("\nHTTP Status Codes Summary:")
    
    #loops through each code and count in status code dictionary
    for code, count in status_code_dict.items():
        
        #sets percentage variable to count divided by total lines times 100
        percentage = (count / total_lines) * 100
        
        #prints formatted code and percentage
        print(f"{code}: {percentage:.2f}%")


#tests

#sets file name variable to appache-access_log
file_name = "appache-access_log"

#sets file data variable to file data from file name
file_data = getFileData(file_name)

#sets client ip dictionary to client ip dictionary from file data
client_ip_dict = genClientIP(file_data)

#sets status code dictionary to status code dictionary from file data
status_code_dict = genStatusCode(file_data)

#prints report from client ip dictionary and status code dictionary
printReport(client_ip_dict, status_code_dict)

