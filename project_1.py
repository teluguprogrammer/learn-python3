products = [
    {
    'id': 1, 
    'name': 'Apple', 
    'price': 200, 
    'quantity': 20
    }, 
    {
    'id': 2, 
    'name': 'Milk', 
    'price': 20, 
    'quantity': 100
    }, 
    {
    'id': 3, 
    'name': 'Rice', 
    'price': 500, 
    'quantity': 20
    }, 
    {
    'id': 4, 
    'name': 'Pepsi', 
    'price': 55, 
    'quantity': 20
    }, 
] 

print('-----------------------------------------------')
print('\t\tSuper Market')
print('-----------------------------------------------')
print('SNo\tName\tPrice\tQuantity')
print('-----------------------------------------------')
for product in products:
    print(product['id'],'\t', product['name'],'\t', product['price'], '\t',product['quantity'])
print('-----------------------------------------------')

total_bill = 0
while True:
    item = int(input('Add item to cart: '))
    quant = int(input('How much: '))
    for product in products:
        if item == product['id']:
            total_bill = product['price'] * quant + total_bill
    choice = input('do you want add another item(y/n): ')
    if choice.lower() == 'n':
        if total_bill >=2000:
            total_bill = total_bill - (total_bill * 5 / 100 )
            print('congrats, you got 5 % discount')
        print('Total Bill Amount: ', total_bill)
        break
    

# item_1 = input('enter your product name: ')
# price_1 = 200
# quan_1 = int(input('enter the quantity: '))

# item_2 = input('enter your product name: ')
# price_2 = 16.50
# quan_2 = int(input('enter the quantity: '))

# item_3 = input('enter your product name: ')
# price_3= 1300
# quan_3 = int(input('enter the quantity: '))

# total_amount = price_1 * quan_1 + price_2 * quan_2 + price_3 * quan_3

# if total_amount >= 2000:
#     discount_amount = int(total_amount * 5 / 100)


# print('-----------------------------------------------')
# print('\t\tSuper Market')
# print('-----------------------------------------------')
# print('SNO\tProduct\tPrice\tQuantity\tAmount')
# print('-----------------------------------------------')
# print('1.\t', item_1,'\t',price_1, '\t', quan_1, '\t\t', price_1 * quan_1 )
# print('2.\t', item_2,'\t',price_2, '\t', quan_2, '\t\t', price_2 * quan_2 )
# print('3.\t', item_3,'\t',price_3, '\t', quan_3, '\t\t', price_3 * quan_3 )
# print('------------------------------------------------')
# print('\t\tActual Amount = ', total_amount)
# print('\t\tDiscount Amount(5%) = ', discount_amount)
# print('-----------------------------------------------')
# print('\t\tTotal Bill Amount = ', total_amount - discount_amount)