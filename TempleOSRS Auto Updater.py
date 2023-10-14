import requests
import time
import json


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

def updatePlayers(playerList):
    amountUpdated = 0
    delayTime = 13.5 #in seconds
    failedPlayers = []

    for player in playerList:
        data = requests.get("https://templeosrs.com/php/add_datapoint.php?player=" + player)

        if data.status_code != 200:
            amountUpdated += 1
            print(amountUpdated + " / " + str(len(playerList)) + " " + player + " failed to update. Gave status code: " + data.status_code)
            failedPlayers.append(player)
            time.sleep(delayTime)

        else:
            amountUpdated += 1
            print(str(amountUpdated) + " / " + str(len(playerList)) + " Updated: " + player)
            time.sleep(delayTime)


    print("Failed to update: " + str(len(failedPlayers))) 
    print("Failed players: " + str(failedPlayers))

def main():
    while True:
        compID = input("Enter the desired competition id: ")

        #check that the compID is a valid integer, if not ask for input again
        if not checkIdIsInt(compID):
            print("Invalid compID. Please enter a valid integer.")
            continue #return to input the compID again

        members = getCompetitionMembers(compID)
        if isinstance(members, list):
            updatePlayers(members)
            continue
        else:
            print(f"API request failed with status code: {members}. Please try again.")
            continue #return to input the compID again

if __name__ == "__main__":
    main()