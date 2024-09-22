from datetime import date
today = date.today()
commands = [
    ('command tell me todays date|what is todays date?', [f"Todays Date is {today}"])
]
def sendcommand():
    return commands