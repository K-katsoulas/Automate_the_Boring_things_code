while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello , Joe . What it the password (it is a fish) ')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted !')
