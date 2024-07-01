
alphabet = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, 
            "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, 
            "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}

def value(message):
    total_value = 0
    for letter in message:
        for key, value in alphabet.items():
            if str(letter) == key:
                total_value = total_value + value
            break
    return total_value


def position(total_value, position):
    position, total_value, rounds = position, total_value, 0
    while True:
        if total_value > 25:
            total_value = total_value - 25
            rounds = rounds + 1
        elif total_value + position > 25:
            total_value = (total_value + position - 1) - 25
        else:
            break
    return rounds, total_value

input_message = "EWPGAJRB"
first_message, second_message = input_message[:int(len(input_message)/2)], input_message[int(len(input_message)/2):]

first_message_value = value(first_message)
final = ""
for x in first_message:
    for x1, y1 in alphabet.items():
        if x1 == x:
            rounds, total_value = position(first_message_value, y1)
            for x2, y2 in alphabet.items():
                if y2 == total_value:
                    print(x2)
            

print(final)