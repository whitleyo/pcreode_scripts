import pdb
def hello_debug():
	
	print('blargh')
	assert(False)

if __name__ == '__main__':
	pdb.set_trace()
	x = 5
	y = 'cats'
	hello_debug()
