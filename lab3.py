food = "steak with broccoli"
print(food[:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

number_list = [45, 98767, -344, 0, 1]
number_list.append(3)
print(number_list)
number_list.insert(3, -1000000001)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(98767)
print(number_list)
print(number_list[:3])
print (number_list[-3:])
print (number_list[-3:])

books = {'Ray bradbury':'f451',
         'John Steinbeck':'mice of men',
         'Gabriel Garcia Marquez':'chronicle of a death foretold',
         'Bruce Cameron':'a dogs purpose'}
print(books.keys())
print(books.values())
print(books.get('Bruce Cameron'))
books.pop('Gabriel Garcia Marquez')
print(books)
del books['Bruce Cameron']
print(books)