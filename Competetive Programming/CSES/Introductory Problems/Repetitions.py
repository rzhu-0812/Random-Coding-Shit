DNA = input()
 
max_chain = 0
chain = 1
prev = None
 
for char in DNA:
    if char == prev:
        chain += 1
    if chain > max_chain:
        max_chain = chain
    if char != prev:
        chain = 1
    prev = char
 
print(max_chain)