import tpass

pin = "1234"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    supplied_pin = getpass.pin(prompt="Enter your PIN: ")

    if supplied_pin == pin:
        print("Correct")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print("Incorrect PIN. Remaining attempts:", remaining_attempts)

if attempts == max_attempts:
    print("Maximum number of attempts reached.")
