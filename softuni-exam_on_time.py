exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

hour_diff = 0
minute_diff = 0

# Positive cases
# Exact time
if exam_hour == arrival_hour and exam_minute == arrival_minute:
    print("On time")

elif exam_hour >= arrival_hour:
    if exam_minute >= arrival_minute:
        hour_diff = exam_hour - arrival_hour
        minute_diff = exam_minute - arrival_minute
        if hour_diff == 0:
            print(f"On time\n{minute_diff:02d} minutes before start")
        else:
            print(f"On time\n{hour_diff}:{minute_diff:02d} hours before the start")
    if exam_minute < arrival_minute:
        hour_diff = exam_hour - arrival_hour
        if hour_diff == 0:
            minute_diff = 60 - arrival_minute
            print(f"On time\n{minute_diff:02d} minutes before start")
        else:
            print(f"On time\n{hour_diff}:{minute_diff:02d} hours before the start")

# Negative cases with the same hour
elif exam_hour == arrival_hour:
    if exam_minute < arrival_minute:
        minute_diff = arrival_minute - exam_minute
        print(f"Late\n{minute_diff:02d} minutes after the start")


# Negative cases with different hour
elif exam_hour < arrival_hour:
    minute_diff = (60 - exam_minute) + arrival_minute
    if minute_diff >= 60:
        minute_diff -= 60
        hour_diff = arrival_hour - exam_hour
        print(f"Late\n{hour_diff}:{minute_diff:02d} hours after the start")
