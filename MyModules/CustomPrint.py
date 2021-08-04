def Pprint(text, title='Not specified',letter_threshold=25,**more_text):
    """Function that takes by default text and title and prints it formated.

    Note:
        It can print more than one thing if it has more arguments as `**kwargs`
        
    Args:
    
        text (str): Data that you want to be displayed after title.
        
        title (str, optional): Title of Data. Defaults to 'Not specified'. 
        
        ::
        
            letter_threshold (int, optional): Number of letters after which Data will be displayed in next line. Defaults to 25.
        
    Examples:
        By passing more arguments like presented you can get better results.
        ::
        
            >>> Pprint([0,1,2,3,4],'First array: ',25,second_array=[5,6,7,8,9],extra_info='This was passed as **kwargs')
            
            ================================================================================

            [ First array:  ]       :  [0, 1, 2, 3, 4]

            [ second array ] :  [5, 6, 7, 8, 9]

            [ extra info ] :

            This was passed as **kwargs

            ================================================================================
        
    """

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
    
def Tprint(text,max_size=120,char=' '):
    """Prints text centered and padded by choosen character.

    Note:
        Usage with `UTF-8` characters is problematic because of them weirdly counting to text length.
    
    Args:
    
        text (str): Text that is centered.
        ::
        
            max_size (int, optional): Width of characters that we want text to be centered in. Defaults to 120.
        char (str, optional): Character that text will be padded with. Defaults to ' '.
        
    Examples:
        >>> Tprint('Title that is centered',char='=')
        =================== Title that is centered ===================
    """
    print(int((max_size-len(text))/2)*char,text,int((max_size-len(text))/2)*char)
    
from math import ceil,floor
def printTable(table_to_copy,title=None,screen_width=162):
    """Provided table of `int` of `float` data (at the moment) displays it formatted and more friendly for reading. The cells are formatted,
    for longest number provided and rows and cells are numbered. Allows for providing title to display and screen width (only usefull to change if working on smaller windows size.
    Prevents line split on smaller screen)

    Args:
        table (list): List of `int` or `float` data.
        title (str, optional): Title to be displayed on top of table. Defaults to None.
        screen_width (int, optional): Just amount of characters to print in lines before title. Defaults to 162.
    """
    table_to_copy=tuple(table_to_copy)
    table=list(table_to_copy)
    
    def Title(title):
        """Starts with printing for whole width of screen `=`, then `*` and then based on length of title prints it in middle, followed by `=`
        symbols in front and back

        Args:
            title (str): The message that should be displayed on top.
        """
        print(screen_width*'=',end='')
        print(screen_width*'*')
        title_length=len(str(title))
        centering_amount=int((screen_width-title_length)/2)
        if title_length<screen_width-4:
            print(centering_amount*'=',title,(screen_width-centering_amount-title_length-2)*'=')
        else:
            print(title)
            
    def Table():
        """Prints table with numbers inside formatted for longest number inside to keep shape.
        """
        
        def TopNumbers():
            """Displays on top of table. Shows cell number in a row.
            """
            numbers=[number for number in range(0,cells_in_row)]
            for i in numbers:
                left_difference=ceil((max_length+3)/2)
                right_difference=max_length+3-left_difference-1+1-len(str(i))
                print(f'{left_difference*" "}{i}{right_difference*" "}',end='')
            print('')
            
        def RowNumber(position=None):
            """Shows on left of table number of row. Displays number of row. If `None` it only prints blank characters to keep shape.

            Args:
                position (int, optional): Shows which number of row to display. Defaults to None.
            """
            left_padding=len(str(table_rows))+2
            if position==None:
                print((left_padding)*' ',end='')
            else:
                print(f'{position}{(left_padding-len(str(position)))*" "}',end='')  
                
                 
        cell_interior_width=max_length+2
        cells_in_row=floor(100/(cell_interior_width))
        table_width=cells_in_row*(cell_interior_width)+1
        table_rows=ceil(len(table)/cells_in_row)
        missing_to_shape=cells_in_row-(len(table)%cells_in_row)
        [table.append(' ') for pos in range(0,missing_to_shape+1)]
        
        RowNumber()
        TopNumbers()
        RowNumber()
        
        print(f'┏{(cells_in_row-1)*(cell_interior_width*"━"+"┳")}{cell_interior_width*"━"+"┓"}')
        for i in range(0,table_rows):
            RowNumber(i)
            for j in range(0,cells_in_row):
                number=table[i*cells_in_row+j]
                left_difference=int((max_length-len(str(number)))/2)
                right_difference=max_length-len(str(number))-left_difference
                if j==0:
                    print(f'┃ {left_difference*" "}{number}{right_difference*" "} ',end='')
                elif j==cells_in_row-1:
                    print(f'┃ {left_difference*" "}{number}{right_difference*" "} ┃')
                else:
                    print(f'┃ {left_difference*" "}{number}{right_difference*" "} ',end='')
            RowNumber()
            if i!=table_rows-1:
                print(f'┣{(cells_in_row-1)*(cell_interior_width*"━"+"╋")}{cell_interior_width*"━"+"┫"}')
            else:
                print(f'┗{(cells_in_row-1)*(cell_interior_width*"━"+"┻")}{cell_interior_width*"━"+"┛"}')
            
    if title!=None:
        Title(title) if len(title)>0 else print('')
        
    max_length=max(list(map(lambda x: len(str(x)),table)))
    all_nums=all(isinstance(pos,(int,float)) for pos in table)
    if all_nums:
        Table()
        
        

  
if __name__=='__main__':
    printTable([1,2,3,0,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2000,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2])

  