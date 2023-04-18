create database Courtship2;

use Courtship2;

#drop table HighSchool;
create table HighSchool (
    highschoolid int auto_increment primary key,
    hs_name varchar(500),
    city varchar(500),
    state varchar(500),
    enrollment int,
    conference varchar(500),
    division varchar(500), #changed from varchar
    type varchar(500)
)
;

#drop table College
create table College (
    collegeid int auto_increment primary key,
    col_name varchar(500) unique,
    state varchar(500),
    enrollment int,
    conference varchar(500),
    division varchar(500), #changed from varchar
    acceptance_rate double,
    average_gpa double,
    average_sat int
)
;

#drop table Player
create table Player (
    playerid int auto_increment primary key,
    first_name varchar(500),
    last_name varchar(500),
    grade varchar(500),
    age int,
    highschoolid int not null, #foreign key
    sat int,
    act int,
    gpa double,
    email varchar(500),
    constraint fkPlayerHS foreign key (highschoolid) references HighSchool (highschoolid)
                    on update cascade
)
;

#drop table PLayer_Activities
create table Player_Activities (
    playerid int, #foreign key
    activities varchar(500),
    constraint fkPLayerAct foreign key  (playerid) references Player (playerid)
                               on update cascade
)
;

#drop table Player_Interests
create table Player_Interests (
    playerid int not null, #foreign key
    collegeid int not null, #foreign key
    college_name varchar(500) not null, #foreign key
    constraint fkPlayerInt foreign key (playerid) references Player (playerid)
                              on update cascade,
    constraint fkPlayerIntColId foreign key (collegeid) references College (collegeid)
                              on update cascade,
    constraint fkPlayerIntColName foreign key (college_name) references College (col_name)
                              on update cascade
)
;

#drop table HS_Coach
create table HS_Coach (
    coachid int auto_increment primary key,
    first_name varchar(500),
    last_name varchar(500),
    age int,
    school int,
    email varchar(500),
    constraint fkHSCoachSchool foreign key (school) references HighSchool (highschoolid)
                       on update cascade
)
;

#drop table Col_Coach
create table Col_Coach (
    coachid int auto_increment primary key,
    first_name varchar(500),
    last_name varchar(500),
    age int,
    school int not null, #foreign key
    email varchar(500),
    constraint fkColCoachSchool foreign key (school) references College (collegeid)
                       on update cascade
)
;

#drop table Player_Stats
create table Player_Stats (
    playerid int not null, #foreign key
    position varchar(500),
    gps int,
    ppg double,
    apg double,
    rpg double,
    bpg double,
    spg double,
    ft_percentage double,
    fg_percentage double,
    threept_percentage double,
    constraint fkPLayerStats foreign key (playerid) references Player (playerid)
                          on update cascade
)
;

#drop table Media
create table Media (
    playerid int not null, #foreign key
    media mediumblob,
    constraint fkPlayerMedia foreign key (playerid) references Player (playerid)
                   on update cascade
)
;

#drop table Video
create table Video (
    playerid int not null, #foreign key
    video mediumblob,
    constraint fkPlayerVideo foreign key (playerid) references Player (playerid)
                   on update cascade
)
;

#drop table HSTeam_Stats
create table HSTeam_Stats (
    highschoolid int not null, #foreign key
    team varchar(500),
    wins int,
    losses int,
    win_percentage double,
    ranking int,
    constraint fkHSStat foreign key (highschoolid) references HighSchool (highschoolid)
                          on update cascade
)
;

#drop table ColTeam_Stats
create table ColTeam_Stats(
    collegeid int not null, #foreign key
    team varchar(500),
    wins int,
    losses int,
    win_percentage double,
    ranking int,
    constraint fkColStat foreign key (collegeid) references College (collegeid)
                          on update cascade
)
;

#drop table HSRoster
create table HS_Roster (
    highschoolid int not null, #foreign key
    playerid int not null, #foreign key
    first_name varchar(500),
    last_name varchar(500),
    position varchar(500),
    height int,
    weight int,
    grade varchar(500),
    jersey_number int,
    constraint fkHSRoster foreign key (highschoolid) references HighSchool (highschoolid)
                       on update cascade,
    constraint fkHSRosterPlayer foreign key (playerid) references Player (playerid)
                       on update cascade
)
;

#drop table Col_Roster
create table Col_Roster (
    collegeid int not null, #foreign key
    first_name varchar(500),
    last_name varchar(500),
    position varchar(500),
    height int,
    weight int,
    grade varchar(500),
    jersey_number int,
    scholarship_type varchar(500),
    constraint fkColRoster foreign key (collegeid) references College (collegeid)
                        on update cascade
)
;

#drop table ScoutingReport
create table ScoutingReport (
    reportid int auto_increment primary key,
    playerid int not null, #foreign key
    comments varchar(5000),
    overallgrade int,
    scout_name varchar(500),
    constraint fkScout foreign key (playerid) references Player (playerid)
                            on update cascade
)
;

#drop table HS_Schedule
create table HS_Schedule (
    highschoolid int not null, #foreign key
    game_date datetime unique,
    opponent varchar(500),
    venue varchar(500),
    isdivision boolean,
    isconference boolean,
    constraint fkHSSchedule foreign key (highschoolid) references HighSchool (highschoolid)
                         on update cascade
)
;

#drop table HS_Visits
create table HS_Visits (
    highschoolid int not null, #foreign key
    game_date datetime not null, #foreign key
    collegeid int not null, #foreign key
    constraint fkHSVisit foreign key (highschoolid) references HighSchool (highschoolid)
                       on update cascade,
    constraint fkHSVisitSchedule foreign key (game_date) references HS_Schedule (game_date)
                       on update cascade,
    constraint fkHSVisitCol foreign key (collegeid) references College (collegeid)
                       on update cascade
)
;

#drop table Col_Schedule
create table Col_Schedule (
    collegeid int not null, #foreign key
    game_date datetime unique,
    opponent varchar(500),
    venue varchar(500),
    isdivision boolean,
    isconference boolean,
    constraint fkColShedule foreign key (collegeid) references College (collegeid)
                          on update cascade
)
;

#drop table Col_Visits
create table Col_Visits (
    collegeid int not null, #foreign key
    game_date datetime not null, #foreign key
    playerid int not null, #foreign key
    constraint fkColVisit foreign key (collegeid) references College (collegeid)
                        on update cascade,
    constraint fkColVisitSchedule foreign key (game_date) references Col_Schedule (game_date)
                        on update cascade,
    constraint fkColVisitPlayer foreign key (playerid) references Player (playerid)
                        on update cascade
)
;
