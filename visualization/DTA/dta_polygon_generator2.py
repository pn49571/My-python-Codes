# normally I'd do this using numpy, but we need to port this to C#
import math
from math import cos, sin, atan2, pi, acos, sqrt
###
# constants I didn't get from Sai
RadiusEarthKm = 6371.0
DtaForwardAngle  = 25	#degrees for fast cells
DtaTime		  = 1	#hours
DtaMinVelocity = 5	#kmph

###
# the info I got from Sai
CellCenter = (-54.2001077156015,-23.146110521118)
CellVertices = [
	(-54.2427857022621,-23.1427031137106),
	(-54.2273175921448,-23.1265268174264),
	(-54.1673175921448,-23.1040774585243),
	(-54.1574445452115,-23.1227031137106),
	(-54.1745467300137,-23.1627031137106),
	(-54.1873175921448,-23.1751088932539),
	(-54.2073175921448,-23.1770936193128),
	(-54.2273175921448,-23.1582236965008) ]

CellRadiusKm = 2.58701914034346
DirectionVector = ( 0.998065820441223, -0.0621660523677342 )
###
# for testing other directions
angle = 2.8*(math.pi/2)
DirectionVector = ( math.sin(angle), math.cos(angle) )
#CellVelocity = 21.8113668924361	#km/h
CellVelocity = 15


###
# functions
def spherical_distance( pt1, pt2, ):
	"""Calculates the distance between two points on a sphere.  Will
	work on vectors of positions as well.

	This is the well known haversine equation.
	"""
	#math imports
	from math import cos, sin, atan2, pi, sqrt

	#copy and convert to radians
	lat1 = pt1[1]*pi/180
	lat2 = pt2[1]*pi/180
	lon1 = pt1[0]*pi/180
	lon2 = pt2[0]*pi/180
	dlat = lat1-lat2
	dlon = lon1-lon2

	a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
	rng = RadiusEarthKm * 2 * atan2( sqrt(a), sqrt( 1-a ) )

	return rng


def rngbrg2latlon( rng, brg, pt ):
	"""converts range and bearing from a lat-lon point to a lat-lon point
	"""
	###
	# gonna need these.  Maybe they've already been imported, but
	# it won't hurt to do it again
	from math import asin, atan2, sin, cos, pi
	#print ("bearing:",brg)
	lat1 = pt[1]*pi/180
	lon1 = pt[0]*pi/180

	d = rng/RadiusEarthKm

	lat2 = asin( sin(lat1)*cos(d) + cos(lat1)*sin(d)*cos(brg) )
	#print ("Cosine bearing",asin( sin(lat1)*cos(d) + cos(lat1)*sin(d)*cos(brg) ))
	lon2 = lon1 + atan2( sin(brg)*sin(d)*cos(lat1), cos(d)-sin(lat1)*sin(lat2) )
	#print("sine bearing",atan2( sin(brg)*sin(d)*cos(lat1), cos(d)-sin(lat1)*sin(lat2) ))
	#lat and lon should be returned in degrees
	return lon2*180/pi, lat2*180/pi

def spherical_bearing( pt1, pt2 ):
	"""Calculates the forward azimuth between pt1 and pt2.  You can
	get the back azimuth by calling on pt2, pt1.
	"""
	#mat imports
	from math import cos, sin, atan2, pi

	#copy and convert to radians
	lat1 = pt1[1]*pi/180
	lat2 = pt2[1]*pi/180
	lon1 = pt1[0]*pi/180
	lon2 = pt2[0]*pi/180

	x = sin(lon2-lon1)*cos(lat2)
	y = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(lon2-lon1)
	return atan2( x, y )


def IntermediatePoint(A, B, D, d):
    crs_AD = spherical_bearing(A, D)
    crs_AB = spherical_bearing(A, B)
    _A = crs_AD - crs_AB
    dist_AD = spherical_distance(A, D)/RadiusEarthKm
    b = dist_AD
    r = sqrt(cos(b) * cos(b) + sin(b) * sin(b) * cos(_A) * cos(_A))
    p = atan2(sin(b) * cos(_A), cos(b))
    if (cos(d) * cos(d) < r*r):
        dp1 = p + acos(cos(d)/r)
        dp2 = p - acos(cos(d)/r)
        dp = max(dp1, dp2)
        _p = rngbrg2latlon(dp * RadiusEarthKm, crs_AB, A)
        return _p






###
# get the direction of motion
DirectionAngle = spherical_bearing( CellCenter, [CellCenter[0]+DirectionVector[0], CellCenter[1]+DirectionVector[1]] )
#~ DirectionAngle = math.atan2( DirectionVector[1], DirectionVector[0] )

# loop through the vertices, and find the one farthest from the center
rngMax = 0
for pt in CellVertices:
	rng = spherical_distance( pt, CellCenter )
	if rng > rngMax:
		rngMax = rng

DtaVertices = []
###
# draw the back of the polygon
brg = math.pi/2	# this is perpendicular to the direction of motion
rng = rngMax + DtaMinVelocity*DtaTime

pt1 = rngbrg2latlon(rng, brg + DirectionAngle, CellCenter)
#we add a little bit to account for possible floating point errors
while brg <= 3*(math.pi/2)+0.02:#
	#print brg*180/math.pi
	pt = rngbrg2latlon( rng, brg+ DirectionAngle, CellCenter )
	DtaVertices.append( pt )
	brg += math.pi/6
#reverse it
brg -= math.pi/6



#skip forward
# brgSkip will be a number between 0 and 1 for all CellVelocity > 0
#brgSkip = (math.atan( CellVelocity/10 ))/(math.pi)
if CellVelocity < 10:
	brgSkip = (math.atan( CellVelocity/DtaMinVelocity ))/(math.pi)
else:
	brgSkip = (math.atan(CellVelocity / 10)) / (math.pi)

brgSkip *= 2
# convert that into an angle
brgSkip *= (math.pi/2)-(DtaForwardAngle)*(math.pi/180)
#print brgSkip*180/math.pi
brg += brgSkip
rng = rngMax + (max(CellVelocity, DtaMinVelocity)*(DtaTime))

# brgtemp = brg
# rngtemp = rngMax + (max(CellVelocity, DtaMinVelocity)*(0.45))

last = DtaVertices[-1]
# #Rngbrg2Latlon(cellCenter, rng, brg + bearingAngleRad);
next = rngbrg2latlon(rng, brg+DirectionAngle, CellCenter)
# print("last point:", last)
# print("next point:", next)


#rng = rngMax + (DtaMinVelocity*(DtaTime))
count = 0
# print("brg caught:", brg)
DtaVertices1 = []
while brg <= ((5*math.pi/2) - brgSkip):
	pt = rngbrg2latlon( rng, brg+DirectionAngle, CellCenter )
	DtaVertices.append( pt )
	print (pt)
	count += 1
	brg += math.pi/16


# add the last point
# print ("count:",count)
brg = (5*(math.pi/2)) - brgSkip
pt = rngbrg2latlon( rng, brg+DirectionAngle, CellCenter )
# but check that we're aren't duplicating anything
# if abs(pt[0]-DtaVertices[-1][0])>0.03 or abs(pt[1]-DtaVertices[-1][1])>0.03:
# 	DtaVertices.append( pt )

# while brgtemp <= ((5*math.pi/2) - brgSkip):
# 	pt = rngbrg2latlon(rngtemp, brgtemp+DirectionAngle, CellCenter )
# 	DtaVertices.append( pt )
# 	print (pt)
# 	count += 1
# 	brgtemp += math.pi/16
#
#
# radiusKm1 = CellVelocity*60/60
# interPt = IntermediatePoint(pt1, pt, CellCenter, radiusKm1/RadiusEarthKm)
# DtaVertices.append(interPt)
minutes = [60]
for i in minutes:
	radiusKm1 = CellVelocity*i/60
	interPt = IntermediatePoint(last, next, CellCenter, radiusKm1/RadiusEarthKm)
	brg1Rad = spherical_bearing(CellCenter, interPt)
	rngKm = spherical_distance(CellCenter, interPt)
	first = interPt
	#DtaVertices.append(interPt)
	interPt = IntermediatePoint(pt1, pt, CellCenter, radiusKm1/RadiusEarthKm)
	brg2Rad = spherical_bearing(CellCenter, interPt)
	#DtaVertices.append(interPt)
	last = interPt

	if (brg2Rad < brg1Rad):
		brg2Rad += 2*pi

	while (brg1Rad < brg2Rad):
		pt = rngbrg2latlon(rngKm, brg1Rad, CellCenter)
		DtaVertices.append(pt)
		brg1Rad += math.pi/16


	lastPt = rngbrg2latlon(rngKm, brg2Rad, CellCenter)
	DtaVertices.append(lastPt)


DtaVertices.append(last)
# for i in DtaVertices1:
# 	DtaVertices.append(i)

print("dta vertices:", DtaVertices)

###
# debugging stuff, plot images and such
import numpy, sys
import matplotlib.pyplot as plt
import enipy.visTools as vt
bbox = [ [CellCenter[1]-.5, CellCenter[1]+.5], [CellCenter[0]-.5, CellCenter[0]+.5]]
#~ bbox = [ [-60,60], [-170,170]]

plt.cla()

figMap, figAx = vt.make_map( bbox, zoom=9 )

xy = numpy.array( CellVertices + [CellVertices[0]] )
xy2 = numpy.array( DtaVertices + [DtaVertices[0]] )
figMap.scatter( CellCenter[0], CellCenter[1], color='r', latlon=True )



##
# direction of motion
ptMoving  = rngbrg2latlon( (CellVelocity+DtaMinVelocity), DirectionAngle, CellCenter )
x,y = figMap( 	[CellCenter[0], ptMoving[0]],
				[CellCenter[1], ptMoving[1]] )
figMap.plot( x,y, 'b-' )

#~ plt.plot( [CellCenter[0]-CellVelocity*DirectionVector[1]/100, CellCenter[0]+CellVelocity*DirectionVector[1]/100],
	      #~ [CellCenter[1]+CellVelocity*DirectionVector[0]/100, CellCenter[1]-CellVelocity*DirectionVector[0]/100], 'k-' )

figMap.plot( xy[:,0], xy[:,1], 'b.-', latlon=True )
figMap.plot( xy2[:,0], xy2[:,1], 'r.-', latlon=True )

label = []
for xpt, ypt in zip(xy2[:, 0], xy2[:, 1]):
	label.append(str(xpt) + " " + str(ypt))

print("label:", label)

for label, xpt, ypt in zip(label, xy2[:, 0], xy2[:, 1]):
	plt.text(xpt, ypt, label,color='green')

print("finished")
plt.show()
#~ plt.axes().set_aspect('equal')
