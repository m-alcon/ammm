'''
AMMM Lab Heuristics v1.2
Greedy solver.
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

from Solver import Solver
from Solution import Solution
from LocalSearch import LocalSearch

# Inherits from a parent abstract solver.
class Solver_Greedy(Solver):

    def greedyConstruction(self, config, problem):
        # get an empty solution for the problem
        solution = Solution.createEmptySolution(config, problem)

        # get services and sort them by their number of passengers in descending order
        services = problem.getServices()
        sortedServices = sorted(services, key=lambda service: service.getPassengers(), reverse=True)

        elapsedEvalTime = 0
        evaluatedCandidates = 0
        # for each service taken in sorted order
        for service in sortedServices:
            serviceId = service.getId()
            feasibleAssignments, service_elapsedEvalTime, service_evaluatedCandidates = solution.findFeasibleAssignments(serviceId)
            elapsedEvalTime += service_elapsedEvalTime
            evaluatedCandidates += service_evaluatedCandidates

            # choose assignment with minimum cost
            minCost = float('infinity')
            choosenAssignment = None
            for feasibleAssignment in feasibleAssignments:
                if feasibleAssignment.totalCost < minCost:
                    minCost = feasibleAssignment.totalCost
                    choosenAssignment = feasibleAssignment

            if choosenAssignment is None:
                solution.makeInfeasible()
                break

            # assign the current service to the bus and the driver that resulted in a minimum cost
            solution.assign(choosenAssignment.serviceId, choosenAssignment.busId, choosenAssignment.driverId)

        return solution, elapsedEvalTime, evaluatedCandidates

    def solve(self, config, problem):
        self.startTimeMeasure()
        self.writeLogLine(float('infinity'), 0)

        solution, elapsedEvalTime, evaluatedCandidates = self.greedyConstruction(config, problem)
        self.writeLogLine(solution.calculateActualCost(), 1)

        localSearch = LocalSearch(config)
        solution = localSearch.run(solution)

        self.writeLogLine(solution.calculateActualCost(), 1)

        avg_evalTimePerCandidate = 0.0
        if (evaluatedCandidates != 0):
            avg_evalTimePerCandidate = 1000.0 * elapsedEvalTime / float(evaluatedCandidates)

        print('')
        print('Greedy Candidate Evaluation Performance:')
        print('  Num. Candidates Eval.', evaluatedCandidates)
        print('  Total Eval. Time     ', elapsedEvalTime, 's')
        print('  Avg. Time / Candidate', avg_evalTimePerCandidate, 'ms')

        localSearch.printPerformance()

        return solution
