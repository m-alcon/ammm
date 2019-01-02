class Bus(object):

    maxBuses = 0

    def __init__(self, capacity, costTime, costDistance):
        self.capacity = capacity
        self.costTime = costTime
        self.costDistance = costDistance