# Puzzle from AoC https://adventofcode.com/2021/day/1

def get_num_from_file(fileobj):
    line_str = fileobj.readline().strip()
    if(line_str != ""):
        return int(line_str)
    else:
        return None

depth_readings_file_path = './first_input.txt'
depth_readings = open(depth_readings_file_path, 'r')

first_reading = get_num_from_file(depth_readings)
second_reading = get_num_from_file(depth_readings)
count = 0
while first_reading != None and second_reading != None:
   count += 1 if second_reading - first_reading > 0 else 0 
   first_reading = second_reading
   second_reading = get_num_from_file(depth_readings)

print(count)

