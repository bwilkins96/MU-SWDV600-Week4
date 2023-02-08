# A program that takes a user multiplier and prints the products 
# of a sequence and the multiplier

def main():
    sequence = [52, 1, 34, 23, 18, -9, 21, 4, 79]
    multiplier = int(input('Enter your multiplier: '))

    print('\nThe products are:')

    for i in range(len(sequence)):
        print(sequence[i] * multiplier, end=" ")
    
    print()

main()