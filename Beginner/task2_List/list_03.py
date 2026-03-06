justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
# Woner women is now the leader so moving her to the first position.
# I solve this problem with 2 methods. 1st is by removing and inserting .
'''justice_league.remove("Wonder Woman")
   justice_league.insert(0, "Wonder Woman")'''

# 2nd method is by poping and inserting.
first_member=justice_league.pop(2)
justice_league.insert(0,first_member)

print(justice_league)