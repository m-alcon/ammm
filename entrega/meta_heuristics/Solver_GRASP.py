'''
AMMM Lab Heuristics v1.2
GRASP solver.
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

import random, time
from Solver import Solver
from Solution import Solution
from LocalSearch import LocalSearch

# Inherits from a parent abstract solver.
class Solver_GRASP(Solver):
    def selectCandidate(self, config, candidateList):
        if not candidateList: return None

        # sort candidate assignments by cost in ascending order
        sortedCL = sorted(candidateList, key=lambda candidate: candidate.totalCost, reverse=False)

        # compute boundary cost as a function of the minimum and maximum costs and the alpha parameter
        alpha = config.alpha
        minTotalCost = sortedCL[0].totalCost
        maxTotalCost = sortedCL[len(sortedCL)-1].totalCost
        boundaryTotalCost = minTotalCost + (maxTotalCost - minTotalCost) * alpha

        # find elements that fall into the RCL (those fulfilling: totalCost < boundaryTotalCost)
        maxIndex = 0
        for x in sortedCL:
            if(x.totalCost > boundaryTotalCost): break
            maxIndex += 1

        # create RCL and pick an element randomly
        rcl = sortedCL[0:maxIndex]          # pick first maxIndex elements starting from element 0
        if not rcl: return None
        return random.choice(rcl)           # pick an element from rcl at random

    def greedyRandomizedConstruction(self, config, problem):
        # get an empty solution for the problem
        solution = Solution.createEmptySolution(config, problem)

        # get services and sort them by their total required resources in descending order
        services = problem.getServices()
        sortedServices = sorted(services, key=lambda service: service.getPassengers(), reverse=True)

        iteration_elapsedEvalTime = 0
        iteration_evaluatedCandidates = 0

        # for each service taken in sorted order
        for service in sortedServices:
            serviceId = service.getId()

            # compute feasible assignments
            candidateList, elapsedEvalTime, evaluatedCandidates = solution.findFeasibleAssignments(serviceId)
            iteration_elapsedEvalTime += elapsedEvalTime
            iteration_evaluatedCandidates += evaluatedCandidates

            # no candidate assignments => no feasible assignment found
            if not candidateList:
                solution.makeInfeasible()
                break

            # select an assignment
            candidate = self.selectCandidate(config, candidateList)
            if candidate is None: break

            # assign the current service to the Bus and Driver that resulted in a minimum cost
            solution.assign(serviceId, candidate.busId, candidate.driverId)

        return(solution, iteration_elapsedEvalTime, iteration_evaluatedCandidates)

    def solve(self, config, problem):
        bestSolution = Solution.createEmptySolution(config, problem)
        bestSolution.makeInfeasible()
        bestTotalCost = bestSolution.calculateActualCost()
        self.startTimeMeasure()
        self.writeLogLine(bestTotalCost, 0)

        total_elapsedEvalTime = 0
        total_evaluatedCandidates = 0

        localSearch = LocalSearch(config)

        iteration = 0
        while time.time() - self.startTime < config.maxExecTime:
            iteration += 1

            # force first iteration as a Greedy execution (alpha == 0)
            originalAlpha = config.alpha
            if iteration == 1: config.alpha = 0

            solution, it_elapsedEvalTime, it_evaluatedCandidates = self.greedyRandomizedConstruction(config, problem)
            total_elapsedEvalTime += it_elapsedEvalTime
            total_evaluatedCandidates += it_evaluatedCandidates

            # recover original alpha
            if iteration == 1: config.alpha = originalAlpha

            if not solution.isFeasible(): continue

            solution = localSearch.run(solution)

            solutionTotalCost = solution.calculateActualCost()
            if(solutionTotalCost < bestTotalCost):
                bestSolution = solution
                bestTotalCost = solutionTotalCost
                self.writeLogLine(bestTotalCost, iteration)

        self.writeLogLine(bestTotalCost, iteration)

        avg_evalTimePerCandidate = 0.0
        if(total_evaluatedCandidates != 0):
            avg_evalTimePerCandidate = 1000.0 * total_elapsedEvalTime / float(total_evaluatedCandidates)

        print('')
        print('GRASP Candidate Evaluation Performance:')
        print('  Num. Candidates Eval.', total_evaluatedCandidates)
        print('  Total Eval. Time     ', total_elapsedEvalTime, 's')
        print('  Avg. Time / Candidate', avg_evalTimePerCandidate, 'ms')

        localSearch.printPerformance()

        return bestSolution
