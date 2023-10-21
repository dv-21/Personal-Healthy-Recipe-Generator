import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('epi_r.csv')

print("WELCOME TO: RECIPE OF THE DAY\n")

intro = input("Press enter to get started!\n")
print("MAIN MENU\n")

while True:   
    # Menu choice
    menu_choice = input("Random recipe recommendation[Enter 1] OR "
                        + "Recipe recommendation with max calorie preference[Enter 2] OR "
                        + "Exit[Enter 0]\n").strip()
    
    if (menu_choice == "0"):
        break

    if (menu_choice == "1"):

        rand_int = random.randint(0, 20052)
        print("\n" + df.iloc[rand_int, 0])
        print("\nCalories: " + str(df.iloc[rand_int, 2]))
        print("\nProtein: " + str(df.iloc[rand_int, 3]))
        print("\nFat: " + str(df.iloc[rand_int, 4]))
        print("\nSodium: " + str(df.iloc[rand_int, 5]))
        print("\nIngrediants and details:")
        for i in range(15, 680, 1):
            if (df.iloc[rand_int, i] >= 1):
                print(df.iloc[:, i].name)
        print("\n")

    if (menu_choice == "2"):
        # Ask the user if they want a recipe with a max calorie cap
        max_cal = int(input("\nWhat is your max calorie preference?[Pls type a number only]: ").strip())
        used_dict = {str(key): 0 for key in range(0, 20053, 1)}
        for i in range(0, 20053, 1):
            rand_int2 = random.randint(0, 20052)
            if ((used_dict[str(rand_int2)] == 0)):
                used_dict[str(rand_int2)] += 1
                if (df.iloc[rand_int2, 2] < max_cal):
                    print(df.iloc[rand_int2, 0])
                    print("Calories: " + str(df.iloc[rand_int2, 2]))
                    print("Protein: " + str(df.iloc[rand_int2, 3]))
                    print("Fat: " + str(df.iloc[rand_int2, 4]))
                    print("Sodium: " + str(df.iloc[rand_int2, 5]))
                    print("Ingrediants and details:")
                    for i in range(15, 680, 1):
                        if (df.iloc[rand_int2, i] >= 1):
                            print(df.iloc[:, i].name)
                    print("\n")
                    break
                else:
                    used_dict[str(rand_int2)] += 1

    









        