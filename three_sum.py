# Prints the sum of three user inputted numbers

def main():
    num_string = input('Enter your three numbers separated by commas: ')
    num_seq = num_string.split(',')

    sum = 0
    for num in num_seq:
        sum += int(num)

    print('\nThe sum is', sum)

main()