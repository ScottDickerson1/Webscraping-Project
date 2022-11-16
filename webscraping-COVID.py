# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from cgi import test
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll('tr')


state_high_rate = ''
state_low_rate = ''
high_rate = 0.0
low_rate = 100.0

state_high_test = ''
state_low_test = ''
high_test = 0.0
low_test = 100.0

for row in table_rows[2:51]:
    td = row.findAll('td')
    state = td[1].text
    total_cases = int(td[2].text.replace(',',''))
    total_deaths = int(td[4].text.replace(',',''))
    total_tests = int(td[10].text.replace(',',''))
    population = int(td[12].text.replace(',',''))

    death_rate = round((total_deaths / total_cases)*100,2)
    test_rate = round((total_tests / population)*100,2)

    if death_rate > high_rate:
        state_high_rate = state
        high_rate = death_rate

    if death_rate < low_rate:
        state_low_rate = state
        low_rate = death_rate

    if test_rate > high_rate:
        state_high_test = state
        high_test = test_rate

    if test_rate < low_test:
        state_low_test = state
        low_test = test_rate

print(f"state with worst death rate: {state_high_rate}")
print(f"Death rate: {high_rate}%")
print()
print(f"State with best death rate: {state_low_rate}")
print(f"Death rate: {low_rate}%")
print()
print(f"State with worst test rate: {state_low_test}")
print(f"Test rate: {low_test}")
print()
print(f"State with best test rate: {state_high_test}")
print(f"Test rate: {high_test}")



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

