# Puzzle from AoC https://adventofcode.com/2021/day/1

def get_command_from_file(fileobj):
    line_str = fileobj.readline().strip()
    if(line_str != ""):
        command_line = line_str.split(' ')
        return (command_line[0], int(command_line[1]))
    else:
        return None

depth_readings_file_path = './second_input.txt'
depth_readings = open(depth_readings_file_path, 'r')

reading = get_command_from_file(depth_readings)
depth = 0
horizontal = 0
while reading != None:
  if reading[0] == "up":
    depth -= reading[1]
  elif reading[0] == "down":
    depth += reading[1]
  elif reading[0] == "forward":
    horizontal += reading[1]
  reading = get_command_from_file(depth_readings)

print(depth)
print(horizontal)
print(depth * horizontal)
