###################################
###         STOCK INFO          ###
###################################

from jugaad_data.nse import NSELive

def get_cp(ticker_data):
	for ticker in ticker_data.keys():
		n = NSELive() 
		quote = n.stock_quote(ticker) # Gets the price
		data = (quote['priceInfo']) 
		cp_temp = data["lastPrice"] # Gets the actual Current Price
		ticker_data[ticker]['cp'] = cp_temp
	return ticker_data
