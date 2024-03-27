import unittest
from getopt import getopt, GetoptError
from sys import exit, argv, path as spath
from os import path as opath

try:
    optlist, args = getopt(argv[1:],'v')
except GetoptError:
    print(GetoptError)
    print(argv[0] + "-v")
    print("... the verbose flag (-v) may be used")
    exit()

VERBOSE = False
RUNALL = False

spath.append(opath.realpath(opath.dirname(__file__)))

for o, a in optlist:
    if o == '-v':
        VERBOSE = True
        break

spath.append(opath.realpath(opath.dirname(__file__)))

## api tests
from ApiTests import *
ApiTestSuite = unittest.TestLoader().loadTestsFromTestCase(ApiTest)

## model tests
from ModelTests import *
ModelTestSuite = unittest.TestLoader().loadTestsFromTestCase(ModelTest)

## logger tests
from LoggerTests import *
LoggerTestSuite = unittest.TestLoader().loadTestsFromTestCase(LoggerTest)

MainSuite = unittest.TestSuite([LoggerTestSuite,ModelTestSuite,ApiTestSuite])