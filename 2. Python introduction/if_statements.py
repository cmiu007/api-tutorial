known_people = ['Jonh', 'Anna', 'Mary']
# person = input('Enter person name: ')

# if person in known_people:
#     print('You know {}'.format(person))
# else:
#     print('You don t know {}'.format(person))

#Exercise


# def who_do_you_know():
#     input_list = input('Enter list separated by comma: ')
#     a = input_list.split(",")
#     # clear spaces if any
#     result = []
#     for b in a:
#         result.append(b.strip())
#     return b
#     # Ask the user for a list'
#     # Split the string to a list
#     # Return tha list
    

def who_do_you_know_simplified():
    input_list = input('Enter the list separated by comma: ')
    return [name.strip().lower() for name in input_list.split(',')]
    
def ask_user():
    user_list = who_do_you_know_simplified()
    user_name = input('Enter the user name: ')
    if user_name.lower() in user_list:
        print('You know {}'.format(user_name))
    else:
        print('You don t know {}'.format(user_name))
    return 

ask_user()