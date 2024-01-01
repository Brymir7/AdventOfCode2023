_input = None
with open("inputs/02.txt", 'r') as f:
    _input = f.read()
_input = _input.split("\n")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

res = {}

for game in _input:
    _id = game.split(":")[0][-1]
    res[_id] = True
    mini_games = game.split(";")
    amount_blue = 0
    amount_red = 0
    amount_green = 0
    for mini_game in mini_games:
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
        print("blue", amount_blue)
        print("green", amount_green)
        print("red", amount_red)
    if amount_blue > MAX_BLUE:
        res[_id] = False
    if amount_red > MAX_RED:
        res[_id] = False
    if amount_green > MAX_GREEN:
        res[_id] = False
res_sum = 0
for key, value in res.items():
    if value:
        res_sum += int(key)
print(res_sum)