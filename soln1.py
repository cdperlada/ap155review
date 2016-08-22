# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:09:11 2016

@author: cdperlada
"""

#1.1a
#A. The Gravitational force is given by $$\tag{1}F = \frac{GmM}{r^2}$$ where $ G = 6.67 x 10^{-11} m^3 kg^{-1} s^{-2} $ is Newton's gravitational constant, $ M = 5.97 x 10^{24} kg $ is the mass of the earth, $m$ is the mass of the satellite and $r$ is the distance separation of the center of the earth and satellite.
#Note that $r$ is given by $$\tag{2}r = R+h$$ where $R = 6371 km$ is the radius of the earth and $h$ is the altitude of the satellite.The centripetal force is given by $$\tag{3} F = \frac{mv^2}{r}.$$ We can write $v$ as $$\tag{4}v = \frac{2 \pi r}{T}.$$ Eq(3) becomes $$\tag{5}F = \frac{4m \pi^2 r}{T^2}$$
#Equating (1) and (5), $$\tag{6}\frac{GmM}{r^2} = \frac{4m \pi^2 r}{T^2}$$ $$\tag{7}r^3=\frac{GMT^2}{4 \pi^2}$$ $$\tag{8}r={\left(\frac{GMT^2}{4 \pi^2}\right)}^{1/3}$$
#Substitute (2) to (8) $$\tag{9}h+R={\left(\frac{GMT^2}{4 \pi^2}\right)}^{1/3}$$ $$\tag{10}h={\left(\frac{GMT^2}{4 \pi^2}\right)}^{1/3}- R$$
#Thus, the altitude $h$ above the Earth’s surface that the satellite must have is $$h={\left(\frac{GMT^2}{4 \pi^2}\right)}^{1/3}- R.$$

from math import pi
G = 6.67E-11
M = 5.97E24
R = 6371.0E3 
period = input('Enter time in seconds: ')  #86148

def altitude(T):
    h = (((G*M*T**2)/(4*pi**2))**(1.0/3.0))-R
    return h

if __name__ == "__main__":
    if altitude(period)<0:
        print 'The altitude is %.3f meters. The satellite is below the earth surface.' % altitude(period)
    elif altitude(period)==0:
        print  'The altitude is %.3f meters. The satellite is on the earth surface' % altitude(period)
    else:
        print  'The altitude is %.3f meters. The satellite is above the earth surface.' % altitude(period)
        
#1.1b and c
#Enter some time: 86400
#The altitude is 35855910.176. The satellite is above the earth surface.
#Enter some time: 5400
#The altitude is 279321.625 meters. The satellite is above the earth surface.
#Enter some time: 2700
#The altitude is -2181559.898 meters. The satellite is below the earth surface. It is impossible.
#D. Enter some time: 86148
#The altitude is 35773762.330 meters. The satellite is above the earth surface.
#For an observer on the surface of the earth, the synchronization of orbital and rotation period means that for an object in geosynchronous orbit it returns exactly to the same position in the sky after of one sidereal day.
#The diffrence between the calculated altitudes is 82147.846 meters.