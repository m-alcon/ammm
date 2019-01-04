'''
AMMM Lab Heuristics v1.2
Representation of a problem instance.
Copyright 2018 Luis Velasco.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from Service import Service
from Bus import Bus
from Driver import Driver

class Problem(object):
    def __init__(self, inputData):
        self.inputData = inputData

        nServices = self.inputData.nServices
        nBuses = self.inputData.nBuses
        nDrivers = self.inputData.nDrivers
        maxBuses = self.inputData.maxBuses
        startingTime = self.inputData.startingTime
        durationTime = self.inputData.durationTime
        durationDist = self.inputData.durationDist
        passengers = self.inputData.passengers
        capacity = self.inputData.capacity
        costTime = self.inputData.costTime
        costDist = self.inputData.costDist
        maxTime = self.inputData.maxTimes
        costBM = self.inputData.costBM
        costEM = self.inputData.costEM
        bm = self.inputData.BM

        self.services = []
        for i in range(nServices):
            self.services.append(
                Service(startingTime[i],durationTime[i],durationDist[i],passengers[i]))

        self.buses = []
        Bus.maxBuses = maxBuses
        for i in range(nBuses):
            self.buses.append(Bus(capacity[i],costTime[i],costDist[i]))

        self.drivers = []
        for i in range(nDrivers):
            self.drivers.append(Driver(maxTime[i],costBM[i],costEM[i],bm[i]))

    def getServices(self):
        return(self.services)

    def getBuses(self):
        return(self.buses)

    def getDrivers(self):
        return(self.drivers)

    def checkInstance(self):

        maxpassengers = 0
        totalDurationTime = 0
        for service in self.services:
            totalDurationTime += service.durationTime
            maxpassengers = max(maxpassengers,service.passengers)

        usefulBuses = 0
        for bus in self.buses:
            if maxpassengers > bus.capacity:
                usefulBuses += 1

        if usefulBuses == 0:
            print('One service can\'t be served by any bus because of not enough capacity (%d).'%maxpassengers)
            return False

        totalMaxMinutes = 0
        for driver in self.drivers:
            totalMaxMinutes += driver.maxTime

        if totalDurationTime > totalMaxMinutes:
            print('Not enough working minutes for the drivers.')
            return False

        return True