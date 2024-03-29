// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2023 all rights reserved


// get colors
import { theme } from '~/palette'


// publish
export default {
    // the container
    badge: {
    },

    // the shape
    shape: {
    },

    // state dependent overrides
    // when this is the current activity
    engaged: {
        // for the badge
        badge: {
        },
        // for the shape
        shape: {
        },
    },

    // when exploring whether this acivity is available
    // e.g. when the cursor hovers over its badge
    available: {
        // for the badge
        badge: {
        },
        // for the shape
        shape: {
        },
    },

    // when the activity is not available
    disabled: {
        // for the badge
        badge: {
        },
        // for the shape
        shape: {
        },
    },
}


// end of file
