from vpython import *

scene = canvas(height=600, width=800)

## ===========
## GLOBAL VARIABLES
## ===========

GM = 1E4
dt = 0.001

##==============


##==============
## PLANET CLASS
##==============

class planet(sphere):
    def __init__(self, name, pos, warna):
        self.name = name
        sphere.__init__(self, pos = pos, radius = 10, make_trail=True, retain =mag(pos)/3 , color=warna)
        vee = (GM/mag(pos))**0.5
        tangent = vector(-self.pos.y, self.pos.x,0)/mag(self.pos)
        self.vel = 1*vee * tangent
        #self.lab = label(text=self.name, pos=self.pos+vector(0,20,0))
        
    
    def acc(self):
        a = -GM*self.pos/(mag(self.pos)**3)
        #self.lab.pos =self.pos
        return(a)

    def move(self):
        self.vel = self.vel + self.acc()*dt
        self.pos = self.pos + self.vel*dt


##==========================
##        CLASS PROBE
##==========================

class cube(box):
    def __init__(self, pos):
        box.__init__(self, pos = pos, color = color.red, size=vector(20,20,20), make_trail = False)
        vee = (GM/mag(pos))**0.5
        tangent = vector(-self.pos.y, self.pos.x, 0)/mag(self.pos)
        self.vel = vee*tangent

        self.isLaunch = False
        self.Flag = False

        #self.lab = label(text = "probe", pos= self.pos)

    
    def vLaunch(self, pl1, pl2):
        a = (mag(pl1.pos) + mag(pl2.pos))/2
        vee = (GM*(2/mag(self.pos)-1/a))**0.5
        return vee
    
    def Lag(self,pl1,pl2):
        a = (mag(pl1.pos)+mag(pl2.pos))/2
        Tau = 2 * pi *((a**3)/GM)**0.5
        tFlight = Tau/2

        Tau2 = 2*pi *((mag(pl2.pos)**3)/GM)**0.5
        lagg = abs(pi-2*pi*tFlight/Tau2)
        return lagg
        

    
    def move(self, pl1, pl2):

        angle = diff_angle(pl1.pos, pl2.pos)
        if angle > 2:
            self.Flag = True

        if angle < self.Lag(pl1,pl2) and self.Flag == True and self.isLaunch == False:
            tangent = vector(-self.pos.y, self.pos.x, 0)/mag(self.pos)
            self.vel = self.vLaunch(pl1,pl2)*tangent
            self.isLaunch = True
            self.make_trail=True
            
        
        if mag(self.pos - pl2.pos) < 1:
            self.pos = pl2.pos
            self.vel = pl2.vel
            self.isLaunch = False
            self.Flag = False
            self.make_trail = False

        
        acc = -GM*self.pos/mag(self.pos)**3
        self.vel = self.vel + acc*dt
        self.pos =self.pos + self.vel*dt
        
        #self.lab.pos = self.pos
        
        







##================================================================
## PUBLIC STATIC VOID MAIN PROGRAM
##================================================================
        

sun = sphere(radius =10, color=color.yellow)

pl = []
name = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
warna =[color.blue, color.white, color.cyan, color.orange, color.purple, color.blue, color.magenta, color.green]
dist = [vec(20,0,0), vector(40,0,0), vector(80,0,0), vector(160,0,0), vector(320,0,0), vector(640,0,0), vector(1280,0,0), vector(2000,0,0) ]

for i in range(8):
    pl = pl + [planet(name[i],dist[i], warna[i])]


probe = cube(pos=pl[0].pos)


k=0

RunSim = True

direction = "out"

while RunSim==True:
    rate(6000)
    for i in range(8):
        pl[i].move()

    probe.move(pl[k], pl[k+1])

    if mag(probe.pos - pl[k+1].pos) <1 and k<7:
        k=k+1
        print(k)
      
    if k >= 4:
            dt = 0.01

    if k< 4:
            dt =0.001
        
    


