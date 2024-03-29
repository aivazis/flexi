// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2023 all rights reserved


// get colors
import { theme } from '~/palette'


// publish
export default {
    // for my toolbar
    box: {
        // paint
        backgroundColor: "hsl(0deg, 0%, 21%, 1)",
    },

    // my opinions on badges
    badge: {
        //  styling
        padding: "0.75rem",
        // make a transparent border of the correctwidth so the badges don't move around
        // when the corresponding activity is engaged
        borderLeft: `2px solid hsl(0deg, 0%, 0%, 0)`,
    },

    // and shapes
    shape: {
    },

    // state dependent overrides
    // when this is the current activity
    engaged: {
        // for the badge
        badge: {
            borderLeft: `2px solid ${theme.banner.name}`,
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
