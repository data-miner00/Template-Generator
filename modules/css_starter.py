#
#  This is a module that is responsible to generate the basic CSS template
#  that contains basic layouts.
#

css = r"""
/* Imports
=========================================== */
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

/* Variables
=========================================== */
/*
 * To use the variables, for example, type
 *      color: var(--color_bg);
 *
 *  where color is the target property and --color_bg
 *  is the actual value for the property as defined in
 *  this :root block.
 */
:root {
    /* Text variables */
    --montserrat: 'Montserrat', sans-serif;
    --lato: 'Lato', sans-serif;

    /* Gradient variables */
    --gradient: linear-gradient(
                    45deg,
                    #845ec2,
                    #d65db1,
                    #ff6f91,
                    #ff9671,
                    #ffc75f,
                    #f9f871
                );
    --gradient1: linear-gradient(
                    90deg,
                    #c33764,
                    #1d2671
                );

    /* Color variables */
    --color_bg: #36393b;
    --color_bbg: #26262b;
    --color_dis: #7289da;
    --color_fram: #e6ebf4;
    --color_misc1: #faa61a;
    --color_misc2: #5fc8fa;
    --color_misc3: #8fc5fa;
    --color_misc4: #f6989d;
    --color_misc5: #efce4c;

    /* Etc */

}

/* Resets
=========================================== */
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

/* Universal Styling
=========================================== */
html {
    font-family: var(--montserrat);
    font-size: 17px;
}

button {
    padding: 8px;
    border-radius: 5px;
}

a {
    text-decoration: none;
}

ul, ol {
    list-style: none;
}

/* Animations
=========================================== */
@keyframes change {
    from {
        background-color: red;
    }
    to {
        background-color: yellow;
    }
}

@keyframes change2 {
    0%   {background-color: red;}
    25%  {background-color: yellow;}
    50%  {background-color: blue;}
    100% {background-color: green;}
}
"""

meta = r"""
/*
 *  CSS template generated from Python {}.
 *  Created by {} on {} at {} using {}
 *  Copyright © {}.
 */

{}"""

import os
import sys
from datetime import date, datetime

sys_info = sys.version.split(' ')

# Info #1: Python Version
python_ver = sys_info[0]

# Info #2: Username/Name

# Info #3: Date
date_today = date.today().strftime("%B %d, %Y")

# Info #4: Time
time_now = datetime.today().strftime("%H:%M:%S")

# Info #5: Year
year = date.today().year

# Info #6: OS
osname = os.name

def css_parser(username: str):
    return meta.format(
        python_ver,
        username,
        date_today,
        time_now,
        osname,
        year,
        css
    )