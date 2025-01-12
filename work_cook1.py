'''В одном файле может быть произвольное количество блюд.
Читать список рецептов из этого файла.
Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.'''

f=open('cook_book.txt',encoding = 'UTF-8')
data = f.read().split()
#print(data)

omlet = {}
omlet['ingredient_name'] = data[2]
omlet['quantity'] = int(data[4])
omlet['measure'] = data[6]

omlet2 = {}
omlet2['ingredient_name'] = data[7]
omlet2['quantity'] = int(data[9])
omlet2['measure'] = data[11]

omlet3 = {}
omlet3['ingredient_name'] = data[12]
omlet3['quantity'] = int(data[14])
omlet3['measure'] = data[16]

utka = {}
utka['ingredient_name'] = data[20]
utka['quantity'] = int(data[22])
utka['measure'] = data[24]

utka2 = {}
utka2['ingredient_name'] = data[25]
utka2['quantity'] = int(data[27])
utka2['measure'] = data[29]

utka3 = {}
utka3['ingredient_name'] = data[30]
utka3['quantity'] = int(data[32])
utka3['measure'] = data[34]

utka4 = {}
utka4['ingredient_name'] = data[35]+' '+data[36]
utka4['quantity'] = int(data[38])
utka4['measure'] = data[40]

kartofel = {}
kartofel['ingredient_name'] = data[44]
kartofel['quantity'] = int(data[46])
kartofel['measure'] = data[48]

kartofel2 = {}
kartofel2['ingredient_name'] = data[49]
kartofel2['quantity'] = int(data[51])
kartofel2['measure'] = data[53]

kartofel3 = {}
kartofel3['ingredient_name'] = data[54]+' '+data[55]
kartofel3['quantity'] = int(data[57])
kartofel3['measure'] = data[59]

omlet_all = [omlet,omlet2,omlet3]
utka_all = [utka, utka2, utka3, utka4]
kartofel_all = [kartofel, kartofel2, kartofel3]

cook_book = {}
name_omlet = data[0]
cook_book[data[0]] = omlet_all
cook_book.setdefault(data[17] +' '+ data[18], utka_all) #Создаёт ключ и значение
cook_book.setdefault(data[41] +' '+ data[42], kartofel_all)
print(f'cook_book = ''{')
for key, value in cook_book.items():
    print(f"{key}:'\n'{value}")


