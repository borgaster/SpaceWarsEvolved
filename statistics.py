import json
from operator import itemgetter
import cPickle
#Return and store statistics
#TODO: add MongoDB support
class Statistics():
    FILENAME = 'score.json'
    def __init__(self, player):
        self.score = player[3]
        self.livesLeft = player[0]
        self.shotsFired = player[1]
        self.accuracy = player[2]*100/player[1]
        self.playerName = ''
        
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
        scores = []
        f = open(Statistics.FILENAME, 'r')
        while True:
            try:
                scores.append(cPickle.load(f))
            except(EOFError):
                break
        return sorted(scores, key=itemgetter('score'), reverse=True)
             
    def toFile(self, playerName):
        self.playerName = playerName
        with open(Statistics.FILENAME, 'a') as f:
            cPickle.dump(self.__dict__, f)

    def isTop(self):
        stats = self.getScores()[-3:]
        if(len(stats) < 3):
            return True
        elif(self.score > stats[2]['score']):
            return True
        else:
            return False
