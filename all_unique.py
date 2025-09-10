def all_unique(s):
    """Task @FreeCodeCamp.org<br/>
    Determine if all characters in the string are unique.
    
    s:str
    
    Returns: Bool
    """
    val=''
    for l in s:
        if l in val:
            return False
        val+=l
    return True
if __name__=="__main__":
    print(all_unique("abc"))
         