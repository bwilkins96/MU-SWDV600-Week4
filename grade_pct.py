# Takes a name, total points, and points scored on an assignment and prints 
# a formatted string conveying the grade percentage

def main():
    name = input("Enter the student's name: ")
    possible_points = float(input('Enter how many points possible for the assignment: '))
    earned_points = float(input('Enter how many points earned for the assignment: '))
    
    percentage_score = (earned_points/possible_points) * 100

    formatted = "{0}'s percentage score is {1:0.2f}%".format(name, percentage_score)
    print('\n' + formatted)

main()