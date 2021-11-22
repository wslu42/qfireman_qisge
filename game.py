import qisge

from microqiskit import QuantumCircuit, simulate

# import numpy as np
# from qiskit import QuantumCircuit, execute, BasicAer, ClassicalRegister, QuantumRegister
# from qiskit.visualization import plot_histogram

import math, random, time

qubitN=3


######################################################
# load images
images = qisge.ImageList([
    'bucket.png',
    'brick.png',
    ])

# Q: is it like _init() and _update()+_draw() ?

pos_x, pos_y = 1, 0

sprite = {}

player = qisge.Sprite(0,x=pos_x,y=pos_y,z=0)
player.size = 2.5

newenemy_list = []
new=0

enemy_list = []
# for i in range(8):
    # enemy_list += [qisge.Sprite(1,x=i+1,y=14,z=0)]

drop = False        
#####################################################
def next_frame(input):
    
    # Q: why we need to do global in every frame?
    global pos_x,pos_y,drop,enemy_list,qubitN,myqc,newenemy_list,new
        
    # Q: can we do key_up detection in udlr like left_ctrl?
    if (0 in input['key_presses']) and (pos_y<16-1):
        pos_y += 1
    if (1 in input['key_presses']) and (pos_x<8):
        pos_x += 1
    if (2 in input['key_presses']) and (pos_y>0):
        pos_y -= 1
    if (3 in input['key_presses']) and (pos_x>1):
        pos_x -= 1
    player.x, player.y = pos_x, pos_y

    if (5 in input['key_presses']): #"x"
        myqc = QuantumCircuit(qubitN,qubitN)
        myqc.h(0)
        # myqc.h(1)
        myqc.cx(0,1)
        res = simulate(myqc,shots=16,get='counts')
      
        slst = []
        for i in res:
            if res[i]>3: #only state with counts >3 will be counted. to avoid explition in H 
                slst += [i]
        state = [sum([2**(len(d)-i-1)*int(v) for i,v in enumerate(d)]) for d in slst]
        state.sort()
        qisge.print(state)

        for i in state:
            enemy_list+=[qisge.Sprite(1,x=i+1,y=14,z=0)]


    if (4 in input['key_presses']):
        drop = not drop
    # if drop:
        # enemy_list[7].y -= 0.1
        # new +=  1
    # if (5 in input['key_presses']): #"x"
    #     newenemy_list += [qisge.Sprite(1,x=9,y=14,z=0)]

    # for i in range(8):
        # if enemy_list[i].y <= 0.5:
        #     enemy_list[i].y = 14

    # how to generate new sprite in game (during next_frame())?
    # if 4 in input['key_presses']:
    #     pos_enemy_x = pos_x
    #     pos_enemy_y = 0
    #     enemy_list += [qisge.Sprite(1,x=pos_enemy_x,y=pos_enemy_y,z=0)]

    # Q: doesn't seems to move from frame to frame, why?
    # for enemy in enemy_list:
    #     enemy.y -= 1
    #     enemy.x = enemy.x