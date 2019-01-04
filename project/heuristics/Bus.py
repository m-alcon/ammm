class Bus(object):

    maxBuses = 0

    def __init__(self, capacity, costTime, costDistance):
        self.capacity = capacity
        self.costTime = costTime
        self.costDistance = costDistance

    def getCapacity(self):
        return self.capacity

    def getMaxBuses(self):
        return self.maxBuses

    def getCostTime(self):
        return self.costTime

    def getCostDistance(self):
        return self.costDistance