#TL;DR - uposledzone wytlumaczenie wymogow zadania,przez co zmarnowane punkty na podejrzenie kilku inputow, bo 
# przykladowe wytlumaczenia zawieraly bledy
def timeConversion(s):
    if "AM" in s:
        if int(s[:2])==12:
            return str(0)+str(int(s[:2])-12)+s[2:len(s)-2]
        return s[:len(s)-2]
    elif "PM" in s:
        if int(s[:2])==12:
            return s[:len(s)-2]
        return str(int(s[:2])+12)+s[2:len(s)-2]

s = input()     


result = timeConversion(s)

print(result)