# Given a list of planets, where each planet is specified by its position along the line and the range of its gravitational field, compute the list of gaps from [0, 1000] through which the spaceship can fly.



# input                output (gaps)           reasoning
# [location, orbit]    
# [3,2]                [0,1],[5,1000]          The field covers [1,5].
# [3,2],[5,1]          [0,1],[6,1000]          The fields cover [1,5] and [4,6].
# [2,1],[5,1]          [0,1],[3,4],[6,1000]    The fields cover [1,3] and [4,6].
# [2,2],[7,1],[4,1]    [5,6],[8,1000]          The fields cover [0,4], [6,8], and [3,5].

def computeGaps(planets):
	pass
	
