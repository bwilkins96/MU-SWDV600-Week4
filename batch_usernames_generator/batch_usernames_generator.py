# Takes names from a file and generates a new file with usernames

def main():
    in_file = open('users-csv.txt', 'r')
    out_file = open('usernames-csv.txt', 'w')

    for line in in_file:
        names = line.split(',')
        usernames = []

        for name in names:
            first_name, last_name = name.strip().split(' ')
            username = (last_name[:5] + first_name[:2]).lower()
            usernames.append(username)

        for username in usernames:
            print(username, end=', ', file=out_file)
        
        print(file=out_file)

    in_file.close()
    out_file.close()
    print('All done!')

main()