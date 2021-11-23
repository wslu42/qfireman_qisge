import qisge
import math, random, time

from microqiskit import QuantumCircuit, simulate

######################################################
# load images
images = qisge.ImageList([
    'bucket.png',
    'brick.png',
    ])

# Q: is it like _init() and _update()+_draw() ?

pos_x, pos_y = 1, 0
qubitN=3

player = qisge.Sprite(0,x=pos_x,y=pos_y,z=0)
player.size = 2.5
# player.sprite_id=100

enemy_list = []

drop = False        
#####################################################
qisge.update()
def next_frame(input):
    
    # Q: why we need to do global in every frame?
    global pos_x,pos_y,qubitN,myqc
    global player
    global drop,enemy_list
        
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
    qisge.print('player_sprite_id: '+str(player.sprite_id))

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
            qisge.update()

    for i in enemy_list:
        qisge.print('enemy_sprite_id: '+str(i.sprite_id))


    if (4 in input['key_presses']):
        drop = not drop
        qisge.print(drop)
