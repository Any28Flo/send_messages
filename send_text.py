from twilio.rest import Client

#My Account Sid and auth token from twilio.com
account = "********"
token = "********"

client = Client(account,token)


message = client.messages.create(
        to="+527227024552",
        from_= "+17625839241",
        body ="Galleta please?! I miss you <3")
print message.sid
