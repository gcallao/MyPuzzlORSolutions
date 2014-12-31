# -*- coding: utf-8 -*-
#The PuzzlOR - October 2014
#Fighters!

#Submitted by Giancarlo Callaoapaza Chávez
#e-mail: callao.gc@gmail.com

import copy
import random

class fighter(object):
    """
    Representation of a fighter.
    """
    def __init__(self, name, health, attackPoints):
        """
        Initialize a fighter instance saving all the parameters as attributes
        of the instance.
        
        name: Name of the fighter.
        health: Health points of the fighter.
        attackPoints: Attack points of the fighter.
        """
        self.name = name
        self.health = health
        self.attackPoints = attackPoints
    
    def getName(self):
        """
        Returns the name of the name of the fighter.
        """
        return self.name
    
    def getHealth(self):
        """
        Returns the health points of the fighter.
        """
        return self.health
        
    def getAttackPoints(self):
        """
        Returns the attack points of the fighter.
        """
        return self.attackPoints
    
    def updateHealth(self, newhealth):
        """
        Updates the health points of the fighter after a round as a defender.
        
        newhealth: Health points remaining of the fighter.
        """
        self.health = newhealth
        
def fightSim(fighterList):
    """
    Simulation of a single fight in mode all-out between a list of fighters. A single fight takes place
    over a series of rounds, each round consisting of a single attack. In each round, one
    random attacker and one random defender are chosen. When attacker attacks a defender, the defender
    loses health points in the amount equivalent to the attacker's attack points. The fighters continue
    to randomly attack and defend in subsequent rounds until there ins only one fighter left, who is declared the winner. 
    
    fighterList: List of fighter instances.
    
    Returns the winner's name in a single fight.
    """
    fighterListSim = copy.deepcopy(fighterList)
    while len(fighterListSim) > 1:      
        attacker = random.choice(fighterListSim)
        fighterListSim.remove(attacker)
        
        defender = random.choice(fighterListSim)   
        fighterListSim.append(attacker)
                                        
        if attacker.getAttackPoints() >= defender.getHealth():
            fighterListSim.remove(defender)
        else:
            fighterListSim[fighterListSim.index(defender)].updateHealth(defender.getHealth()-attacker.getAttackPoints())

    return fighterListSim[0].getName()
        
def runFightSim(fighterList, numTrials):
    """
    Simulation of a series of single fights in mode all-out between a list of fighters. 
    
    fighterList: List of fighter instances.
    numTrials: Number of single fights to be simulated.
    
    Returns a dictionary with the fighter names as keys and their winning simulated probabilities
    as values.
    """
    fighterDict = {}
    for i in range(len(fighterList)):
        fighterDict[fighterList[i].getName()] = 0
    
    for trial in range(numTrials):
        fight = fightSim(fighterList)
        fighterDict[fight] = round(fighterDict[fight] + 1/float(numTrials),5)
         
    return fighterDict
        
Allan = fighter("Allan", 10, 4)
Barry = fighter("Barry", 12, 3)
Charles = fighter("Charles", 16, 2)
Dan = fighter("Dan", 18, 1)

fighters = [Allan, Barry, Charles, Dan]
print runFightSim(fighters, 100000)

#Winning Simulated probabilities over 100000 trials: {'Barry': 0.26242, 'Dan': 0.16278, 'Charles': 0.31951, 'Allan': 0.25529}
#The fighter which is most likely to win is CHARLES (0.31951)