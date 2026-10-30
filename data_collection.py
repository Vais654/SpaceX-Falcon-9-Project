import requests, pandas as pd
from pathlib import Path
def fetch_launches():
    url="https://api.spacexdata.com/v4/launches/query"
    payload={"query":{},"options":{"pagination":False,"populate":[
      {"path":"rocket","select":{"name":1}},
      {"path":"launchpad","select":{"name":1,"latitude":1,"longitude":1}},
      {"path":"cores.core","select":{"serial":1}}]}}
    r=requests.post(url,json=payload,timeout=60); r.raise_for_status()
    rows=[]
    for x in r.json()["docs"]:
        core=(x.get("cores") or [{}])[0]; pad=x.get("launchpad") or {}; rocket=x.get("rocket") or {}
        rows.append({"FlightNumber":x.get("flight_number"),"Mission":x.get("name"),
          "Date":x.get("date_utc"),"Year":pd.to_datetime(x.get("date_utc"),utc=True,errors="coerce").year,
          "LaunchSite":pad.get("name"),"Latitude":pad.get("latitude"),"Longitude":pad.get("longitude"),
          "Rocket":rocket.get("name"),"LandingAttempt":core.get("landing_attempt"),
          "LandingSuccess":core.get("landing_success"),"LaunchSuccess":x.get("success")})
    return pd.DataFrame(rows)
if __name__=="__main__":
    Path("data").mkdir(exist_ok=True); raw=fetch_launches(); raw.to_csv("data/launches_raw.csv",index=False)
    clean=raw[raw.LandingSuccess.notna()].copy(); clean["Class"]=clean.LandingSuccess.astype(int)
    clean.to_csv("data/launches_clean.csv",index=False)
    print("Raw launches:",len(raw),"Known landing outcomes:",len(clean))
