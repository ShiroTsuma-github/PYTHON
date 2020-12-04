import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183,
            173, 173,175, 178, 183, 193, 178, 173, 174, 183,
            183, 180, 168, 180, 170,178, 182, 180, 183, 178,
            182, 188, 175, 179, 183, 193, 182, 183,177, 185,
            188, 188, 182, 185, 191]

# print(heights)
heights_arr = np.array(heights)     
#zapsiuje wbudowana liste pythona na numpy array
print(heights_arr)
#dla kazdej pozycji wyzszej od 188(warunku) daje true,dla pozostalych false i potem sumuje true
print((heights_arr > 188).sum())    
#.size zwraca calkowity rozmiar arrayu
print(heights_arr.size)         
#.shape zwraca ksztalt naszego arrayu #jezeli chcemy znalezc ilosc wymiarow arrayu uzywamy to
print(heights_arr.shape)    
    
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 
        49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 
        51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 
        54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 
        64, 46, 54, 47, 70]
#połączenie w jedną liste 90 obiektów
heights_and_ages = heights + ages   
#zamiana tego w array 90 obiektów,który zamieniamy w 2 wymiarowy po 45 obiektów
heights_and_ages_arr = np.array(heights_and_ages).reshape((2,45))
print(heights_and_ages_arr.shape)
print(heights_and_ages_arr)
print(heights_and_ages_arr.dtype)       #wyswietla typ danych z arrayu

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 
                 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 
                 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]





