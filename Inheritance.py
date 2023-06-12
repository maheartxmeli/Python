#Creating class called User with attributes
class User:
    name = 'Anonymous'
    email = ''
    password = '2023pW!'
    account_number = 123456789

#creating child class Employee to add additional info to User class
class Employee(User):
    base_wage = 15.00
    department = 'Accounting'

#creating child class Customer to add additional info to User class
class Customer(User):
    mailing_address = ''
    mailing_list = True
