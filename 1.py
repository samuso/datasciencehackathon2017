import numpy
import matplotlib.pyplot as plt

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
		if date in dict2:
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

dict1 = get_closes(prices,ticker_samples[0])
dict2 = get_closes(prices,ticker_samples[1])
list1, list2 = get_similar_date(dict1, dict2)
print len(list1)
print len(dict1)

print len(prices)
print numpy.corrcoef(list1, list2)[0, 1]




