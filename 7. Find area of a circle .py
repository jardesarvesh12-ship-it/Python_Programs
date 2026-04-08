# Area = pi * r2


# Using hardcoded pi value
PI = 3.142
r = 5 # radius
area = PI * (r * r)
print(area)



# Using math.pi
import math
r = 5
area = math.pi * (r ** 2)
print(area)


# Using math.pow()
import math
radius = 5
area = math.pi * math.pow(radius, 2)
print(area)




# Using numpy.pi
import numpy as np
r = 5 # radius
area = np.pi * (r ** 2)
print(area)