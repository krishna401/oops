import json

def write_json(data, filename):
    with open(filename, 'w') as book:
       json.dump(data, book, indent=4)

def elementExits(element):
#return True if passed element is Present else return False
    with open('addressbook.json') as addressbook:
         dataonfile = json.load(addressbook)
         for data in dataonfile["personalDetail"]:
              if data.get("firstname") == element:
                  return True
    return False

def add(): # to add new Entry into the  JSON File
    
    fristname = input("enter your frist name: ")
    lastname  = input("enter your last name: ")
    address = input("enter your Address: ")
    city = input("enter your city: ")
    state = input("enter your state: ")
    pin = input("enter your pin number: ")
    mobilenumber =  str(input("enter your mobile number: "))
    try:
         
       addressDetail = {
         "fristname":fristname,
         "lastname":lastname,
         "address":address,
         "city":city,
         "state":state,
         "pin":pin,
         "mobilenumber":mobilenumber
       }
       with open('addressbook.json') as addressbook:
            dataonfile = json.load(addressbook)
            temp = dataonfile["personalDetail"]
            temp.append(addressDetail)
       write_josn(dataonfile, 'addressbook.json')
       print("data saved")
    except:
         addressDetail = {
            "personlDetail": [
               {
                "fristname": fristname,
                "lastname": lastname,
                "address":address,
                "city":city,
                "state":state,
                "pin":pin,
                "mobilenumber":mobilenumber
               }
             ]}
         write_json(addressDetail, 'addressbook.json')
         print("data saved")

def search(element): #search for data based on lastname or fristname or mobilenumber

    with open('addressbook.json') as addressbook:
        dataonfile = json.load(addressbook)
    for data in dataonfile["personalDetail"]:
        if element == data.get("fristname") or element == data.get("mobilenumber") or element == data.get("lastname"):
           print(data)

def dalete(element): #delete a object from jSON file based on Frist name

    if elementExists(element) == False:
       print("Data not present")
       return None
    with open('adressbook.json') as addressbook:
         dataonfile = json.load(addressbook)
    temp = []
    for data in dataonfile["personalDetail"]:
        if element == data.get("fristname"):
           pass
        else:
            temp.append(data)
    dictionary = {"personalDetail": temp }
    write_json(dictionary, 'addressbook.json')
    print("data deleted")


#add()
search("manikanta")
#delete()
 
