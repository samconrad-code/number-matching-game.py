items = [2, 6, 13, 20, 21, 34, 45]

user_input = []
for i in range(1, 8):
    number = int(input(f"Enter number {i}: "))
    user_input.append(number)

matches = 0
for number in user_input:
    for item in items:
        if number == item:
            matches = matches + 1
            break

print(f"You matched {matches} number(s).")
if matches == 7:
    print("You Win! ")
else:
    print("Nice try!")