# Encrypts an inputted message using a Caesar cipher
# with an inputted shift key and stores encrypted message in a file

def main():
    message = input('Enter the message to encrypt: ')
    key = int(input('Enter the shift key: '))
    output_file_name = input('Enter the output file name: ')

    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[len(alphabet) - key:] + alphabet[:len(alphabet) - key]

    encrypted_message = ''
    for char in message:
        letter_idx = alphabet.find(char)
        encrypted_char = shifted_alphabet[letter_idx]

        if letter_idx > -1:
            encrypted_message += encrypted_char
        else:
            encrypted_message += char

    output_file = open(output_file_name, 'w')
    print(encrypted_message, file=output_file)
    output_file.close()
        
    print(f'Done writing encrypted message to {output_file_name}')

main()