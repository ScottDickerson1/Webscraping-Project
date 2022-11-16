import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import keys1
from twilio.rest import Client



webpage = 'https://ebible.org/asv/JHN'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

random_chap = random.randint(1,21)

if random_chap < 10:
    random_chap = '0' + str(random_chap)
else:
    random_chap = str(random_chap)


webpage = 'http://ebible.org/asv/JHN' + random_chap + '.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

verses = soup.findAll('div',class_='p')

verses_list = []

for verse in verses:
    verses_list = verses.text.split(".")

myverse = 'Chapter:' + random_chap + 'Verse:' + random.choice(verses_list[:len(verses_list)-2])
print(myverse)

client = Client(keys1.accountSID,keys1.authToken)

twilioNumber = '+13466395490'
myNumber = '+17133010723'

message = Client.messages.create(to=myNumber,from_=twilioNumber,body=myverse)

print(message.status)


