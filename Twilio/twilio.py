from twilio.rest import TwilioRestClient #pipinstall twilio

Account_SID = "xxxxxxxxxxxxxxxxxxxxx"
Auth_Token = "xxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
client.message.create(
    to = "+xxxxxxxxxxxxxxxx",
    from = "xxxxxxxxxxxxxx",
    body = "Hello me",
    )
