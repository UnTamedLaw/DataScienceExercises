#dictionary keys must be unique
import random
dict_1 = {"key1": "value1", "key2": "value2"}

print(dict_1)

dict_2 = {"key1": 1, "key2": ["list_element1", 34], "key3": "value3",

"key4": {"subkey1": "v1"}, "key5": 4.5}
print(dict_2)

# access and set values in a dictionary
dict_2["key2"] = "My new value"

dict_3 = {}
dict_3["key1"] = "Value1"

#iterate over a dictionary"
dict_iterate = {"key1": 1, "key2": ["list_element1", 34], "key3": "value3", "key4": {"subkey1": "v1"}, "key5": 4.5}
for k, v in dict_iterate.items():
    print (" {} - {}".format(k, v))

list_1 = [random.randint(0,30) for x in range(0, 100)]

#create a unique valued list from list_1 
list(dict.fromkeys(list_1).keys())

#dict.fromkeys and keys.fromkeys creates a dict where the keys from the iterable where the values default to None.

#deleting values from a dict
five_list = {"key1": 1, "key2": ["list_element1", 34], "keys3" : "value3", "keys4" : {"subkey1" : "v1"}, "key5" : 4.5 }

del five_list["key2"]
print(five_list)

#dictionary comprehension 
#generating a dict that has 0-9 as keys and the square key as the values
list_10 = [x for x in range(0, 10)]
dict_squared = { x : x**2 for x in list_1}

#using only dictionary comprehension without using a list
dict_squared2 = { x: x**2 for x in range(9)}
print(dict_squared2)

#generating a dict using the dict function
dict_generate = dict([('Tom', 100), ('Dick', 200), ('Harry', 300)])
#2nd way
dict_generate2 = dict(Tom=100, Dick=200, Harry=300)
