from load_gmat import *
theScript = "ToLuna"
gmat.LoadScript(theScript + ".script")

burn = gmat.GetObject("TOI")
Time = gmat.GetObject("LeoTime")
start = gmat.GetObject("StartEpoch")

print()

closest = 1000000000.0
dt = 4000
dv = 2.9
startTime = 0.0

# Scan through the delta-V using the burn object 
for i in range(10) :
   # Scan through the cost time in low Earth orbit
   for j in range(20) :
      # Scan through the epoch of the insertion state into orbit
      for k in range(25) :
         StartEpoch = k / 2.0
         start.SetField("Value", StartEpoch / 24) 
         Time.SetField("Value", 1500.0 + i * 100) 
         burn.SetField("Element1", 3.0 + j * 0.01) 
         gmat.RunScript()
         MoonDistance = gmat.GetRuntimeObject("MoonDistance")
         theRange = MoonDistance.GetNumber("Value")
         if closest > theRange :
            closest = theRange
            dt = Time.GetNumber("Value")
            dv = burn.GetNumber("Element1")
            startTime = start.GetNumber("Value")
            #launch = time of launch
            #coast time = time spacecraft spent coasting to moon
            #dv = burn requirement 
            #moon distance = final distance to moon (theRange)
            # Report intermediate results if they are better than previous values
            print(closest, "Launch ", startTime, " Coast time: ", dt, "   Delta-V: ", dv, "   Moon Distance: ", theRange)

# build the name for the solution script
theSolution = theScript + "_solution.script"
print("\nSaving solution to ", theSolution, "\n")

# set the values for the best solution found
start.SetField("Value", startTime) 
Time.SetField("Value", dt) 
burn.SetField("Element1", dv) 

gmat.SaveScript(theSolution)
