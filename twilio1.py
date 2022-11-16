import keys1
from twilio.rest import Client


client = Client(keys1.accountSID,keys1.authToken)

TwilioNumber = "+13466395490"

myCellPhone = "+17133010723"

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body="Hi there!")

print(textmessage.status)