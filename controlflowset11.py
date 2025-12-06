rows = [{"cpu": 10}, {"cpu": 55}, {"cpu": 90}]

for r in rows:
    if r["cpu"] < 20:
        print("Idle")
    elif r["cpu"] < 50:
        print("Normal")
    elif r["cpu"] < 80:
        print("Busy")
    else:
        print("Overloaded")

             
