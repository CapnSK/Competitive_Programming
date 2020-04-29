hours = int(input())
longitude = float(input())

time = (hours/360)*longitude

hour = int(time)%12
minute = (time - int(time))*60

hourAngle =(hour*30) + (minute*(1/2))
minuteAngle = minute*6

# print(hourAngle,minuteAngle)

differnce = abs(hourAngle - minuteAngle)
differnce = min(differnce,360-differnce)

print(str.format('{0:.2f}',differnce) , end='')