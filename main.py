import ezgmail, os
from rich.console import Console

console = Console()
ezgmail.init()
console.print("[bold][bright_green on black]Connected as: "+ ezgmail.EMAIL_ADDRESS)

#Unreads regex.
console.print("[bold][bright_yellow]Checking for removal requests...")
unreadThreads = ezgmail.search("'subject:Remove label:unread")

if unreadThreads == []:
    console.print("[bright_green]No removal requests found.")

elif len(unreadThreads) >= 0:
    console.print(f"[bright_yellow]Found {len(unreadThreads)} removal requests.")


# Read emails
with open("data/emails.txt") as emailsList:
    lines = len(emailsList.readlines())
    console.print(f"[bright_green][bold]Found {lines} emails to send to..")
    
    #Send from text.txt
    with open("data/emails.txt") as emailBody:
        text = emailBody.read()
        console.print("[bold][bright_green]Fetched email text")
        for i in emailsList.readline():
            ezgmail.send("david.cotiu@gmail.com","Test",text)
        console.print("[black on bright_green][bold]Done! Sent emails!")

print("Disconnected!")
exit(0)