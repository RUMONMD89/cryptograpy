alphabet = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']
message = open('message1.txt')
message = message.read()
message = message.split()

solution = ''

for number in message:
    num = int(number)
    decrypted_num = pow(num, -1, 41)
    solution += (alphabet[decrypted_num])

print(solution)
