from stravalib import Client
from datetime import datetime, timedelta, date
import pandas as pd

MY_TOKEN = 'Your Token Here'

client = Client(access_token=MY_TOKEN)

print("Getting Activities")
activities = client.get_activities(after="2025-01-28", limit=2)  

act_list =[]
dates =[]
descriptions = []
act_types = []



for activity in activities:
    act_list.append(activity.id)
    dates.append(activity.start_date_local)
    descriptions.append(activity.name)
    act_types.append(activity.type)

#Dictionary to store zone durations
zones = {"0": [], 
         "1": [],
         "2": [],
         "3": [],
         "4": []}

#Pull heart rate data from activitiy zones and organize into a dictionary
print("Pulling and organizing zone data")
k = 1
for i in act_list:
    try:
        get_hr_zones = client.get_activity_zones(i)[0].distribution_buckets #0 for HR, 1 for Power
        for j in range(0,5):
            zone_dur = get_hr_zones[j].time #returns time in zone in seconds 
            if zone_dur is None:
                zone_dur = 0
            zones[str(j)].append(str(timedelta(seconds = zone_dur)))
        print("Pulled data for activity " +str(k) +"...")
        k = k + 1
    except IndexError:
        for j in range(0,5):
            zones[str(j)].append(str(timedelta(seconds = 0)))
        print("No Heart Rate Data found in Activity "+ str(k))
        k = k + 1

#print(dates)
#print(descriptions)
#print(act_types)
#print(zones)        
    
df = pd.DataFrame({"date": dates,
                   "description": descriptions,
                   "type": act_types,
                   "z1": zones["0"],
                   "z2": zones["1"],
                   "z3": zones["2"],
                   "z4": zones["3"],
                   "z5": zones["4"]},
                  #index=act_list
                  )

print(df)

#Outputs a csv named with today's date    
log_name = (str(datetime.today().strftime('%Y-%m-%d'))+".csv")
df.to_csv(log_name, index=False)

