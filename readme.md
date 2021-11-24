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

```python
import qisge
import math, random, time

from microqiskit import QuantumCircuit, simulate

######################################################
# prepare placeholders and var definition

images = qisge.ImageList([
    'bucket.png',
    'brick.png',
    'brick.png',
    ])

qubitN = 3

enemy_list = [[qisge.Sprite(100,x=1,y=14,z=0),qisge.Sprite(100,x=7,y=14,z=0)] for i in range(1000)]
enemy_count = 0

#####################################################
# refresh game frames and get inputs 

qisge.update()
def next_frame(input):
    
    global pos_x,pos_y,qubitN,myqc
    global paddle,enemy_list
    global drop,enemy_count,hit,hittemp
        

    if (5 in input['key_presses']): #"x"
        myqc = QuantumCircuit(qubitN,qubitN)

        if random.randint(0,2)==0:
            myqc.x(0)
        elif random.randint(0,2)==1:
            myqc.h(0)
            myqc.cx(0,1)
        else:
            myqc.h(0)
            myqc.cx(0,1)
            myqc.cx(1,2)
        res = simulate(myqc,shots=16,get='counts')
      
        slst = []
        for i in res:
            if res[i]>3: #only state with counts >3 will be counted. to avoid explition in H 
                slst += [i]
        state = [sum([2**(len(d)-i-1)*int(v) for i,v in enumerate(d)]) for d in slst]
        state.sort()
        qisge.print(state)

        for i in range(len(state)):
            qisge.print(i)
            enemy_list[enemy_count][i].image_id=1
            enemy_list[enemy_count][i].x = state[i]+1
        enemy_count+=1

    for i in range(enemy_count):
        for j in range(2):
            enemy_list[i][j].y -= 0.2

```
![image](https://user-images.githubusercontent.com/29524895/143313980-8a4919fd-0fc5-42f8-8afc-70164a863113.gif)


### Design a circuit composer UI and take inputs

### Display bucket(s) according to the measurement outcome

## Useful tools
### qisge.print()
### qisge.update()
