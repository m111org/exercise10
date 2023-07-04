import glob
import os
import sys

# Get directory name
if sys.platform == "win32":
    hdir = os.environ["HOMEPATH"]
else:
    hdir = os.environ["HOME"]

# Construct a portable wildcard pattern
print("# Construct a portable wildcard pattern")

pattern = os.path.join(hdir, "*.*")
print(pattern)
# TODO Use glob.glob to obtain list of file names
print( "# TODO Use glob.glob to obtain list of file names")
print(glob.glob(pattern))
# TODO use os.path.getsize to find file size
print("# TODO use os.path.getsize to find file size")
for f in  glob.glob(pattern):
    print(f, os.path.getsize(f))
# TODO add test to display files that do not have size of zero
print("# TODO add test to display files that do not have size of zero")
for f in glob.glob(pattern):
    if os.path.getsize(f) > 0:
        print(f, os.path.getsize(f))

# TODO remove the lead directory names from each file
# using os.path.basename()
print("# TODO remove the lead directory names from each file")

for f in os.path.basename(f):
    filename = os.path.basename(f)
    print(filename)



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

