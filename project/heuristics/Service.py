class Service(object):

    def __init__(self, startingTime, durationTime, durationDist, passengers):
        self.startingTime = startingTime
        self.durationTime = durationTime
        self.durationDist = durationDist
        self.passengers = passengers

    def itOverlapsInTime(self, start, end):
        finalTime = self.startingTime + self.durationTime
        if start > finalTime or end < self.startingTime:
            return False

        return True

    def getpassengers(self):
        return self.passengers

    def getDurationTime(self):
        return self.durationTime

    def getStartingTime(self):
        return self.startingTime