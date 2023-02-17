print('What is your name? ')
user_name = input()
user_name = user_name.title()

print('How old are you? ')
user_age = int(input())

user_birthyear = (2023 - user_age) #this doesn't account for birthdays that haven't happened in the current year.

print( 'Hello', str(user_name)+'!', 'You were born in', str(user_birthyear)+'.' )