from enum import Enum

# We draw the image at a larger scale and then resize it down to get anti-aliasing
# This is necessary because PIL's draw methods don't anti-alias
IM_SIZE = 64
IM_DRAW_SCALE = 2
IM_DRAW_SIZE = IM_SIZE * IM_DRAW_SCALE

class Location(Enum):
	FIRST_QUADRANT = (IM_DRAW_SIZE / 2, IM_DRAW_SIZE / 2)
	SECOND_QUADRANT = (0, IM_DRAW_SIZE / 2)
	THIRD_QUADRANT = (0, 0)
	FOURTH_QUADRANT = (IM_DRAW_SIZE / 2, 0)
	
"""	 _______________
	|		|		|
	|	1	|	2	|
	|		|		|
	|_______|_______|
	|		|		|
	|	3	|	4	|
	|		|		|
	|_______|_______|
"""