from datetime import datetime

# log_file = "cybersicurity.logs"
log_file = input("enter file name :")

current_time = datetime.now()

with open(log_file,"r") as file:
    logs = file.readlines()

total_log = len(logs)

print("===== SOC LOG ANALYZER =====")

ERROR_COUNT=0
WARNING_COUNT=0
INFO_COUNT=0

for log in logs:
    log = log.strip()
    print(log)

    if "ERROR" in log:
        ERROR_COUNT+=1
    elif "WARNING" in log:
        WARNING_COUNT+=1
    elif "INFO" in log:
        INFO_COUNT+=1

print("\n====-****/SUMMARY/****-====\n")
INFO_PERCENTAGE = (INFO_COUNT/total_log)*100
ERROR_PERCENTAGE = (ERROR_COUNT/total_log)*100
WARNING_PERCENTAGE = (WARNING_COUNT/total_log)*100


print("===-TOTAL_PERCENTAGE-===\n")
print(f"info :{INFO_PERCENTAGE:.2f}%")
print(f"error:{ERROR_PERCENTAGE:.2f}%")
print(f"warning:{WARNING_PERCENTAGE:.2f}%")

print("\nERROR_COUNT :",ERROR_COUNT)
print("WARNING_COUNT",WARNING_COUNT)
print("INFO_COUNT",INFO_COUNT)
print("\ntotal_log->",total_log)


print("\n===ERROR-LOGS===\n")

for log in logs:
    if "ERROR" in log:
        print(log.strip())
    


with open("Report.txt","w") as Report:
    Report.write("====/SUMMARY/====\n")
    Report.write(f"DATE :{current_time.strftime('%d-%m-%Y')}\n")
    Report.write(f"TIME :{current_time.strftime('%H:%S:%M')}\n\n")

    Report.write(f"total logs:{total_log}\n")
    Report.write(f"info logs:{INFO_COUNT}\n")
    Report.write(f"error logs:{ERROR_COUNT}\n")
    Report.write(f"warning logs:{WARNING_COUNT}\n\n")


    Report.write("*****PERCENTAGE*****\n")
    Report.write(f"info:{INFO_PERCENTAGE:.2f}%\n")
    Report.write(f"error:{ERROR_PERCENTAGE:.2f}%\n")
    Report.write(f"warning:{WARNING_PERCENTAGE:.2f}%\n")

with open("ERROR_LOGS.txt","w") as error_file:
    for log in logs:
        if "ERROR" in log:
            error_file.write(log)


    