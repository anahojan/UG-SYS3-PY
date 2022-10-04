

#Naloga1 loop
from tkinter import N
from token import NEWLINE


sez = [2, 6, 44, 85, 21]
for x in sez:
    y=x*x
    print(y)

#4
#36
#1936
#7225
#441
print('\n')

#Naloga2


from random import randint

value=randint(1,24)
print(value)

print('\n')

#naloga3
for x in range(10):
    if x==0:
        print('Current number: ' + str(x)  + ' Previous number: '+  str(0) + ' Sum ' + str(x) )
    else:
        print('Current number: ' + str(x)  + ' Previous number: '+  str(x-1) + ' Sum ' + str(x+x-1) )

# Current number: 0 Previous number: 0 Sum 0
# Current number: 1 Previous number: 0 Sum 1
# Current number: 2 Previous number: 1 Sum 3
# Current number: 3 Previous number: 2 Sum 5
# Current number: 4 Previous number: 3 Sum 7
# Current number: 5 Previous number: 4 Sum 9
# Current number: 6 Previous number: 5 Sum 11
# Current number: 7 Previous number: 6 Sum 13
# Current number: 8 Previous number: 7 Sum 15
# Current number: 9 Previous number: 8 Sum 17

#naloga4

def remove_char(str, n):
    s=str[n:]
    print(s)

remove_char("python", 4)
#on