Description of all task :

Task 1:   How to Start the Project After Cloning
•	Clone the repository
•	Place the 'instruments.csv' file in the project folder
•	Run the Python script:
•	python task1_symbol_token_map.py

      -> What the Script Does
•	Opens the instruments.csv file
•	Reads all rows and skips the header
•	Filters only:
•	Exchange: NSE
•	Instrument Type: EQ (cash/equity stocks)
•	Creates a dictionary where:
o	       key   = Trading Symbol  
o	       value = Instrument Token
•	Prints the final mapping


Task 2:  How to Start the Project After Cloning
•	Clone the repository
•	Install required dependencies:
•	pip install yfinance pandas
•	Run the script:
•	python task02_download_resample.py
•	Enter the required inputs when prompted.

      -> What the script does
•	Validates user inputs
•	Downloads market data from Yahoo Finance
•	Removes missing values
•	Adds date and time columns
•	Optional) Resamples to a different timeframe (OHLC + Volume)
•	Saves the final processed dataframe into /data folder as CSV

Task 3 :  How to Start the Project After Cloning
o	Clone the repository
o	Ensure Python is installed
o	Install required dependency:
•	pip install pandas
o	Run the script:
•	python task03_sma.py

    -> What the Script Does
•	Creates a DataFrame with Date and Close price
•	Loops through each row to compute SMA manually
•	For each row, takes the average of current and previous two Close values
•	Adds a new column SMA_3 to the DataFrame
•	Prints the final data containing Date, Close, and SMA values
	 
Task 6:  How to Start the Project After Cloning
•	Clone the repository
•	Install required dependencies:
  o	pip install yfinance pandas
•	Run the script:        
  o python task06_intraday_pnl.py
       
     -> What the Script Does
•	Downloads last 7 days historical 1-minute data for the selected stock
•	Adds separate Date and Time columns
•	For each day:
•	Finds first candle at or after entry time
•	Finds last candle at or before exit time
•	Entry price = Open price of entry candle
•	Exit price = Close price of exit candle
•	Calculates P&L = Exit Price − Entry Price
•	Stores daily results and calculates total P&L
	
  Final 1: 
/task01/symbol-token-map 
Methods: GET, POST
•	Description: 
Reads the instruments CSV file (from JSON body) and returns a Symbol → Token mapping for all NSE Equity (EQ) instruments.

Final 2:
Endpoint: /task02/download
Methods: GET, POST
•	Purpose:
Downloads stock data from Yahoo Finance, cleans it, optionally resamples it (1m → 5m, 15m, 1h, etc.), and saves the result as a CSV.

Final 3:
/task03/sma
TASK 03 – SMA (Simple Moving Average) API Documentation
Methods: GET, POST
•	Description
This API calculates a 3-day Simple Moving Average (SMA-3) based on a list of dates and corresponding closing prices.

Final 4:
GET http://127.0.0.1:5000/hello
•	Description:
Simple test API.
Used to check if Flask server is running.
Returns a static message.

POST http://127.0.0.1:5000/hello_post
•	Description
Accepts a JSON body containing a "name" key.
Returns a greeting message using the provided name. 
    
Finaltask 5: 
/api/expiry (GET & POST)
•	Purpose
Returns weekly, monthly, or both expiry dates based on a given date.







