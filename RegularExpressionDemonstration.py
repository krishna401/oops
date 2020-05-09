import re


string = """Hello <<name>>, We have your full name as <<full name>> in our system.
your contact number is 91-xxxxxxxxxx.Please,let us know in case of any clarification
Thank you BridgeLabz 07/04/2019."""


name = input("enter the name:")
fullname = input("enter the fullname:")
mobilenumber = input("enter the mobile number: ")
date = input("enter the date:")

string2 = re.sub("<<name>>",name, string)
string2 = re.sub("<<full name>>",fullname, string2)
string2 = re.sub("xxxxxxxxxx",mobilenumber, string2)
string2 = re.sub("07/04/2019.",date, string2)
print(string2)
