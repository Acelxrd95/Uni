string = input()
vowels = ["a","e","i","o","u"]
if string[0] in vowels:
    print(string + "ay") 
else:
    letter1 = string[0]
    rest = string[1:]
    print(rest + letter1 + "ay")