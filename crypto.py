from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import keys1
from twilio.rest import Client


client = Client(keys1.accountSID,keys1.authToken)

TwilioNumber = "+13466395490"

myCellPhone = "+17133010723"

url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
print(title.text)

tablecells = soup.findAll("div", attrs={"class":"table-cell"})

counter = 1

for x in range(1,6):
    name = tablecells[counter].text
    current_price = float(tablecells[counter+1].text.replace(',',''))
    open_price = float(tablecells[counter+4].text.replace(',',''))
    change = round(((current_price - open_price)/open_price)*100,2)
    calc_change = 1 + abs(change/100)
    calc_price = calc_change*open_price

    print(f"Crypto Name: {name}")
    print(f"Current Price: {current_price}")
    print(f"Percent increase/decrease in price: {change}")
    print(f"Calculated increase in price: {calc_price}")
    print()
    input()

    if name == 'BBTCUSDBitcoin' and current_price < 40000:
            textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body="Bitcoin has dropped below $40,000")
    if name == 'EETHUSDEthereum' and current_price < 3000:
            textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body="Ethereum has dropped below $3,000")

    
    counter += 10