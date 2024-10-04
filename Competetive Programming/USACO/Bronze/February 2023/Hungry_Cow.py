N, T = map(int, input().split())
days = [tuple(map(int, input().split())) for _ in range(N)] + [(T + 1, 0)]

curr_bale = 0
curr_day = days[0][0]
bales_ate = 0

for day in days:
    if day[0] - curr_day > curr_bale:
        bales_ate += curr_bale
        curr_bale = 0
    else:
        bales_ate += day[0] - curr_day
        curr_bale -= day[0] - curr_day 
    
    curr_bale += day[1]
    curr_day = day[0]
        
print(bales_ate)