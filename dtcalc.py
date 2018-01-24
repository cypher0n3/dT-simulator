#!/usr/bin/python
from random import randint

successes = 0
explosions = 0
exploded = True
thisdieexploded = False
thisdieexplosioncounter = 0
thidiesuccesses = 0
explodedary = []
successary = []

n = 1000000000
x = 0

while x != n:
    x +=1
    # print(x)
    thisdieexploded = False
    thisdieexplosioncounter = 0
    thisdiesuccesses = 0
    while exploded == True:
        roll = randint(1, 10)

        if roll >= 6:
            successes +=1
            thisdiesuccesses +=1

            if roll >= 9:
                exploded = True
                explosions +=1
                thisdieexploded = True
                thisdieexplosioncounter +=1
            else:
                exploded = False

        else:
            exploded = False

    if thisdieexploded == True:
        explodedary.append(thisdieexplosioncounter)

    successary.append(thisdiesuccesses)
    exploded = True

numones = 0
numtwos = 0
numthrees = 0
numfours = 0
numfives = 0
numsixes = 0
numsevens = 0
numeights = 0
numnines = 0
numtens = 0
numgreaterten = 0

for val in explodedary:
    if val == 1:
        numones +=1
    if val == 2:
        numtwos +=1
    if val == 3:
        numthrees +=1
    if val == 4:
        numfours +=1
    if val == 5:
        numfives +=1
    if val == 6:
        numsixes +=1
    if val == 7:
        numsevens +=1
    if val == 8:
        numeights +=1
    if val == 9:
        numnines +=1
    if val == 10:
        numtens +=1
    if val > 10:
        numgreaterten +=1

susnumones = 0
susnumtwos = 0
susnumthrees = 0
susnumfours = 0
susnumfives = 0
susnumsixes = 0
susnumsevens = 0
susnumeights = 0
susnumnines = 0
susnumtens = 0
susnumgreaterten = 0
totsuccessroll = 0

for susval in successary:
    if susval >= 1:
        totsuccessroll +=1
    if susval >= 1:
        susnumones +=1
    if susval >= 2:
        susnumtwos +=1
    if susval >= 3:
        susnumthrees +=1
    if susval >= 4:
        susnumfours +=1
    if susval >= 5:
        susnumfives +=1
    if susval >= 6:
        susnumsixes +=1
    if susval >= 7:
        susnumsevens +=1
    if susval >= 8:
        susnumeights +=1
    if susval >= 9:
        susnumnines +=1
    if susval >= 10:
        susnumtens +=1
    if susval > 10:
        susnumgreaterten +=1

avg = (float(successes) / n) * 100
avgexp = float(explosions) / n

avgsuccessful = float(totsuccessroll) /n
avgsus1 = (float(susnumones) / n) * 100
avgsus2 = (float(susnumtwos) / n) * 100
avgsus3 = (float(susnumthrees) / n) * 100
avgsus4 = (float(susnumfours) / n) * 100
avgsus5 = (float(susnumfives) / n) * 100
avgsus6 = (float(susnumsixes) / n) * 100
avgsus7 = (float(susnumsevens) / n) * 100
avgsus9 = (float(susnumnines) / n) * 100
avgsus8 = (float(susnumeights) / n) * 100
avgsus10 = (float(susnumtens) / n) * 100
avgsusgreater10 = (float(susnumgreaterten) / n) * 100

print("Rolled ", n, " times.")
print("Number of successes, including exlosions: ", successes)
print("Total number of explosions: ", explosions)
# print("Average success rate on ", n, " dice: ", avg, "%")
# print("Average explosions: ", avgexp)
print("Biggest success: ", max(successary))
print("")
# print("Odds of getting a successful roll: ", avgsuccessful)
print("Odds of getting at least 1 successes: ", avgsus1, "%")
print("Odds of getting at least 2 successes: ", avgsus2, "%")
print("Odds of getting at least 3 successes: ", avgsus3, "%")
print("Odds of getting at least 4 successes: ", avgsus4, "%")
print("Odds of getting at least 5 successes: ", avgsus5, "%")
print("Odds of getting at least 6 successes: ", avgsus6, "%")
print("Odds of getting at least 7 successes: ", avgsus7, "%")
print("Odds of getting at least 8 successes: ", avgsus8, "%")
print("Odds of getting at least 9 successes: ", avgsus9, "%")
print("Odds of getting at least 10 successes: ", avgsus10, "%")
print("Odds of > 10 successes: ", avgsusgreater10, "%")
'''
print("Number of single explosions: ", numones)
print("Number of double explosions: ", numtwos)
print("Number of triple explosions: ", numthrees)
print("Number of 4 explosions: ", numfours)
print("Number of 5 explosions: ", numfives)
print("Number of 6 explosions: ", numsixes)
print("Number of 7 explosions: ", numsevens)
print("Number of 8 explosions: ", numeights)
print("Number of 9 explosions: ", numnines)
print("Number of 10 explosions: ", numtens)
print("Number of > 10 explosions: ", numgreaterten)
'''
