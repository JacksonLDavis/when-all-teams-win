"""
This Python program was originally made in 2023.

Context:
The Texas Rangers won the World Series for the first time in 2023.
As of 2023, they are one of the 25 teams in the MLB that have won the World Series at least once.
There are still 5 other teams in the MLB that have never won the World Series.

This Python program simulates when the 5 remaining teams in the MLB will win a World Series.
This program assumes that the winner of the World Series each year is determined randomly,
and that there will always be the same 30 MLB teams each year.

This program can be modified to simulate when teams in other sports leagues will win their
first championships.
"""

import random as rand

######################################################################################################
# The following variables can be changed so that this program can be applied to other sports leagues #
######################################################################################################

championship_name = "World Series"  # string

total_teams = 30  # integer, must be at least 2
teams_without = 5  # integer, must be at least 1, must be lower than total_teams
current_year = 2023  # integer or float

number_trials = 10000  # integer, must be at least 1

######################################################################################################
######################################################################################################
######################################################################################################

average_year = []  # will be of the form [last team, second last team, third last team, ...]
for h in range(teams_without):
    average_year.append(0)

# calculate the average year for each team
for i in range(number_trials):
    # set status for all teams at the start of a trial
    teams = []
    for j in range(total_teams - teams_without):
        teams.append(1)
    for k in range(teams_without):
        teams.append(0)
    # create changeable clones
    current_year_changeable = current_year
    teams_without_changeable = teams_without
    # determine a winner each year until each team wins the championship
    while teams_without_changeable > 0:
        while teams.count(0) == teams_without_changeable:
            current_year_changeable += 1
            winner = rand.randint(0, total_teams - 1)  # choose a winner
            teams[winner] = 1
        teams_without_changeable -= 1
        average_year[teams_without_changeable] += current_year_changeable
for m in range(teams_without):
    average_year[m] /= number_trials

# print out the results
for n in range(teams_without):
    print("Average year when team #" + str(total_teams - teams_without + n + 1) +
          " wins the " + championship_name + ": " + str(average_year[teams_without - n - 1]))

"""
Extra Reading:
When 5/30 teams have not yet won the World Series, that means that there is a 5/30 = 1/6 chance that one of those teams
will win the World Series each year assuming that the team that wins the World Series is determined randomly.
It would make sense to say that one of those teams will win the World Series at around 2029.

The following math predicts when the five remaining teams will win the World Series:
    Team #26: 5/30 = 1/6   =>   6 years until team wins => 2023   + 6   = 2029
    Team #27: 4/30 = 1/7.5 => 7.5 years until team wins => 2029   + 7.5 = 2036.5
    Team #28: 3/30 = 1/10  =>  10 years until team wins => 2036.5 + 10  = 2046.5
    Team #29: 2/30 = 1/15  =>  15 years until team wins => 2046.5 + 15  = 2061.5
    Team #30: 1/30 = 1/30  =>  30 years until team wins => 2061.5 + 30  = 2091.5 (total years passed: 68.5)

Because it does not make sense for years to have decimals, I would round these numbers up to
2029, 2037, 2047, 2062, and 2092.
"""
