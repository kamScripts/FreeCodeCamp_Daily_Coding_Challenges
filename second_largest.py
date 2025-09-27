def second_largest(arr:list)->int:
    """
    @FreeCodeCamp.org Daily Challange
    Given an array, return the second largest distinct number.
    second_largest([2, 3, 4, 6, 6])
    
    Returns: int
    """
    return sorted(set(arr))[-2]