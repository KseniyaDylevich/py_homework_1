x = int (input('введите координату x: \n')) 
y = int (input('введите координату y: \n'))

if (x > 0 and y > 0):
    print ('1')

if (x < 0 and y > 0):
    print ('2')

if (x < 0 and y < 0):
    print ('3')

if (x > 0 and y < 0):
    print ('4')