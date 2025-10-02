# File Handling
with open("file.txt", "w") as f:
    f.write("Hello\nPython\nRocks")

with open("file.txt", "r") as f:
    print(f.read())

with open("file.txt", "r") as f:
    lines = f.readlines()
    print("Total lines:", len(lines))
