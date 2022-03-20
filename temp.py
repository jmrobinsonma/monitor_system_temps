import os
import subprocess
from plyer import notification


def temp(args = '-jf'):
	cmd = 'sensors'
	fetch = subprocess.Popen([cmd,args],stdout=subprocess.PIPE)
	output = str(fetch.communicate())
	output = output.split('\n')
	output = output[0].split('\"')
	res = []
	
	for line in output:
		res.append(line.split('\\')[0])

	msg = f"""
{res[21].split(',')[0]}{res[24].split(',')[0]}
{res[5]}{res[10].split(',')[0]}
{res[25].split(',')[0]}{res[28].split(',')[0]}
{res[29].split(',')[0]}{res[32].split(',')[0]}
"""
	notification.notify(
		title = "System Temp",
		message = msg,
		app_icon = "Paomedia-Small-N-Flat-Dashboard-alt.ico",
		timeout = 5,
	)



temp()


