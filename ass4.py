
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
kLa=0.007
 #1/s Mass transfer Coefficient(Perry's Handbook)
A=1
pT=1#"""atm"""
Hc=.034## (in M/atm at T=298.15K)
de=([0.523, 0.554])
MDc=.523/40#"M"-# kg/ m^3 http://www.peacesoftware.de/einigewerte/calc_co2.php5,http://www.peacesoftware.de/einigewerte/calc_methan.php5
Hm=.0014## (in M/atm at T=298.15K)
a=350 # m^2/m^3
kg=.00002 #gmol/m^2-Pa-s Mass transfer Coefficient
MDm=.554/40#"M"
kGa=7*10**(-7) # gmol/L-Pa-s
Pwsat=0.03125#"atm"
def deriv(y,t):
    yc=y[0]/(y[0]+y[1]+y[2])
    ym=y[1]/(y[0]+y[1]+y[2])
    yw=y[2]/(y[0]+y[1]+y[2])
    xc=y[3]/(y[3]+y[4]+y[5])
    xm=y[3]/(y[3]+y[4]+y[5])
    xw=y[3]/(y[3]+y[4]+y[5])
    
    dGc=-kLa*A*(yc*pT*Hc-MDc*xc)
    dLc=-kLa*A*(yc*pT*Hc-MDc*xc)
    dGm=-kLa*A*(ym*pT*Hm-MDm*xm)
    dLm=-kLa*A*(ym*pT*Hm-MDm*xm)
    dGw=kGa*A*(pT*yw-Pwsat)
    dLw=kGa*A*(pT*yw-Pwsat)
    return array([dGc,dLc,dGm,dLm,dGw,dLw])

a=array([10,10,80])
t=linspace(0,10,100)
def error(a):
    yinitial=array([50,a[0],50,a[1],0,a[2]])
    sol=odeint(deriv,yinitial,t)
    return array([sol[99,1],sol[99,3],sol[99,5]-100])
ans=fsolve(error,a)
print ans    
    
    