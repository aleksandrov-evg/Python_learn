i = int(input())
deviation = 0
numberInput = 0
SumInput = 0
SumInputSquare = 0
while i != 0:
    SumInput += i
    SumInputSquare += i ** 2
    numberInput += 1
    i = int(input())
    if i == 0 and numberInput > 1:
        deviation = ((SumInputSquare -
                      ((SumInput ** 2) / numberInput)) /
                     (numberInput - 1)) ** 0.5
print(deviation)
