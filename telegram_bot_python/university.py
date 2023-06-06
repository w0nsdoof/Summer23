from datetime import datetime

def weekday():
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    now = datetime.now()
    num = datetime.isoweekday(now)

    return weekdays.get(num, "Invalid day")

def semester():

    now = datetime.now()

    # for FALL semester  (Осенний семестр)
    start_fall = datetime(now.year, 9, 1) # year , month = septermber, day
    end_fall = datetime(now.year, 1, 15)

    # for SPRING semester (Весенний семестр)
    start_spring = datetime(now.year, 1, 16)
    end_spring = datetime(now.year, 6, 1)

    # for SUMMER semester (Летний семестр)
    start_summer = datetime(now.year, 6, 5)
    end_summer = datetime(now.year, 7 , 15)

    if end_fall < start_fall:
        end_fall = end_fall.replace(year = end_fall.year + 1) 

    if start_fall <= now <= end_fall:
        return ["🍁Fall", start_fall, end_fall]

    elif start_spring <= now <= end_spring:
        return ["🌺Spring", start_spring, end_spring]
    
    elif start_summer <= now <= end_summer:
        return ["🌴Summer", start_summer, end_summer]
    else:
        return ["🍿Chill",]

def week_numero():
    now = datetime.now()

    sem = semester()

    if sem[0] == "🍿Chill":
        return "0"
    else:
        return (now - sem[1]).days // 7 

