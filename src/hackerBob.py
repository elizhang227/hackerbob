user_input = input('Please enter a string: ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
password = 'abc'
ciphered = ""
rotate_by = 13
i = 0

for char in user_input:
    index_in_alphabet = alphabet.index(char)
    new_index = index_in_alphabet + rotate_by
    if new_index >= len(alphabet):
        new_index = new_index - len(alphabet)
    ciphered += alphabet[new_index]
    #print(ciphered) #can comment out

if ciphered == password:
    print('You got it right')
else:
    print('Wrong sucka')

### To return which letter was right ###

# for char in ciphered:
#     if ciphered == password[i]:
#         print('you guessed it')
#         i += 1
#     else:
#         print('you wrong')
#         i += 1
