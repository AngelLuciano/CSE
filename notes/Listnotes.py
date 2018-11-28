print(3 == 3)
print(3 != 4)
# creating a list
fruit = ["apples", "oranges", "blackberries", "strawberries",
         "blueberries", "raspberries", "pineapple", "mango", "coconut"]
print(fruit)

# pulling items from a list
print(fruit[1])

# Getting the length of the list
print(len(fruit))
print("The length of the list in %d" % len(fruit))

# modifying lists
fruit[8] = "Banana"
print(fruit)

# looping through lists
for item in fruit:
    print(item)


Shoes = ["retro 1", 'retro 3', 'retro 2', 'retro 4', 'retro 5']

print(Shoes)
print(fruit[1])
print(len(Shoes))
print("the length of the list is %s" % len(Shoes))
Shoes[2] = "Retro 12"
print(Shoes)
for item in Shoes:
    print(item)

new_list = ['eggs', 'cheese', 'oranges', 'raspberries']
new_list[2] = 'apples'
print("the last thing in the list is %s" % new_list[len(new_list)-1])


Food_list = ['pizza', 'taco', 'burrito', 'tamales', 'chicken', 'noodles','flan', 'sushi', 'salad', 'carne asada', 'pie']

print(Food_list[2:5])
print(Food_list[3:4])
print(Food_list[10:])
print(Food_list[:5])

Food_list.append('oranges')
Food_list.append('bacon')
print(Food_list)

Food_list.insert(2, 'Goat')
print(Food_list)

Food_list.remove('taco')
Food_list.remove('pie')
print(Food_list)

Food_list.pop(0)
print(Food_list)

brand_list = ['nike', 'jordan', 'champion']
brand_list.insert(2, 'adidas')
brand_list.remove('champion')
print(brand_list)

print(Food_list.index('chicken'))

brands = ['apple', 'samsung', 'HTC']

string1 = 'turqoise'
list1 = list(string1)
print(list1)

# changing back in (list→string)