import os
import argparse

def add_ip(args):
	print (args.ip + ', ' + args.fname)

def list_ips(args):
	print ('hello buckaroo')

def delete_ip(args):
	print ('Deleting ' + args.fname + '...')

def main():
	'''
	dir_path, file_name = os.path.split(os.path.abspath(__file__))
	data_path = os.path.join(dir_path, 'data/ip_addrs.json')
	'''
	parser = argparse.ArgumentParser(description="Save a list of your most commonly used IP addresses")
	subparser = parser.add_subparsers()

	# Add command
	add_parser = subparser.add_parser('add', help="Save new IP")
	add_parser.add_argument('ip', help="IP Address")
	add_parser.add_argument('fname', help="Friendly name for the IP (Quotes)")
	add_parser.set_defaults(func=add_ip)

	# List command
	list_parser = subparser.add_parser('list', help="Show all saved IPs")
	list_parser.set_defaults(func=list_ips)

	# Delete command
	delete_parser = subparser.add_parser('remove', help="Remove IP record by friendly name")
	delete_parser.add_argument('fname', help="Record's friendly name")
	delete_parser.set_defaults(func=delete_ip)


	args = parser.parse_args()
	args.func(args)

if __name__ == '__main__':
	main()
