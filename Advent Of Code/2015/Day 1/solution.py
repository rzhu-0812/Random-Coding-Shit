with open('input.txt', 'r')as i:
    str = i.read()

left_p = str.count('(')
right_p = str.count(')')

print(left_p - right_p)

floor = 0

for i in range(len(str)):
    if str[i] == '(':
        floor += 1
    elif str[i] == ')':
        floor -= 1
    
    if (floor < 0):
        print(i + 1)
        break