my_set = { 1, 2, 3, 4, 5} # unordered unique elements

# dictionaires -> keys and values

my_dict = { 'name': 'Jose', 'age': 90, 'grades': [1, 20, 11, 14] }
my_dict2 = { 1: 20, 3: 77, 8: 210}

lottery_player = {
    'name': 'George',
    'numbers': (3, 4, 5, 2, 11) # tupple
}
print(lottery_player)
print(sum(lottery_player['numbers']))


universities_list = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'UCLA',
        'location': 'US'
    }
]
print(universities_list[1])
print('Univ name is : ' + universities_list[1]['name'])
