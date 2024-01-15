
names = []

with open("names.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        names.append(line)
num = 0
for name in names:
    num += 1
    with open("example.txt") as temp_file:
        temp = temp_file.read()
        temp = temp.replace("name",name)
    with open(f"letter{num}.txt", mode="w") as final_file:
        final_file.write(f"{temp}")

