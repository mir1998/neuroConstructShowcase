#
#
#   File to test current configuration of HH project.
#
#   To execute this type of file, type '..\..\..\nC.bat -python XXX.py' (Windows)
#   or '../../../nC.sh -python XXX.py' (Linux/Mac). Note: you may have to update the
#   NC_HOME and NC_MAX_MEMORY variables in nC.bat/nC.sh
#
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Medical Research Council and the
#   Wellcome Trust
#
#

import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using nC.bat -python XXX.py' or 'nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc

projFile = File(os.getcwd(), "../Ex10_NeuroML2.ncx")

print "Project file for this test: "+ projFile.getAbsolutePath()


##############  Main settings  ##################

simConfigs = []

simConfigs.append("AbstractCells")

simDt =                 0.001

#simulators =            ["NEURON"]
simulators =            ["NEURON", "LEMS"]


numConcurrentSims =     4

varTimestepNeuron =     False

plotSims =              True
plotVoltageOnly =       True
analyseSims =           True
runInBackground =       True
verbose =               True
runSims =               True

#############################################


def testAll(argv=None):
    if argv is None:
        argv = sys.argv

    print "Loading project from "+ projFile.getCanonicalPath()


    simManager = nc.SimulationManager(projFile,
                                      numConcurrentSims,
                                      verbose)

    simManager.runMultipleSims(simConfigs =      simConfigs,
                               simDt =           simDt,
                               simulators =      simulators,
                               runInBackground = runInBackground,
                               runSims = runSims,
                               varTimestepNeuron = varTimestepNeuron)
    

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          plotSims =          plotSims,
                          analyseSims =       analyseSims)

    # These were discovered using analyseSims = True above.
    # They need to hold for all simulators
    '''spikeTimesToCheck = {'CGAbst_0'  : [17.9716, 22.4136, 27.1705, 32.3506, 38.134, 44.8546, 53.2245, 64.6112, 75.5588, 86.8877, 97.8855],
                         'CGAbst2_0'  : [24.3711, 25.5105, 26.722, 28.018, 29.415, 30.9363, 32.6154, 34.506, 36.7044, 39.4271, 43.6248, 77.6337, 79.3465, 81.2841, 83.5555, 86.423, 91.5845, 125.478, 127.191, 129.128, 131.4, 134.267, 139.428, 173.322, 175.035, 176.972, 179.244, 182.111, 187.273],
                         'CGIaF_0'   : [27.3298, 55.0556, 82.7814, 104.1956, 118.0584, 131.9214, 145.7844, 159.6474, 173.5104, 187.3734],
                         'CGIaFRef_0'   : [40.9952, 92.5842, 144.173, 195.762]}'''

    spikeTimesToCheck = {'CGIaF_0'   : [27.3298, 55.0556, 82.7814, 104.1956, 118.0584, 131.9214, 145.7844, 159.6474, 173.5104, 187.3734],
                         'CGIaFRef_0'   : [40.9952, 92.5842, 144.173, 195.762],
                         'CG_IaF_GrC_0'   : [51.8383, 55.1162, 58.3941, 61.672, 64.9499, 68.2278, 71.5057, 74.7836, 78.0615, 81.3394, 84.6173, 87.8952, 91.1731, 94.451, 97.7289, 101.007, 104.285, 107.563, 110.841, 114.118, 117.396, 120.674, 123.952, 127.23, 130.508, 133.786, 137.064, 140.342, 143.62, 146.898],
                         'CG_IaF_GrC_NoRef_0'   : [51.8383, 53.1175, 54.3967, 55.6759, 56.9551, 58.2343, 59.5135, 60.7927, 62.0719, 63.3511, 64.6303, 65.9095, 67.1887, 68.4679, 69.7471, 71.0263, 72.3055, 73.5847, 74.8639, 76.1431, 77.4223, 78.7015, 79.9807, 81.2599, 82.5391, 83.8183, 85.0975, 86.3767, 87.6559, 88.9351, 90.2143, 91.4935, 92.7727, 94.0519, 95.3311, 96.6103, 97.8895, 99.1687, 100.448, 101.727, 103.006, 104.286, 105.565, 106.844, 108.123, 109.402, 110.682, 111.961, 113.24, 114.519, 115.798, 117.078, 118.357, 119.636, 120.915, 122.194, 123.474, 124.753, 126.032, 127.311, 128.59, 129.87, 131.149, 132.428, 133.707, 134.986, 136.266, 137.545, 138.824, 140.103, 141.382, 142.662, 143.941, 145.22, 146.499, 147.778, 149.057]}

    spikeTimeAccuracy = 0.52

    threshold = {'CGAbst_0'    : -41,
                 'CGAbst2_0'   : 0,
                 'CGIaF_0'     : -55.1,
                 'CGIaFRef_0'  : -55.1,
                 'CG_IaF_GrC_0'  : -40.1,
                 'CG_IaF_GrC_NoRef_0'  : -40.1}

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy,
                                  threshold = threshold)

    print report

    return report


if __name__ == "__main__":
    testAll()
