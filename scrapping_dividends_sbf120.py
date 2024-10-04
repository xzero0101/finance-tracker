import requests, json, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

sbf_120 = {}

for i in range(1, 10):  
    url = os.getenv('URL') + str(i)
    response = requests.get(url)    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 5:
                company = cols[0].text.strip().replace("SRD", "").replace(" ", "").replace("\n", "")
                dividend_2024 = cols[5].text.strip()
                sbf_120[company] = dividend_2024

sorted_dict = {k: v for k, v in sorted(sbf_120.items(), key=lambda item: item[1], reverse=True)}
print(json.dumps(sorted_dict, indent=4))