from flask import Flask,jsonify
import socket
import os

hostname = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
cpu = os.cpu_count()
mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
mem= mem_bytes/(1024*3)
hostname = hostname +" ip is : "+ str(ip) +" cpu is : " + str(cpu) + " memory is : " + str(mem)

app= Flask(__name__)

@app.route("/")

def hello():
	return jsonify ("hostname is: %s " %hostname)
	
