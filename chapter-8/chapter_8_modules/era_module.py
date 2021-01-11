def formatInnings(full_innings, partial_innings):
    """Format and combine full and partial innings"""

    if partial_innings == 0:
        total_inn = full_innings

    elif partial_innings == 1 or partial_innings == 2:  # In baseball, .1 = 1/3 innings, and .2 = 2/3 innings

        if partial_innings == 1:
            partial_innings = .333
        elif partial_innings == 2:
            partial_innings = .666

        total_inn = full_innings + partial_innings
    else:
        print("That doesn't make any sense. (partial innings always less than 3!) Quitting.")
        quit()

    return total_inn

def getERA(earned_runs, innings_pitched, game_length=9):
    """ Returns a pitchers earned run average """
    # ERA = '(earned_runs / innings_pitched) * 9' (9 is the total innings in a baseball game.)
    # Ignores partial inning completion
    era = (earned_runs / innings_pitched) * game_length
    era = round(era, 2)
    return era
