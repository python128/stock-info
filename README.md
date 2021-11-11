# `stifo`
A simple terminal app that gives you LIVE stock prices and advices you to `buy`, `sell` or `keep` your stocks based on the data given. 
![Example Picture](./Stock-Info.jpg)
###### `stifo` stands for STock InFO

## Installation
- Clone the git repository in your preferred directory.

As simple as that!

If you want to run the command from anywhere, you have to add `stifo` file to your $PATH.
But you still have to mention either the absolute path or relative path for the file.

## Configuration
For this app to work, you need to provide a few details in any file of your choice.
Format: (of configuration)
```
symbol,bp,sp # Ticker Symbol, Buy Price, Sell Price - DON'T LEAVE ANY SPACES BETWEEN COMMAS
HDFC,5000,10000 # Example 
```
Where:
- `Ticker Symbol` is the Symbol of the stock [Eg: for ICICI bank, the symbol is `ICICIBANK`].
- `Buy Price(BP)` is the price at which you would like to buy the stock.
- `Sell Price(SP)` is the price at which you would like to sell the stock.

You can view the ticker symbols in [google finance](https://www.google.com/finance/). Please use the `NSE` ticker symbols only.

You can have the BP and SP as either `float` or `int` values.
No need to have the ticker symbol as string. 

## Requirements
- Python 3.7+ 
- Certain modules:

|Modules|Description|
|--------|---------|
|pprint | pre-installed with python |
|pandas | pip install pandas |
|tabulate | pip install tabulate |
|sys | pre-installed with python |
|jugaad_data | pip install jugaad-data |
|argparse | pip install argparse |


## Running
After the configuration, we can run Stock-Info by running the following: `python stifo` OR `python3 stifo`

It will give you a result such as this:
![Example Picture](./Stock-Info.jpg)

```
usage: stifo [-h] [-t] file_name

positional arguments:
  file_name   File to read from(input file)

optional arguments:
  -h, --help  Show this help message and exit
  -t, --type  Changes type to csv format
```

## Miscellaneous
- If you don't give any data, it will give an error.
- If you give wrong data(ticker symbol is not correct), it will give an error.

If you find any Issue or have a Feature Request, please open an issue.
If you have an idea for a feature, please open a PR.

## TODO
- [x] Make a single file.
- [x] Add arguments.
  - [x] Input file [mandatory]
  - [x] Output type(csv, tabular, tsv, etc) [optional; default = tabular]
  - [x] Help message
- [ ] Package.

#### PLEASE USE AT YOUR OWN RISK
