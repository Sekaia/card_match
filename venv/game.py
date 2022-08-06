# game class

# Memory Game
#  |  A  |  B  |  C  |  D  |
# 1|     |     |     |     |
# 2|     |     |     |     |
# 3|     |     |     |     |
# 4|     |     |     |     |

# cards hidden when game starts, but allow player to enter a spot, example: A3
# and then a second spot, example: C2
# then we will flip the cards:

#  |  A  |  B  |  C  |  D  |
# 1|     |     |     |     |
# 2|     |     | Py  |     |
# 3| Py  |     |     |     |
# 4|     |     |     |     |

# if they dont match, try again.
# if they match, keep them flipped over.
# when all cards are flipped, print game over