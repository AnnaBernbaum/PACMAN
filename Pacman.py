# pacman code XP
# myPacmanAgents.py

from pacman import Directions
from game import Agent
import random
import game
import util

class MyPacmanAgent(game.Agent):
  # Getting legal actions
  def getAction(self, state):
    return Directions.STOP
  
  # Mode 1: Strive for big biscuits
  def getBigBiscuits(self, state):
    legal = state.getLegalPacmanActions()
    return Directions.STOP
  
  # Mode 2: Chase and eat as many ghosts as possible
   def eatGhosts(self, state):
    return Directions.STOP
  
  # Mode 3: Avoid ghosts
   def avoidGhosts(self, state):
    return Directions.STOP
