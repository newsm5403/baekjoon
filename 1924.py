x, y = map(int, input().split())
max_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
start = 0
for i in range(x-1):
    start = (max_day[i] % 7 + start) % 7
anw = (start + y % 7 - 1) % 7
print(week[anw])             