#SHITTY CODE,ALE NIE CHCIALO MI SIE TE ZADANIE ROBIC LEPIEJ

def dayOfProgrammer(year):
    leap=0
    day=256
    if year==1918:
        day+=13
    if year<=1917:
        if year%4==0:
            leap=1
    else:
        if (year%400==0) or (year%4==0 and year%100!=0):
            leap=1
    days_from_start_to_month_end=(31,59,90,120,151,181,212,243,273,304,334,365)
    for position,month in enumerate(days_from_start_to_month_end):
        if day>=month and day<days_from_start_to_month_end[position+1]:
            return (f'{day-leap-month}.0{position+2}.{year}')
        
            

# year = int(input().strip())
year = 1918
result = dayOfProgrammer(year)
print(result)

