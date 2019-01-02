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

        # Validate rc
        rc = data.rc
        if(len(rc) != nCPUs):
            raise Exception('Size of rc(%d) does not match with value of nCPUs(%d).' % (len(rc), nCPUs))

        for value in rc:
            if(not isinstance(value, (int, long, float)) or (value < 0)):
                raise Exception('Invalid parameter value(%s) in rc. Should be a float greater or equal than zero.' % str(value))

        # Validate CK
        CK = data.CK
        if(len(CK) != nCPUs):
            raise Exception('Size of first dimension of CK(%d) does not match with value of nCPUs(%d).' % (len(CK), nCPUs))

        for ckEntry in CK:
            if(len(ckEntry) != nCores):
                raise Exception('Size of second dimension of CK(%d) does not match with value of nCores(%d).' % (len(ckEntry), nCores))

            for value in ckEntry:
                if(value not in [0, 1]):
                    raise Exception('Invalid parameter value(%s) in CK. Should be an integer value [0, 1].' % str(value))

        # Validate TH
        TH = data.TH
        if(len(TH) != nTasks):
            raise Exception('Size of first dimension of TH(%d) does not match with value of nTasks(%d).' % (len(TH), nTasks))

        for thEntry in TH:
            if(len(thEntry) != nThreads):
                raise Exception('Size of second dimension of TH(%d) does not match with value of nThreads(%d).' % (len(thEntry), nThreads))

            for value in thEntry:
                if(value not in [0, 1]):
                    raise Exception('Invalid parameter value(%s) in TH. Should be an integer value [0, 1].' % str(value))
