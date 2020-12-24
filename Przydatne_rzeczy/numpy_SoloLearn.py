import numpy as np
#					PAMIĘTAĆ ROW-X COLUMN-Y
#                      ARRAY[ROW,COLUMN]
def pprint(text, title='Not specified',letter_threshold=25,**more_text):
    print(80*'=')
    print('')
    text = str(text)
    if len(text) > letter_threshold:
        print(f'[ {title} ] :')
        print('')
        print(text)
    else:
        print(f'[ {title} ]	:  {text}')
    print('')
    for item in more_text:
        altered_item=item.replace('_',' ')
        if len(str(more_text[item])) <= letter_threshold:
            print(f'[ {altered_item} ] :  {more_text[item]}')
            print('')
        else:
            print(f'[ {altered_item} ] :')
            print('')
            print(more_text[item])
            print('')
    print(80*'=')
    
def Tprint(text,offset=40):
    print(offset*' ',text)
    
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183,
            173, 173,175, 178, 183, 193, 178, 173, 174, 183,
            183, 180, 168, 180, 170,178, 182, 180, 183, 178,
            182, 188, 175, 179, 183, 193, 182, 183,177, 185,
            188, 188, 182, 185, 191]

# print(heights)
heights_arr = np.array(heights)     
#zapsiuje wbudowana liste pythona na numpy array
Tprint('GETTING STARTED #1',32)
pprint(heights_arr,'Numpy heights array',
       Sum_of_objects_that_are_true_for_condition=(heights_arr > 188).sum(),
       Size_of_array=heights_arr.size,
       Shape_of_array=heights_arr.shape)
"""
dla kazdej pozycji wyzszej od 188(warunku) daje true,dla pozostalych false i potem sumuje true  
.size zwraca calkowity rozmiar arrayu       
.shape zwraca ksztalt naszego arrayu #jezeli chcemy znalezc ilosc wymiarow arrayu uzywamy to
""" 

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 
        49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 
        51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 
        54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 
        64, 46, 54, 47, 70]
#połączenie w jedną liste 90 obiektów
heights_and_ages = heights + ages   
#zamiana tego w array 90 obiektów,który zamieniamy w 2 wymiarowy po 45 obiektów
heights_and_ages_arr = np.array(heights_and_ages).reshape((2,45))
Tprint('GETTING STARTED #2',32)
pprint(heights_and_ages_arr.shape,'Shape of Heights and ages array',
       Heights_and_ages_array=heights_and_ages_arr,
       type_of_data_in_array=heights_and_ages_arr.dtype)	#.dtype wyswietla typ danych w arrayu

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183,   #ze wzgledu na wystepowanie floata [pozycja 0],
                 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178,  #cala lista zostanie zmieniona na floaty
                 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
Tprint('INDEXING AND SLICING',30)
pprint(heights_arr[2],'Third position in heights array',
       Getting_third_position_in_2D_array=heights_and_ages_arr[1,2],	#podajemy,ze chcemy pozycje [1][2] 
       Slicing_for_first_3_objects_in_2D_array=heights_and_ages_arr[0,0:3],	#podajemy, ze chcemy z array[0] pozyskac fragment [0:3]
       Slicing_for_specified_values_from_every_column=heights_and_ages_arr[:,0],    #dla kazdego z wymiarow arrayu wyswietla podana wartosc/przedzial
       )
Tprint('ASSIGNING VALUES',32)
heights_arr[3]=165
heights_and_ages_arr[0,2]=100
heights_and_ages_arr[1,:]=180
heights_and_ages_arr[:2,:2]=0
pprint('heights_arr[3] = 165','Changing value in single dimension array',30,
       Changed_heights_list=heights_arr,
       Changing_value_in_2D_array='heights_and_ages_arr[0,2] = 165', #dla obiektu 3 z y=0
       Changing_slice_of_list='heights_and_ages_arr[1,:] = 180',    #ustawienie dla każdego obiektu(y=1)=180
       Slicing_to_change_subset_of_the_array='heights_and_ages_arr[:2,:2] = 0',
       Changed_list=heights_and_ages_arr,
       )
Tprint('ASSIGNING AN ARRAY TO AN ARRAY',23)
heights_and_ages_arr[:,0]=[190,58]
new_record=np.array([[180,183,190],[54,50,69]])
heights_and_ages_arr[:,42:] = new_record
pprint('heights_and_ages_arr[:,0]=[190,58]','Changing value in fields works, as long, as shape of arrays matches',
       Updating_data_in_subarray_with_numpy_array='new_record=np.array([[180,183,190],[54,50,69]])',
       Usage='heights_and_ages_arr[:,42:] = new_record',
       Changed_list=heights_and_ages_arr,
    )
Tprint('COMBINING TWO ARRAYS',25)




