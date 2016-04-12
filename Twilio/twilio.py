from twilio.rest import TwilioRestClient #pipinstall twilio

Account_SID = "ACb8e28dc4a841b1204a3ab6d957c7cbbf"
Auth_Token = "8a5bde354ffa747c950b18b8477ebaca"
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
client.message.create(
    to = "+380504571301",
    from = "+12674335886",
    body = "Hello me",
    )
