import numpy
import matplotlib.pyplot as plt
import math

ticker_samples = ['XL US Equity', 'ETP US Equity', 'HIK LN Equity', 'T CN Equity', 'ULTA US Equity', 'FGR FP Equity', 'NEM US Equity', 'FDS US Equity', 'BG/ LN Equity', 'ICICIBC IN Equity', 'BKG LN Equity', 'BHI US Equity']

# list1 = [1,3,4,5,6]
# list2 = [11,12,14,15,16]
# print numpy.corrcoef(list1, list2)[0, 1]

def get_closes(prices, ticker):
	ticker_price_dict = {}
	for date in prices[ticker]:
		if prices[ticker][date] != '':
			ticker_price_dict[date] = prices[ticker][date]
	return ticker_price_dict

def get_similar_date(dict1, dict2):
	filtered_list1 = []
	filtered_list2 = []
	for date in dict1:
		if dict1[date] != '':
			if date in dict2:
				if dict2[date] != '':
					filtered_list1.append(float(dict1[date]))
					filtered_list2.append(float(dict2[date]))
	return filtered_list1, filtered_list2

prices = {}
counter = 0
with open("Equity.csv", 'r') as infile:
	for line in infile:
		if counter > 1:
			raw_line_data = line.split(',')
			ticker = raw_line_data[0]
			date = raw_line_data[1]
			close = raw_line_data[5]
			if ticker not in prices:
				prices[ticker] = {}
			prices[ticker][date] = close
		counter += 1

# plt.plot(get_closes(prices, '000001 CH Equity'))
# plt.show()

coefs = {}
found_tickers = []
current_ticker = '000001 CH Equity'
for i in range(30):
	print "we up in da house"
	coefs[current_ticker] = {}
	min_c = 1.0
	next_ticker = ''
	for ticker in prices:
		if ticker != current_ticker:
			list1, list2 = get_similar_date(prices[ticker], prices[current_ticker])
			c = numpy.corrcoef(list1, list2)[0, 1]
			if c < abs(min_c) and ticker not in found_tickers:
				min_c = c
				next_ticker = ticker
	found_tickers.append(current_ticker)
	current_ticker = next_ticker

print found_tickers

all_dem_cs = []
for ticker1 in found_tickers:
	list_of_cs = []
	for ticker2 in found_tickers:
		list1, list2 = get_similar_date(prices[ticker1], prices[ticker2])
		list_of_cs.append(numpy.corrcoef(list1, list2)[0, 1])
	all_dem_cs.append(list_of_cs)

buff = ' ,'
for t in  found_tickers:
	buff += t + ','
buff = buff[:-1] + '\n'

counter = 0
for c_list in all_dem_cs:
	buff += found_tickers[counter] + ','
	counter += 1
	for c in c_list:
		buff += str(int(c * 1000)) + ','
	buff = buff[:-1] + '\n'

print buff

with open('out.csv', 'w') as out_file:
	out_file.write(buff)


