exam_start_hour = int(input()) # 10
exam_start_minutes = int(input()) # 30

arrival_hour = int(input()) # 10
arrival_minutes = int(input()) # 00


total_minutes_start_exam = (exam_start_hour * 60) + exam_start_minutes
total_minutes_arrival = (arrival_hour * 60) + arrival_minutes
difference = total_minutes_start_exam - total_minutes_arrival

if difference == 0:
    print("On time")

elif 0 < difference <= 30:
    print("On time")
    print(f"{difference} minutes before the start")  # Time needs to be added

elif 30 < difference <= 59:
    print("Early")
    print(f"{difference} minutes before the start")

elif difference > 59:
    hours = difference // 60
    minutes = difference % 60
    print(f"Early\n{hours}:{minutes:02d} hours before the start")

# Negative cases 

elif -59 <= difference < 0:
    print("Late")
    print(f"{abs(difference)} minutes after the start")
    
elif difference <= -60:
    print("Late")
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    print(f"Late\n{hours}:{minutes:02d} hours after the start")
