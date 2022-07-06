#   Exercise 2-2
#
#   Using only single-character output statements that output a hash mark,
#   a space, or an end-of-line symbol, write a program that outputs the
#   following shape:
#
#      ##
#     ####
#    ######
#   ########
#   ########
#    ######
#     ####
#      ##
#


# Top Half
toprows = 1

while toprows <= 4:
    tophash = 1
    topspace = 1

    while topspace <= 3 - (toprows -1):
        print(' ', end=' ')
        topspace += 1

    while tophash <= 2 + 2 * (toprows - 1):
        print('#', end=' ')
        tophash += 1
    toprows += 1
    print('\n')


# Bottom Half

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