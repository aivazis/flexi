# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2023 all rights reserved


# externals
import flexi


# declaration
class About(flexi.shells.command, family='flexi.cli.about'):
    """
    Display information about this application
    """


    @flexi.export(tip="print the copyright note")
    def copyright(self, plexus, **kwds):
        """
        Print the copyright note of the flexi package
        """
        # show the copyright note
        plexus.info.log(flexi.meta.copyright)
        # all done
        return


    @flexi.export(tip="print out the acknowledgments")
    def credits(self, plexus, **kwds):
        """
        Print out the license and terms of use of the flexi package
        """
        # make some space
        plexus.info.log(flexi.meta.header)
        # all done
        return


    @flexi.export(tip="print out the license and terms of use")
    def license(self, plexus, **kwds):
        """
        Print out the license and terms of use of the flexi package
        """
        # make some space
        plexus.info.log(flexi.meta.license)
        # all done
        return


    @flexi.export(tip="print the version number")
    def version(self, plexus, **kwds):
        """
        Print the version of the flexi package
        """
        # make some space
        plexus.info.log(flexi.meta.header)
        # all done
        return


# end of file
