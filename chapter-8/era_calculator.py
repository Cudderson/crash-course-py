# 8-16
# Simple practice with modules
import era_module as era


print("Ready to calculate your Earned Run Average.\n")
game_length = input("\nTypical games are 9 innings. Is this true for this pitcher's league?(yes/no): ")
earned_runs = int(input("How many earned runs did the pitcher allow? "))
full_innings_pitched = int(input("\nHow many full-innings did the pitcher pitch? (33.2 = 33): "))
partial_innings_pitched = int(input("\nEnter any additional outs the pitcher made."
                                        "(If total innings = 33.2, enter 2: "))

if game_length == "yes":
    total_inn = era.formatInnings(full_innings_pitched, partial_innings_pitched)
    era = era.getERA(earned_runs, total_inn)

elif game_length == "no":
    game_length = int(input("How many innings does this league play per game?: "))
    total_inn = era.formatInnings(full_innings_pitched, partial_innings_pitched)
    era = era.getERA(earned_runs, total_inn, game_length=game_length)

else:
    print("Did not understand command.")

print(f"\nYour results are in!\n\n"
      f"Pitcher ERA: {era}\n")

print("Closing program.")
quit()
