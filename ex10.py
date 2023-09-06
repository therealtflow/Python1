
w = input('Enter a word or phrase: ')
l = list(w)
a = list


a = [[l[x], l[x+1], l[x+2]] for x in range(0,3)]
if len(l)%3 == 0 : 
    a.append([l[len(l)-3], l[len(l)-2], l[len(l)-1]])
if len(l)%3 == 2 :
    a.append([l[len(l)-2], l[len(l)-1]])
else : 
    a.append([l[len(l)-1]])

print(a)


