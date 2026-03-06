# to separate Aquaman and flash from each other.
justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
# Either we choose Green Lantern or Superman, to move between in them.
justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern")
print(justice_league)