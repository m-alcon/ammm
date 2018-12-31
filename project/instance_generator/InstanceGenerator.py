'''
AMMM Instance Generator v1.0
Instance Generator class.
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

import os, random

# Generate instances based on read configuration. 
class InstanceGenerator(object):
    def __init__(self, config):
        self.config = config
    
    def generate(self):
        instancesDirectory = self.config.instancesDirectory
        fileNamePrefix = self.config.fileNamePrefix
        fileNameExtension = self.config.fileNameExtension
        numInstances = self.config.numInstances

        numServices = self.config.numServices
        numDrivers = self.config.numDrivers
        numBuses = self.config.numBuses

        minStartTime  = self.config.minStartTime
        maxStartTime  = self.config.maxStartTime
        minDurationTime = self.config.minDurationTime
        maxDurationTime = self.config.maxDurationTime
        minDurationDistance = self.config.minDurationDistance
        maxDurationDistance = self.config.maxDurationDistance
        minPassangers = self.config.minPassangers
        maxPassangers = self.config.maxPassangers

        minCapacity = self.config.minCapacity
        maxCapacity = self.config.maxCapacity
        minCostTime = self.config.minCostTime
        maxCostTime = self.config.maxCostTime
        minCostDist = self.config.minCostDist
        maxCostDist = self.config.maxCostDist
        minMaxTime = self.config.minMaxTime
        maxMaxTime = self.config.maxMaxTime

        minCostBM = self.config.minCostBM
        maxCostBM = self.config.maxCostBM
        minCostEM = self.config.minCostEM
        maxCostEM = self.config.maxCostEM
        minBM = self.config.minBM
        maxBM = self.config.maxBM

        if(not os.path.isdir(instancesDirectory)):
            raise Exception('Directory(%s) does not exist' % instancesDirectory)

        for i in xrange(0, numInstances):
            instancePath = os.path.join(instancesDirectory, '%s_%d.%s' % (fileNamePrefix, i, fileNameExtension))
            fInstance = open(instancePath, 'w')

            fInstance.write('nServices=%d;\n' % numServices)
            fInstance.write('nDrivers=%d;\n' % numDrivers)
            fInstance.write('nBuses=%d;\n' % numBuses)

            startTime = []
            durationTime = []
            durationDistance = []
            passangers = []
            for s in xrange(0, numServices):
                sTime = random.randint(minStartTime, maxStartTime)
                dTime = random.randint(minDurationTime, maxDurationTime)
                dDistance = random.randint(minDurationDistance, maxDurationDistance)
                passang = random.randint(minPassangers, maxPassangers)
                startTime.append(sTime)
                durationTime.append(dTime)
                durationDistance.append(dDistance)
                passangers.append(passang)
            
            fInstance.write('startingTime=[%s];\n' % (' '.join(map(str, startTime))))
            fInstance.write('durationTime=[%s];\n' % (' '.join(map(str, durationTime))))
            fInstance.write('durationDist=[%s];\n' % (' '.join(map(str, durationDistance))))
            fInstance.write('passangers=[%s];\n' % (' '.join(map(str, passangers))))

            capacity = []
            costTime = []
            costDist = []
            for b in xrange(0, numBuses):
                cap = random.randint(minCapacity, maxCapacity)
                cTime = random.randint(minCostTime, maxCostTime)
                cDist = random.randint(minCostDist, maxCostDist)
                capacity.append(cap)
                costTime.append(cTime)
                costDist.append(cDist)

            fInstance.write('capacity=[%s];\n' % (' '.join(map(str, capacity))))
            fInstance.write('costTime=[%s];\n' % (' '.join(map(str, costTime))))
            fInstance.write('costDist=[%s];\n' % (' '.join(map(str, costDist))))

            maxTime = []
            costBM = []
            costEM = []
            bm = []
            for d in xrange(0, numDrivers):
                mTime = random.randint(minMaxTime, maxMaxTime)
                cBM = random.randint(minCostBM, maxCostBM)
                cEM = random.randint(minCostEM, maxCostEM)
                aux_bm = random.randint(minBM, maxBM)
                maxTime.append(mTime)
                costBM.append(cBM)
                costEM.append(cEM)
                bm.append(aux_bm)
            
            fInstance.write('maxTime=[%s];\n' % (' '.join(map(str, maxTime))))
            fInstance.write('costBM=[%s];\n' % (' '.join(map(str, costBM))))
            fInstance.write('costEM=[%s];\n' % (' '.join(map(str, costEM))))
            fInstance.write('BM=[%s];\n' % (' '.join(map(str, bm))))

            fInstance.close()
