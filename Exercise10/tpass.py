import getpass


pin = "1234"  # Store the PIN as a string
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    supplied_pin = input("Enter your PIN: ")

    if supplied_pin == pin:
        print("Correct")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print("Incorrect PIN. Remaining attempts:", remaining_attempts)

if attempts == max_attempts:
    print("Maximum number of attempts reached.")
