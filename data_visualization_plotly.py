import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
diamonds = pd.read_csv("diamonds.csv")
print(diamonds.head())
diamonds = diamonds.drop(['serial'], axis = 1)
print(diamonds.head())
diamonds.info()
print(diamonds.describe())
bins = int(len(diamonds) ** (1/2))
fig = px.histogram(diamonds,x = 'price',title = "Histogram of diamond prices",nbins = bins, width = 600,height = 400)
fig.show()
fig = px.histogram(diamonds,x = "cut")
fig.show()
mean_price = diamonds.groupby("cut")["price"].mean().reset_index()
print(mean_price)
fig = px.bar(mean_price, x = "cut", y = "price")
fig.update_layout(title = "Average diamond prices for each cut category", xaxis_title="",yaxis_title="Mean price($)")
fig.show()
fig = px.box(diamonds,x = "clarity", y = "carat")
fig.update_layout(title = "Distribution of diamond carats for each clarity category",xaxis_title = "Clarity",yaxis_title = "Carat")
fig.show()
fig = px.violin(diamonds, x = "cut",y = "price",box = True)
fig.show()
fig = px.scatter(diamonds.sample(5000), x = "price", y = "carat")
fig.update_layout(title = "Price vs. Carat", xaxis_title = "Price ($)",yaxis_title = "Carat")
fig.show()
sample = diamonds.sample(3000)
fig = px.scatter(sample, x="price", y="carat", size = "carat", color="cut")
fig.show()
fig = px.imshow(diamonds.corr(numeric_only=True),color_continuous_scale="Inferno_r")
fig.show()

df = pd.read_csv("volcano_db.csv", encoding="iso-8859-1")
fig = px.histogram(df, x = "Country").update_xaxes(categoryorder = "total descending")
fig.show()
print(df.head())
labels=df.Status.unique()
values=df['Status'].value_counts()
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
fig = go.Figure(data = go.Scattergeo(
    lon = df['Longitude'],
    lat = df['Latitude'],
    mode = 'markers'
))
fig.update_layout(title = 'volcanoes', geo_scope = 'world')
fig.show()
fig = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        mode = 'markers',
        showlegend=False,
        marker=dict(color="crimson", size=4, opacity=0.5))
        )
fig.update_geos(
    projection_type="orthographic",
    landcolor="white",
    oceancolor="MidnightBlue",
    showocean=True,
    lakecolor="LightBlue"
)
fig.show()