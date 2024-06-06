def welcome():   
    print('Hi! Welcome to Mcdonalds')
    print('1) Cheeseburger')
    print('2) Fries')
    print('3) Soda')
    print('4) Ice Cream')
    print('5) Cookie')


def get_item(x):
    if x == 1:
        return 'Cheeseburger'
    elif x == 2:
        return 'Fries'
    elif x == 3:
        return 'Soda'
    elif x == 4:
        return 'Ice Cream'
    elif x == 5:
        return 'Cookie'
    else: 
        return 'Invalid item'
    
def main():
    welcome()
    item = int(input('What do you want?: '))
    print(get_item(item))

main()
    


    