import random
#Stochastic Simulations

def noReplacementSimulation(numTrials):
    notTheSame = 0
    for i in range(numTrials):   #repeat simulations... 
        bucket = ['r','r','r','g','g','g']
        bag = []
        for b in range(3):  #randomly grab three from the bucket and put them in the bag
            ball = random.choice(bucket)
            bucket.remove(ball)
            bag.append(ball)  
        temp = bag[0]            
        for j in range(len(bag)):  #the marbles in the bag were not all the same color
            if(bag[j] != temp):
                notTheSame += 1  
                break

    #percentage of trials where all the colors were the same...
    return float(numTrials - notTheSame) / float(numTrials) 


print noReplacementSimulation(10000)
