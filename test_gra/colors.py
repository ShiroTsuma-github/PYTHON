def color_convert(color):
    basic_colors={
                "maroon":[[128,0,0],"800000"],
                "dark red":[[139,0,0],"8B0000"],
                "brown":[[165,42,42],"A52A2A"],
                "firebrick":[[178,34,34],"B22222"],
                "crimson":[[220,20,60],"DC143C"],
                "red":[[255,0,0],"FF0000"],
                "tomato":[[255,99,71],"FF6347"],
                "coral":[[255,127,80],"FF7F50"],
                "indian red":[[205,92,92],"CD5C5C"],
                "light coral":[[240,128,128],"F08080"],
                "dark salmon":[[233,150,122],"E9967A"],
                "salmon":[[250,128,114],"FA8072"],
                "light salmon":[[255,160,122],"FFA07A"],
                "orange red":[[255,69,0],"FF4500"],
                "dark orange":[[255,140,0],"FF8C00"],
                "orange":[[255,165,0],"FFA500"],
                "gold":[[255,215,0],"FFD700"],
                "dark golden rod":[[184,134,11],"B8860B"],
                "golden rod":[[218,165,32],"DAA520"],
                "pale golden rod":[[238,232,170],"EEE8AA"],
                "dark khaki":[[189,183,107],"BDB76B"],
                "khaki":[[240,230,140],"F0E68C"],
                "olive":[[128,128,0],"808000"],
                "yellow":[[255,255,0],"FFFF00"],
                "yellow green":[[154,205,50],"9ACD32"],
                "dark olive green":[[85,107,47],"556B2F"],
                "olive drab":[[107,142,35],"6B8E23"],
                "lawn green":[[124,252,0],"7CFC00"],
                "chart reuse":[[127,255,0],"7FFF00"],
                "green yellow":[[173,255,47],"ADFF2F"],
                "dark green":[[0,100,0],"006400"],
                "green":[[0,128,0],"008000"],
                "forest green":[[34,139,34],"228B22"],
                "lime":[[0,255,0],"00FF00"],
                "lime green":[[50,205,50],"32CD32"],
                "light green":[[144,238,144],"90EE90"],
                "pale green":[[152,251,152],"98FB98"],
                "dark sea green":[[143,188,143],"8FBC8F"],
                "medium spring green":[[0,250,154],"00FA9A"],
                "spring green":[[0,255,127],"00FF7F"],
                "sea green":[[46,139,87],"2E8B57"],
                "medium aqua marine":[[102,205,170],"66CDAA"],
                "medium sea green":[[60,179,113],"3CB371"],
                "light sea green":[[32,178,170],"20B2AA"],
                "dark slate gray":[[47,79,79],"2F4F4F"],
                "teal":[[0,128,128],"008080"],
                "dark cyan":[[0,139,139],"008B8B"],
                "aqua":[[0,255,255],"00FFFF"],
                "cyan":[[0,255,255],"00FFFF"],
                "light cyan":[[224,255,255],"E0FFFF"],
                "dark turquoise":[[0,206,209],"00CED1"],
                "turquoise":[[64,224,208],"40E0D0"],
                "medium turquoise":[[72,209,204],"48D1CC"],
                "pale turquoise":[[175,238,238],"AFEEEE"],
                "aqua marine":[[127,255,212],"7FFFD4"],
                "powder blue":[[176,224,230],"B0E0E6"],
                "cadet blue":[[95,158,160],"5F9EA0"],
                "steel blue":[[70,130,180],"4682B4"],
                "corn flower blue":[[100,149,237],"6495ED"],
                "deep sky blue":[[0,191,255],"00BFFF"],
                "dodger blue":[[30,144,255],"1E90FF"],
                "light blue":[[173,216,230],"ADD8E6"],
                "sky blue":[[135,206,235],"87CEEB"],
                "light sky blue":[[135,206,250],"87CEFA"],
                "midnight blue":[[25,25,112],"191970"],
                "navy":[[0,0,128],"000080"],
                "dark blue":[[0,0,139],"00008B"],
                "medium blue":[[0,0,205],"0000CD"],
                "blue":[[0,0,255],"0000FF"],
                "royal blue":[[65,105,225],"4169E1"],
                "blue violet":[[138,43,226],"8A2BE2"],
                "indigo":[[75,0,130],"4B0082"],
                "dark slate blue":[[72,61,139],"483D8B"],
                "slate blue":[[106,90,205],"6A5ACD"],
                "medium slate blue":[[123,104,238],"7B68EE"],
                "medium purple":[[147,112,219],"9370DB"],
                "dark magenta":[[139,0,139],"8B008B"],
                "dark violet":[[148,0,211],"9400D3"],
                "dark orchid":[[153,50,204],"9932CC"],
                "medium orchid":[[186,85,211],"BA55D3"],
                "purple":[[128,0,128],"800080"],
                "thistle":[[216,191,216],"D8BFD8"],
                "plum":[[221,160,221],"DDA0DD"],
                "violet":[[238,130,238],"EE82EE"],
                "magenta / fuchsia":[[255,0,255],"FF00FF"],
                "orchid":[[218,112,214],"DA70D6"],
                "medium violet red":[[199,21,133],"C71585"],
                "pale violet red":[[219,112,147],"DB7093"],
                "deep pink":[[255,20,147],"FF1493"],
                "hot pink":[[255,105,180],"FF69B4"],
                "light pink":[[255,182,193],"FFB6C1"],
                "pink":[[255,192,203],"FFC0CB"],
                "antique white":[[250,235,215],"FAEBD7"],
                "beige":[[245,245,220],"F5F5DC"],
                "bisque":[[255,228,196],"FFE4C4"],
                "blanched almond":[[255,235,205],"FFEBCD"],
                "wheat":[[245,222,179],"F5DEB3"],
                "corn silk":[[255,248,220],"FFF8DC"],
                "lemon chiffon":[[255,250,205],"FFFACD"],
                "light golden rod yellow":[[250,250,210],"FAFAD2"],
                "light yellow":[[255,255,224],"FFFFE0"],
                "saddle brown":[[139,69,19],"8B4513"],
                "sienna":[[160,82,45],"A0522D"],
                "chocolate":[[210,105,30],"D2691E"],
                "peru":[[205,133,63],"CD853F"],
                "sandy brown":[[244,164,96],"F4A460"],
                "burly wood":[[222,184,135],"DEB887"],
                "tan":[[210,180,140],"D2B48C"],
                "rosy brown":[[188,143,143],"BC8F8F"],
                "moccasin":[[255,228,181],"FFE4B5"],
                "navajo white":[[255,222,173],"FFDEAD"],
                "peach puff":[[255,218,185],"FFDAB9"],
                "misty rose":[[255,228,225],"FFE4E1"],
                "lavender blush":[[255,240,245],"FFF0F5"],
                "linen":[[250,240,230],"FAF0E6"],
                "old lace":[[253,245,230],"FDF5E6"],
                "papaya whip":[[255,239,213],"FFEFD5"],
                "sea shell":[[255,245,238],"FFF5EE"],
                "mint cream":[[245,255,250],"F5FFFA"],
                "slate gray":[[112,128,144],"708090"],
                "light slate gray":[[119,136,153],"778899"],
                "light steel blue":[[176,196,222],"B0C4DE"],
                "lavender":[[230,230,250],"E6E6FA"],
                "floral white":[[255,250,240],"FFFAF0"],
                "alice blue":[[240,248,255],"F0F8FF"],
                "ghost white":[[248,248,255],"F8F8FF"],
                "honeydew":[[240,255,240],"F0FFF0"],
                "ivory":[[255,255,240],"FFFFF0"],
                "azure":[[240,255,255],"F0FFFF"],
                "snow":[[255,250,250],"FFFAFA"],
                "black":[[0,0,0],"000000"],
                "dim gray / dim grey":[[105,105,105],"696969"],
                "gray / grey":[[128,128,128],"808080"],
                "dark gray / dark grey":[[169,169,169],"A9A9A9"],
                "silver":[[192,192,192],"C0C0C0"],
                "light gray / light grey":[[211,211,211],"D3D3D3"],
                "gainsboro":[[220,220,220],"DCDCDC"],
                "white smoke":[[245,245,245],"F5F5F5"],
                "white":[[255,255,255],"FFFFFF"]
                }
    """
    copies=[]
    counter=0
    for i in basic_colors:
        for j in basic_colors:
            if basic_colors[j]==basic_colors[i]:
                counter+=1
        if counter>=2:
            copies.append(i)
        counter=0
    print(copies)
    """       
    color_to_use=basic_colors.get(color)
    return color_to_use        


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable


















#extending lines