import datetime

men = input("Enter duration in minutes: \n")

mod = datetime.timedelta(minutes=float(men))

tsec = int(mod.total_seconds())

hours, rsec = divmod(tsec, 3600)

minutes, seconds = divmod(rsec, 60)
print(f"""-----------------------------------------
{hours} hours {minutes} minutes {seconds} seconds""")
