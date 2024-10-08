import seaborn as  sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rng = np.random.RandomState(0)
x = np.linspace(0,10,500)
y = np.cumsum(rng.randn(500,6),0)
plt.plot(x,y)
plt.legend('ABCDEF',ncol=2,loc='upper left')
plt.show()
data = np.random.multivariate_normal([0,0],[[5,2],[2,2]],size = 2000)
data = pd.DataFrame(data,columns = ['x','y'])
plt.scatter(data['x'],data['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bivariate Normal Distribution')
plt.show()
for col in 'xy':
    plt.hist(data[col], alpha = 0.5)
#plt.show()
for col in 'xy':
    sns.kdeplot(data[col],fill=True)
plt.show()
sns.histplot(data['x'], kde = True)
sns.histplot(data['y'], kde = True)
with sns.axes_style('white'):
    sns.jointplot(x = "x", y = "y", data = data, kind ='kde',fill_contours = True, cmap ='viridis',alpha = 0.5)
plt.show()
#IRIS dataset - histogram, violinplot, pairplot,jointplot
iris = sns.load_dataset("iris")
print(iris.head())

sns.histplot(x="petal_length",bins = 20, kde = True, color = "green",data=iris)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Distribution of Petal Lengths in Iris Flowers")
plt.show()
sns.violinplot(x="species",y="petal_length",data=iris)
plt.show()
sns.pairplot(iris,hue = 'species',size = 2.5)
plt.show()
sns.jointplot(x="sepal_length",y="sepal_width",data=iris)
plt.show()
#tips dataset - scatterplot,histogram, kdeplot, boxplot, heatmap, facetgrid
tips = sns.load_dataset('tips')
print(tips.head())
sns.scatterplot(x="total_bill",y = "tip",hue="sex",size="size",sizes=(50,200), data = tips)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Relationship between Total Bill and Tip")
plt.show()
sns.histplot(data=tips,x="total_bill")
plt.show()
sns.kdeplot(data=tips,x="total_bill",hue="time",fill=True,alpha = 0.6,linewidth = 1.5)
plt.title("Density Plot of Total Bill by Meal Time")
plt.xlabel("Total Bill ($)")
plt.ylabel("Density")
plt.show()
sns.boxplot(x="day",y="total_bill",hue = "time",data=tips)
plt.show()
corr = tips.corr(numeric_only=True)
sns.heatmap(corr)
plt.show()
tips['tip_pct'] = 100*tips['tip']/tips['total_bill']
grid = sns.FacetGrid(tips,row="sex",col="time",margin_titles=True)
grid.map(plt.hist,"tip_pct",bins = np.linspace(0,40,15))
#fmri dataset - lineplot
fmri = sns.load_dataset("fmri")
print(fmri.head())
sns.lineplot(x="timepoint",y="signal",hue ="event",style ="region",markers = True,dashes = False,data=fmri)
plt.xlabel("Timepoint")
plt.ylabel("Signal Intensity")
plt.title("Changes in Signal Intensity over Time")
plt.show()
#titanic dataset - barplot
titanic = sns.load_dataset("titanic")
print(titanic.head())
sns.barplot(x="class", y="fare", hue="sex", errorbar=None, palette="muted", data=titanic)
plt.xlabel("Class")
plt.ylabel("Fare")
plt.title("Average Fare by Class and Gender on the Titanic")
plt.show()
#flights dataset - heatmap
flights = sns.load_dataset('flights')
flights = flights.pivot_table(index='year',columns="month",values= 'passengers')
sns.heatmap(flights, cmap='Blues', annot=True, fmt='.0f')
plt.title('Passengers per month')
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()