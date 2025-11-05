#NSE500Datapull
import os
import requests
import pandas as pd
from datetime import datetime

# Setup headers to make NSE API accept the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/"
}

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Start a session
session = requests.Session()
session.headers.update(headers)

# Fetch the NIFTY 500 index data
session.get("https://www.nseindia.com", timeout=10)
url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500"
response = session.get(url, timeout=10)
data = response.json()

# Convert to a pandas DataFrame
df = pd.DataFrame(data["data"])

# Save to CSV file with today's date
today = datetime.now().strftime("%Y-%m-%d")
filename = f"data/nifty500_data_{today}.csv"

df.to_csv(filename, index=False)
print(f"✅ Nifty 500 data saved to {filename}")
