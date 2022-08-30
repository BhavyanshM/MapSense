import numpy as np
import matplotlib.pyplot as plt

def convert_file(name):
	f = open(name + '.csv', 'r')
	f_csv = open(name + '_Extracted.csv', 'w+')
	f_format = open(name + '_Format.txt', 'w+')

	start = False

	for l in f:

		values = l.strip().split(',')
		# print(len(values))

		if start == True:
			for i in range(1, len(values)):
				if values[i] == '':
					values[i] = '0'
				f_csv.write("{}\t".format(values[i]))
			f_csv.write('\n')
		else:
			for i in range(len(values)):
				f_format.write("{}\t".format(values[i]))
			f_format.write('\n')

		if values[0] == "Frame":
			start = True

		print('Values:', len(values), values)

	# print()
	# print()

def plot_data(name):
	csv_name = name + '_Extracted.csv', 'w+'
	format_name = name + '_Format.txt', 'w+'

	# for l in open(format_name):
	# 	words = l.strip().split("\t")
	# 	if words[0] == "Name":
	# 		print(words)

	import os
	print(os.listdir('./'))

	data = np.genfromtxt(csv_name, delimiter='\t')

	print(data.shape)

	t = np.linspace(0, data.shape[0], data.shape[0])



	# fig = plt.figure(figsize=(10,10))
	# plt.plot(data[:,1], data[:,2], 'ro')
	# plt.show()

if __name__ == "__main__":
	plot_data('Take 2022-04-30 06.08.04 PM')
