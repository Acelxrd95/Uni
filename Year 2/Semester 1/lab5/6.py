def string2dict(string: str) -> dict:
    ret_dict = {}
    for char in string:
        if char.isalpha():
            if char in ret_dict:
                ret_dict[char] += 1
            else:
                ret_dict.update({char: 1})
    return ret_dict


print(string2dict("Hello World"))
