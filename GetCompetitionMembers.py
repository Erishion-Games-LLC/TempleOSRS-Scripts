import requests
import time
import json

temple_API = requests.get("https://templeosrs.com/api/compmembers.php?id=5488")

def checkIdIsInt(Id):
    try:
        Id = int(Id)
        return True
    except ValueError:
        return False

def getCompetitionMembers(compID):
    response = requests.get("https://templeosrs.com/api/compmembers.php?id=" + str(compID))

    if response.status_code == 200:
        data = json.loads(response.text)
        playerList = [player.strip('"') for player in data]
        return playerList
    else:
        return None
    
def writePlayersToFile(members):
    for member in members:
        currentMember = member.replace(" ", "_", -1)

        with open("Members.txt", mode="a") as f:
            f.writelines(currentMember) 
            f.write("\n")

def writePlayersToConsole(members):
    for member in members:
        currentMember = member.replace(" ", "_", -1)
        print(currentMember)

def main():
    while True:
        compID = input("Enter the desired competition id: ")

        #check that the compID is a valid integer, if not ask for input again
        if not checkIdIsInt(compID):
            print("Invalid compID. Please enter a valid integer.")
            continue #return to input the compID again

        members = getCompetitionMembers(compID)
        writePlayersToFile(members)
        writePlayersToConsole(members)
        

        

if __name__ == "__main__":
    main()
