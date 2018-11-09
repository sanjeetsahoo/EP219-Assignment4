import numpy as np        #import NumPy library
import matplotlib.mlab as mlab  # import matplotlib 
from astropy.table import Table # import 
import matplotlib.pyplot as plt #import matplot Library for plotting histogram
data = np.genfromtxt('recoilenergydata_EP219.csv', skip_header=1, delimiter=",", dtype=float)
#Extract data from csv file into NumPy array excluding first row and using integers from columns M, N, O
#print(data)
from sympy import *

#clearly labelled histogram of the data
t = Table(data, names=('er', 'events'), meta={'name': 'first table'})#making an astropy table of data
plt.bar(t['er'], t['events'])# making a plot having events as height and recoil energy as x axis
plt.ylabel("Number of events")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title('Histogram for no of events for recoil energy ')#giving titles

plt.show()#showing the plot

#Assuming background only processes, calculating the mean number of events and making a histogram of this expected background.
dd = t['er']/10#taking recoil energy /10 as an array dd
t['dn_der'] = 1000*np.exp(-dd)# storing the background energy as another column in the table,
#since bin size is one the total no of events, i.e., curve area in each bin is t['dn_der']*1 which has not been shown
t['dn_t'] = t['dn_der']/t['events'] #averaging
plt.bar(t['er'], t['dn_t'])#  making a plot having average background events as height and recoil energy as x axis
plt.ylabel("Expected value of background")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title('Histogram for Expected value of background vs recoil energy')#giving titles
plt.show()#showing the plot

# defining a function for calculating the signal values for sigma = 0.01
def fun1(x,sigma):
    #for different segments if statements has been used to assign the values to the function
    if x.any() <= 5:
        return 0
    elif x.any()>5 and x.any()<15:
        return sigma*20*(x - 5)
    elif x.any()>=15 and x.any()<=25:     
        return sigma*20*(25-x)
    else:
        return 0

er1 =t['er']
ans1 = []#an empty list
ans2 = []#an empty list
ans3 = []#an empty list
ans4 = []#an empty list
ans5 = []#an empty list
for val in er1:
    ans1.append(fun1(val,0.01))#having the func value appended in the empty list for different value of recoil energy for sigma = 0.01
    ans2.append(fun1(val,0.1))#having the func value appended in the empty list for different value of recoil energy for sigma = 0.1
    ans3.append(fun1(val,1))#having the func value appended in the empty list for different value of recoil energy for sigma = 1
    ans4.append(fun1(val,10))#having the func value appended in the empty list for different value of recoil energy for sigma = 10
    ans5.append(fun1(val,100))#having the func value appended in the empty list for different value of recoil energy for sigma = 100

t['sig0.01'] = ans1# having seperate column in the table for the value of signal+backgroung for sigma =0.01
t['sig0.1'] = ans2# having seperate column in the table for the value of signal+backgroung for sigma =0.1
t['sig1'] = ans3# having seperate column in the table for the value of signal+backgroung for sigma = 1
t['sig10'] = ans4# having seperate column in the table for the value of signal+backgroung for sigma =10
t['sig100'] = ans5# having seperate column in the table for the value of signal+backgroung for sigma =100
dd = t['er']/10#taking recoil energy /10 as an array dd
t['dn_der'] = 1000*np.exp(-dd)# storing the background energy as another column in the table,

t['tot'] = t['dn_der'] + t['sig0.01']#calculating total signal+ background for sigma = 0.1
t['mean'] = t['tot']/t['events']# averaging

plt.bar(t['er'], t['mean'])# making a plot having average signal+ background events as height and recoil energy as x axis
plt.ylabel("Expected value of background and signal")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title(r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=0.01')#giving titles
plt.show()#showing the plot

t['tot1'] = t['dn_der'] + t['sig0.1']#calculating total signal+ background for sigma = 0.1
t['mean1'] = t['tot1'] /t['events']# averaging

plt.bar(t['er'], t['mean1'])# making a plot having average signal+ background events as height and recoil energy as x axis
plt.ylabel("Expected value of background and signal")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title(r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=0.1')#giving titles
plt.show()#showing the plot

t['tot2'] = t['dn_der'] + t['sig1']#calculating total signal+ background for sigma = 1
t['mean2'] = t['tot2'] /t['events']# averaging

plt.bar(t['er'], t['mean2'])# making a plot having average signal+ background events as height and recoil energy as x axis
plt.ylabel("Expected value of background and signal")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title(r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=1')#giving titles
plt.show()#showing the plot

t['tot3'] = t['dn_der'] + t['sig10']#calculating total signal+ background for sigma = 10
t['mean3'] = t['tot3'] /t['events']# averaging

plt.bar(t['er'], t['mean3'])# making a plot having average signal+ background events as height and recoil energy as x axis
plt.ylabel("Expected value of background and signal")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title(r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=10')#giving titles
plt.show()#showing the plot

t['tot4'] = t['dn_der'] + t['sig100']#calculating total signal+ background for sigma = 100
t['mean4'] = t['tot4'] /t['events']# averaging

plt.bar(t['er'], t['mean4'])# making a plot having average signal+ background events as height and recoil energy as x axis
plt.ylabel("Expected value of background and signal")#giving y labels
plt.xlabel("Measured recoil energies(keV)")#giving x labels
plt.title(r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=100')#giving titles
plt.show()#showing the plot

# log likelihood function
N = sum(t['events'])#total number of events
def prob(aa):
    totl = aa# assigning aa to totl
    prob = totl/N #calculating the prob of the events
    return prob #return the probability from the function
t['s'] = prob(t['tot']) #making separate columns in the t table for sigma = 0.01
t['s1'] = prob(t['tot1'])#making separate columns in the t table for sigma = 0.1
t['s2'] = prob(t['tot2'])#making separate columns in the t table for sigma = 1
t['s3'] = prob(t['tot3'])#making separate columns in the t table for sigma = 10
t['s4'] = prob(t['tot4'])#making separate columns in the t table for sigma = 100
# defining a function for plotting different probability functions for different sigma 
def gr(aa,name):
    f = plt.bar(t['er'], aa)# making a plot having average signal+ background events as height and recoil energy as x axis
    plt.ylabel("Expected value of background and signal")#giving y labels
    plt.xlabel("Measured recoil energies(keV)")#giving x labels
    plt.title(name)#giving titles
    # plt.show()#showing the plot
    return f
#plotting the prob for sigma =100
gr(t['s4'],r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=100')

<BarContainer object of 40 artists>

#plotting the prob for sigma =10
gr(t['s3'],r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=10')

<BarContainer object of 40 artists>

#plotting the prob for sigma =1
gr(t['s2'],r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=1')

<BarContainer object of 40 artists>

#plotting the prob for sigma =0.1
gr(t['s1'],r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=0.1')

<BarContainer object of 40 artists>

#plotting the prob for sigma =0.01
gr(t['s'],r'Histogram for Expected value of signal and background vs recoil energy for $\sigma$=0.01')

<BarContainer object of 40 artists>

#likelihood function
sigma = np.linspace(0,1000, num = 500)#distributing sigma 
ff = []#empty array
for aa in sigma:
    cc = []
    am = 0
    for mm in er1:
        tt =np.log(fun1(mm,aa) + 1000*np.exp(-(mm/10)))#taking the log of total signal +background 
        cc.append(tt)
        ff.append(sum(cc))#taking the likelihood

#plotting the histogram of likelihood
plt.hist(ff, histtype='step')

plt.ylabel("Number of events")
plt.xlabel(r"log(Likelihood)")
#plt.xlim(-15.5,-5)
plt.title(r'Histogram for log(likelihood) ')
plt.show()

#taking sigma as symbol
sigma = Symbol('sigma', real=True)
#defing function of sigma again
def f(sigma):
    #for different segments if statements has been used to assign the values to the function
    for aa in er1:        
        if aa >5 and aa<15:
            return sigma*20*(aa - 5)
        elif aa>=15 and aa<=25:     
            return sigma*20*(25-aa)
        else:
            return 0
#differentiating with respect to sigma
fun1_p = f.diff(sigma)
#solving to find maxima
solve(fun1_p, sigma)
