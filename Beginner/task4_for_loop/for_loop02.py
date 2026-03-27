total_jumping_jacks = 100
done = 0

while done < total_jumping_jacks:
    # Perform 10 jumping jacks
    done += 10
    print(f"You completed {done} jumping jacks.")

    if done == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip remaining sets? (yes/y or no/n): ").lower()

        if skip == "yes" or skip == "y":
            print(f"You completed a total of {done} jumping jacks.")
            break

    remaining = total_jumping_jacks - done
    print(f"{remaining} jumping jacks remaining.\n")