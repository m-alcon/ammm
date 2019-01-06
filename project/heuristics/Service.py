class Service(object):

    def __init__(self, selfId, startingTime, durationTime, durationDist, passengers):
        self.id = selfId
        self.startingTime = startingTime
        self.durationTime = durationTime
        self.durationDist = durationDist
        self.passengers = passengers

    def itOverlapsInTime(self, startingTime2, finalTime2):
        startingTime1 = self.startingTime
        finalTime1 = startingTime1 + self.durationTime
        if  (startingTime1 <= startingTime2 and finalTime1 >= startingTime2) or (startingTime1 <= finalTime2 and finalTime1 >= finalTime2) or (startingTime1 >= startingTime2 and finalTime1 <= finalTime2):
            return False

        return True

    def getPassengers(self):
        return self.passengers

    def getDurationTime(self):
        return self.durationTime

    def getDurationDist(self):
        return self.durationDist

    def getStartingTime(self):
        return self.startingTime

    def getId(self):
        return self.id