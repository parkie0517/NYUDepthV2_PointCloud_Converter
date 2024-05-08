count = 0

with open('filename.txt', 'r') as file:
    # Read each line in the file one at a time
    for line in file:
        # Print each line
        print(line.strip())
        count += 1
print(count)