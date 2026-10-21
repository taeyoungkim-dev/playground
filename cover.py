import sys

def read_map(map_file_path):
	with open(map_file_path) as file:
		ruf_grid = file.read()
	
    

def draw_map():
    pass


def calculate_path():
    pass


def main():
    map_file_path = sys.argv[1]
    print("map_file_path :"+map_file_path)
    read_map(map_file_path)
    calculate_path()
    draw_map()
    

if __name__ == "__main__":
    main()
