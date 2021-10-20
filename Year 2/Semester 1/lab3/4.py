arcolors = [
    ["purple", "red", "yellow", "blue", "green"],
    ["green", "purple", "orange", "pink", "blue"],
    ["white", "black", "purple", "black", "yellow"],
]
for i in range(len(arcolors)):
    for j in range(len(arcolors[i])):
        if arcolors[i][j] == "purple":
            arcolors[i][j] = "yellow"

print(arcolors)
