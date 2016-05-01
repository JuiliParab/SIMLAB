# various libraries imported for analysis of curvefitting
import scipy,numpy
import scipy.optimize,scipy.stats
import numpy.random
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels
import statsmodels.stats
import statsmodels.stats.stattools as stools
import os
import numpy as np
from scipy.optimize import leastsq
xdata=[1,2,3,4,5,6]
xdata=np.asarray(xdata)
ydata=[40,50,60,70,80,90]
ydata=np.asarray(ydata)
plt.style.use("ggplot")

def fitfunc(p,xdata):
    f=p[0]*xdata+p[1]
    return f

def errfunc(p,xdata,ydata):
    e=fitfunc(p,xdata)-ydata
    return e
    
guess=np.array([10,10])
res=leastsq(errfunc,guess,args=(xdata,ydata))


(popt,pcov)=res   #optimize p
perr=scipy.sqrt(scipy.diag(pcov))    #vector of sd of p
M=len(ydata)
N=len(popt)
#Residuals
y=fitfunc(xdata,popt)
residuals=(y-ydata)
meany=scipy.mean(ydata)
squares=(y-meany)
squaresT=(ydata-meany)

SSM=sum(squares**2) #corrected sum of squares
SSE=sum(residuals**2)  #sum of squares of errors
SST=sum(squaresT**2)  #total corrected sum of squares
	
DFM=N-1   #for model
DFE=M-N   #for error
DFT=M-1   #total
	
MSM=SSM/DFM #mean squares for model(explained variance)
MSE=SSE/DFE #mean squares for errors(should be small wrt MSM) unexplained variance
MST=SST/DFT #mean squares for total	
	
R2=SSM/SST  #proportion of explained variance
R2_adj=1-(1-R2)*(M-1)/(M-N-1) #adjusted R2

#t test to see if parameters are diff from zero	
t_stat=popt/perr
t_stat=t_stat.real #t stat for popt diff from0
p_p=1-scipy.stats.t.cdf(t_stat,DFE)#should be low for a good fit
z=scipy.stats.t(M-N).ppf(0.95)
p95=perr*z
#Chi squared Analysis on residual
chisquared=sum(residuals**2)
dof=M-N
chisquared_red=chisquared/dof
p_chi2=1-scipy.stats.chi2.cdf(chisquared,dof)
sederr_reg=scipy.sqrt(chisquared_red)
chisquare=(p_chi2,chisquared,chisquared_red,dof,R2,R2_adj)
print 'chi result',chisquare

#Analysis of residual
w,p_shapiro=scipy.stats.shapiro(residuals)
mean_res=scipy.mean(residuals)
stddev_res=scipy.sqrt(scipy.var(residuals))
t_res=mean_res/stddev_res #t statistic to check that mean res is non zero
p_res=1-scipy.stats.f.cdf(F,DFM,DFE)

#If p_res<05, null hypothesis is rejected and mean is non zero
#i.e R^2>0 and atleast one of the fitting parameter >0
#should be high for good fit

F=MSM/MSE#explained variance/unexplained variance (Should be large)
p_F=1-scipy.stats.f.cdf(F,DFM,DFE)
#if p_F <0.05,null hypothesis rejecte
#i.e R^2>0 an at;east one of the fitting parameters >0
dw=stools.durbin_watson(residuals)
resanal=(p_shapiro,w,mean_res,p_res,F,p_F,dw)
 """
 Test to seee goodness of fit p0.95 is the vector of 95% confidence range,Shapiro test is to
 check if residuals are normally distriduted and Durbn -Watson test tcheck if they are correlated
 
 #p_shapiro>0.05
 #dw should be near 2 and away frm 0 & 4
 """
if ax:
    formataxis(ax)
    ax.plot(ydata,y,'ro')
    ax.errorbar(ydata,y)
    ymin,ymax=min((min(y),min(ydata))),max((max(y),max(ydata)))
    ax.plot([ymin,ymax],[ymin,ymax],'b')
    
    ax.xaxis.label.set_text('Data')
    ax.yaxis.label.set_text('Fitted')
    
    sigmay,avg_stddev_data=get_stderr_fit(f,xdata,popt,pcov)
    yplus=y+sigmay
    yminus=y-sigmay
    ax.plot(y,yplus,'c',alpha=0.6,linestyle='--',linewidt=0.5)
    ax.plot(y,yminus,'c',alpha=0.6,linestyle='--',linewidt=0.5)
    ax.fill_between(y,yminus,yplus,facecolor='cyan',alpha=0.5)
    titletext='Parity plot fot fit\n'
    titletext+=r'$r^2$=%5.2f,$r^2_{adj}$=%5.2f, '
    titletext+='$\sigma_{exp}$=%5.2f,$\chi^2_{\nu}$=%5.2f,$p_{\chi^2}$=%5.2f, '
    titletext+='$\sigma_{err}^{reg}$=%5.2f'
    ax.title.set_text(titletext%(R2,R2_adj,avg_stddev_data,chisquared_red,p_chi2,stderr_reg))
    ax.figure.canvas.draw()
if ax2:#test for homoscedasticity
    formataxis(ax2)
    ax2.plot(Y,residuals,'ro')
		
    ax2.xaxis.label.set_text('Fitted data')
    ax2.yaxis.label.set_text('Residuals')
    		
    titletext='Analysis of residuals\n'
    titletext+=r'mean=%5.2f,$p_{res}$=%5.2f,$p_{shapiro}$=%5.2f,$Durbin-Watson$=%2.1f'
    titletext+='\n F=%5.2f,$p_F$=%3.2e'
    ax2.title.set_text(titletext%(mean_res,p_res,p_shapiro,dw,F,p_F))
    		
    ax2.figure.canvas.draw()
    		
    return popt,pcov,perr,p95,p_p,chisquare,resanal
    
    
# Code to calcu;ate std error of fit
def get_stderr_fit (fitfunc,p):
    y=fitfunc(xdata,popt)
    listdy=[]
    for i in range(len(opt)):
        p=popt[i]
        dp=abs(p)/1e6+1e-20
        popt[i+=dp
        yi=fitfunc(xdata,popt)
        dy=(yi-y)/dp
        listdy.append(dy)
        popt[i]-=dp
    listdy=scipy.array(listdy)
   #listdY is an array with N rows and M columns, N=len(popt), M=len(xdata[0])
	#pcov is an array with N rows and N columns
    left=scipy.dot(listdv,T,pcov)
    # left an array with M rowsand N column
    right=scipy.dot(left,listdy)
	#right is an array of M rows and M columns
    sigma2y=right.diagonal()
    #sigma2y is standard error of fit and function  of X
    mean_sigma2y=scipy.mean(right.diagonal())
    M=xdata.shape[1];print M
    N=len(popt);print N
    avg_stddev_data=scipy.sqrt(M*mean_sigma2y/N)
    #this is because if exp error is constant at sig_dat,then mean_sigma2y=N/M*sig_dat**2
    sigmay=scipy.sqrt(sigma2y)
    return sigmay,avg_stddev_data

#code to format axis
def formataxis(ax):
	ax.xaxis.label.set_fontname('Georgia')
	ax.xaxis.label.set_fontsize(12)
	ax.yaxis.label.set_fontname('Georgia')
	ax.yaxis.label.set_fontsize(12)	
	ax.title.set_fontname('Georgia')
	ax.title.set_fontsize(12)
	
	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(8)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(8)

    
    
