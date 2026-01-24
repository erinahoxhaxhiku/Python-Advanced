'''
Temperatura = 12.5
emri = "Erina"
mosha = 18

print(Temperatura)
print(emri)
print(mosha)

print(type(Temperatura))
print(type(emri))
print(type(mosha))
'''

#Kalkulime

x=8
y=10

result = x+y
print(result)

#update values

age = 30

age += 1

print(age)

#combine values

first_name = "Erina"
last_name = "Hoxhaxhiku"

full_name = first_name + " " + last_name
print(full_name)

#array(lists)

fav_colors = ["red", "green", "blue", "yellow", "purple"]
first = fav_colors[0]
second = fav_colors[1]

print(first)
print(second)

#method for list
#append - shton(add) ni element ne fund te listes
fav_colors.append("orange")
print(fav_colors)

#insert - shtojna ni element ne nje vend specifik
fav_colors.insert(2, "white")
print(fav_colors)

#metoda remove
fav_colors.remove("blue")
print(fav_colors)

#delete e hek me numer psh me pozit
del fav_colors[4]
print(fav_colors)

#update - e ndrron psh prej red ne pink

fav_colors[0] = "pink"
print(fav_colors)


