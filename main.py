# Import the random module
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

len_of_names = len(names)

random_choice= random.randint(0, len_of_names - 1)

person_who_pays = names[random_choice]

print(person_who_pays + " is going to buy the meal today!")