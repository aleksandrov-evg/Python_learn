number = input()
textNext = 'The next number for the number '
textPrev = 'The previous number for the number '
strNext = textNext + number + ' is ' + str(int(number) + 1) + '.'
strPrev = textPrev + number + ' is ' + str(int(number) - 1) + '.'
print(strNext)
print(strPrev)
