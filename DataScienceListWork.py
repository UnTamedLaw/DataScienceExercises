import random

#my version
total = 0
for x in range(3):
    list_1 = [random.randint(0, 100) for x in range (0, 100)]
    list_2 = [x for x in list_1 if x % 3 == 0]
    difference2 = len(list_1) - len(list_2)
    total += difference2
mean = total/3.0
print(mean)

number_of_experiments = 10
difference_list = []

#books
for i in range(0, number_of_experiments):
    random_number_list = [random.randint(0, 100) for x in range(0, 100)]
    list_with_divisible_by_3 = [a for a in random_number_list if a % 3 == 0]
    difference3 = len(random_number_list) - len(list_with_divisible_by_3)
    difference_list.append(difference3)
print(difference_list)
avg_diff = sum(difference_list) / float(len(difference_list))
print(avg_diff)