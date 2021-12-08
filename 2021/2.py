# Puzzle from AoC https://adventofcode.com/2021/day/1

def get_num_from_file(fileobj):
    line_str = fileobj.readline().strip()
    if(line_str != ""):
        return int(line_str)
    else:
        return None

depth_readings_file_path = './second_input.txt'
depth_readings = open(depth_readings_file_path, 'r')

count = 0

first_reading = get_num_from_file(depth_readings)
second_reading = get_num_from_file(depth_readings)
third_reading = get_num_from_file(depth_readings)
fourth_reading = get_num_from_file(depth_readings)

while fourth_reading != None:
   first_window = first_reading + second_reading + third_reading
   second_window = second_reading + third_reading + fourth_reading
   count += 1 if second_window - first_window > 0 else 0 
   first_reading = second_reading
   second_reading = third_reading
   third_reading = fourth_reading
   fourth_reading = get_num_from_file(depth_readings)

print(count)

