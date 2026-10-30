import pandas as pd
from dash import Dash,dcc,html,Input,Output
import plotly.express as px
from pathlib import Path
p=Path("data/launches_clean.csv")
if not p.exists(): raise SystemExit("Run notebook 01 first.")
df=pd.read_csv(p); app=Dash(__name__)
sites=sorted(df.LaunchSite.dropna().unique())
app.layout=html.Div([html.H1("SpaceX Falcon 9 Landing Analysis"),
 dcc.Dropdown(options=[{"label":"All sites","value":"ALL"}]+[{"label":s,"value":s} for s in sites],value="ALL",id="site"),
 dcc.Graph(id="year"),dcc.Graph(id="sites"),html.Div(id="summary")])
@app.callback(Output("year","figure"),Output("sites","figure"),Output("summary","children"),Input("site","value"))
def update(site):
 d=df if site=="ALL" else df[df.LaunchSite==site]
 y=d.groupby("Year",as_index=False).Class.mean(); s=d.groupby("LaunchSite",as_index=False).Class.mean()
 a=px.line(y,x="Year",y="Class",markers=True,title="Landing success rate by year"); a.update_yaxes(tickformat=".0%")
 c=px.bar(s,x="LaunchSite",y="Class",title="Landing success rate by launch site"); c.update_yaxes(tickformat=".0%")
 return a,c,"Launches analysed: {} | Success rate: {:.1%}".format(len(d),d.Class.mean())
if __name__=="__main__": app.run(debug=True)
