def main():
    encoded = None
    while True:
        print('Menu \n ------------- \n 1. Encode \n 2. Decode \n 3. Quit')
        print()
        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
        elif option == '2':
            decoded = decode(encoded)
            print('The encoded password is '+ encoded + ' and the original password is ' + decoded + ".")
        elif option == '3':
            break
def encode(password):
    print('Your password has been stored')
    for item in password:
        temp = int(item) + 3
        new += str(temp)

    return new


#Cole Emerine is adding the decode file that decodes the encoded password back to the original
def decode(encoded)
    for item in encoded:
        temp = int(item)-3
        decode += str(temp)

    return decode