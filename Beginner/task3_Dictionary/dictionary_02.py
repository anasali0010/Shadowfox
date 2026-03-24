my_expense={
    "Hotel":1200,
    "food":800,
    "Transportation":500,
    "Attraction":300,
    "Miscellaneous":2000,
    "Juice":500
}
my_partner_expense={
    "Hotel":1000,
    "food":900,
    "Transportation":600,
    "Attraction":400,
    "Miscellaneous":150,
    "Juice":500
}


my_total = sum(my_expense.values())
partner_total = sum(my_partner_expense.values())

print("My total expense:", my_total)
print("Partner total expense:", partner_total)

if my_total > partner_total:
    print("I spent more by:", my_total - partner_total)
else:
    print("My partner spent more by:", partner_total - my_total)

max_diff = 0
max_category = ""

for category in my_expense:
    diff = abs(my_expense[category] - my_partner_expense[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print("Highest difference:", max_category, "-", max_diff)