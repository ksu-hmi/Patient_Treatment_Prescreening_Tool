import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account

url = "https://github.com/ksu-hmi/Patient_Treatment_Prescreening_Tool/blob/main/Python_Project_Data.xlsx?raw=true" # Make sure the url is the raw version of the file on GitHub
download = requests.get(https://github.com/ksu-hmi/Patient_Treatment_Prescreening_Tool/blob/main/Python_Project_Data.xlsx?raw=true).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_xlsx(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print (df.head())