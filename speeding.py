def speeding(speeds: list, limit: int) ->list:
    """
    @FREECODECAMP.ORG DAILY CHALLENGE
    https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-26
    
    Given an array of numbers representing the speed at which vehicles were observed traveling,
    and a number representing the speed limit, return an array with two items,
    the number of vehicles that were speeding, followed by the average amount beyond
    the speed limit of those vehicles.

    If there were no vehicles speeding,
    return [0, 0]
    ELSE
    return [TOTAL, AVG].
    """
    res={"count":0,"total":0}
    for s in speeds:
        if s > limit:
            res["count"]+=1
            res["total"]+=s-limit
    if res["total"]>0:
        res["total"]=res["total"]/res["count"]
    return [res["count"],res["total"]]