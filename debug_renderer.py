import matplotlib.pyplot as plt
import matplotlib.patches as patches
from dungeon_generator import Rect
from dungeon_generator import BSP_Node
from dungeon_generator import generate_partitions

# Create a figure and axes
fig, ax = plt.subplots(1)

area = BSP_Node(Rect(1, 1, 64, 64))
partitions = generate_partitions([area], 4)

x = 0
y = 0
width = 7
height = 7

for partition in partitions:
    rect = partition.area
    
    r = patches.Rectangle((rect.x, rect.y), rect.width, rect.height, linewidth=1, edgecolor='r', facecolor='none')
    
    ax.add_patch(r)

# Set x and y limits to ensure the rectangle is visible
plt.xlim(0, 70)
plt.ylim(0, 70)

# Show the plot
plt.show()