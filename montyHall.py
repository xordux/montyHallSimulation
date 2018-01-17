import random as rand

#meta data
numberOfGates=3
reps=1000
willSwitch=True
win = 0

for rep in range(reps):
    #prepare the gates
    gates=['goats']*numberOfGates
    car=rand.randrange(0,numberOfGates,1)
    gates[car]='car'
    choosen=rand.randrange(0,numberOfGates,1)

    #remove numberOfGates-2 gates (Leaving choosen gate and car gate)
    pastChoosen=False
    pastCar=False
    i = 0
    j = 0
    print(gates)
    print(choosen)
    while j < (numberOfGates - 2):
        if(i == choosen and i == car):
            pastChoosen=True
            pastCar=True
            i = i + 1
        
        if(i == choosen):
            pastChoosen=True
            i = i + 1
        if(i == car):
            pastCar=True
            i = i + 1
        if(i == choosen):
            pastChoosen = True
            i = i + 1
        if pastChoosen == False:
            choosen = choosen - 1
        if pastCar == False:
            car = car - 1
        print(i)
        del gates[i]
        j = j + 1

    otherChoice = -1

    if choosen == 0:
        otherChoice = 1
    elif choosen == 1:
        otherChoice = 0

    # take decision: whether you want to switch or keep your gate
    if willSwitch:
        otherChoice,choosen = choosen,otherChoice

    if gates[choosen] == 'car':
        win = win + 1

print(str(win)+" wins out of "+str(reps)+" trials")

