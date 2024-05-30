#inputs
height = int(input('How tall are you? '))
credits = int(input('how many credits do you have? '))

if height >= 137 and credits >=10:
    print('Enjoy your ride!')
elif height < 137 and credits >= 10 :
    print('You are no tall enough to ride.')
elif height >= 137 and credits < 10:
    print('You dont have enough credits.')
else:
    print('You dont have any requirements.')