import random

rolls = 20
count_6 = 0
count_1 = 0
two_sixes_in_row = 0

prev_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    if roll == 6:
        count_6 += 1

    if roll == 1:
        count_1 += 1

    if roll == 6 and prev_roll == 6:
        two_sixes_in_row += 1

    prev_roll = roll

print("\n--- Statistics ---")
print("Number of times 6 appeared:", count_6)
print("Number of times 1 appeared:", count_1)
print("Two 6s in a row:", two_sixes_in_row)