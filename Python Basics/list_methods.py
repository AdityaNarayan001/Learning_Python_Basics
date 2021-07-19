numbers = [2, 5, 7, 10, 4, 5]
print('......................')
print(numbers.count(5)) #it tells how many times we have 5 in list numbers
print('......................')
numbers.insert(0,30) #it insert 30 at index number 0 in list
print(numbers)
print('......................')
numbers.append(20) #it adds 20 in list from back
print(numbers)
print('......................')
numbers.remove(7) #it removes 7 from the list
print(numbers)
print('......................')
numbers.pop()  #it removes the last elemnt from the list
print(numbers)
print('......................')
print(numbers.index(10)) #it returns the index number of element 10
print(10 in numbers) #it reurns True or False and indicates the presence of 10 in list
print('......................')
numbers.sort() #it will sort the list elements in a order
print(numbers)
numbers.reverse() #it will reverse the list
print(numbers)
print('......................')
numbers2 = numbers.copy() #copy is used to take a copy to numbers2
numbers.append(50)
print(numbers)
print(numbers2) #see there is no effect of append on numbers2
print('......................')
numbers.clear() #it clears all the elements in list
print(numbers)
print('......................')

