# A step-by-step tutorial to build a quantum game with Qisge


## Setup Unity (for Windows OS)

## Locate the asset folder in Unity

## Locate the master file game.py and start coding in python

## (optional) Setup the qiskit environment for Unity

## A brief intro to micro-qiskit

## Game design basic: the idea of frames

## Layouts and map design

In qisge currently it supports 2D graphics, and the canvas size is x=28 and y=16 blocks, respectively. Below snippet gives us an idea of the boundary of the map as well as the point of origin. If we count carefully there are total 27 blocks in the x direction while 15 blocks in the y direction, as indicated by the nested for loops in the code. Also we can tell the point of origin is at the lower-left corner of the canvas.

```python
import qisge

images = qisge.ImageList(['block.png'])
for x in range(27):
    for y in range(15):
        qisge.Sprite(0,x=x,y=y,z=0)
        
def next_frame(input):
  global _
```
![image](https://user-images.githubusercontent.com/29524895/143141638-615682d7-168a-4812-bbaa-0221fa4917e3.png)

## Data structure of sprites

## Make our first sprite

## Control the sprite through input['key_presses']

## Let's do simple some classical simulations: falling objects at terminal velocities

### Use qisge.Sprite to generate random falling dummies and catch with a bucket

### Let the dummy drops and detect the boundary collision

### Let user control the paddle to catch the dummy

## Get started with something quantum!

### Generate random falling dummies with QuantumCircuit 

### Design a circuit composer UI and take inputs

### Display bucket(s) according to the measurement outcome

## Useful tools
### qisge.print()
### qisge.update()
