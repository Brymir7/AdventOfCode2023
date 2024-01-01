
# input
_input = None
with open("inputs/01.txt", 'r') as f:
    _input = f.read()
_input = _input.split("\n")

digit_str_to_int = {
    "one" : "1",
    "two" : "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
solution = []
for word in _input:
    digits = []
    digit_strings_in_word = []

    for idx, char in enumerate(word):       
        if char.isdigit():
            digits.append((idx, char))
    for key, value in digit_str_to_int.items():
        idx_of_digit_string = word.find(key)
        if idx_of_digit_string != -1:
            digit_strings_in_word.append((idx_of_digit_string, value))
    print("Digits in word:", digit_strings_in_word)
    print("Integers in word:", digits)         
    res = {}
    for idx, value in digits:
        if idx not in res:
            res[idx] = value
    for idx, value in digit_strings_in_word:
        if idx not in res:
            res[idx] = value
    
    minimum = min(res.keys())
    maximum = max(res.keys())  
    number_for_word = res[minimum]+res[maximum]
    print(number_for_word)
    solution.append(int(number_for_word))

print(sum(solution))