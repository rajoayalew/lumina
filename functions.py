import subprocess

command = subprocess.check_output(["xrandr", "--listmonitors"])
command = str(command)

location = command.find(":")
number = int(command[location + 2])

monitors = []

def numMonitors():   
    return number
    
def listMonitors():
    
    for monNumber in range(0, number):
        preloc = command.find("{}:".format(monNumber))

        plusStart = command.find("+", preloc) 

        if command[plusStart + 1] == "*":
            plusStart += 2
        else:
            plusStart += 1

        space = command.find(" ", plusStart)

        displayName = command[plusStart:space]
        monitors.append(displayName)
    
    return (monitors)

def getBrightness(monitor):
    verbose = subprocess.check_output(["xrandr", "--verbose"])
    verbose = str(verbose)

    location = verbose.find(monitor)
    brightness = verbose.find("Brightness: ", location)
    brightness += 12
    space = verbose.find("tClones", brightness) - 3
    value = float(verbose[brightness:space])

    return value

#listMonitors()
# = getBrightness(monitors[0])
#print (x)




