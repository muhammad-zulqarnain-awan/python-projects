
letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encoding(letters_list, message, shift_number):

    encoded_message = ""

    for index in range(len(message)):
        if message[index] in letters_list:
            char = message[index]
            new_char = letters_list[(letters_list.index(char) + shift) % len(letters_list)]
            encoded_message += new_char
        else:
            encoded_message += message[index]

    return encoded_message

def decoding(letters_list, message, shift_number):

    decoded_message = ""

    for index in range(len(message)):
        if message[index] in letters_list:
            char = message[index]
            new_char = letters_list[(letters_list.index(char) - shift) % len(letters_list)]
            decoded_message += new_char
        else:
            decoded_message += message[index]
    return decoded_message

end = False
while end == False:
    user_choice = input('Type "encode" for encryption, and "decode" for decryption.\n')

    if user_choice == "encode":
        message = input("Type the message you want to encode: ")
        shift = int(input("Enter the number you want to shift the letters: "))

        print(f"Encoded Message: {encoding(letters_list,message,shift)}")

    elif user_choice == "decode":
        message = input("Type the message you want to decode: ")
        shift = int(input("Enter the number you want to shift the letters: "))

        print(f"Encoded Message: {decoding(letters_list,message,shift)}")

    cont = input('Do you want to start again? "Yes" or "No"\n')
    
    if cont == "No":
        print("Thank you for using our service!")
        end = True
