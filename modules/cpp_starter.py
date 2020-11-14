

cpp = '''

/*
  C++ template generated from Python {}
  Created by {} on {} at {}.
  Copyright © {}.
*/

/* Imports
=========================================== */
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <ionamip>
#include <cstdlib>
#include <Windows.h>

// Data structures 
#include <stack>
#include <queue>
#include <array>
#include <map>
#include <set>
#include <vector>

/* Using namespaces
=========================================== */
using namespace std;

/* Function prototypes
=========================================== */
void hello_world();
int addition(int, int);

/* Entry point
=========================================== */
int main(int argc, char* argv[]) {

    hello_world();

    return 0;
}

void hello_world() {
    cout << "Hello World" << endl;
    return;
}

int addition(int num1, int num2) {
    return num1 + num2;
}
'''

import sys
import os
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

def cpp_parser(username: str):
	return cpp.format(
		python_ver,
		username,
		date_today,
        time_now,
        osname,
        year
	)


extensions = ["cpp", "cxx", "C", "c++", "cp", "cc", "CPP"]


