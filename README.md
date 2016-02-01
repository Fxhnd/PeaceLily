# PeaceLily

![Peace Lily](http://images.christmastimeclipart.com/images/2/1263842142136_5/img_1263842142136_51.jpg)

An Arduino powered plant monitoring system. 

## Usage

       usage: Query.py [-h] --port PORT [--file FILE] [--time TIME] [--user USER]
                [--pass USER]

        Monitor your plants!

        optional arguments:
        -h, --help   show this help message and exit
        --port PORT  Serial port connection to arduino
        --file FILE  Local file to save result data
        --time TIME  Interval time for polling for new data
        --user USER  Username for email account
        --pass USER  Password for email account

          
## Installation

### Required Parts
1. Arduino (http://store-usa.arduino.cc/products/a000066)
2. Adafruit HTU21D-F (https://www.adafruit.com/products/1899#tutorials)
3. Adafruit TSL2591  (https://www.adafruit.com/products/1980#tutorials)
4. SparkFun Soil Moisture Sensor (https://www.sparkfun.com/products/13322)

### Wiring Diagram

[Make a picture later]

### Arduino

Make sure to download the following packages and install them before trying to compile the arduino sketch. Instructions for each driver package can be found in their respective README's.
* Adafruit Unified Sensor Driver (https://github.com/adafruit/Adafruit_Sensor)
* Library for the HTU21D-F (https://github.com/adafruit/Adafruit_HTU21DF_Library)
* Library for the TSL2591 (https://github.com/adafruit/Adafruit_TSL2591_Library)

After the sketch is compiled just upload it to your arduino and move on to the next step.

### Python

This module is able to send data to an established plot.ly account for quick visualizations. In order to be able to utilize this feature you will first need create a plot.ly account and setup python to stream data. Thankfully, the people over at plot.ly have documented this process well and a thorough guide can found here, (https://plot.ly/python/user-guide/#Installation-guidelines).

Once that is setup you'll need to edit a couple lines inside the python file _Graph_. Replace the following python list with the stream tokens you created while following the guide on plot.ly. You will need to create four tokens to use this feature.

    tls.set_credentials_file(stream_ids=["A", "list of", "four", "stream tokens"])
    
Once this part is done you should be all set to just run the program.
