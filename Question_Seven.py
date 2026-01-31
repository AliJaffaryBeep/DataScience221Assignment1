def timeConversion(seconds_since_midnight):


    hours24 = seconds_since_midnight // 3600
    remainder = seconds_since_midnight % 3600
    minutes = remainder // 60
    seconds = remainder % 60

    am_pm = "AM" if hours24 < 12 else "PM"

    hours12 = hours24 % 12
    if hours12 == 0:
        hours12 = 12

    return f"{hours12} {minutes} {seconds} {am_pm}"


# test

print(timeConversion(6767))