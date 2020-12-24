def Pprint(text, title='Not specified',letter_threshold=25,**more_text):
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
    
def Nprint(text, end='', flush=True):
    print(text, end=end, flush=flush)
    


