#parent class
class User:
    name = "Mariah"
    email = "mariah@gmail.com"
    password = "hi123"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("welcome back, {}!".format(entry_name))
        else:
            print("The email or password entered is incorrect.")


#child class to User
class Subscriber(User):
    base_subscription = 7.00
    plan_name = "Premium"
    subscription_number = "93028"

     #child's method using subscription_number
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_subscription = input("Enter your subscription number: ")
        if (entry_email == self.email and entry_subscription == self.subscription_number):
            print("Welcome back our valued subscriber {}!".format(entry_name))
        else:
            print("Sorry, your subscription number does not match the email entered.")

#child class to User
class Administrator(User):
    admin_username = "administrator1"
    admin_password = "iamAdmin"

    #method using admin_password
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        admin_username = input("Enter your admin username: ")
        admin_password = input("Enter your admin password: ")
        if (entry_email == self.email and admin_password == self.admin_password):
            print("Welcome, admin!")
        else:
            print("Sorry, the credentials entered are invalid.")




