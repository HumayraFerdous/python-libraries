import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#displaying plots in Matplotlib
x1 = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x1,np.sin(x1),'-')
plt.plot(x1,np.cos(x1),'--')
plt.show()

plt.subplot(2,1,1)
plt.plot(x1,np.sin(x1))

plt.subplot(2,1,2)
plt.plot(x1,np.cos(x1))
plt.show()
x = np.linspace(0,2,100)
plt.plot(x,x,label = 'linear')
plt.plot(x,x**2,label = 'quadratic')
plt.plot(x,x**3,label = 'cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple plot")
plt.legend()
plt.show()
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()
fig, ax = plt.subplots(2)
ax[0].plot(x1,np.sin(x1),'b-')
ax[1].plot(x1,np.cos(x1),'b-')
fig = plt.figure()
x2 = np.linspace(0,5,10)
y2 = x2**2
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x2,y2,'r')
axes.set_xlabel('x2')
axes.set_ylabel('y2')
axes.set_title('title')

x3 = np.arange(0.0,6.0,0.01)
plt.plot(x3,[xi**2 for xi in x3],'b-')
#Scatter plot
x7 = np.linspace(0,10,30)
y7 = np.sin(x7)
plt.plot(x7,y7,'o',color = 'black')

#histogram
data1 = np.random.randn(1000)
plt.hist(data1)

#bar chart
data2 = [5,25,50,20]
plt.bar(range(len(data2)),data2)

#horizontal bar chart
data2 = [5,25,50,20]
plt.barh(range(len(data2)),data2)

#Stacked bar chart
A = [15, 30, 45, 22]
B = [15, 25, 50, 20]
z2 = range(4)
plt.bar(z2, A, color = 'b')
plt.bar(z2, B, color = 'r', bottom = A)

#pie chart
x10 = [35,25,20,20]
labels = ['Computer','Electronics','Mechanical','Chemical']
plt.pie(x10,labels = labels)

#box plot
data3 = np.random.randn(100)
plt.boxplot(data3)
plt.show()