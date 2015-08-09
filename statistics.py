
import json
import pygame
from operator import itemgetter
#Should return and store statistics in JSON format for file
class Statistics():
    FILENAME = 'score.json'
    def __init__(self, player, playerName):
        self.score = player[3]
        self.livesLeft = player[0]
        self.shotsFired = player[1]
        self.accuracy = player[2]*100/player[1]
        self.playerName = playerName
        
    def drawStatistics(self):
        statisticsText = [[""],
        ["Score <> "+str(self.score)+" points"],
        ["Total lives left <> "+str(self.livesLeft)+""],
        ["Total shots fired <> "+str(self.shotsFired)+""],
        [" -> missed: "+str(player[1]-player[2])+""],
        ["Accuracy <> "+str(self.accuracy)+"%"]]  
        return statisticsText
    
    def toJSON(self):
        return json.dumps(self.__dict__)
    
    def getScores(self):
        stats = []
        for entry in open(FILENAME, 'rb'):
            stats.append(json.loads(entry))
        return sorted(stats, key=sortScore)
    
    def toFile(self):
        with open(FILENAME, 'ab') as outFile:
            json.dump(self.__dict__, outFile)
            outFile.write('\n')
            outFile.close()
        
    def sortScore(self, json):
        return int(json['score'])
                
    def isTop(self):
        stats = self.getScores()[:3]
        if(self.score > stats[2].score):
            return True
        else:
            return False
                   