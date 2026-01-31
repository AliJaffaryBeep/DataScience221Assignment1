import math

def circleAreaCoverage(RadiusOfCircle1, RadiusOfCircle2):


    if RadiusOfCircle1 <= 0 or RadiusOfCircle2 <= 0:
        return "Invalid input: radii must be positive."

    area1 = math.pi * (RadiusOfCircle1 ** 2)
    area2 = math.pi * (RadiusOfCircle2 ** 2)

    smaller = min(area1,area2)
    larger = max(area1,area2)

    coverage_percentage = (smaller / larger) * 100

    return coverage_percentage

"""
Input values like print(circleAreaCoverage(2, 5))  

"""
print(circleAreaCoverage(2,5))