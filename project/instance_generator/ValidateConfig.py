'''
AMMM Instance Generator v1.0
Config attributes validator.
Copyright 2016 Luis Velasco and Lluis Gifre.

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

# Validate config attributes read from a DAT file. 
class ValidateConfig(object):
    @staticmethod
    def validate(data):
        # Validate that mandatory input parameters were found
        for paramName in ['instancesDirectory', 'fileNamePrefix', 'fileNameExtension', 'numInstances',
                          'numServices', 'numDrivers', 'numBuses', 'maxBuses', 'minStartTime', 'maxStartTime',
                          'minDurationTime', 'maxDurationTime', 'minDurationDistance', 'maxDurationDistance',
                          'minPassangers', 'maxPassangers', 'minCapacity', 'maxCapacity', 'minCostTime',
                          'maxCostTime', 'minCostDist', 'maxCostDist', 'minMaxTime', 'maxMaxTime', 'minCostBM',
                          'maxCostBM', 'minCostEM', 'maxCostEM', 'minBM', 'maxBM']:
            if(not data.__dict__.has_key(paramName)):
                raise Exception('Parameter(%s) not contained in Configuration' % str(paramName))
        
        instancesDirectory = data.instancesDirectory
        if(len(instancesDirectory) == 0): raise Exception('Value for instancesDirectory is empty')

        fileNamePrefix = data.fileNamePrefix
        if(len(fileNamePrefix) == 0): raise Exception('Value for fileNamePrefix is empty')

        fileNameExtension = data.fileNameExtension
        if(len(fileNameExtension) == 0): raise Exception('Value for fileNameExtension is empty')

        numInstances = data.numInstances
        if(not isinstance(numInstances, (int, long)) or (numInstances <= 0)):
            raise Exception('numInstances(%s) has to be a positive integer value.' % str(numInstances))

        numServices = data.numServices
        if(not isinstance(numServices, (int, long)) or (numServices <= 0)):
            raise Exception('numServices(%s) has to be a positive integer value.' % str(numServices))

        numBuses = data.numBuses
        if(not isinstance(numBuses, (int, long)) or (numBuses <= 0)):
            raise Exception('numBuses(%s) has to be a positive integer value.' % str(numBuses))

        maxBuses = data.maxBuses
        if(not isinstance(maxBuses, (int, long)) or (maxBuses <= 0)):
            raise Exception('maxBuses(%s) has to be a positive integer value.' % str(maxBuses))

        numDrivers = data.numDrivers
        if(not isinstance(numDrivers, (int, long)) or (numDrivers <= 0)):
            raise Exception('numDrivers(%s) has to be a positive integer value.' % str(numDrivers))

        minStartTime = data.minStartTime
        if(not isinstance(minStartTime, (int, long)) or (minStartTime < 0)):
            raise Exception('minStartTime(%s) has to be a positive integer value.' % str(minStartTime))

        maxStartTime = data.maxStartTime
        if(not isinstance(maxStartTime, (int, long)) or (maxStartTime <= 0)):
            raise Exception('maxStartTime(%s) has to be a positive integer value.' % str(maxStartTime))

        minDurationTime = data.minDurationTime
        if(not isinstance(minDurationTime, (int, long)) or (minDurationTime <= 0)):
            raise Exception('minDurationTime(%s) has to be a positive integer value.' % str(minDurationTime))

        maxDurationTime = data.maxDurationTime
        if(not isinstance(maxDurationTime, (int, long)) or (maxDurationTime <= 0)):
            raise Exception('maxDurationTime(%s) has to be a positive integer value.' % str(maxDurationTime))

        minDurationDistance = data.minDurationDistance
        if(not isinstance(minDurationDistance, (int, long)) or (minDurationDistance <= 0)):
            raise Exception('minDurationDistance(%s) has to be a positive integer value.' % str(minDurationDistance))

        maxDurationDistance = data.maxDurationDistance
        if(not isinstance(maxDurationDistance, (int, long)) or (maxDurationDistance <= 0)):
            raise Exception('maxDurationDistance(%s) has to be a positive integer value.' % str(maxDurationDistance))

        minPassangers = data.minPassangers
        if(not isinstance(minPassangers, (int, long)) or (minPassangers <= 0)):
            raise Exception('minPassangers(%s) has to be a positive integer value.' % str(minPassangers))

        maxPassangers = data.maxPassangers
        if(not isinstance(maxPassangers, (int, long)) or (maxPassangers <= 0)):
            raise Exception('maxPassangers(%s) has to be a positive integer value.' % str(maxPassangers))

        minCapacity = data.minCapacity
        if(not isinstance(minCapacity, (int, long)) or (minCapacity <= 0)):
            raise Exception('minCapacity(%s) has to be a positive integer value.' % str(minCapacity))

        maxCapacity = data.maxCapacity
        if(not isinstance(maxCapacity, (int, long)) or (maxCapacity <= 0)):
            raise Exception('maxCapacity(%s) has to be a positive integer value.' % str(maxCapacity))

        minCostTime = data.minCostTime
        if(not isinstance(minCostTime, (int, long)) or (minCostTime <= 0)):
            raise Exception('minCostTime(%s) has to be a positive integer value.' % str(minCostTime))

        maxCostTime = data.maxCostTime
        if(not isinstance(maxCostTime, (int, long)) or (maxCostTime <= 0)):
            raise Exception('maxCostTime(%s) has to be a positive integer value.' % str(maxCostTime))

        minCostDist = data.minCostDist
        if(not isinstance(minCostDist, (int, long)) or (minCostDist <= 0)):
            raise Exception('minCostDist(%s) has to be a positive integer value.' % str(minCostDist))

        maxCostDist = data.maxCostDist
        if(not isinstance(maxCostDist, (int, long)) or (maxCostDist <= 0)):
            raise Exception('maxCostDist(%s) has to be a positive integer value.' % str(maxCostDist))

        minMaxTime = data.minMaxTime
        if(not isinstance(minMaxTime, (int, long)) or (minMaxTime <= 0)):
            raise Exception('minMaxTime(%s) has to be a positive integer value.' % str(minMaxTime))

        maxMaxTime = data.maxMaxTime
        if(not isinstance(maxMaxTime, (int, long)) or (maxMaxTime <= 0)):
            raise Exception('maxMaxTime(%s) has to be a positive integer value.' % str(maxMaxTime))

        minCostBM = data.minCostBM
        if(not isinstance(minCostBM, (int, long)) or (minCostBM <= 0)):
            raise Exception('minCostBM(%s) has to be a positive integer value.' % str(minCostBM))

        maxCostBM = data.maxCostBM
        if(not isinstance(maxCostBM, (int, long)) or (maxCostBM <= 0)):
            raise Exception('maxCostBM(%s) has to be a positive integer value.' % str(maxCostBM))

        minCostEM = data.minCostEM
        if(not isinstance(minCostEM, (int, long)) or (minCostEM <= 0)):
            raise Exception('minCostEM(%s) has to be a positive integer value.' % str(minCostEM))

        maxCostEM = data.maxCostEM
        if(not isinstance(maxCostEM, (int, long)) or (maxCostEM <= 0)):
            raise Exception('maxCostEM(%s) has to be a positive integer value.' % str(maxCostEM))

        minBM = data.minBM
        if(not isinstance(minBM, (int, long)) or (minBM <= 0)):
            raise Exception('minBM(%s) has to be a positive integer value.' % str(minBM))

        maxBM = data.maxBM
        if(not isinstance(maxBM, (int, long)) or (maxBM <= 0)):
            raise Exception('maxBM(%s) has to be a positive integer value.' % str(maxBM))
        