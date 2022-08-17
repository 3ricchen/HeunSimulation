import main, cmath, math


def set_epsilon(val):
    main.epsilon = val
    main.alpha = (main.gamma + main.delta + main.epsilon - 1) / 2
    main.beta = main.alpha

set_epsilon(0)


def runstep():
    mats = main.findMatrices()
    R = mats[2]
    new_epsilon = 1/(2*math.pi)*math.acos((abs(R[0,0]+R[1,1])-2)/2)
    set_epsilon(new_epsilon)
    print(main.epsilon)
    #print(cmath.polar(R[0,0]+R[1,1])[1] + math.pi*main.epsilon)
    #print(cmath.polar(R[0, 0])[1] + math.pi * main.epsilon)
    #print(cmath.polar(R[1, 1])[1] + math.pi * main.epsilon)
    print()

for i in range(100):
    runstep()