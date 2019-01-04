class Service(object):

    def __init__(self, startingTime, durationTime, durationDist, passangers):
        self.startingTime = startingTime
        self.durationTime = durationTime
        self.durationDist = durationDist
        self.passangers = passangers

    def itOverlapsInTime(self, start, end):
        finalTime = self.startingTime + self.durationTime

    def getPassangers(self):
        return self.passangers

    def getDurationTime(self):
        return self.durationTime