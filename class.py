
class User:
    #defining the attributes
    name = 'name'
    email = ''
    password = 'password123'
    account = 0

    #assign values to object properties using the __init__() function
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    #defining methods of the class
    def account(self):
        email_input = input('Enter your email: ')
        password_input = input('Enter your password: ')
        if (email_input == self.email and password_input == self.password):
            print('Welcome back, {}'.format(self.name))
        else:
            print('You do not have authorization to enter.')


if __name__ == '__main__':
    #creating object
    firstUser = User('Mabel', 'm.young@company.com', 'Pw!2020', '13490')
    print(firstUser.name)
