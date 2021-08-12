import plotly.express as px
import plotly.graph_objects as go
import plotly
import pandas as pd

df =pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/titanic.csv")

fig = px.scatter(df, x="Pclass", y="Age", color="Sex")
fig.add_trace(px.scatter(df, x="Pclass", y="Age", color="Survived").data[0])
fig.add_trace(px.scatter(df, x="Pclass", y="Age", color="Survived").data[1])

updatemenus=[dict(type = "buttons", direction = "left",
             buttons=list([
             dict(args=[{'visible': [True  , True  , False , False ]} ,],
                  label = "sex"   , method="update"),

             dict(args=[{'visible': [False , False , True  , True  ]} ,],
                  label = "survived", method="update")
             ])),]

fig.update_layout(updatemenus = updatemenus,
                  legend_title_text='')

fig.show()
