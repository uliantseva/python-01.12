
def password_required(fun):
    def credentials_():
        password = input('Please enter password: ')
        if password == '1234':
            print('Correct password')
            fun()
        else:
            print('Incorrect password')
    return credentials_

@password_required
def bank_credentials():
    print("Bank card: 0000-1111-2222-3333-4444")
    print("Bank password: 1234")
    print("amount: 100 000 000$")

@password_required
def instagram_credentials():
    print("username: snowden")
    print("password: cia")

bank_credentials()
instagram_credentials()
