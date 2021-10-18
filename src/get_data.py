###################################
###          READS FILE         ###
###################################

import pandas as pd
import sys

def ret_tuple():
	raw_data = pd.read_csv("./data.csv", index_col=0).to_dict("index")

	if raw_data == {}:
		print("ERROR: \nPlease provide some ticker values along with BP and SP")
		sys.exit(1)

	for val in raw_data.values():
		bp = val['bp']
		sp = val['sp']
		if bp > sp:
			print("ERROR: \nYou will get wrong info. \nPlease make sure that SP is greater than BP in data.csv!! \nExiting..")
			sys.exit(1)
		
	return raw_data # Returns symbols, Buy Price, Sell Price

