x=int(input('weigth of package :'))
y=str(input('shipping method :'))
if x==1:
    if y=='standard':
        print('$5')
    elif y=='express':
        print('$10')
if x<=5:
    if y=='standard':
        print('$10')
    elif y=='express':
        print('$20')
if x>5:
    if y=='standard':
        print('$15')
    elif y=='express':
        print('$30')                        
    
    