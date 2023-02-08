# A program that produces a username

def main():
    first_name = input('Enter your first name: ').lower()
    last_name = input('Enter your last name: ').lower()

    username = last_name[:5] + first_name[:2]
    print(f'\nYour username is {username}')

main()