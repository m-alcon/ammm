'''
AMMM Lab Heuristics v1.2
Instance file validator.
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

# Validate instance attributes read from a DAT file.
# It validates the structure of the parameters read from the DAT file.
# It does not validate that the instance is feasible or not.
# Use Problem.checkInstance() function to validate the feasibility of the instance.
class ValidateInputData(object):
    @staticmethod
    def validate(data):
        # Validate that all input parameters were found
        for paramName in ['nServices', 'nBuses', 'nDrivers', 'maxBuses', 'startingTime',
                    'durationTime', 'durationDist', 'passangers', 'capacity', 'costTime',
                    'costDist', 'maxTime', 'costBM', 'costEM', 'bm']:
            if(not data.__dict__.has_key(paramName)):
                raise Exception('Parameter/Set(%s) not contained in Input Data' % str(paramName))

        # Validate nServices
        nServices = data.nServices
        if(not isinstance(nServices, (int, long)) or (nServices <= 0)):
            raise Exception('nTasks(%s) has to be a positive integer value.' % str(nTasks))

        # Validate nBuses
        nBuses = data.nBuses
        if(not isinstance(nBuses, (int, long)) or (nBuses <= 0)):
            raise Exception('nTasks(%s) has to be a positive integer value.' % str(nTasks))

        # Validate nDrivers
        nDrivers = data.nDrivers
        if(not isinstance(nDrivers, (int, long)) or (nDrivers <= 0)):
            raise Exception('nTasks(%s) has to be a positive integer value.' % str(nTasks))

        # Validate maxBuses
        maxBuses = data.maxBuses
        if(not isinstance(maxBuses, (int, long)) or (maxBuses <= 0)):
            raise Exception('nTasks(%s) has to be a positive integer value.' % str(nTasks))

        # Validate startingTime
        startingTime = data.startingTime
        if(len(startingTime) != nServices):
            raise Exception('Size of startingTime(%d) does not match with value of nThreads(%d).' % (len(startingTime), nServices))

        for value in startingTime:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in startingTime. Should be a float greater or equal than zero.' % str(value))

        # Validate durationTime
        durationTime = data.durationTime
        if(len(durationTime) != nServices):
            raise Exception('Size of durationTime(%d) does not match with value of nThreads(%d).' % (len(durationTime), nServices))

        for value in durationTime:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in durationTime. Should be a float greater or equal than zero.' % str(value))

        # Validate durationDist
        durationDist = data.durationDist
        if(len(durationDist) != nServices):
            raise Exception('Size of durationDist(%d) does not match with value of nThreads(%d).' % (len(durationDist), nServices))

        for value in durationDist:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in durationDist. Should be a float greater or equal than zero.' % str(value))

        # Validate passangers
        passangers = data.passangers
        if(len(passangers) != nServices):
            raise Exception('Size of passangers(%d) does not match with value of nServices(%d).' % (len(passangers), nServices))

        for value in passangers:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in passangers. Should be a float greater or equal than zero.' % str(value))

        # Validate capacity
        capacity = data.capacity
        if(len(capacity) != nBuses):
            raise Exception('Size of capacity(%d) does not match with value of nBuses(%d).' % (len(capacity), nBuses))

        # Validate costTime
        costTime = data.costTime
        if(len(costTime) != nBuses):
            raise Exception('Size of costTime(%d) does not match with value of nBuses(%d).' % (len(costTime), nBuses))

        for value in costTime:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in costTime. Should be a float greater or equal than zero.' % str(value))

        # Validate costDist
        costDist = data.costDist
        if(len(costDist) != nBuses):
            raise Exception('Size of costDist(%d) does not match with value of nBuses(%d).' % (len(costDist), nBuses))

        for value in costDist:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in costDist. Should be a float greater or equal than zero.' % str(value))

        # Validate maxTime
        maxTime = data.maxTime
        if(len(maxTime) != nDrivers):
            raise Exception('Size of maxTime(%d) does not match with value of nDrivers(%d).' % (len(maxTime), nDrivers))

        for value in maxTime:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in maxTime. Should be a float greater or equal than zero.' % str(value))

        # Validate costBM
        costBM = data.costBM
        if(len(costBM) != nDrivers):
            raise Exception('Size of costBM(%d) does not match with value of nDrivers(%d).' % (len(costBM), nDrivers))

        for value in costBM:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in costBM. Should be a float greater or equal than zero.' % str(value))

        # Validate costEM
        costEM = data.costEM
        if(len(costEM) != nDrivers):
            raise Exception('Size of costEM(%d) does not match with value of nDrivers(%d).' % (len(costEM), nDrivers))

        for value in costEM:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in costEM. Should be a float greater or equal than zero.' % str(value))

        # Validate maxTime
        BM = data.BM
        if(len(BM) != nDrivers):
            raise Exception('Size of BM(%d) does not match with value of nDrivers(%d).' % (len(BM), nDrivers))

        for value in BM:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in BM. Should be a float greater or equal than zero.' % str(value))