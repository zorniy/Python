from vpython import *

scene = canvas(height=600, width = 800)

sun = sphere(radius = 5, color=color.yellow)
M = 1000
G = 1000

planet1 = sphere(pos = vector(40, 0, 0), radius=3, make_trail=True)
planet2 = sphere(pos = vector(80, 0, 0), radius =3, color=color.red, make_trail=True)
cube = box(pos=planet1.pos, color=color.yellow, make_trail=False, size=vector(3,3,3))


tangent1 = vector(-planet1.pos.y, planet1.pos.x, planet1.pos.z)/mag(planet1.pos)
vel1 = tangent1*(G*M/mag(planet1.pos))**0.5


tangent2 = vector(-planet2.pos.y, planet2.pos.x, planet2.pos.z)/mag(planet2.pos)
vel2 = tangent2*(G*M/mag(planet2.pos))**0.5

cube.vel = vel1


acc1 = vector(0,0,0)
acc2 = vector(0,0,0)

dt = 0.0001

RunSim = True
isLaunch = False
flag = False

l1=label(pos=vector(0,-100,0))

#=======================================
#Calculations Tiem!
#=======================================

r1 = mag(planet1.pos)
r2 = mag(planet2.pos)

a = (r1+r2)/2
vLaunch = (G*M*(2/r1 -1/a))**0.5

Tau = 2*pi*((a**3)/(G*M))**0.5
tFlight = Tau/2

a2 = mag(planet2.pos)
Tau2 = 2*pi*((a2**3)/(G*M))**0.5
omega = 2*pi/Tau2
phi = omega * tFlight



#========================================
#Ende of Calculations
#========================================

while RunSim:

    rate(2000)

    acc1 = -G*M*planet1.pos/mag(planet1.pos)**3
    vel1 = vel1 + acc1*dt
    planet1.pos = planet1.pos + vel1*dt

    

    acc2 = -G*M*planet2.pos/mag(planet2.pos)**3
    vel2 = vel2 + acc2*dt
    planet2.pos = planet2.pos + vel2*dt

 
    cube.acc = -G*M*cube.pos/mag(cube.pos)**3
    cube.vel = cube.vel + cube.acc*dt
    cube.pos = cube.pos + cube.vel*dt

    r1 = mag(planet1.pos)
    r2 = mag(planet2.pos)
    d = mag(planet2.pos-planet1.pos)

    
    angle=diff_angle(planet2.pos, planet1.pos)


    if angle > 3.14:
        flag = True

    if flag == True and angle < pi-phi and isLaunch == False:
        l1.text="probe is \n ALUNCH!"
        tangent = vector(-planet1.pos.y, planet1.pos.x, 0)/mag(planet1.pos)
        cube.vel = vLaunch * tangent
        cube.make_trail=True
        
        isLaunch = True

    if mag(planet2.pos - cube.pos) < 1:
        l1.text = "probe is \n ARIRVE!"
        cube.pos = planet2.pos
        cube.vel=vel2
        #RunSim = False
    
l2 = label(pos=vector(0, 20, 0), text="TAM MAT")
        
