import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
import matplotlib.animation as animation

with open("input.txt") as f:
    s = f.read().splitlines()

a = len(s)
b = len(s[0])

#Step:

#        1
# * -> 4   2
#        3

#if * == 1:

#            S+1
# S -> S+1000   S+1000
#

#Reindeer =

#
#   0 ... 1 ... 2 ... 0
#
#

#Scores =

#
#   S ... S ... S ... S
#

#for every step:
#
# temp_reindeer = (reindeer_step@reindeer)*walls
# newscores = update_scores(scores, reindeer)*walls
# reindeer = (newscores > scores)*temp_reindeer
# scores = scores*(scores > newscores) + newscores*(newscores > scores)

#def update_scores(scores, reindeer):
#   for i in range(A):
#       for j in range(B):
#           if reindeer[i,j] == 1:
#               scores[i-1,j] = scores[i,j] + 1
#               scores[i,j+1] = scores[i,j] + 1000
#           etc.
#   return scores

#There is room for effectivization here. For instance, if we partition reindeer into 4 types
#up_reindeer, right_reindeer, etc.
#Then at every step, updating scores is a simple matrix multiplication: updateScoresUp @upReindeer etc.
# and the reindeer are updated by tempUpReindeer = shiftUp @ (upReindeer + rightReindeer + ...)
