#strings can be defined using single quotes and double quotes
str_1 = "hello world!"
str_1[0] #return as "h"
str_1[-1] #return as !

#accessing the elements of a string is like accessing a list
str_1 = "Hello World! I am learning data wrangling"
# print(str_1 [2:10]) 'llo Worl"
#str_1[-31:]  # 'd! I am learning data wrangling'
#str_1[-10:-5] # ' wran'

#string functions 
str_1 = "Hello World! I am learning data wrangling"
len(str_1)
str_1.lower()
str_1.upper()

str_1 = "A complicated string looks like this"

#find method is case-sensitive. If found it will return first index where it is found
#print(str_1.find("complicated"))

#replace method 
str_1.replace("complicated", "simple")

#split method
str_1 = "Name, Age, Sex, Address"
list_1 = str_1.split(", ")
#print(list_1)
list_2 = " | ".join(list_1)
#print(list_2)
