# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 11:53:26 2018

@author: G Sriram
"""
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
import pickle
import os
import sys
class Faculty(object):
    def __init__(self,e_no,name,class_handled):
        '''
        A Function which initialises the Employee ID, Name, and Classes Handled
        '''
        self.name=name
        self.e_no=e_no
        self.class_handled=class_handled
        
    def get_eno(self):
        return self.e_no
    
    def get_name(self):
        return self.name
    
    def get_class_handled(self):
        return self.class_handled

class TimeTable(object):
    def __init__(self,e_no,timeTable):
        self.e_no=e_no
        self.timeTable=timeTable
        
    def get_eno(self):
        return self.e_no
    
    def getTimeTable(self):
        return self.timeTable
    
def readFaculty():
    '''
    Function which reads the file and returns a list of objects of type Faculty
    '''
    fr=open('FacultyDetails.file','rb')
    a=[]
    while True:
        try:
            x=pickle.load(fr)
            a.append(x)
        except EOFError:
            break
    fr.close()
    return a

def searchFaculty(e_no):
    ''' 
    Function to return Faculty Details  given the Employee ID
    '''              
    flist=readFaculty()
    for i in flist:
        if(i.get_eno()==e_no):
            return i
        
    
def enterFacultyDetails():
    '''
    Function which takes in the Faculty Details and returns an object of type Faculty
    '''
    e_no=str(input("Enter the Employee ID of the Faculty: "))
    if(searchFaculty(e_no)!=None):
        raise ValueError
    name=str(input("Enter the Name of the Faculty: "))
    x=str(input("Enter the classes handled by the faculty(Semester followed by Section and commas seperating each class. Suffix by 'L' if lab Eg: 2A,4B,2BL): "))
    y=x.upper()
    classhandled=y.replace(' ','').split(',')
    return Faculty(e_no,name,classhandled)

def enterFacultyDetails1(e_no):
    '''
    Function which takes in the Faculty Details and returns an object of type Faculty
    '''
    
    name=str(input("Enter the Name of the Faculty: "))
    x=str(input("Enter the classes handled by the faculty(Semester followed by Section and commas seperating each class. Suffix by 'L' if lab Eg: 2A,4B,2BL): "))
    y=x.upper()
    classhandled=y.replace(' ','').split(',')
    return Faculty(e_no,name,classhandled)

def writeFaculty(a):
    '''
    Function which writes into a binary object file the details of the faculty
    '''
    fw=open('FacultyDetails.file','ab')
    pickle.dump(a,fw)
    fw.close()
    

def enterTimeTable(e_no):
    '''
    Function to enter the time table of a Faculty and returns an object of type TimeTable
    '''
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    result=[]
    facdetails=searchFaculty(e_no)
    print("Faculty Name:",facdetails.get_name())
    print()
    print()
    for i in days:
        a=[]
        x=1
        if(i=='Saturday'):
            while(x<=4):
              while True:
                  y=input("Enter the class handled on " + str(i) + ", hour no." + str(x) +": ")
                  y=y.upper()
                  y=y.replace(' ','')
                  if(y in (facdetails.get_class_handled()+['X'])):
                      break
                  else:
                      print("Enter a valid input!")
              a.append(y)
              x+=1
            result.append(a)  
            continue
        while(x<=7):
              while True:
                  y=input("Enter the class handled on " + str(i) + ", hour no." + str(x) +": ")
                  y=y.upper()
                  y=y.replace(' ','')
                  if(y in (facdetails.get_class_handled()+['X'])):
                      break
                  else:
                      print("Enter a valid input!")
              a.append(y)
              x+=1
        result.append(a)
    return TimeTable(e_no,result)

def writeTimeTable(a):
    '''
    Function to Write the Time Table into a file given object of type TimeTable
    '''
    fw=open('TimeTable.file','ab')
    pickle.dump(a,fw)
    fw.close()

def readTimeTable():
    '''
    Function which reads the file and returns a list of objects of type TimeTable
    '''
    fr=open('TimeTable.file','rb')
    a=[]
    while True:
        try:
            x=pickle.load(fr)
            a.append(x)
        except EOFError:
            break
    fr.close()
    return a


def searchTimeTable(e_no):
    ''' 
    Function to return TimeTable Details  given the Employee ID
    '''              
    flist=readTimeTable()
    for i in flist:
        if(i.get_eno()==e_no):
            return i
        
def modifyFaculty(e_no):
    '''
    Function which modifies the faculty details given the Employee ID
    '''
    flist=readFaculty()
    fw=open('FacultyDetails1.file','ab')
    for i in flist:
        if(i.get_eno()==e_no):
            f=enterFacultyDetails1(e_no)
            pickle.dump(f,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('FacultyDetails.file')
    os.rename('FacultyDetails1.file','FacultyDetails.file')
    
def modifyTimeTable(e_no):
    '''
    Function which modifies the Time Table given the Employee ID
    '''
    flist=readTimeTable()
    fw=open('TimeTable1.file','ab')
    for i in flist:
        if(i.get_eno()==e_no):
            f=enterTimeTable(e_no)
            pickle.dump(f,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('TimeTable.file')
    os.rename('TimeTable1.file','TimeTable.file')
    
def deleteFaculty(e_no):
    '''
    Function which erases the faculty details and timetable given the Employee ID
    '''
    flist=readFaculty()
    fw=open('FacultyDetails1.file','ab')
    for i in flist:
        if(i.get_eno()==e_no):
            continue
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('FacultyDetails.file')
    os.rename('FacultyDetails1.file','FacultyDetails.file')
    
    flist=readTimeTable()
    fw=open('TimeTable1.file','ab')
    for i in flist:
        if(i.get_eno()==e_no):
            continue
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('TimeTable.file')
    os.rename('TimeTable1.file','TimeTable.file')
    
def get_daily_timeTable(e_no,day):
    '''
    Function which returns the timetable of a faculty for a specific day
    '''
    a=searchTimeTable(e_no)
    i=days.index(day)
    x=a.getTimeTable()
    return (e_no,x[i])

def get_free_hrs(e_no,day):
    '''
    Function which returns the number of free hours the faculty has per day
    '''
    a=get_daily_timeTable(e_no,day)
    return a[1].count('X')
    
def findFreeSubstitute(e_no,day,hr):
    '''
    Function which returns the Faculties who are free in the specified hour and day sorted by how free they are
    '''
    x=get_daily_timeTable(e_no,day)
    y=x[1][hr-1]
    if y=='X':
        raise ValueError
    flist=readFaculty()
    a=[]
    b=[]
    for i in flist:
        if(y in i.get_class_handled() and str(i.get_eno())!=str(e_no)):
            z=get_daily_timeTable(i.get_eno(),day)
            if(z[1][hr-1]=='X'):    
                a.append(i)
    timeTableDict={}
    for i in a:
        dailyTimeTable=get_daily_timeTable(i.get_eno(),day)
        numFreeHrs=get_free_hrs(i.get_eno(),day)
        timeTableDict[dailyTimeTable[0]]=numFreeHrs
    timeTableDictCopy=sorted(timeTableDict, key=timeTableDict.__getitem__,reverse=True)
    for j in timeTableDictCopy:
        b.append(searchFaculty(j))
    return b

def findLabSubstitute(e_no,day,hr):
    '''
    Function which returns the Faculties who are not free but have a lab session in the specified hour and day sorted by how free they are
    '''
    x=get_daily_timeTable(e_no,day)
    y=x[1][hr-1]
    if y=='X':
        raise ValueError
    flist=readFaculty()
    a=[]
    b=[]
    for i in flist:
        if(y in i.get_class_handled() and str(i.get_eno())!=str(e_no)):
            z=get_daily_timeTable(i.get_eno(),day)
            if(z[1][hr-1][-1]=='L'):    
                a.append(i)
    timeTableDict={}
    for i in a:
        dailyTimeTable=get_daily_timeTable(i.get_eno(),day)
        numFreeHrs=get_free_hrs(i.get_eno(),day)
        timeTableDict[dailyTimeTable[0]]=numFreeHrs
    timeTableDictCopy=sorted(timeTableDict, key=timeTableDict.__getitem__,reverse=True)
    for j in timeTableDictCopy:
        b.append(searchFaculty(j))
    return b

def menu():
    '''
    Function which creates a user interface
    '''
    while True:
        os.system('cls')
        print("Main Menu".center(40))
        print()
        print("1. Add New Faculty")
        print("2. Add New Time Table for Faculty")
        print("3. Modify Faculty Details")
        print("4. Modify Faculty TimeTable")
        print("5. Delete Faculty Details")
        print("6. Find Substitute Teacher")
        print("7. Exit")
        try:
            ch=int(input("Enter your choice(1-7): "))
        except ValueError:
            print("Enter a valid choice!")
            input("\n\nPress <Enter> to return back to the menu.")  
            menu()
        else:
            if(ch in range(1,8)):
                break
            else:
                print("Please Enter a valid choice!")
                input("\n\nPress <Enter> to return back to the menu.")   
                menu()
    if(ch==1):
        os.system('cls')
        print("Add a Faculty".center(40))
        try:
            f=enterFacultyDetails()
        except ValueError:
            print("Faculty Already Exists!")
        else:
            
            writeFaculty(f)
            print("Faculty Successfully added!")
        finally:
            input("\n\nPress <Enter> to return back to the menu.")
            menu()
    if(ch==2):
        os.system('cls')
        print("Instructions".center(40))
        print("You will now be redirected to a prompt asking the Time Table of a certain Faculty." )
        print("1. Enter the Employee ID of the Faculty First")
        print("2. You will be prompted to enter the TimeTable hour by hour for each day starting from Monday")
        print("3. The Time Table should be Entered as Follows: ")
        print("    (i) Enter the Semester number taken by the Faculty followed by the Section. Eg. 2A")
        print("    (ii) If the Faculty is Free, just type 'X'")
        print("    (iii) If the Faculty is handling a Lab, Enter the semester number and the section as shown in step (i) followed by 'L'. Eg. 2AL")
        print("4. Do not leave any prompt Empty or do not stop the process halfway")
        input("Press <Enter> to continue")
        os.system('cls')
        e_no=str(input("Enter the Employee ID of the Faculty: "))
        if(searchFaculty(e_no)==None):
            print("Faculty Not Found!")
            input("\n\nPress <Enter> to return back to the menu.")
            menu()
        tt=enterTimeTable(e_no)
        writeTimeTable(tt)
        print("Time Table Succesfully Added!")
        input("\n\nPress <Enter> to return back to the menu.")
        menu()
        
    if(ch==3):
        os.system('cls')
        print("Modify Faculty details".center(40))
        try:
            e_no=input("Enter the Employee ID of the Faculty to modify: ")
            if(searchFaculty(e_no)==None):
                raise ValueError("X")
            modifyFaculty(e_no)
            print("Successfully Modified!")
        except:
            print("Faculty not found/Unable to modify the details.")
        finally:
            input("\n\nPress <Enter> to return back to the menu.")
            menu() 
    if(ch==4):
        os.system('cls')
        print("Instructions".center(40))
        print("You will now be redirected to a prompt asking the Time Table of a certain Faculty." )
        print("1. Enter the Employee ID of the Faculty First")
        print("2. You will be prompted to enter the TimeTable hour by hour for each day starting from Monday")
        print("3. The Time Table should be Entered as Follows: ")
        print("    (i) Enter the Semester number taken by the Faculty followed by the Section. Eg. 2A")
        print("    (ii) If the Faculty is Free, just type 'X'")
        print("    (iii) If the Faculty is handling a Lab, Enter the semester number and the section as shown in step (i) followed by 'L'. Eg. 2AL")
        print("4. Do not leave any prompt Empty or do not stop the process halfway")
        input("Press <Enter> to continue")
        os.system('cls')
        print("Modify Time Table".center(40))
        try:
            e_no=input("Enter the Employee ID of the Faculty to modify: ")
            if(searchFaculty(e_no)==None):
                raise ValueError("X")
            modifyTimeTable(e_no)
            if(searchTimeTable(e_no)==None):
                print("TimeTable not found! Please add a new Time Table first. ")
                input("\n\nPress <Enter> to return back to the menu.")
                menu()  
            print("Successfully Modified!")
        except:
            print("Faculty not found/Unable to modify the details.")
        finally:
            input("\n\nPress <Enter> to return back to the menu.")
            menu()  
    if(ch==5):
        try:
            ch=None
            os.system('cls')
            e_no=input("Enter the Employee ID of the Faculty to delete: ")
            if(searchFaculty(e_no)==None):
                raise ValueError("X")
            a=searchFaculty(e_no)
            print("Faculty to be deleted:",a.get_name())
            ch=input("Are you sure? (y/n) ")
            if(ch.upper()=='Y'):
                deleteFaculty(e_no)
                print("Successfully Deleted!")
            else:
                print("Faculty not deleted")
        except:
            print("Faculty not found/Unable to delete the details.")
        finally:
            input("\n\nPress <Enter> to return back to the menu.")
            menu()
    if(ch==6):
       os.system('cls')
       print("Find Substitute Faculty".center(40))
       e_no=str(input("\nEnter the Employee ID of the Faculty who is absent: "))
       if(searchFaculty(e_no)==None):
           print("Faculty Not Found!")
           input("Press <Enter> to return back to the menu.")
           menu()
       m=searchFaculty(e_no)
       print("\nFaculty absent:",m.get_name())
       while True:
           
           day=str(input("\nEnter the day today: "))
           day=day.capitalize()
           day=day.replace(' ','')
           if day in days:
               break
           else:
               print("Enter a valid day! Please Try again.")
       x=get_daily_timeTable(e_no,day)
       print("\n\nClasses handled by the faculty: \n") 
       cnt=1
       for i in x[1]:
           if(i!='X'):
               print("Hour",cnt,':',i,end='; ')
           cnt+=1
       while True:
           try:
              hr=int(input("\n\nEnter the hour to be substituted for: "))
              if(day == "Saturday" and hr in range(1,5)):
                  break
              elif(day!="Saturday" and hr in range(1,8)):
                  break
              else:
                  print("Enter a valid hour! Please try again")
           except ValueError:
               print("Enter a valid hour! Please try again!")
           else:
               break
       os.system('cls')
       m=searchFaculty(e_no)
       if(x==None):
           print("TimeTable not found! Please add the TimeTable of the Faculty First!")
           input("Press <Enter> to return back to the menu.")
           menu()    
       y=x[1][hr-1]      
       print("\n\nFaculty absent:",m.get_name())
       print("\nClass Handled by the Faculty:",y,'\n\n')
       try:
           x=findFreeSubstitute(e_no,day,hr)
           y=findLabSubstitute(e_no,day,hr)
       except ValueError:
           print("The faculty is free during the hour.")
       else:
           print("Faculties who are free during the specified hour: \n")
           if(x==[]):
               print("None.")
           count=1
           for i in x:
               print(str(count)+". "+i.get_name())
               count+=1
           print("\n\nFaculties who are not free but have a lab session: \n")
           if(y==[]):
               print("None.")
           count=1
           for i in y:
               print(str(count)+'. '+i.get_name())
               count+=1
       finally:
           input("\n\nPress <Enter> to return back to the menu")
           menu()
    if(ch==7):
        sys.exit()
print("Time Table Management System".center(40))
print()
print()
print("Done by: G. Sriram".center(40))
input()
menu()
