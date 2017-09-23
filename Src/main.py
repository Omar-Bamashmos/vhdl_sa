###############################################
# VHDL static analysis program
# Authoer: Omar Ba mashmos
################################################

def main (arg):
	try:
		vhdl_file = open(arg)
	except():
		print("File was not found")
		
	src_code = vhdl_file.read()
	lines_list = src_code.split("\n")
	
	#start parsing
	