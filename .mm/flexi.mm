# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# flexi consists of a python package
flexi.packages := flexi.pkg
# libraries
flexi.libraries := 
# python extensions
flexi.extensions :=
# a ux bundle
flexi.webpack := flexi.ux
# and some tests
flexi.tests := flexi.pkg.tests


# load the packages
include $(flexi.packages)
# the libraries
include $(flexi.libraries)
# the extensions
include $(flexi.extensions)
# the ux
include $(flexi.webpack)
# and the test suites
include $(flexi.tests)


# end of file
