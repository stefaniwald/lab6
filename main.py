def menu():
    print('Menu')
    print('------------- ')
    print('1. Encode ')
    print('2. Decode ')
    print('3. Quit')

def encode(password):
    new_pass = ''
    for num in password:
        new_pass += str(int(num) + 3)
    return new_pass

if __name__ == "__main__":
    while True:
        menu()
        menu_op = int(input('\nPlease enter an option: '))
        if menu_op == 1:
            original_password = input('Please enter your password to encode ')
            encoded_password = encode(original_password)
            print('Your password has been encoded and stored!\n')
        elif menu_op == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}.\n')
        else:
            break
