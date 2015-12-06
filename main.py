import random
from operator import itemgetter

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    return random.randint(0, 100)

def normalize(data):
	new_data = []
	for __ in xrange(len(data[0].split()) - 1):
		new_data.append([])
	for row in data:
		row_data = row.split()
		for index, item in enumerate(row_data[1:]):
			new_data[index].append((float(row_data[0]), float(item)))
	for feature in new_data:
		feature.sort(key=itemgetter(1))
	# import pprint
	# pprint.pprint(new_data)
	return new_data


if __name__ == "__main__":
	print "Welcome to Sachin's Incredible Feature Selection Algorithm."
	# TODO remove this
	# file_name = raw_input("Type in the name of the file to test: ")
	file_name = "cs_170_small80.txt"
	# choice = raw_input("Type the number of the algorithm you want to run.\n1) Forward Selection\n2) Backward Selection\n3) Sachin's Special Algorithm.\nChoice: ")
	print "\n\n"
	new_data = []
	with open(file_name, "r") as f:
		data = f.readlines()
		num_features = len(data[0].strip().split()) - 1
		print "This dataset has %d features (not including the class attribute), with %d instances\n" % (num_features, len(data))
		print "Please wait while I normalize the data..."
		new_data = normalize(data)
	print "Done.\n"
	