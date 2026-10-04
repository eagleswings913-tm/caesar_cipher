
action_type = ''
action_types = ['encode', 'decode']
users_message = ''
users_encoded_message = ''
users_decoded_message = ''
shift_number = 0
shift_number_range = [str(x) for x in range(1, 26)]
characters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters.extend(numbers)
exclusions = ['-', ',', ' ']

continue_play = True
while continue_play:
    while True:
        action = input('Enter action: (encode/decode): ').lower()
        if action in action_types:
            action = action.lower()
            break
        else:
            print('Invalid action! Please enter one of these actions encode/decode')

    users_message = input('Enter your message: ')
    while True:
        shift_number = input('Enter cipher shift number: (1 - 36) ')
        if shift_number in shift_number_range:
            shift_number = int(shift_number)
            break
        else:
            print('Invalid shift number! Please enter a number between 1 and 36')

    # create encoded message
    for letter in users_message:
        if letter in exclusions:
            users_encoded_message += letter
        elif letter not in characters:
            pass
        else:
            index = characters.index(letter)
            if index + shift_number > 35:
                users_encoded_message = users_encoded_message + characters[index + shift_number - 36]
            else:
                users_encoded_message = users_encoded_message + characters[index + shift_number]

    print(f'Here is your encoded message: {users_encoded_message}')
    # print(characters)
    if input('Do you want to play again? (y/n): ').lower() == 'n':
        continue_play = False
    else:
        action = ''
        users_message = ''
        users_encoded_message = ''
        shift_number = 0
print('Thank you for playing!')

