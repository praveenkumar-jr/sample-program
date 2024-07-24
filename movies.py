membership=str(input('member or non-member:'))
person_age=int(input('enter your age:'))
if membership=='yes':
    print('member')
    print('you will get a flat rate of $8')
else:
    print('non member')
if person_age<12:
    print('$5')
elif person_age<=17:
    print('$7')
elif person_age<=64:
    print('$10')
elif person_age>64:
    print('$6')            
               
               