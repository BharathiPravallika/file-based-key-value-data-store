import threading #Threading in python is used to run multiple threads (tasks, function calls) at the same time. 
#Python threads are used in cases where the execution of a task involves some waiting.
# import threading can only be for python 3.0+. Use import thread for python 2.0
from threading import*
import time

dct = {} #for data storing purpose we are using dictionary as dct

#CREATE OPERATION STARTED
#syntax: "create(key_name,value,timeout_value)" #according to the given question timeout is optional.
#we can continue by passing two arguments(key and value) without taking timeout too.

def create(key,value,timeout=0):
    if key in dct:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(dct)<(1024*1020*1024) and value<=(16*1024*1024): #given constraints: file size must be lesser than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dct[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name encountered!! key_name must contain only alphabets and no special characters or numbers")#error message3

#FOR READ OPERATION
#Syntax: "read(key_name)"

def read(key):
    if key not in dct:
        print("error: Please enter a valid key. entered key does not exist in database.") #error message4
    else:
        b=dct[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#FOR DELETE OPERATION
#Syntax: "delete(key_name)"

def delete(key):
    if key not in dct:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dct[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dct[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del dct[key]
            print("key is successfully deleted")


#Let's have one additional operation 'modify' in order to change the value of key before its expiry time if provided
#FOR MODIFY OPERATION
#Syntax "modify(key_name,new_value)"

def modify(key,value):
    b=dct[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dct:
                print("error: Please enter a valid key, entered key does not exist in database.") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dct[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in dct:
            print("error: Please enter a valid key, entered key does not exist in database.") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dct[key]=l