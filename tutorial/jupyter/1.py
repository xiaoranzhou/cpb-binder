# Generating the plant architecture 
from CPlantBox_PiafMunch import * #import all the libraries
p = pb.Plant()
r0 = pb.RootRandomParameter(p)  # with default values,
r1 = pb.RootRandomParameter(p)  # all standard deviations are 0
s1 = pb.StemRandomParameter(p)
s2 = pb.StemRandomParameter(p)


s5 = pb.StemRandomParameter(p)
s6 = pb.StemRandomParameter(p)

s7 = pb.StemRandomParameter(p)
s8 = pb.StemRandomParameter(p)

l1 = pb.LeafRandomParameter(p)
l2 = pb.LeafRandomParameter(p)

r0.name = "taproot"
r0.a = 0.2  # [cm] radius
r0.subType = 1  # [-] index starts at 1
r0.lb = 5  # [cm] basal zone
r0.la = 10  # [cm] apical zone
r0.lmax = 90  # [cm] maximal root length, number of lateral branching nodes = round((lmax-lb-la)/ln) + 1
r0.ln = 1.  # [cm] inter-lateral distance (16 branching nodes)
r0.theta = 0.  # [rad]
r0.r = 1  # [cm/day] initial growth rate
r0.dx = 10  # [cm] axial resolution
r0.successor = [2]  # add successors
r0.successorP = [1]  # probability that successor emerges
r0.tropismT = pb.TropismType.gravi  #
r0.tropismN = 1.8  # [-] strength of tropism
r0.tropismS = 0.2  # [rad/cm] maximal bending

r1.name = "lateral"
r1.a = 0.1  # [cm] radius
r1.subType = 2  # [1] index starts at 1
r1.lmax = 15  # # [cm] apical zone
r1.lmaxs = 0.15  # [cm] standard deviation of the apical zone
r1.theta = 90. / 180. * np.pi  # [rad]
r1.r = 2  # initial growth rate
r1.dx = 1  # [cm] axial resolution
r1.tropismT = pb.TropismType.gravi  # exo
r1.tropismN = 2  # [-] strength of tropism
r1.tropismS = 0.1  # [rad/cm] maximal bending

s1.name = "mainstem"
s1.subType = 1

s1.lmax = 100
s1.lb = 90
s1.la = 4
s1.ln = 3
s1.lnf = 0
s1.RotBeta = 0
s1.BetaDev = 0
s1.InitBeta = 0
s1.gf = 1
s1.successor = [5]
s1.successorP = [1]
s1.tropismT = 5
s1.theta = 0.
s1.tropismN = 18
s1.tropismS = 0.01
s1.r = 3


s5.name = "horizontal_stem"
s5.subType = 5
s5.lmax = 60
s5.lb = 0
s5.la = 2
s5.ln = 10
s5.lnf = 0
s5.RotBeta = 0.5
s5.BetaDev = 0
s5.InitBeta = 0
s5.gf = 1
s5.successor = [6]
s5.successorP = [1]
s5.tropismT = 5
s5.theta = 0.5
s5.tropismN = 18
s5.tropismS = 0.01
s5.r =2


s6.name = "small_vertical_stem"
s6.subType = 6
s6.lmax = 9
s6.lb = 3
s6.la = 2
s6.ln = 3
s6.lnf = 0
s6.RotBeta = 1
s6.BetaDev = 0
s6.InitBeta = 0
s6.gf = 1
s6.successor = [7]
s6.successorP = [1]
s6.tropismT = 4
s6.theta = 0.5
s6.tropismN = 18
s6.tropismS = 1
s6.r = 1




s8.name = "1_year_branch_stem"
s8.subType = 8
s8.lmax = 20
s8.lb = 2
s8.la = 2
s8.ln = 1
s8.lnf = 0
s8.RotBeta = 0.5
s8.BetaDev = 0
s8.InitBeta = 0
s8.gf = 1
s8.successor = [2]
s8.successorP = [1]
s8.tropismT = 5
s8.theta = 0.25
s8.tropismN = 3
s8.tropismS = 0.00
s8.r =3


s2.name = "bud stem for leaves"
s2.subType = 2
s2.lmax = 0
s2.la = 0
s2.ln = 0
s2.lnf = 0
s2.RotBeta = 0
s2.BetaDev = 0
s2.InitBeta = 0.
s2.theta = 0.5
s2.gf = 1
s2.tropismT = 4

s2.tropismN = 18
s2.tropismS = 2
s2.r = 3




l1.name = 'leaf_under_second_stem'
l1.subType = 2
l1.lb = 2
l1.la = 0.2
l1.lmax = 5
l1.r = 0.5
l1.RotBeta = 0.5
l1.BetaDev = 0
l1.InitBeta = 0.
l1.tropismT = 1
l1.tropismN = 5
l1.tropismS = 0.15
l1.theta = 0.35
l1.gf = 1

l2.name = 'leaf_on_second_stem'
l2.subType = 3
l2.lb = 2
l2.la = 0.2
l2.lmax = 5
l2.r = 0.5
l2.RotBeta = 0.5
l2.BetaDev = 0
l2.InitBeta = 0.
l2.tropismT = 1
l2.tropismN = 5
l2.tropismS = 0.15
l2.theta = 0.35
l2.gf = 1


s7.name = "1_year_stem"
s7.subType = 7
s7.lmax = 60
s7.lb = 0
s7.la = 2
s7.ln = 20
s7.lnf = 0
s7.RotBeta =1
s7.BetaDev = 0
s7.InitBeta = -0.5
s7.gf = 1
s7.successor = [8]
s7.successorP = [1]
s7.tropismT = 1
s7.theta = 0.5
s7.tropismN = 2
s7.tropismS = 0.01
s7.r =3


p.setOrganRandomParameter(r0)
p.setOrganRandomParameter(r1)
p.setOrganRandomParameter(s1)
p.setOrganRandomParameter(s2)


p.setOrganRandomParameter(s5)
p.setOrganRandomParameter(s6)
p.setOrganRandomParameter(s7)
p.setOrganRandomParameter(s8)
p.setOrganRandomParameter(l1)

srp = pb.SeedRandomParameter(p)  # with default values
srp.seedPos = pb.Vector3d(0., 0., -3.)  # [cm] seed position
srp.maxB = 0  # [-] number of basal roots (neglecting basal roots and shoot borne)
srp.firstB = 0  # [day] first emergence of a basal root
srp.delayB = 0  # [day] delay between the emergence of basal roots
srp.maxTil = 0
srp.nC = 0
# srp.nZ = 0
srp.nCs = 0
p.setOrganRandomParameter(srp)

#  Simulating the plant growth

time = 480

p.initialize(True)

p.simulate(time)

p.write("champagnat.vtp")
fig = visual_plant(p)

fig.show()

plotly.offline.plot(fig, filename='champagnat.html')