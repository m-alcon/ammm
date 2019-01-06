'''
AMMM Lab Heuristics v1.2
Local Search algorithm.
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

# A change in a solution in the form: move serviceId from curBusId to newBusId and from curDriverId to newDriverId.
# This class is used to carry sets of modifications.
# A new solution can be created based on an existing solution and a list of
# changes can be created using the createNeighborSolution(solution, changes) function.
class Change(object):
    def __init__(self, serviceId, curBusId, newBusId, curDriverId, newDriverId):
        self.serviceId = serviceId
        self.curBusId = curBusId
        self.newBusId = newBusId
        self.curDriverId = curDriverId
        self.newDriverId = newDriverId

# Implementation of a local search using two neighborhoods and two different policies.
class LocalSearch(object):
    def __init__(self, config):
        self.enabled = config.localSearch
        self.nhStrategy = config.neighborhoodStrategy
        self.policy = config.policy

        self.elapsedTime = 0
        self.iterations = 0

    def createNeighborSolution(self, solution, changes):
        # unassign the tasks specified in changes
        # and reassign them to the new CPUs

        newSolution = copy.deepcopy(solution)

        for change in changes:
            newSolution.unassign(change.serviceId, change.curBusId, change.curDriverId)

        for change in changes:
            feasible = newSolution.assign(change.serviceId, change.newBusId, change.newDriverId)
            if not feasible: return None

        return newSolution


    def evaluateNeighbor(self, solution, changes):
        newServiceIdToBusId = copy.deepcopy(solution.serviceIdToBusId)
        newDriverIdToTimeWorked = copy.deepcopy(solution.driverIdToTimeWorked)

        for change in changes:
            serviceId = change.serviceId
            service = solution.services[serviceId]

            curBusId = change.curBusId
            newBusId = change.newBusId
            curDriverId = change.curDriverId
            newDriverId = change.newDriverId

            newServiceIdToBusId[serviceId] = newBusId
            newDriverIdToTimeWorked[curDriverId] -= service.getDurationTime()
            if newDriverId in newDriverIdToTimeWorked:
                newDriverIdToTimeWorked[newDriverId] += service.getDurationTime()
            else:
                newDriverIdToTimeWorked[newDriverId] = service.getDurationTime()

            # Some constraint comprovation (easiest ones)
            if  solution.buses[newBusId].getCapacity() < service.getPassengers() or solution.drivers[newDriverId].getMaxTime() < newDriverIdToTimeWorked[newDriverId]:
                return float('infinity')

        busCost = 0
        for serviceId,busId in newServiceIdToBusId.items():
            service = solution.services[serviceId]
            bus = solution.buses[busId]
            busCost += service.getDurationTime()*bus.getCostTime()
            busCost += service.getDurationDist()*bus.getCostDistance()

        driverCost = 0
        for driverId,timeWorked in newDriverIdToTimeWorked.items():
            driver = solution.drivers[driverId]
            if timeWorked > driver.getBM():
                driverCost += driver.getBM()*driver.getCostBM()
                driverCost += (timeWorked-driver.getBM())*driver.getCostEM()
            else:
                driverCost += timeWorked*driver.getCostBM()

        return busCost + driverCost

    def getAssignmentsSortedByPassengers(self, solution):
        # create vector of service assignments.
        # Each element is a tuple <service, bus, driver, passengers>
        assignments = []
        for service in solution.services:
            serviceId = service.getId()
            busId = solution.getBusIdAssignedToServiceId(serviceId)
            driverId = solution.getDriverIdAssignedToServiceId(serviceId)
            bus = solution.buses[busId]
            driver = solution.drivers[driverId]
            passengers = service.getPassengers()
            assignment = (service, bus, driver, passengers)
            assignments.append(assignment)

        # For best improvement policy it does not make sense to sort the services since all of them must be explored.
        # However, for first improvement, we can start by the services assigned to services with more passengers.
        if self.policy == 'BestImprovement': return assignments

        # Sort assignments by the passengers of the service assigned in descending order.
        sorted_assignments = sorted(assignments, key=lambda assignment:assignment[3], reverse=True)
        return sorted_assignments

    def exploreNeighborhood(self, solution):
        services = solution.services

        actualCost = solution.calculateActualCost()
        bestNeighbor = solution

        if self.nhStrategy == 'Reassignment':
            sortedAssignments = self.getAssignmentsSortedByPassengers(solution)

            for assignment in sortedAssignments:
                service = assignment[0]
                bus = assignment[1]
                driver = assignment[2]

                serviceId = service.getId()
                curBusId = bus.getId()
                curDriverId = driver.getId()

                for bus in solution.buses:
                    newBusId = bus.getId()

                    for driver in solution.drivers:
                        newDriverId = driver.getId()
                        if newBusId == curBusId and newDriverId == curDriverId: continue

                        changes = []
                        changes.append(Change(serviceId, curBusId, newBusId, curDriverId, newDriverId))
                        neighborCost = self.evaluateNeighbor(solution, changes)
                        if actualCost > neighborCost:
                            neighbor = self.createNeighborSolution(solution, changes)
                            if neighbor is None: continue
                            if neighbor.calculateActualCost() != neighborCost:
                                print('NEIGHBOR COSTS DOESN\'T MATCH')
                            if self.policy == 'FirstImprovement':
                                return neighbor
                            else:
                                bestNeighbor = neighbor
                                actualCost = neighborCost

        # elif(self.nhStrategy == 'Exchange'):
        #     # For the Exchange neighborhood and first improvement policy, try exchanging
        #     # two services, one from highly loaded CPU and the other from lowly loaded
        #     # CPU. It can be done by picking task1 from begin to end of sortedAssignments,
        #     # and task2 from end to begin.

        #     sortedAssignments = self.getAssignmentsSortedByCPULoad(solution)
        #     numAssignments = len(sortedAssignments)

        #     for i in xrange(0, numAssignments):             # i = 0..(numAssignments-1)
        #         assignment1 = sortedAssignments[i]

        #         task1 = assignment1[0]
        #         taskId1 = task1.getId()

        #         curCPU1 = assignment1[1]
        #         curCPUId1 = curCPU1.getId()

        #         for j in xrange(numAssignments-1, -1, -1):  # j = (numAssignments-1)..0
        #             if(i >= j): continue # avoid duplicate explorations and exchange with itself.

        #             assignment2 = sortedAssignments[j]

        #             task2 = assignment2[0]
        #             taskId2 = task2.getId()

        #             curCPU2 = assignment2[1]
        #             curCPUId2 = curCPU2.getId()

        #             # avoid exploring pairs of tasks assigned to the same CPU
        #             if(curCPUId1 == curCPUId2): continue

        #             changes = []
        #             changes.append(Change(taskId1, curCPUId1, curCPUId2))
        #             changes.append(Change(taskId2, curCPUId2, curCPUId1))
        #             neighborHighestLoad = self.evaluateNeighbor(solution, changes)
        #             if(curHighestLoad > neighborHighestLoad):
        #                 neighbor = self.createNeighborSolution(solution, changes)
        #                 if(neighbor is None): continue
        #                 if(self.policy == 'FirstImprovement'):
        #                     return(neighbor)
        #                 else:
        #                     bestNeighbor = neighbor
        #                     curHighestLoad = neighborHighestLoad

        else:
            raise Exception('Unsupported NeighborhoodStrategy(%s)' % self.nhStrategy)

        return bestNeighbor

    def run(self, solution):
        if not self.enabled: return solution
        if not solution.isFeasible(): return solution

        bestSolution = solution
        bestCost = bestSolution.calculateActualCost()

        startEvalTime = time.time()
        iterations = 0

        # keep iterating while improvements are found
        keepIterating = True
        while keepIterating:
            keepIterating = False
            iterations += 1

            neighbor = self.exploreNeighborhood(bestSolution)
            curCost = neighbor.getCost()
            if bestCost > curCost:
                bestSolution = neighbor
                bestCost = curCost
                keepIterating = True

        self.iterations += iterations
        self.elapsedTime += time.time() - startEvalTime

        return bestSolution

    def printPerformance(self):
        if not self.enabled: return

        avg_evalTimePerIteration = 0.0
        if self.iterations != 0:
            avg_evalTimePerIteration = 1000.0 * self.elapsedTime / float(self.iterations)

        print('')
        print('Local Search Performance:')
        print('  Num. Iterations Eval.', self.iterations)
        print('  Total Eval. Time     ', self.elapsedTime, 's')
        print('  Avg. Time / Iteration', avg_evalTimePerIteration, 'ms')
