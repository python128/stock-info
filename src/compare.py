###################################
###         COMPARISON          ###
###################################

def compare(ticker_data):
	"""
	if cp < bp:
		final.append("buy")
	elif cp > sp:
		final.append("sell")
	"""
	for ticker in ticker_data:
		if ticker_data[ticker]['cp'] < ticker_data[ticker]['bp']:
			ticker_data[ticker]['status'] = 'buy'
		elif ticker_data[ticker]['cp'] >= ticker_data[ticker]['sp']:
			ticker_data[ticker]['status'] = 'sell'
		else:
			ticker_data[ticker]['status'] = 'keep'
	return ticker_data
