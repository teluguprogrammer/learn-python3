# 1. input:  name, age
# 2. output: if age > 18 .. you are allowed to cost your vote. else: You are not allowed to cost your vote.

name = input('name: ')
age = int(input('age: '))
nationality = input('nationality: ')

if age >=18 and nationality.lower() == 'indian':
    print('Congrats, You can vote!!')
elif nationality.lower() != 'indian':
    print('Sorry, you are not Indian!!')
else:
    print('Sorry, try next year!!')