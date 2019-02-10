from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC86c7207d85647b94f1fa463810d2f371"
# Your Auth Token from twilio.com/console
auth_token  = "70e432f65b7a595d321a83ba453985c3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919643088798", 
    from_="+19164389714",
    body="Hello from Python! and Work Work Work")

print(message.sid)
