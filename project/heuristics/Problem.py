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
        passangers = self.inputData.passangers
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
                Service(startingTime[i],durationDist[i],durationDist[i],passangers[i]))

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
        totalCapacityCPUs = 0.0
        maxCoreCapacity = 0.0
        for cpu in self.cpus:
            capacity = cpu.getTotalCapacity()
            totalCapacityCPUs += capacity
            for coreId in cpu.getCoreIds():
                capacity = cpu.getTotalCapacityByCore(coreId)
                maxCoreCapacity = max(maxCoreCapacity, capacity)
                
        totalResourcesTasks = 0.0
        for task in self.tasks:
            resources = task.getTotalResources()
            totalResourcesTasks += resources
            
            threadIds = task.getThreadIds()
            for threadId in threadIds:
                threadRes = task.getResourcesByThread(threadId)
                if(threadRes > maxCoreCapacity): return(False)
            
            feasible = False
            for cpu in self.cpus:
                capacity = cpu.getTotalCapacity()
                feasible = (resources < capacity)
                if(feasible): break
            
            if(not feasible): return(False)
        
        if(totalCapacityCPUs < totalResourcesTasks): return(False)
        
        return(True)