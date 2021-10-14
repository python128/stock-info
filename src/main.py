###################################
###            MAIN             ###
###################################

from compare import compare
from stockinfo import get_cp
from get_data import ret_tuple
from pprint import pprint
import pandas as pd
from tabulate import tabulate

ticker_data = ret_tuple()
ticker_data = get_cp(ticker_data) # Gets cp

final1 = compare(ticker_data)

final = pd.DataFrame.from_dict(final1, orient='index')
col = "status"
first_col = final.pop(col)
final.insert(0, col, first_col)

headers = ['Status', 'BP', 'SP', 'CP']
final = tabulate(final, headers, tablefmt="fancy_grid")

print(final)
