# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2023 all rights reserved

# bash completion script for flexi
function _flexi() {
    # get the partial command line
    local line=${COMP_LINE}
    local word=${COMP_WORDS[COMP_CWORD]}
    # ask flexi to provide guesses
    COMPREPLY=($(flexi complete --word="${word}" --line="${line}"))
}

# register the hook
complete -F _flexi flexi

# end of file
