class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # A method  describing the user
    def describe_user(self):
        print('=== SUMMARY USER ===')
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    # A method printing a greeting to the user
    def greet_user(self):
        #
        print(f'Hello, how are you, {self.first_name} {self.last_name}?')

    # Random method or something
    def description_user(self):
        print(f'User is logged in our site')

# Create several instances representing different users
main_user = User('James', 'Akash')
admin_user = User('N/A', 'N/A')
guest_user = User('0200321x', '0')

#
print('\n')
main_user.describe_user()
main_user.greet_user()
#
print('\n')
admin_user.describe_user()
admin_user.greet_user()
#
print('\n')
guest_user.describe_user()
guest_user.greet_user()
