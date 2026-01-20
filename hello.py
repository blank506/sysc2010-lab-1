import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print ("libraries are imported successfully!")
#create a small series
data = pd.Series([1, 3, 5, np.nan, 6, 8])
print(data)
print("hi there")

#this will for the task on hand section:Q1

#Amp = 5V/// F=10Hz/// t=for 1 sec/// fs=500

Time = np.arange(0,1,1/500)#the arrange function parameters are (start,stop,steps)we want a sample each (1/500)sec
Sine_Wave = 5 * np.sin(2 * np.pi * 10 * Time)#we follow the formula for generating a sinusiodal signal(angler freq is 2.pi.F)
plt.plot(Time,Sine_Wave)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Visualizing Synthetic Signals")
plt.show