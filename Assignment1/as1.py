def combination(tuple):
    """
    usage : combination(tuple) -> print all combinations
    """
    nodup_list=[]
    for i in tuple:
        if i not in nodup_list:
            nodup_list.append([i])
    result = comb_div(nodup_list)
    for i in result:
        print(i, end = " ")

def comb_div(list):
    """
    combination divide section
    """
    listlen = len(list)
    if listlen <= 1:
        return list
    middle = listlen//2
    llist = comb_div(list[:middle])
    rlist = comb_div(list[middle:])
    return comb_cal(llist, rlist)

def comb_cal(left, right):
    """
    combination conquer section
    """
    new_list = left+right
    for i in left:
        for j in right:
            new_list.append(i+j)       
    return new_list

# if __name__ == "__main__":
#     list = {1,1,2,2,3,4,5,4}
#     combination(list)
#     ## test