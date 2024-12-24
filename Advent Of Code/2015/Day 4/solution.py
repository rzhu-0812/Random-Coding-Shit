import hashlib

key = 'iwrupvqb'
num = 0

while True:
    data = f'{key}{num}'.encode('utf-8')
    result = hashlib.md5(data).hexdigest()
   
    if result.startswith('00000'):
        print(num)
        break
    
    num += 1

num = 0

while True:
    data = f'{key}{num}'.encode('utf-8')
    result = hashlib.md5(data).hexdigest()
   
    if result.startswith('000000'):
        print(num)
        break
    
    num += 1
    