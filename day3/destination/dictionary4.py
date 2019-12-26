info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

for key,value in info.items():
    if  isinstance(value,str):
        print(key.ljust(15),value)
    else:
        for subkey,subvalue in value.items():
            name = key +  '.' + subkey
            print(name.ljust(15),subvalue)