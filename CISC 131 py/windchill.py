def windChill():
    """
    This function computes and prints a table
    showing the windchill index.
    """
    #first print the first line
    print(" ", end="")
    for temp in range(-40, 60, 10):
        #if temp == 0:
            #print(" ", end="")
        #elif temp > -10:
            #print(" ", end="")
        #print("   ", temp, end="")
        print("{:7d}".format(temp), end="")

    #print the rest of the lines
    print(" ")
    for wind_speed in range(5, 55, 5):
        #print the wind speed
        #if wind_speed < 10:
            #print(" ", end="")
        #print(wind_speed, end=" ")
        print("{:2d}".format(wind_speed), end="")

        #print the windchill values for each temperature
        for temp in range(-40, 60, 10):
            wind_power = wind_speed ** 0.16
            windchill = 35.74 + 0.6215*temp - 35.75*(wind_power)+0.4275*temp*wind_power
            #windchill = int(windchill*10)/10
            #if windchill > 0:
                #print(" ", end="")
            #if windchill > -10 and windchill < 10:
                #print(" ", end="")
            #print("",windchill, end=" ")
            print("{:7.1f}".format(windchill), end="")
        print("")

windChill()
