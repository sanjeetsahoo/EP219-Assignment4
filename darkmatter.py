import numpy as np        #import NumPy library
import matplotlib.mlab as mlab  # import matplotlib 
from astropy.table import Table # import 
import matplotlib.pyplot as plt #import matplot Library for plotting histogram
data = np.genfromtxt('recoilenergydata_EP219.csv', skip_header=1, delimiter=",", dtype=float)
#Extract data from csv file into NumPy array excluding first row and using integers from columns M, N, O
#print(data)

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
def fun1(x):
    #for different segments if statements has been used to assign the values to the function
    if x <= 5:
        return 0
    elif x>5 and x<15:
        return 0.01*20*(x - 5)
    elif x>=15 and x<=25:     
        return 0.01*20*(25-x)
    else:
        return 0

er1 =t['er']
ans1 = []#an empty list
for val in er1:
    ans1.append(fun1(val))#having the func value appended in the empty list for different value of recoil energy
t['sig0.01'] = ans1# having seperate column in the table for the value of signal+backgroung for sigma =0.01

# defining a function for calculating the signal values for sigma = 0.1
def fun2(x):
    #for different segments if statements has been used to assign the values to the function
    if x <= 5:
        return 0
    elif x>5 and x<15:
        return 0.1*20*(x - 5)
        print("hey")
    elif x>=15 and x<=25:     
        return 0.1*20*(25-x)
    else:
        return 0

ans2 = []#an empty list
for val in er1:
    ans2.append(fun2(val))#having the func value appended in the empty list for different value of recoil energy
t['sig0.1'] = ans2# having seperate column in the table for the value of signal+backgroung for sigma =0.1

# defining a function for calculating the signal values for sigma = 1
def fun3(x):
    #for different segments if statements has been used to assign the values to the function
    if x <= 5:
        return 0
    elif x>5 and x<15:
        return 1*20*(x - 5)
        
    elif x>=15 and x<=25:     
        return 1*20*(25-x)
    else:
        return 0
ans3 = []#an empty list
for val in er1:
    ans3.append(fun3(val))#having the func value appended in the empty list for different value of recoil energy
t['sig1'] = ans3# having seperate column in the table for the value of signal+backgroung for sigma =1

# defining a function for calculating the signal values for sigma = 10
def fun4(x):
    #for different segments if statements has been used to assign the values to the function
    if x <= 5:
        return 0
    elif x>5 and x<15:
        return 10*20*(x - 5)
        
    elif x>=15 and x<=25:     
        return 10*20*(25-x)
    else:
        return 0

er1 =t['er']
ans4 = []#an empty list
for val in er1:
    ans4.append(fun4(val))#having the func value appended in the empty list for different value of recoil energy
t['sig10'] = ans4# having seperate column in the table for the value of signal+backgroung for sigma =10

# defining a function for calculating the signal values for sigma = 100
def fun5(x):
    #for different segments if statements has been used to assign the values to the function
    if x <= 5:
        return 0
    elif x>5 and x<15:
        return 100*20*(x - 5)
        
    elif x>=15 and x<=25:     
        return 100*20*(25-x)
    else:
        return 0
ans5 = []#an empty list
for val in er1:
    ans5.append(fun5(val))#having the func value appended in the empty list for different value of recoil energy
t['sig100'] = ans5# having seperate column in the table for the value of signal+backgroung for sigma =100

dd = t['er']/10#taking recoil energy /10 as an array dd
t['dn_der'] = 1000*np.exp(-dd)# storing the background energy as another column in the table,
t['tot'] = t['dn_der'] + t['sig0.01']#calculating total signal+ background for sigma = 0.01
t['mean'] = t['tot'] /t['events']# averaging

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


