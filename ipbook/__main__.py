import os

def main():
	dir_path, file_name = os.path.split(os.path.abspath(__file__))
	data_path = os.path.join(dir_path, 'data/ip_addrs.json')
	print(data_path)
	print open(data_path).read();

if __name__ == '__main__':
	main()