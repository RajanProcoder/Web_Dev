import time

# Get total seconds from user
my_time = int(input("Enter Time in sec: "))

# Loop backwards from total time down to 1
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24
    
    # Print formatted time on the same line
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)

print("Times Up!        ")
