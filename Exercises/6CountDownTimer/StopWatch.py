import time

timer = 0
while True:
    time.sleep(1)
    seconds = timer % 60
    minutes = int(timer / 60) % 60
    hours = int(timer / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    timer += 1
