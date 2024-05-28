# Forza Telemetry Data Monitor
Listen for UDP telemetry data from Forza Motorsport 2023 and display in real time.

I'm just messing around, and you should [check out other people's repositories](https://github.com/search?q=forza+telemetry+stars%3A%3E0&type=repositories&s=updated&o=desc) that may have actual usable applications that make use of the Forza telemetry.

# To do
* Look through the available telemetry data and choose more data points that I would like to display
* Break into separate files; before trying to do any kind of real GUI, separate terminal windows could display different data points
* Create a simple GUI
* GUI customizations: ability to toggle individual parts on and off
* GUI customizations: change display qualities - e.g. sizes and positions of individual elements, choice to display numerals or bar or radial gauge etc?

# Attributions
* [theRTB/ForzaGUI](https://github.com/theRTB/ForzaGUI) - I used the "ForzaDataPacket" class defined in 'fdp.py' to help with parsing and outputting the desired attributes from the received packets.

# External links
* [Forza Motorsport "Data Out" Documentation](https://support.forzamotorsport.net/hc/en-us/articles/21742934024211-Forza-Motorsport-Data-Out-Documentation)
