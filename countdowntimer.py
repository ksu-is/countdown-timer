import time

def get_seconds_input():
    """
    Prompt the user to enter the number of seconds for the countdown.
    """
    while True:
        try:
            seconds = int(input("Enter the number of seconds for the countdown: "))
            if seconds < 0:
                print("Please enter a non-negative integer.")
            else:
                return seconds
        except ValueError:
            print("Please enter a valid integer.")

def countdown(seconds):
    """
    Display the countdown starting from the specified number of seconds.
    """
    print('Countdown starts now...')
    for i in range(seconds, -1, -1):
        print(i, end=' ', flush=True)
        time.sleep(1)
    print("\nCountdown ended...\n")

def main():
    """
    Main function to handle user interaction.
    """
    print("===== Welcome to Countdown Timer =====")
    while True:
        choice = input("Do you want to set a countdown (y/n): ")
        if choice.lower() == 'y':
            seconds = get_seconds_input()
            countdown(seconds)
        elif choice.lower() == 'n':
            print('Exiting...')
            break
        else:
            print('Invalid input. Please enter "y" or "n".')

if __name__ == "__main__":
    main()
