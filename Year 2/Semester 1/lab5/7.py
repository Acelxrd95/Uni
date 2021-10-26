def dbllist2dict(list1: list, list2: list) -> dict:
    if len(list1) == len(list2):
        ret_dict = {}
        for i in range(len(list1)):
            ret_dict.update({list1[i]: list2[i]})
    else:
        raise Exception("Lists are not equal in length")
    return ret_dict


li1 = ["Red", "Green", "Blue"]
li2 = [1, 2, 3]

print(dbllist2dict(li1, li2))
