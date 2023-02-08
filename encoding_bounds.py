# Prints the char values represented by an inputted range of numbers

def main():
    lower = int(input('Enter the lower ordinal bound: '))
    upper = int(input('Enter the upper ordinal bound: '))

    print(f'\nThe characters from {lower} to {upper} are:')
    for i in range(lower, upper+1):
        print(chr(i), end=" ")
    
    print()

main()