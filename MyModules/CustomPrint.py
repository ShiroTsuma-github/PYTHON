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