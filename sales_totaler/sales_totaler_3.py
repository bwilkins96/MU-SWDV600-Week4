# Takes sales numbers from a file and outputs a file 
# with those rows and the sum at the end
# alternative version 2

def main():
    sales_file_name = input('Enter sales file name: ')
    totals_file_name = input('Enter name for total sales file: ')

    sales_file = open(sales_file_name, 'r')
    totals_file = open(totals_file_name, 'w')

    for row in sales_file:
        total = 0
        values = row.split(' ')

        for i in range(len(values)):
            val = float(values[i].strip()[1:])
            total += val
            values[i] = (f'${val:8.2f}')
        
        values.append(f'${total:8.2f}')
        new_row = ' '.join(values)

        print(new_row, file=totals_file)

    sales_file.close()
    totals_file.close()

    print(f'\nDone writing totals to {totals_file_name}')

main()