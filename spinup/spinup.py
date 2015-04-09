#!/usr/bin/env python

import subprocess
import os
import shutil
import time

#basinPrefix = "CRB_"
#basinPrefix = "HJA_"
basinPrefix = "WCOR_"
basinId = "1"
#rawDataFilename = basinPrefix+basinId+"_grow_basin.daily"
combinedDataFilename = basinPrefix+"combined_growth_daily_"+basinId
worldfileName =  basinPrefix+"world_"+basinId
worldfileHeader = basinPrefix+"world_"+basinId+".hdr"
flowtableName = basinPrefix+"flowtable_"+basinId+".flow"

startyear = "1980"
startmonth = "1" 
startday = "1"
starthour = "1"
startdate = startyear+" "+startmonth+" " + startday + " " +starthour

endyear = "2012"
endmonth = "12"
endday = "31"
endhour = "24"
enddate = endyear+" "+endmonth+" " + endday + " " +endhour

statedumpYear = "2012"
statedumpMonth = "12"
statedumpDay = "31"
statedumpHour = "23"
statedumpDate = "2012 12 31 23"
prefix = basinPrefix+basinId

statedumpTimestamp = "Y"+statedumpYear+"M"+statedumpMonth+"D"+statedumpDay+"H"+statedumpHour

iteration_counter = 0

loop = True
while (True):
	#loop = False
	#run the model
	rhessysCommand = "nice rhessys5.19 -t ../tecfiles/tec.clim -w ../world/" + \
			worldfileName + " -whdr ../world/"+worldfileHeader+" -st "+startdate +  \
			" -ed " + enddate + " -pre ../out/"+prefix+" -r ../flow/"+flowtableName + \
			" -gw 0.0 1.0 -netcdfgrid  -b -g -s 1 10"
	#subprocess here
	subprocess.call(rhessysCommand, shell=True)
	
	
#HJA_world_1
#HJA_world_1.state [rename to HJA_world_1_state1]
#
#HJA_world_1_state1
#HJA_world_1_state1.state [rename to HJA_world_1_state2]
#
#HJA_world_1_state2
#HJA_world_1_state2.state [rename to HJA_world_1_state3]
	
	statefileName = worldfileName+"."+statedumpTimestamp+".state"
	renamedStatefileName = basinPrefix+basinId+"_state"+str(iteration_counter)
	print "Statefile: "+"../world/"+statefileName+"\n"
	print "Renamed: "+"../world/"+renamedStatefileName+"\n"
	os.rename("../world/"+statefileName, "../world/"+renamedStatefileName)
	worldfileName=renamedStatefileName
	
	#combine outputs
	
	rawDataFilename = basinPrefix+basinId+"_grow_basin.daily"
	combineFile = open("../out/"+combinedDataFilename, "a")
	currentFile = open("../out/"+rawDataFilename, "r")
	firstLine = True
	
	line_counter = 0;
	
	for line in currentFile:
		#skip the header line if this isn't the first file
		line_counter = line_counter + 1		
		if (line_counter == 1 and iteration_counter > 0):
			continue
			
		combineFile.write(line)

		
	
	
	currentFile.close()
	combineFile.close()
	printHeader = False #we've finished reading at least one file, so all others are not first file.
	
	#run r script
	print "running r: Rscript /home/cee-user/RHESSysScripts/spinup/cnstoregrapher.r ../out/"+combinedDataFilename + " ../out/"+basinPrefix+"spinupplot_"+basinId+str(iteration_counter)+".pdf"+ "\n"
	rCommand = "Rscript /home/cee-user/RHESSysScripts/spinup/cnstoregrapher.r ../out/"+combinedDataFilename + " ../out/"+basinPrefix+"spinupplot_"+basinId+str(iteration_counter)+".pdf"
	subprocess.call(rCommand, shell=True)
	
	
	iteration_counter = iteration_counter + 1
	
	
