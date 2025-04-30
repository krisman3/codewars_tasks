exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())


print_hour = 0
print_minute = 0

final_exam_minutes = (exam_hour * 60) + exam_minute
final_arrival_minutes = (arrival_hour * 60) + arrival_minute
final_difference = final_exam_minutes - final_arrival_minutes
if final_difference * -1 > 59:
    print_hour = final_difference // 60
    print_minute = final_difference % 60
    ### stuck here

print(f"final exam minutes: {final_exam_minutes}\n"
      f"final arrival minutes: {final_arrival_minutes}\n"
      f"final difference: {final_difference}")

print(f"{final_exam_minutes} / {final_arrival_minutes}")

if final_arrival_minutes == final_exam_minutes:
    print("On time")
elif final_exam_minutes > final_arrival_minutes:
    print(f"On time\n{final_difference // 60}:{final_difference%60:02d}")
elif final_exam_minutes < final_arrival_minutes:
    print(f"Late\n{final_difference // 60}:{final_difference%60:02d}")