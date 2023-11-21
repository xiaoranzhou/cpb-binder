
# loading libraries, you need to run it only once when using the notebook
from CPlantBox_PiafMunch import *
# Read XML and make plants:
# Step 1: make a plant object
p = pb.Plant()

# Step 2: read XML parameters
p.openXML('../../modelparameter/plant/sympodial_dichasium.xml')
# p.openXML('../../modelparameter/plant/leaf_opposite_decussate.xml')

# try other leaf arrangements
# p.openXML('../../modelparameter/plant/leaf_opposite_decussate.xml')
# p.openXML('../../modelparameter/plant/leaf_alternate.xml')

# try a more complex plant
# p.openXML('../../modelparameter/plant/logo_plant.xml')

# initialize the parameters
p.initialize()

# simulation for 3 days
p.simulate(300) 
# uncommen the line below to simulate it for 10 days
# p.simulate(10) 


# Visualize it

p.write("sympodial_dichasium.vtp")
