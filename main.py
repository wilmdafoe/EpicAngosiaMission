"""
This code takes data of strings, sorts them into lists,
and removes fake data and replaces it with valid data
"""

def remove_label(data):
    """Removes the labels from the beginning of each element"""
    updated_data = []
    for element in data:
        parts = element.split(":")
        updated_data.append(parts[1])
    return updated_data
def formatted_message(data):
    """Correctly prints the data in the correct format"""
    for element in data:
        print(element, end=", ")
    print("")
    
#Data of all the characters in a single string
danar = "Sender:R.Danar|Receiver:K.Ravonn|Msg:Protocol Echo active. Underground network still intact. Proceed to Grid 9."
korr = "Sender:Z.Korr|Receiver:M.Tohrel|Msg:Recon path clear. Assault team may advance through sector 12 undetected."
tohrel = "Sender:M.Tohrel|Receiver:J.Torlek|Msg:Requesting isolation. Aggression spike recorded post-briefing."
torlek = "Sender:J.Torlek|Receiver:I.Vesh|Msg:Order recall of transmission logs. Reformist materials breached chain of command."
ravonn = "Sender:K.Ravonn|Receiver:R.Danar|Msg:Lockdown bypass successful. Awaiting next phase of network reactivation."
vesh = "Sender:I.Vesh|Receiver:Z.Korr|Msg:Literature distributed. Morale rising in eastern block. Watch for disciplinary action."
tolan = "Name:Tolan Revek|Rank:Specialist|Unit:Research Division|Reason for Removal:No evidence of combat or enhancement; cross-check with Federation intelligence flagged inconsistencies in medical data."
#Split the strings to turn each data element into an element of a list
danar = danar.split("|")
korr = korr.split("|")
tohrel = tohrel.split("|")
torlek = torlek.split("|")
ravonn = ravonn.split("|")
vesh = vesh.split("|")
tolan = tolan.split("|")
#Remove the labels from the beginning of each element in the list
danar = remove_label(danar)
korr = remove_label(korr)
tohrel = remove_label(tohrel)
torlek = remove_label(torlek)
ravonn = remove_label(ravonn)
vesh = remove_label(vesh)
tolan = remove_label(tolan)
#Print the formatted messages
print("Sender, Receiver, Encoded Message")
formatted_message(danar)
formatted_message(korr)
formatted_message(tohrel)
formatted_message(torlek)
formatted_message(ravonn)
formatted_message(vesh)
#Print there is an incorrect message
print("\nFalse Message Detected: ", end="")
formatted_message(tolan)
#Make the correct message by replacing tolan's message
sarn = []
for i in range(4):
    if i == 0:
        message = "Sarn Delar"
    if i == 1:
        message = "Medical Liaison" 
    if i == 2:
        message = "Enhancement Oversight Council"
    if i == 3:
        message = "Non-enhanced official. Administered post-combat reconditioning programs. Potential ethical violations in suppressing psychological treatment records."
    sarn_element = tolan[i].replace(tolan[i], message)
    sarn.append(sarn_element)
del(tolan)
#Print the full message
print("\nFixed Message:\nName, Rank, Unit, Notes")
formatted_message(sarn)
#Credit
print("\nCompiled by Ensign O.William, Data Operations, USS Enterprise-D")
