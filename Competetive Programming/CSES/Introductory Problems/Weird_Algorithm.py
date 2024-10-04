num = int(input())
out = []
 
while num != 1:
    out.append(str(num))
    if num % 2 == 0:
        num = int(num / 2)
    else:
        num = int(3 * num + 1)
 
out.append("1")
 
print(" ".join(out))