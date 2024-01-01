
# input
_input = None
with open("inputs/01.txt", 'r') as f:
    _input = f.read()
_input = _input.split("\n")

solution = []
for word in _input:
    digits = []
    for char in word:
        if char.isdigit():
            digits.append(char)
            break
    for char in word[::-1]:
        if char.isdigit():
            digits.append(char)
            break
    solution.append(int("".join(digits)))

print(sum(solution))