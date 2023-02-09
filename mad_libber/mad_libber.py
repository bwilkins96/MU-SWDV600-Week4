# A mad libs program based on the poem 'Ozymandias'

def print_mad_lib(name, noun, place, verb, adjective, animal):
    print('My name is {0}, {1} of {1}s;'.format(name, animal))
    print('Look on my {0}s, ye {1}s, and {2}!'.format(noun, animal, verb))
    print('Nothing beside remains. Round the decay')
    print('Of that colossal {0}, boundless and {1}'.format(place, adjective))
    print('The lone and {0} {1}s stretch far away.'.format(adjective, noun))

def main():
    print('--------------\nMad Lib Maker\n--------------')
    name = input('Name: ')
    noun = input('Noun: ')
    place = input('Place: ')
    verb = input('Verb: ')
    adjective = input('Adjective: ')
    animal = input('Animal: ')

    print()
    print_mad_lib(name, noun, place, verb, adjective, animal)

main()