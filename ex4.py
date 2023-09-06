size = int(input('Enter a number: '))
values = [int(input('Enter a number: ')) for _ in range(size)]
print(values)
Sum = sum(values)
Average = Sum/size
print('Average: ' , Average)
