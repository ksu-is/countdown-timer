import time

def set_countdown():
    while True:
        try:
            seconds = int(input("Enter amount of seconds: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    print('Countdown starts now...')
    for i in range(seconds, -1, -1):
        print(i, end=' ', flush=True)
        time.sleep(1)
    print("\nCountdown ended...\n")

print("===== Welcome to Countdown Timer =====")
while True:
    choice = input("Do you want to set a countdown (y/n): ")
    if 'y' in choice.lower():
        set_countdown()
    elif 'n' in choice.lower():
        print('Exiting...')
        break
    else:
        print('Invalid input...please try again')
