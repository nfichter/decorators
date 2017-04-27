import time

def log(func):
	def inner(*arg):
		return func.func_name+": "+str(arg)
	return inner

def runtime(func):
	def inner(*arg):
		t1 = time.time()
		func(*arg)
		t2 = time.time()
		return "execution time: "+str(t2-t1)
	return inner

#@runtime
#@log
def print_new(word1, word2):
	time.sleep(3)
	return word1 + " " + word2

print print_new("hello","goodbye")