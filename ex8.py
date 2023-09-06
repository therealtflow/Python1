numlist = []
seen = []
dup = []
onelist = []
count = 1

while count < 11 : 
    i = input('Enter number: ')
    numlist.append(i)
    count += 1

for i in numlist : 
    dup.append(i) if i in seen else seen.append(i)

for i in seen : 
    if i not in dup : onelist.append(i)
    
print('Original List: ', numlist)
print('Numbers that appear only once: ', onelist )

