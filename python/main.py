message="hello's areej" #we can also write 'hello\'s areej
print(message)
#for multiple line
mul="""" i am arej saffer. 
im from ajk"""
print(mul)
#length
print(len(message))
print(message[0]) #index error when we exceed limit
print(message[0:5])
print(message[7:])
print(message.capitalize())
print(message.count("l"))
print(message.find("areej")) # if i type wrong that not exit in varible assigning than it return -1,-3
print(message.replace("areej","python"))
#concatenation
name="areej"
father_name="safeer"
#message='{},{}.welcome!'.format(name,father_name)
#print(name+','+father_name +'.welcome!')
print(f'my name is{name},my father name is {father_name}')
print(message)
print(dir(name))
my_list=[0,1,2,4,5]
print()