from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


players = Blueprint('players', __name__)

# Create the profile for a certain player
@players.route('/playerProfile', methods=['POST'])
def create_playerProfile():
    
    # access json data from request object

    req_data = request.get_json()

    first_name = req_data['first_name']
    last_name = req_data['last_name']
    grade = req_data['grade']
    age = req_data['age']
    highschoolid = req_data['highschoolid']
    sat = req_data['sat']
    act = req_data['act']
    gpa = req_data['gpa']
    email = req_data['email']

    # construct the insert statement

    insert_statement = 'INSERT INTO Player (first_name, last_name, grade, age, highschoolid, sat, act, gpa, email) VALUES (\''
    insert_statement += first_name + '\', \'' + last_name + '\', \'' + grade + '\', ' + str(age) + ', ' + str(highschoolid) + ', '
    insert_statement += str(sat) + ', ' + str(act) + ', ' + str(gpa) + ', \'' + email + '\');'


    # execute query

    cursor = db.get_db().cursor()
    cursor.execute(insert_statement)
    db.get_db().commit()
    return "Player Profile successfully created"


# Update the player profile for a certain player
@players.route('/playerProfile/<playerID>', methods=['PUT'])
def update_playerProfile(playerID):
    
    # access json data from request object

    req_data = request.get_json()

    first_name = req_data['first_name']
    last_name = req_data['last_name']
    grade = req_data['grade']
    age = req_data['age']
    highschoolid = req_data['highschoolid']
    sat = req_data['sat']
    act = req_data['act']
    gpa = req_data['gpa']
    email = req_data['email']

    # construct the update statement

    update_statement = "UPDATE Player SET "

    # need to see which attributes the user wants to update

    if (first_name):
        update_statement += "first_name = \'" + first_name + "\', "
    if (last_name):
        update_statement += "last_name = \'" + last_name + "\', "
    if (grade):
        update_statement += "grade = \'" + grade + "\', "
    if (age):
        update_statement += "age = " + str(age) + ", "
    if (highschoolid):
        update_statement += "highschoolid = " + str(highschoolid) + ", "
    if (sat):
        update_statement += "sat = " + str(sat) + ", "
    if (act):
        update_statement += "act = " + str(act) + ", "
    if (gpa):
        update_statement += "gpa = " + str(gpa) + ", "
    if (email):
        update_statement += "email = \'" + email + "\', "
    
    # need to get rid of the last comma and space if that's the end of the set
    update_statement = update_statement[:- 2]

    update_statement += " WHERE playerid = " + playerID + ";"
    current_app.logger.info(update_statement)

    # execute the update query
    
    cursor = db.get_db().cursor()
    cursor.execute(update_statement)
    db.get_db().commit()

    # query the database to return all the info for the updated player
    query = "SELECT first_name, last_name, grade, age, highschoolid, sat, act, gpa, email FROM Player WHERE playerid = " + playerID + ";"

    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    

    return jsonify(json_data)

# Retrieve the information of all other players
@players.route('/playerProfile', methods=['GET'])
def get_allPlayers():
    cursor = db.get_db().cursor()

    query = "SELECT playerid, first_name, last_name, grade, age, highschoolid, sat, act, gpa, email FROM Player;"

    # use cursor to query the database for the coach profile that has an ID that matches the given ID
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)



# Delete the player profile for a certain player
@players.route('/playerProfile/<playerID>', methods=['DELETE'])
def delete_playerProfile(playerID):
    
    # query to delete the player with the corresponding id from the table 
    delete_statement = 'DELETE FROM Player WHERE playerid = ' + playerID + ';'
    
    # execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_statement)
    db.get_db().commit()

    return "Player Profile successfully deleted"

# Retrieve the profile for a certain coach so a player can view their information
@players.route('/coachProfile/<CCoachID>', methods=['GET'])
def get_collegeCoachProfile(CCoachID):
    cursor = db.get_db().cursor()

    query = 'SELECT first_name, last_name, age, school, email FROM Col_Coach WHERE coachid = ' + CCoachID + ';'

    # use cursor to query the database for the coach profile that has an ID that matches the given ID
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Retrieve a list of all colleges that are currently recruiting
@players.route('/colleges', methods=['GET'])
def get_colleges():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of college names
    cursor.execute('SELECT col_name, conference, division FROM College')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# Retrieve the profile of a certain college
@players.route('/collegeProfile/<collegeID>', methods=['GET'])
def get_collegeProfile(collegeID):
    cursor = db.get_db().cursor()

    query = 'SELECT col_name, state, enrollment, conference, division, acceptance_rate, average_gpa, average_sat FROM College WHERE collegeid = ' + collegeID + ';'

    # use cursor to query the database for the college profile that has an ID that matches the given ID
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# Retrieve the schedule of upcoming games for a certain college
@players.route('/schedule/<collegeID>', methods=['GET'])
def get_collegeSchedule(collegeID):
    cursor = db.get_db().cursor()

    query = 'SELECT game_date, opponent, venue, isdivision, isconference FROM Col_Schedule WHERE collegeid = ' + collegeID + ';'

    # use cursor to query the database for the college schedule for a college that has an ID that matches the given ID
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Retrieve the roster of a certain college's basketball team
@players.route('/roster/<collegeID>', methods=['GET'])
def get_collegeRoster(collegeID):
    cursor = db.get_db().cursor()

    query = 'SELECT first_name, last_name, position, height, weight, grade, jersey_number, scholarship_type FROM Col_Roster WHERE collegeid = ' + collegeID + ';'

    # use cursor to query the database for the college roster for a college that has an ID that matches the given ID
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

