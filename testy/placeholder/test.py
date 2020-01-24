basic_colors={
            "black":[[0,0,0],"#FFFFFF"],
            "maroon":[[128,0,0],"#800000"],
            "dark red":[[139,0,0],"#8B0000"],
            "brown":[[165,42,42],"#A52A2A"],
            "firebrick":[[178,34,34],"#B22222"],
            "crimson":[[220,20,60],"#DC143C"],
            "red":[[255,0,0],"#FF0000"],
            "tomato":[[255,99,71],"#FF6347"],
            "coral":[[255,127,80],"#FF7F50"],
            "indian red":[[205,92,92],"#CD5C5C"],
            "light coral":[[240,128,128],"#F08080"],
            "dark salmon":[[233,150,122],"#E9967A"],
}
wynik=""
try:
    hold=[]
    for x in basic_colors.values():
        hold.append(x)
    for x in range(0,len(hold)):
        print(hold[x][1])
        if hold[x][1] == "#FFFFFF":
            wynik=hold[x],x
    
except:
    raise 
finally:
    print("\n\n\n",wynik)
    pass