import random
from operator import itemgetter

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    return random.randint(0, 100)

def normalize_for_nn(data):
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

def normalize(data):
	normal_data = []
	for i in xrange(len(data)):
		row = data[i].strip().split()
		features = []
		for feature in row[1:]:
			features.append(feature)
		normal_data.append((row[0], features))
	return normal_data

def forward_selection(data): 
	current_set_of_features = []
	print "Beginning search"
	best_accuracy_all = (0, [])
 	for i in xrange(len(data[0][1])):
 		feature_to_add = -1
 		best_accuracy = 0

 		for k in xrange(len(data[0][1])):
 			if (k+1) not in current_set_of_features:
 				accuracy = leave_one_out_cross_validation(data, current_set_of_features, k+1)
 				set_of_features = current_set_of_features[:]
 				set_of_features.append(k+1)
 				print "Using feature(s)", set_of_features, "accuracy is", accuracy, "%"
 				if accuracy > best_accuracy:
 					best_accuracy = accuracy
 					feature_to_add = k + 1

 		current_set_of_features.append(feature_to_add)

 		if best_accuracy_all[0] > best_accuracy:
 			print "(Warning, Accuracy has decreased! Continuing search in case of local maxima)"
 		else:
 			best_accuracy_all = (best_accuracy, current_set_of_features[:])
 		
 		print "Feature set", current_set_of_features, " was best, accuracy is ", best_accuracy, "\n"
 	return best_accuracy_all


if __name__ == "__main__":
	print "Welcome to Sachin's Incredible Feature Selection Algorithm."
	# TODO remove this
	# file_name = raw_input("Type in the name of the file to test: ")
	file_name = "cs_170_small80.txt"
	choice = input("Type the number of the algorithm you want to run.\n1) Forward Selection\n2) Backward Selection\n3) Sachin's Special Algorithm.\nChoice: ")
	print "\n"
	new_data = []
	orig_data = []
	with open(file_name, "r") as f:
		data = f.readlines()
		num_features = len(data[0].strip().split()) - 1
		print "This dataset has %d features (not including the class attribute), with %d instances\n" % (num_features, len(data))
		print "Please wait while I normalize the data..."
		data_for_nn = normalize_for_nn(data)
		orig_data = normalize(data)
	print "Done.\n"
	if choice == 1:
		print forward_selection(orig_data)
	elif choice == 2:
		pass
	else:
		pass
	
	