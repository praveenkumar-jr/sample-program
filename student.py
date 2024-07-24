stu_score=int(input('enter the score:'))
if stu_score>90:
    print('A')
elif stu_score>80:
    print('B')
elif stu_score>70:
    print('C')
elif stu_score>60:
    print('D')
elif stu_score<60:
    print('check all assingment')
assingment=str(input('check assingnment:'))
if assingment=='yes':
    print('E') 
elif assingment=='no':
    print('F')                  