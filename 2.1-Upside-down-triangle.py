#
#   Exercise 2-1
#
#   Using only single-character output statements that output a hash mark,
#   a space, or an end-of-line symbol, write a program that outputs the
#   following shape:
#
#   ########
#    ######
#     ####
#      ##
#


myrow = 1


while myrow <= 4:
    hash = 0
    space = 1
    
    while space <= myrow - 1:
        print(' ', end=' ')
        space += 1
    
    while hash <= 9 - 2* myrow:
        print('#', end=' ')
        hash += 1
  
    myrow += 1
    print('\n')

