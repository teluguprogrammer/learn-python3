def hello_name(name):
    print('Hello, ',name,'. How are you?')


def check_number(number):
    if number % 2 == 0:
        print('This is Even number.')
    else:
        print('This is Odd number.')


def check_max(a=0, b=0, c=0):
    if a >b:
        if a > c:
            return a
        else:
            print('max: ', c)
    else:
        if b > c:
            print('max: ', b)
        else:
            print('max: ', c)

        

def is_even(num):
    if num % 2 == 0:
        return True
    return False


sum_of_even = 0

for i in range(1, 101):
    value = is_even(i)
    if value:
        sum_of_even =  sum_of_even + i

print('sum of all even numbers till 100: ', sum_of_even)