from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

collegeCoach = Blueprint('collegeCoach', __name__)

# Create the profile for a certain coach
@collegeCoach.route('/coachProfile', methods=['POST'])
def create_coachProfile():
    
    # access json data from request object

    req_data = request.get_json()

    first_name = req_data['first_name']
    last_name = req_data['last_name']
    age = req_data['age']
    email = req_data['email']
    school = req_data['school']

    # construct the insert statement

    insert_statement = 'INSERT INTO Col_Coach (first_name, last_name, age, email, school) VALUES (\''
    insert_statement += first_name + '\', \'' + last_name + '\', ' + str(age) + ', \'' + email + '\', ' + str(school) + ');'

    current_app.logger.info(insert_statement)

    # execute query

    cursor = db.get_db().cursor()
    cursor.execute(insert_statement)
    db.get_db().commit()
    return "Coach Profile successfully created"

@collegeCoach.route('/ScoutingReport', methods=['POST'])
def create_ScoutingReport():
    
    # access json data from request object

    req_data = request.get_json()

    playerid = req_data['playerid']
    comments = req_data['comments']
    overallgrade = req_data['overallgrade']
    scout_name = req_data['scout_name']

    # construct the insert statement

    insert_statement = 'INSERT INTO ScoutingReport (playerid, comments, overallgrade, scout_name) VALUES ('
    insert_statement += str(playerid) + ", '" + comments + "', " + str(overallgrade) + ", '" + scout_name + "');"

    current_app.logger.info(insert_statement)

    # execute query

    cursor = db.get_db().cursor()
    cursor.execute(insert_statement)
    db.get_db().commit()
    return "Scouting Report successfully created"

# Retrieve the scouting report based on the given reportID
@collegeCoach.route('/ScoutingReport', methods=['GET'])
def get_ScoutingReport():

    cursor = db.get_db().cursor()

    # Construct the query

    query = "SELECT playerid, comments, overallgrade, scout_name FROM ScoutingReport;"

    # use cursor to query the database for the player profile that has an ID that matches the given ID
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

    
# Delete the coach profile for a certain coach
@collegeCoach.route('/coachProfile/<coachID>', methods=['DELETE'])
def delete_coachProfile(coachID):
    
    # query to delete the player with the corresponding id from the table 
    delete_statement = 'DELETE FROM Col_Coach WHERE coachid = ' + coachID + ';'
    
    # execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_statement)
    db.get_db().commit()

    return "Coach Profile successfully deleted"

# Delete the roster for a certain college
@collegeCoach.route('/roster/<collegeid>', methods=['DELETE'])
def delete_roster(collegeid):
    # Construct delete statement
    delete_statement = 'DELETE FROM Col_Roster WHERE collegeid = ' + collegeid + ';'

    # Execute delete statement
    cursor = db.get_db().cursor()
    cursor.execute(delete_statement)
    db.get_db().commit()

    return "Roster for college successfully deleted"


# Retrieve all rosters for all college teams
@collegeCoach.route('/roster', methods=['GET'])
def get_roster():

    cursor = db.get_db().cursor()

    # Construct the query

    query = "SELECT collegeid, first_name, last_name, position, height, weight, grade, jersey_number, scholarship_type FROM Col_Roster;"

    # use cursor to query the database for the player profile that has an ID that matches the given ID
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




# Retrieve the profile for a certain player so a coach can view their information
@collegeCoach.route('/PlayerProfile/<PlayerID>', methods=['GET'])
def get_PlayerProfile(PlayerID):
    cursor = db.get_db().cursor()

    query = "SELECT first_name, last_name, grade, age, highschoolid, sat, act, gpa, email FROM Player WHERE playerid = " + PlayerID + ";"

    # use cursor to query the database for the player profile that has an ID that matches the given ID
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

# Retrieve the stats for a certain player so a coach can view their information
@collegeCoach.route('/PlayerStats/<PlayerID>', methods=['GET'])
def get_PlayerStats(PlayerID):
    cursor = db.get_db().cursor()

    select_statement = "SELECT playerid, position, gps, ppg, apg, rpg, bpg, spg, ft_percentage, fg_percentage, threept_percentage FROM Player_Stats WHERE playerid = " + PlayerID + ";"

    # use cursor to query the database for the player stats that has an ID that matches the given ID
    cursor.execute(select_statement)

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

@collegeCoach.route('/ColTeam_Stats/<collegeid>', methods=['PUT'])
def update_team_stats(collegeid):
    req_data = request.get_json()

    # Extract values from the request body
    team = req_data['team']
    wins = req_data['wins']
    losses = req_data['losses']
    ranking = req_data['ranking']

    # Construct the update statement
    update_statement = "UPDATE ColTeam_Stats SET "
    
    if (team):
        update_statement += "team = \'" + team + "\', "
    if (wins):
        update_statement += "wins = " + str(wins) + ", "
    if (losses):
        update_statement += "losses = " + str(losses) + ", "
    if (ranking):
        update_statement += "ranking = " + str(ranking) + ", "

    # need to get rid of the last comma and space if that's the end of the set
    update_statement = update_statement[:- 2]

    update_statement += " WHERE collegeid = " + collegeid + ";"

    # Execute the update statement
    cursor = db.get_db().cursor()
    cursor.execute(update_statement)
    db.get_db().commit()

    # Return a success message
    return f"Team stats for college {collegeid} updated successfully."

@collegeCoach.route('/colRoster/<collegeid>', methods=['PUT'])
def update_college_roster(collegeid):
    req_data = request.get_json()

    # Extract values from the request body
    first_name = req_data['first_name']
    last_name = req_data['last_name']
    position = req_data['position']
    height = req_data['height']
    weight = req_data['weight']
    grade = req_data['grade']
    jersey_number = req_data['jersey_number']
    scholarship_type = req_data['scholarship_type']

    # Construct the update statement

    update_statement = "UPDATE Col_Roster SET "

    if (first_name):
        update_statement += "first_name = \'" + first_name + "\', "
    if (last_name):
        update_statement += "last_name = \'" + last_name + "\', "
    if (position):
        update_statement += "position = \'" + position + "\', "
    if (height):
        update_statement += "height = " + str(height) + ", "
    if (weight):
        update_statement += "weight = " + str(weight) + ", "
    if (grade):
        update_statement += "grade = \'" + grade + "\', " 
    if (jersey_number):
        update_statement += "jersey_number = " + str(jersey_number) + ", "
    if (scholarship_type):
        update_statement += "scholarship_type = \'" + scholarship_type + "\', "
    
    # need to get rid of the last comma and space if that's the end of the set
    update_statement = update_statement[:- 2]

    update_statement += " WHERE collegeid = " + collegeid + ";"

    # Execute the update statement
    cursor = db.get_db().cursor()
    cursor.execute(update_statement)
    db.get_db().commit()

    # Return a success message
    return f"Player for college {collegeid} updated successfully."


