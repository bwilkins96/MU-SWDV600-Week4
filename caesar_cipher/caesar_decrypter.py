# Decrypts a Caesar cipher encrypted message in an inputted file
# with an inputted shift key and prints it to the shell

def main():
    input_file_name = input('Enter the encrypted message file name: ')
    key = int(input('Enter the shift key: ')) 
    # use 3 for example.txt

    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[len(alphabet) - key:] + alphabet[:len(alphabet) - key]

    input_file = open(input_file_name, 'r')
    encrypted_message = input_file.read()

    message = ''
    for char in encrypted_message.strip():
        letter_index = shifted_alphabet.find(char)
        decrypted_char = alphabet[letter_index]

        if letter_index > -1:
            message += decrypted_char
        else:
            message += char

    input_file.close()
    print(f'\nThe message is: {message}')    

main()