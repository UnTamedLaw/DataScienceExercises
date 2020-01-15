#A tuple consists of values separated by commas, they are immutable. Once created they cannot change their alues. 

tuple_1 = ()
#creating a tuple with only one value...don't forget the trailing comma!
tuple_1 = "Hello",
tuple_1 = "hello", "there", 45
#unpacking a tuple
#it means getting the values contained in the tuple into different variables 
tuple_1 = "Science", "Rocks" 

hello, world = tuple_1
print(hello)
print(world)