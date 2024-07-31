!pip install yfinance
!pip install pandas
!pip install matplotlib

#import libraries
import yfinance as yf
import pandas as pd
import matplotlib_inline

#create ticker module
apple = yf.Ticker("AAPL")

#extract data
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

#extract info as dictionary
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info

#display country
apple_info['country']
#display share price
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
#reset index
apple_share_price_data.reset_index(inplace=True)

#plot dividends
apple.dividends
apple.dividends.plot()

#create object for AMD
amd = yf.Ticker("AMD")

# Display the type to confirm it's a yfinance Ticker object
print(type(amd))

!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json

#get info AMD
import json
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
amd_info

#load the downloaded JSON file
with open('amd.json') as json_file:
    amd_info = json.load(json_file)

#print the country associated with AMD
country = amd_info.get('country')
print("The country for AMD is:", country)

#print sector associated with AMD
sector = amd_info.get('sector')
print("The sector for AMD is:", sector)

# Obtain stock data with the maximum period
amd_stock_data = amd.history(period="max")

# Reset index to ensure the date is a column
amd_stock_data.reset_index(inplace=True)

# Find the Volume traded on the first day (first row)
volume_first_day = amd_stock_data.iloc[0]['Volume']

print("Volume traded on the first day:", volume_first_day)
