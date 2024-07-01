
alphabet = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, 
            "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, 
            "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}

x = "BDFHJ"
pos = 4
y = 47

x = 0
while True:
    if y > 25:
        y = y - 25
        x = x + 1
    elif y + pos > 25:
        y = (y + pos - 1) - 25
    else:
        break
print(x, "", y)

