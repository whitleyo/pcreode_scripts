# Find out file type

my_file = '170906_SamBrain_DS18_DGE.txt'
my_fileobj = open(my_file)

my_file_str = my_fileobj.read()
my_file_lines = my_file_str.split('\n')

for i in range(0,3,1):

	print('line' + str(i))
	print('unsplit')
	print(my_file_lines[i])
	print('split')
	print(my_file_lines[i].split('\t'))
