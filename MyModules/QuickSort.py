def QuickSortNestedList(array):
    """Quick sort using recursion that allows sorting lists

    Args:
    
        array (list): List of lists 

    Note:
        It sorts by `first` object of list in every position, so first object in nested list should be `numeric`
    
    Returns:
    
        list : sorted list of lists by first object
    Examples:
        >>> x=[[5,'cake'],[1,'soda'],[12,'pizza'],[-2,'spoon']]
        >>> result=QuickSortNestedList(x)
        >>> print(result)
        [[-2, 'spoon'], [1, 'soda'], [5, 'cake'], [12, 'pizza']]
    """
    
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0][0]
        for x in array:
            if x[0] < pivot:
                less.append(x)
            elif x[0] == pivot:
                equal.append(x)
            elif x[0] > pivot:
                greater.append(x)
        return QuickSortNestedList(less)+equal+QuickSortNestedList(greater)
    else:
        return array
def QuickSortList(array):
    """Quick sort using recurention that allows sorting lists

    Args:

        array (list): List of objects

    Note:
        Every object in list should be `numeric`
    
    Returns:
    
        list : sorted objects
    Examples:
        >>> x=[5,1,12,-2]
        >>> result=QuickSortList(x)
        >>> print(result)
        [-2,1,5,12]
    """
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return QuickSortList(less)+equal+QuickSortList(greater)
    else:
        return array
    
    
