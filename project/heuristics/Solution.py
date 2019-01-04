'''
AMMM Lab Heuristics v1.2
Representation of a solution instance.
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

import copy, time
from Problem import Problem

# Assignment class stores the load of the highest loaded CPU
# when a task is assigned to a CPU.
class Assignment(object):
    def __init__(self, serviceId, busId, driverId):
        self.serviceId = serviceId
        self.busId = busId
        self.driverId = driverId

# Solution includes functions to manage the solution, to perform feasibility
# checks and to dump the solution into a string or file.
class Solution(Problem):
    @staticmethod
    def createEmptySolution(config, problem):
        solution = Solution(problem.inputData)
        solution.setVerbose(config.verbose)
        return solution

    def __init__(self, inputData):
        super(Solution, self).__init__(inputData)

        self.serviceIdToBusId = {}
        self.serviceIdToDriverId = {}

        self.busIdToServicesId = {}
        self.driverIdToServicesId = {}

        self.driverIdToTimeWorked = {}

        self.feasible = True
        self.verbose = False

    def setVerbose(self, verbose):
        if(not isinstance(verbose, (bool)) or (verbose not in [True, False])):
            raise Exception('verbose(%s) has to be a boolean value.' % str(verbose))
        self.verbose = verbose

    def makeInfeasible(self):
        self.feasible = False

    def isFeasible(self):
        return self.feasible

    def calculateActualCost(self):
        busCost = 0
        for serviceId,busId in self.serviceIdToBusId.items():
            service = self.services[serviceId]
            bus = self.buses[busId]
            busCost += service.getDurationTime()*bus.getCostTime()
            busCost += service.getDurationDist()*bus.getCostDist()

        driverCost = 0
        for driverId,timeWorked in self.driverIdToTimeWorked.items():
            driver = self.drivers[driverId]
            if timeWorked > driver.getBM():
                driverCost += driver.getBM()*driver.getCostBM()
                driverCost += (timeWorked-driver.getBM())*driver.getCostEM()
            else:
                driverCost += timeWorked*driver.getCostBM()

        return busCost + driverCost

    def isFeasibleToAssignServiceToBus(self, serviceId, busId):
        if serviceId in self.serviceIdToBusId:
            if self.verbose : print('Service(%s) already has a bus assigned.' % str(serviceId))
            return False

        service = self.services[serviceId]
        bus = self.buses[busId]

        # Constraint 1
        passengers = service.getpassengers()
        capacity = bus.getCapacity()
        if passengers > capacity:
            if self.verbose: print('Bus(%s) has not enough capacity for Service(%s)' % (str(busId), str(serviceId)))
            return False

        #Constraint 2.b
        start = service.getStartingTime()
        end = start + service.getDurationTime()
        for sId in self.busIdToServicesId[busId]:
            if self.services[sId].itOverlapsInTime(start, end):
                if self.verbose: print('Bus(%s) serves other Service(%s) that overlaps with Service(%s)' % (str(busId), str(sId), str(serviceId)))
                return False

        # Constraint 4
        maxBuses = bus.getMaxBuses()
        usedBuses = len(self.serviceIdToBusId)
        if maxBuses >= usedBuses:
            if self.verbose: print('maxBuses(%s) overpassed by usedBuses(%s)' % (str(maxBuses), str(busesWorking)))
            return False

        return True

    def isFeasibleToAssignServiceToDriver(self, serviceId, driverId):
        if serviceId in self.serviceIdToDriverId:
            if self.verbose : print('Service(%s) already has a driver assigned' % str(serviceId))
            return False

        service = self.services[serviceId]
        driver = self.drivers[driverId]

        #Constraint 2.d
        start = service.getStartingTime()
        end = start + service.getDurationTime()
        for sId in self.driverIdToServicesId[driverId]:
            if self.services[sId].itOverlapsInTime(start, end):
                if self.verbose: print('Driver(%s) serves other Service(%s) that overlaps with Service(%s)' % (str(busId), str(sId), str(serviceId)))
                return False

        # Constraint 3
        serviceTime = service.getDurationTime()
        maxTime = driver.getMaxTime()
        timeWorked = 0
        if driverId in self.driverIdToTimeWorked:
            timeWorked = self.driverIdToTimeWorked[driverId]
        if timeWorked + serviceTime > maxTime:
            if self.verbose:
                print('Driver(%s) can not work more than maxTime(%s), tried timeWorked(%s) + serviceTime(%s) for service(%s)'
                    % (str(driverId), str(maxTime),str(timeWorked),str(serviceTime),str(serviceId)))
            return False

        return True

    def getBusIdAssignedToServiceId(self, serviceId):
        if serviceId in self.serviceIdToBusId:
            return self.serviceIdToBusId[serviceId]
        else: return None

    def getDriverIdAssignedToServiceId(self, serviceId):
        if serviceId in self.serviceIdToDriverId:
            return self.serviceIdToDriverId[serviceId]
        else: return None

    def assign(self, serviceId, busId, driverId):
        # Check feasibility
        if not self.isFeasibleToAssignServiceToBus(serviceId,busId):
            if self.verbose: print('Unable to assign Service(%s) to Bus(%s)' % (str(serviceId), str(busId)))
            return False

        if not self.isFeasibleToAssignServiceToDriver(serviceId,driverId):
            if self.verbose: print('Unable to assign Service(%s) to Driver(%s)' % (str(serviceId), str(driverId)))
            return False

        # Assign
        service = self.services[serviceId]
        bus = self.buses[busId]
        driver = self.drivers[driverId]

        ## Bus
        self.serviceIdToBusId[serviceId] = busId
        if busId in self.busIdToServicesId:
            self.busIdToServicesId[busId].append(serviceId)
        else:
            self.busIdToServicesId[busId] = [serviceId]

        ## Driver
        self.serviceIdToDriverId[serviceId] = driverId
        if driverId in self.driverIdToServicesId:
            self.driverIdToServicesId[driverId].append(serviceId)
        else:
            self.driverIdToServicesId[driverId] = [serviceId]
        if driverId in self.driverIdToTimeWorked:
            self.driverIdToTimeWorked[driverId] = self.services[serviceId].getDurationTime()
        else:
            self.driverIdToTimeWorked[driverId] += self.services[serviceId].getDurationTime()

        if self.verbose: print('Assign Service(%s) to Bus(%s) and Driver(%s)' % (str(serviceId), str(busId), str(driverId)))
        return True

    def isFeasibleToUnassignServiceFromBus(self, serviceId, busId):
        if not serviceId in self.serviceIdToBusId:
            if self.verbose: print('Service(%s) is not assigned to any Bus.' % str(serviceId))
            return False
        elif self.serviceIdToBusId[serviceId] != busId:
            if self.verbose: print('Service(%s) is not assigned to Bus(%s).' % (str(serviceId),str(busId)))
            return False

        return True

    def isFeasibleToUnassignServiceFromDriver(self, serviceId, driverId):
        if not serviceId in self.serviceIdToDriverId:
            if self.verbose: print('Service(%s) is not assigned to any Driver.' % str(serviceId))
            return False
        elif self.serviceIdToDriverId[serviceId] != driverId:
            if self.verbose: print('Service(%s) is not assigned to Driver(%s).' % (str(serviceId),str(driverId)))
            return False

        return True

    def unassign(self, serviceId, busId, driverId):
        if not self.isFeasibleToUnassignServiceFromBus(serviceId, busId):
            if self.verbose: print('Unable to unassign Service(%s) from Bus(%s)' % (str(serviceId), str(busId)))
            return False

        if not self.isFeasibleToUnassignServiceFromDriver(serviceId, driverId):
            if self.verbose: print('Unable to unassign Service(%s) from Driver(%s)' % (str(serviceId), str(driverId)))
            return False

        # Unassign
        service = self.services[serviceId]
        bus = self.buses[busId]
        driver = self.drivers[driverId]

        ## Bus
        self.serviceIdToBusId.pop(serviceId)
        self.busIdToServicesId[busId].remove(serviceId)
        if not self.busIdToServicesId[busId]:   #Empty list
            self.busIdToServicesId.pop(busId)

        ## Driver
        self.serviceIdToDriverId.pop(serviceId)
        self.driverIdToServicesId[driverId].remove(serviceId)
        if not self.driverIdToServicesId[driverId]:   #Empty list
            self.driverIdToServicesId.pop(driverId)
        self.driverIdToTimeWorked[driverId] -= self.services[serviceId].getDurationTime()
        if self.driverIdToServicesId[driverId] == 0:
            self.driverIdToTimeWorked.pop(driverId)

        if self.verbose: print('Unassign Service(%s) to Bus(%s) and Driver(%s)' % (str(serviceId), str(busId), str(driverId)))
        return True

    def findFeasibleAssignments(self, serviceId):
        startEvalTime = time.time()
        evaluatedCandidates = 0

        feasibleAssignments = []
        for busId,bus in enumerate(self.buses):
            for driverId,driver in enumerate(self.drivers):
                feasible = self.assign(serviceId, busId, driverId)

                evaluatedCandidates += 1
                if not feasible: continue

                assignment = Assignment(serviceId, busId, driverId)
                feasibleAssignments.append(assignment)

                self.unassign(serviceId, busId, driverId)

        elapsedEvalTime = time.time() - startEvalTime
        return (feasibleAssignments, elapsedEvalTime, evaluatedCandidates)

    def findBestFeasibleAssignment(self, serviceId):
        bestAssignment = Assignment(serviceId, None, None)
        bestCost = float('infinity')
        for bus in self.buses:
            for driver in self.drivers:
                feasible = self.assign(serviceId, busId, driverId)
                if not feasible: continue

                actualCost = self.calculateActualCost()
                if bestCost > actualCost:
                    bestAssignment.busId = busId
                    bestAssignment.driverId = driverId
                    bestCost = actualCost
                elif bestCost == actualCost:
                    

                self.unassign(serviceId, busId)

        return bestAssignment

    def __str__(self):  # toString equivalent
        nTasks = self.inputData.nTasks
        nThreads = self.inputData.nThreads
        nCPUs = self.inputData.nCPUs
        nCores = self.inputData.nCores

        strSolution = 'z = %10.8f;\n' % self.highestLoad

        # Xhk: decision variable containing the assignment of threads to cores
        # pre-fill with no assignments (all-zeros)
        xhk = []
        for h in xrange(0, nThreads):   # h = 0..(nThreads-1)
            xhkEntry = [0] * nCores     # results in a vector of 0's with nCores elements
            xhk.append(xhkEntry)

        # iterate over hash table threadIdToCoreId and fill in xhk
        for threadId,coreId in self.threadIdToCoreId.iteritems():
            xhk[threadId][coreId] = 1

        strSolution += 'xhk = [\n'
        for xhkEntry in xhk:
            strSolution += '\t[ '
            for xhkValue in xhkEntry:
                strSolution += str(xhkValue) + ' '
            strSolution += ']\n'
        strSolution += '];\n'

        # Xtc: decision variable containing the assignment of tasks to CPUs
        # pre-fill with no assignments (all-zeros)
        xtc = []
        for t in xrange(0, nTasks):     # t = 0..(nTasks-1)
            xtcEntry = [0] * nCPUs      # results in a vector of 0's with nCPUs elements
            xtc.append(xtcEntry)

        # iterate over hash table taskIdToCPUId and fill in xtc
        for taskId,cpuId in self.taskIdToCPUId.iteritems():
            xtc[taskId][cpuId] = 1

        strSolution += 'xtc = [\n'
        for xtcEntry in xtc:
            strSolution += '\t[ '
            for xtcValue in xtcEntry:
                strSolution += str(xtcValue) + ' '
            strSolution += ']\n'
        strSolution += '];\n'

        return(strSolution)

    def saveToFile(self, filePath):
        f = open(filePath, 'w')
        f.write(self.__str__())
        f.close()
