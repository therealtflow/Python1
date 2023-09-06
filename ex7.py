
list = []
i = input('Enter a number or enter QUIT to stop: ')
while i != str('QUIT') : 
    list.append(i)
    i = input('Enter a number or enter QUIT to stop: ')
if i == str('QUIT') : print(list)
