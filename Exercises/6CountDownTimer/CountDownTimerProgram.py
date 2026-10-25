import time

timer = int(input("Please enter your second for timer: "))
for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Wake up! Time is over")
