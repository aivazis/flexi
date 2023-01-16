# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2023 all rights reserved


# support
import flexi


# declaration
class Config(flexi.shells.command, family="flexi.cli.config"):
    """
    Display configuration information about this package
    """


    # version info
    @flexi.export(tip="the version information")
    def version(self, **kwds):
        """
        Print the version of the flexi package
        """
        # print the version number
        print(f"{flexi.meta.version}")
        # all done
        return 0


    # configuration
    @flexi.export(tip="the top level installation directory")
    def prefix(self, **kwds):
        """
        Print the top level installation directory
        """
        # print the installation location
        print(f"{flexi.prefix}")
        # all done
        return 0


    @flexi.export(tip="the directory with the executable scripts")
    def path(self, **kwds):
        """
        Print the location of the executable scripts
        """
        # print the path to the bin directory
        print(f"{flexi.prefix}/bin")
        # all done
        return 0


    @flexi.export(tip="the directory with the python packages")
    def pythonpath(self, **kwds):
        """
        Print the directory with the python packages
        """
        # print the path to the python package
        print(f"{flexi.home.parent}")
        # all done
        return 0


    @flexi.export(tip="the location of the {flexi} headers")
    def incpath(self, **kwds):
        """
        Print the locations of the {flexi} headers
        """
        # print the path to the headers
        print(f"{flexi.prefix}/include")
        # all done
        return 0


    @flexi.export(tip="the location of the {flexi} libraries")
    def libpath(self, **kwds):
        """
        Print the locations of the {flexi} libraries
        """
        # print the path to the libraries
        print(f"{flexi.prefix}/lib")
        # all done
        return 0


# end of file
