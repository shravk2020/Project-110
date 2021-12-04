import pandas as pd 
import plotly.figure_factory as ff 
import statistics
import random
import plotly.graph_objects as go 

df = pd.read_csv("newdata.csv")

data = df['reading_time'].tolist()

mean = statistics.mean(data)
print("The mean is ", mean)

standev = statistics.stdev(data)
print("The standard deviation is ", standev)

fig = ff.create_distplot([data], ['reading_time'], show_hist = False)
fig.show()

round1data = []
meanList = []

for x in range(0, 100):
    for i in range(0,30):
        randomIndex = random.randint(0,len(data)-1)
        val = data[randomIndex]
        round1data.append(val)
    mean = statistics.mean(round1data)
    meanList.append(mean)

sampleMean = statistics.mean(meanList)
print("Sample Mean is ", sampleMean)

sampleStandev = statistics.stdev(meanList)
print("Sample Standard Deviation is ", sampleStandev)


fig = ff.create_distplot([meanList], ["reading_time_sample_data"], show_hist = False)
fig.show()
