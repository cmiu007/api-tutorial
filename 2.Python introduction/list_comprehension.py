# my_list = [0, 1 , 2, 3, 4]

# an_equal_list = [ x for x in range(5)]
# print(an_equal_list)

# multiply_list = [ x * 3 for x in range(5) ]
# print(multiply_list)

# odd_numbers_list = [ n for n in range(10) if n % 2 == 0]
# print(odd_numbers_list)

people_you_know = ['Greg', ' John', 'anna', 'GREG']
normalised_people = [ person.strip().lower() for person in people_you_know]
print(normalised_people)

a = input('enter: ')
print(a.strip().lower())