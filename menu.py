#!/usr/bin/python3
import subprocess
import cgi
print("context-type:text/html")
print()
rec=cgi.FieldStorage()
order=rec.getvalue("ord")
name=rec.getvalue("name")
value=rec.getvalue("val")
order=order.lower();
cmd=""
if not("don't" in order or "do not" in order):
	if "date" in order:
		print("DATE IS:")
		cmd="date"
		print(subprocess.getoutput(cmd))
	elif "cal" in order:
		print("CALENDAR IS:")
		cmd="cal"
		print(subprocess.getoutput(cmd))
	elif "docker" in order:
		if "run" in order:
			if value!=None:
				print("Copy the following container name for future reference:")
				if name==None:
					cmd="sudo docker run -dit {}".format(value)
				else:
					cmd="sudo docker run -dit --name {0} {1}".format(name,value)
			else:
				print("NO IMAGE SPECIFIED")
		elif "start" in order:
			if name!=None:
				cmd="sudo docker start {}".format(name)
			else:
				print("NO CONTAINER SPECIFIED")
		elif "stop" in order:
			if name!=None:
				cmd="sudo docker stop {}".format(name)
			else:
				print("NO CONTAINER SPECIFIED")
		elif "remove" in order or "rm" in order:
			if name!=None:
				cmd="sudo docker rm {}".format(name)
		elif "container" in order:
			cmd="sudo docker ps"
		elif "image" in order:
			cmd="sudo docker images"
		elif "volume" in order:
			cmd="sudo docker volume ls"
		print(subprocess.getoutput(cmd))
	elif "ip" in order or "network" in order or "address" in order:
		print("NETWORK DETAILS ARE:")
		if name!=None:
			cmd="ifconfig {}".format(name)
		else:
			cmd="ifconfig"
		print(subprocess.getoutput(cmd))
	elif "list" in order or "show" in order or "ls" in order:
		if name!=None:
			if value==None:
				cmd="sudo ls {}".format(name)
			elif value=="long":
				cmd="sudo ls -l {}".format(name)
		else:
			if value==None:
				cmd="sudo ls"
			elif value=="long":
				cmd="sudo ls -l"
		print(subprocess.getoutput(cmd))
	elif "present" in order or "directory" in order:
		print("PRESENT WORKING DIRECTORY IS:")
		cmd="pwd"
		print(subprocess.getoutput(cmd))
	elif "storage" in order or "volume" in order:
		print("STORAGE DETAILS ARE:")
		cmd="sudo df -h"
		print(subprocess.getoutput(cmd))
	elif "execute" in order:
		cmd="sudo "+value
		print(subprocess.getoutput(cmd))
