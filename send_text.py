from twilio.rest import Client

#My Account Sid and auth token from twilio.com
account = "AC7d3aac936d3ee4ab7c8253605d0d6eb8"
token = "9c74be9665c070f09d6bda42dc18fc6e"

client = Client(account,token)


message = client.messages.create(
        to="+527227024552",
        from_= "+17625839241",
        body ="Galleta please?! I miss you <3")
print message.sid
