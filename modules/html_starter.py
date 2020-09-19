#
#  This is a module that responsible for generating the template codes
#  for a basic HTML template.
#

html = r"""
<!DOCTYPE html>
<!--
	HTML template generated from Python {}.
    Created by {} on {} at {}.
    Copyright © {}.
-->
<html lang="en">
<head>
	<!-- Metadata Section -->
	<meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />

    <!-- Icon for Page -->
	<link rel="icon" href="https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582748_1280.png" type="image/gif" sizes="16x16">

    <!-- Title for Page -->
	<title>{}</title>

    <!-- External CSS -->
    <link rel="stylesheet" href="" />

	<!-- Internal CSS -->
	<style>
        {}
	</style>
</head>
<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<body>
	<!-- Your contents should put in here -->
	<div class="container">
        <img src="https://www.w3.org/html/logo/downloads/HTML5_1Color_Black.svg" />
		<p>Open up basic.html to edit your contents right away!</p>
	</div>

	<!-- Javascript imports over here -->
	<script src=""></script>
    {}

	<!-- Javascript here -->
	<script>
		// Sample scripts
		const container = document.getElementsByClassName("container");
        console.log(container);
	</script>

	<!-- No Javascript Message -->
	<noscript>
        Please enable Javascript on this webpage!
	</noscript>
</body>
</html>
"""

import sys
import os
from datetime import date, datetime

jquery_src = r'<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>'

sys_info = sys.version.split(' ')

# Info #1: Python Version
python_ver = sys_info[0]

# Info #2: Username/Name
username = ""

# Info #3: Date
date_today = date.today().strftime("%B %d, %Y")

# Info #4: Time
time_now = datetime.today().strftime("%H:%M:%S")

# Info #5: Year
year = date.today().year

# Info #6: Title
page_title = ""

# Info #7: Internal CSS
internal_css = r"""@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');
		* {
			margin: 0;
			padding: 0;
			box-sizing: border-box;
		}
        .container {
			width: 100vw;
			height: 100vh;
			background: #bdbdbd;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
		}
		@keyframes rotate {
			from { transform: rotateX(0deg); }
			to { transform: rotateX(359deg); }
		}
		img {
			width: 180px;
			animation: rotate 30s infinite;
		}
		p {
			display: block;
			margin-top: 10px;
			width: 280px;
			font-family: 'Libre Baskerville', serif;
			font-size: 18px;
			text-align: center;
		}"""

# Info #8: jQuery?
jquery_res = r''

	
# HTML parser function
def html_parser(username: str, page_title: str, want_jquery: bool):
    global jquery_res
    
    if want_jquery:
        jquery_res = jquery_src

    return html.format(
		python_ver, 
		username, 
		date_today, 
		time_now, 
		year, 
		page_title, 
		internal_css,
		jquery_res
	)
