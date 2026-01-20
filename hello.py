import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print ("libraries are imported successfully!")
#create a small series
data = pd.Series([1, 3, 5, np.nan, 6, 8])
print(data)
print("hi there")

#this will be for the task on hand section:Q1

#Amp = 5V/// F=10Hz/// t=for 1 sec/// fs=500

Time = np.arange(0,1,1/500)#the arrange function parameters are (start,stop,steps)we want a sample each (1/500)sec
Sine_Wave = 5 * np.sin(2 * np.pi * 10 * Time)#we follow the formula for generating a sinusiodal signal(angler freq is 2.pi.F)

plt.plot(Time,Sine_Wave)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Visualizing Synthetic Signals")
plt.show

#this will be for the task on hand section:Q2

#Amp = 5V/// F=10Hz/// t=for 1 sec/// fs=500 

Time = np.arange(0,1,1/500)
Sine_Wave = 5 * np.sin(2 * np.pi * 10 * Time)
# Generate Gaussian noise
noise = 0.25 * np.random.randn(500)
# Noisy signal
noisy_signal = Sine_Wave + noise

plt.figure()
plt.plot(Time, Sine_Wave, label="Clean Signal")
plt.plot(Time, noisy_signal, label="Noisy Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Clean vs Noisy Signal")
plt.legend()
plt.grid(True)
plt.savefig("Task4_2.png")
plt.show()

#this will be for the task on hand section:Q3

num_samples = 120

time = np.arange(0, num_samples * 60, 60)

temperature = 36 + np.random.uniform(-0.5, 0.5, num_samples)

# Create DataFrame
data = {
    "Time (s)": time,
    "Temperature (°C)": temperature
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sensor_readings.csv", index=False)

# Read the CSV file
df_read = pd.read_csv("sensor_readings.csv")

# Extract samples 41 to 80
subset = df_read.iloc[41:81]

# Plot extracted data
plt.figure()
plt.plot(subset["Time (s)"], subset["Temperature (°C)"], marker='o')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Sensor Readings (Samples 41 to 80)")
plt.grid(True)
plt.show()
 
 # this is the final change