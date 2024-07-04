
alphabet = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, 
            "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, 
            "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}

input_message = input("")
first_message, second_message = input_message[:int(len(input_message)/2)], input_message[int(len(input_message)/2):]

total_value = 0
for letter in first_message:
    for key, value in alphabet.items():
        if str(letter) == key:
            total_value = total_value + value
            break

print(total_value)
