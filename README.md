## Overview

Code to provide access to the [UltraGeoPoint](https://ipintelligence.neustar.biz/portal/home#documentation) \(must be logged in\).

To use this code you will need to create a [config.ini](https://en.wikipedia.org/wiki/INI_file#Format) file 
that contains a _GEOPOINT_ section and _api_key_ and _api_secret_ keys.

You can run the code from the command line as follows:

> python ultrageopoint.py IP_ADDRESS [FORMAT]

For example:

> python ultrageopoint.py 8.8.8.8 json