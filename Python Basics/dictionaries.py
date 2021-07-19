#in dictonaries value is stored in key:value format where each key is unique and cannot be duplicated
customer = {
    'name':'John Smith',
    'age':30,
    'is_verified':True
}
print(customer)
print(customer['name'])   #this method can also get the value with key but if the key value will be wrong then it displays error
print(customer.get('Name'))   #but in .get() error is not displayed it shows none
customer['name'] = 'Harry Smith'  #We can also update dictonaries
print(customer['name'])
customer['birthdate'] = 'Jan 1 1980' #we can easily add key:value pair
print(customer['birthdate'])