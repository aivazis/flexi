// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2021 all rights reserved


// externals
import React from 'react'
// local
// context
import { Context } from './context'


// register a panel
export default ({ ref = null, min = 0, max = Infinity, auto = false }) => {
    // grab the state mutator
    const { addPanel } = React.useContext(Context)

    // if the caller didn't provide a ref, make one
    const panel = ref === null ? React.useRef(null) : ref

    // after the initial mount
    React.useEffect(() => {
        // register the panel
        addPanel({ ref: panel, min, max, false })
    }, [])

    // build and return the context relevant to this panel
    return panel
}


// end of file
