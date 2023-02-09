# A mad libs program based on the poem 'Ozymandias'
# Alternative version

def get_mad_lib(name, noun, place, verb, adjective, animal):
    mad_lib = 'My name is {0}, {5} of {5}s;\n'
    mad_lib += ('Look on my {1}s, ye {5}s, and {3}!\n')
    mad_lib += ('Nothing beside remains. Round the decay\n')
    mad_lib += ('Of that colossal {2}, boundless and {4}\n')
    mad_lib += ('The lone and {4} {1}s stretch far away.')

    return mad_lib.format(name, noun, place, verb, adjective, animal)

def main():
    print('--------------\nMad Lib Maker\n--------------')
    name = input('Name: ')
    noun = input('Noun: ')
    place = input('Place: ')
    verb = input('Verb: ')
    adjective = input('Adjective: ')
    animal = input('Animal: ')

    mad_lib = get_mad_lib(name, noun, place, verb, adjective, animal)
    print('\n' + mad_lib)
    
main()