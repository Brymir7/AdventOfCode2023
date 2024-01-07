_input = None
with open("inputs/02.txt", 'r') as f:
    _input = f.read()
_input = _input.split("\n")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

res = {}

for game in _input:
    _id_idx = game.find(":")
    _id_str = ""
    while game[_id_idx-1].isdigit():
        _id = game[_id_idx-1]
        _id_str += _id
        _id_idx -= 1
    _id = _id_str[::-1]
    res[_id] = True
    mini_games = game.split(";")

    for mini_game in mini_games:
        amount_blue = 0
        amount_red = 0
        amount_green = 0
        if "blue" in mini_game:
            idx = mini_game.find("blue")
            reversed_string_numbers = ""
            while mini_game[idx-2].isdigit():
                reversed_string_numbers+=mini_game[idx-2]
                idx -= 1
            amount_blue += int(reversed_string_numbers[::-1])
        if "red" in mini_game:
            idx = mini_game.find("red")
            reversed_string_numbers = ""
            while mini_game[idx-2].isdigit():
                reversed_string_numbers+=mini_game[idx-2]
                idx -= 1
            amount_red += int(reversed_string_numbers[::-1])
        if "green" in mini_game:
            idx = mini_game.find("green")
            reversed_string_numbers = ""
            while mini_game[idx-2].isdigit():
                reversed_string_numbers+=mini_game[idx-2]
                idx -= 1
            amount_green += int(reversed_string_numbers[::-1])

        if amount_blue > MAX_BLUE:
            print("_id", _id)
            res[_id] = False
        if amount_red > MAX_RED:
            print("_id:", _id)
            res[_id] = False
        if amount_green > MAX_GREEN:
            print("_id:", _id)
            res[_id] = False
        if _id == "16":
            print("Blue:", amount_blue)
            print("Red:", amount_red)
            print("Green:", amount_green)
            
            
res_sum = 0
for key, value in res.items():
    if value:
        print("ID:", key, "is valid")
    if value:
        res_sum += int(key)
print(res_sum)