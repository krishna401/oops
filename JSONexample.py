import json

#python object (dict):
Rice = {
        "propertie name" : "bashmati",
        "weight" : 45,
        "price" :"150"
}

Atta = {
        "propertie name": "Arhar",
        "weight" : 80,
        "price": "102"
}

   
Sugar = {
        "properties name": "andhra",
        "weight" : 20,
        "price":"40",
}   

   
      

rice=json.dumps(Rice)
atta=json.dumps(Atta)
sugar=json.dumps(Sugar)
print(rice)
print(atta)
print(sugar)
