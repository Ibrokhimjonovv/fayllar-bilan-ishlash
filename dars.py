# with open('malumot.txt', 'w') as file:
#     file.write("Salom dunyo\nHello world")
# print("Fayl yaratildi")

# with open('malumot.txt', 'r') as file1:
#     data = file1.read()
#     print(data)
import json
lugat = {
    'Mahalla':{
        "ko'cha":"Oltin yo'l",
        'mahalla':'Muazinboy'
                }
}


lugat2 = {
    'Mahalla1':{
        "ko'cha1":"Oltin yo'l",
        'mahalla1':'Muazinboy'
                }
}
# with open('ishla.json', 'w') as filebase:
    
#     json.dump(lugat, filebase, indent = 3)


with open('ishla.json', 'r') as file:
    data = json.load(file)


with open('ishla.json', 'w') as filebase:
    data.update(lugat2)
    json.dump(data, filebase, indent = 3)