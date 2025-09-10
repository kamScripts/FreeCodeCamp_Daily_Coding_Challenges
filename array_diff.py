def array_diff(arr1,arr2):
    """Given two arrays with strings values, return a new
    array containing all the values that appear in only
    one of the arrays.
    
    arr1: [*str],\n
    arr2: [*str] 
    
    Returns: [arr1 \ arr2]
    """
    return sorted((set(arr1) ^ set(arr2)))
if __name__ == "__main__":
    diff=array_diff(['a','b','c', 'e'], ['a','b','c','d'])
    print(diff)