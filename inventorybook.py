import json

name = input("enter product name: ")
quantity = str(input("enter amount of product: "))
type = input("enter type of product :")
productprice = str(input("enter  Product Price: "))


#used for writing the data into the JSON file
def write_json(data, filename):
    with open(filename, 'w') as inventry:
        json.dump(data, inventry, indent=4)


try:
    inventryDetail = {
        "productName": name,
        "productQuantity" : quantity,
        "productType":type,
        "productPrice":productprice
    }
    with open('inventBook.json') as inventry:
        dataOnFile = json.load(inventry)
        temp = dataOnFile["productDetail"]
        temp.append(inventryDetail)
    write_json(dataOnFile, 'inventBook.json')
except:
    inventryDetil = {
       "productDetail": [
         {
           "productName":name,
           "productQuantity":quantity,
           "productType" : type,
           "productPrice":productprice}
         ]}
    
    with open('inventBook.json', 'w') as inventry:
        json.dump(inventryDetail,inventry, indent=4)
