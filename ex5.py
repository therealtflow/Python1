
values1 = [int(input('Enter a number for the first list: ')) for _ in range(5)]
values2 = [int(input('Enter a number for the second list: ')) for _ in range(5)]

print('First List: ', values1)
print('Second List: ', values2)
print('Common List: ', (list(set(values1).intersection(values2))))

