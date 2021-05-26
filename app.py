########################################################################
# Impoorts Required for Flask Server Functionality
########################################################################
from flask import Flask, render_template, url_for, abort, redirect, request

########################################################################
# Primative and non-Primitve user-data imports for text/database
########################################################################
from data import ServerAccounts, ServerMailing
#from database import database
#from mailing import send_message

########################################################################
# Server Settup / Socket Address Initilization and Referects
########################################################################

#Server-Side Configurations
DEBUG_MODE = False
LIGHT_MODE = True	
CONSTRUCTION_MODE = False
app = Flask(__name__)
accounts = ServerAccounts()
mailing = ServerMailing()

#route a new port for connection to the general domain in the case a connection
#has been made without an intended html file
@app.route('/', methods=['post', 'get'])
def index():
	return render_template('index.html', title='Grackle', sub_title='Official Site', navbar=True, footer=True, under_work = CONSTRUCTION_MODE)

#route a new port for connection to the support page where visitors can either look for
#the repository of pre-asnwered issues and the ability to open chat logs
@app.route('/troubleshooting', methods=['post', 'get'])
def troubleshooting():
	return render_template('troubleshooting.html', title='Grackle', sub_title='Find a Solution', navbar=True, footer=True, under_work = CONSTRUCTION_MODE)

#route a new port for connection to the signup page for creating new accounts on the 
#manakin platform for encrypted message communication
@app.route('/login', methods=['post', 'get'])
def signup():
	return render_template('login.html', title='Grackle', sub_title='Welcome Back', navbar=False, footer=False, under_work = CONSTRUCTION_MODE)

#in the case the user has typed a sub-address that does not exist direct them to a
#cannot be found page | once again we start by routing a new port for connection
@app.errorhandler(404)
def handle(error):
	return render_template('unkownaddr.html', title='Grackle', sub_title="Something's not Right", navbar=False, footer=False, under_work = CONSTRUCTION_MODE)
	
#we only want to run this server from this file, only during the build-phase should we have
#debugging turned on which will automaticly update the page on commit
if __name__ == "__main__":
	app.run(debug=DEBUG_MODE, host='0.0.0.0')
