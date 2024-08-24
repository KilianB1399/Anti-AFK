import pyautogui
import time

total_duration = 18000
key_press_duration = 0.5

for i in range(3, 0, -1):
    print(f"Starting in {i}...")
    time.sleep(1)

print("Go!")

start_time = time.time()

while time.time() - start_time < total_duration:
    elapsed_time = time.time() - start_time
    remaining_time = total_duration - int(elapsed_time)
    
    if int(elapsed_time) < total_duration:
        print(f"Time remaining: {remaining_time} seconds")

    pyautogui.keyDown('d')
    time.sleep(key_press_duration * 1)
    pyautogui.keyUp('d')

    pyautogui.keyDown('a')
    time.sleep(key_press_duration * 1)
    pyautogui.keyUp('a')

print("Simulation complete!")
