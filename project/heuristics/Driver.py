class Driver(object):

    def __init__(self, selfId, maxTime, costBM, costEM, bm):
        self.id = selfId
        self.maxTime = maxTime
        self.costBM = costBM
        self.costEM = costEM
        self.bm = bm

    def getMaxTime(self):
        return self.maxTime

    def getCostBM(self):
        return self.costBM

    def getCostEM(self):
        return self.costEM

    def getBM(self):
        return self.bm

    def getId(self):
        return self.id