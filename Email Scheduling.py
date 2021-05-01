# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:42:20 2018

@author: G Sriram
"""

import smtplib                                #inports smtplib to access the E-Mail server
import getpass                                #imports getpass library for hiding the password
#Beginning of UI

print("Welcome to the E-mail scheduling app.")
sender=input("Please Enter your G-Mail ID: ")
reciever=input("Please Enter the E-Mail you are sending to: ")
p=getpass.getpass('Enter your password: ')    #password input
print("Trying to login.....")

try:                                            #Tries to access the E-mail account 
    username=sender.split('@')
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username[0],str(p))
    print("Login Successful!")
    msg=input("Enter your message: ")
    server.sendmail(str(sender),str(reciever),msg)
    server.close()
except:
    print("E-mail not sent/Login Failed.")      #if it fails to access
    input("Press <Enter> to continue.")
else:
    print("Succesfully sent!")                  #upon successful completion of the program
    input("Press <Enter> to continue.")