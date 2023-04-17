create database Courtship;

use Courtship;

#drop table HighSchool;
create table HighSchool (
    highschoolid int auto_increment primary key,
    hs_name varchar(50),
    city varchar(50),
    state varchar(50),
    enrollment int,
    conference varchar(50),
    division int, #changed from varchar
    type varchar(50)
)
;

#drop table College
create table College (
    collegeid int auto_increment primary key,
    col_name varchar(50) unique,
    state varchar(50),
    enrollment int,
    conference varchar(50),
    division varchar(50), #changed from varchar
    acceptance_rate double,
    average_gpa double,
    average_sat int
)
;

#drop table Player
create table Player (
    playerid int auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    grade varchar(50),
    age int,
    highschoolid int not null, #foreign key
    sat int,
    act int,
    gpa double,
    email varchar(50),
    constraint fkPlayerHS foreign key (highschoolid) references HighSchool (highschoolid)
                    on update cascade
)
;

#drop table PLayer_Activities
create table Player_Activities (
    playerid int, #foreign key
    activities varchar(50),
    constraint fkPLayerAct foreign key  (playerid) references Player (playerid)
                               on update cascade
)
;

#drop table Player_Interests
create table Player_Interests (
    playerid int not null, #foreign key
    collegeid int not null, #foreign key
    college_name varchar(50) not null, #foreign key
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
    first_name varchar(50),
    last_name varchar(50),
    age int,
    school int,
    email varchar(50),
    constraint fkHSCoachSchool foreign key (school) references HighSchool (highschoolid)
                       on update cascade
)
;

#drop table Col_Coach
create table Col_Coach (
    coachid int auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    age int,
    school int not null, #foreign key
    email varchar(50),
    constraint fkColCoachSchool foreign key (school) references College (collegeid)
                       on update cascade
)
;

#drop table Player_Stats
create table Player_Stats (
    playerid int not null, #foreign key
    position varchar(50),
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
    team varchar(50),
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
    team varchar(50),
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
    first_name varchar(50),
    last_name varchar(50),
    position varchar(50),
    height int,
    weight int,
    grade varchar(50),
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
    first_name varchar(50),
    last_name varchar(50),
    position varchar(50),
    height int,
    weight int,
    grade varchar(50),
    jersey_number int,
    scholarship_type varchar(50),
    constraint fkColRoster foreign key (collegeid) references College (collegeid)
                        on update cascade
)
;

#drop table ScoutingReport
create table ScoutingReport (
    reportid int auto_increment primary key,
    playerid int not null, #foreign key
    comments varchar(500),
    overallgrade int,
    scout_name varchar(50),
    constraint fkScout foreign key (playerid) references Player (playerid)
                            on update cascade
)
;

#drop table HS_Schedule
create table HS_Schedule (
    highschoolid int not null, #foreign key
    game_date datetime unique,
    opponent varchar(50),
    venue varchar(50),
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
    opponent varchar(50),
    venue varchar(50),
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

#insert statements
insert into College
values (1, 'NU', 'MA', 12000, 'CAA', 'I', .08, 3.5, 1450),
       (2, 'CCSU', 'CT', 8000, 'CSA', 'II', .47, 3.1, 1340);

insert into HighSchool
values (1, 'Franklin High', 'Franklin', 'MA', 1400, 'Central MA', 'I', 'Public'),
       (2, 'Ridgefield High', 'Ridgefield', 'CT', 1000, 'Western CT', 'I', 'Public');

insert into Col_Coach
values (1, 'Hubert', 'Robinson', 42, 2, 'robinson.h@ccsu.edu'),
       (2, 'Joseph', 'Aoun', 54, 1, 'aoun.j@northeastern.edu');

insert into Col_Roster
values (2, 'Lawrence', 'Osher', 'Center', 72, 275, 'Junior', 33, 'Full'),
       (2, 'Tony', 'Calderone', 'Point Guard', 83, 140, 'Senior', 11, 'None'),
       (1, 'Derek', 'Joyce', 'Small Forward', 55, 200, 'Sophomore', 25, 'Half'),
       (1, 'Stephanie', 'Yee', 'Power Forward', 88, 200, 'Freshman', 27, 'Full');

insert into Col_Schedule
values (2, '2023-06-07 19:00:00', 'Binghamton University', 'Matthews Arena', 1, 1),
       (2, '2023-06-09 20:00:00', 'UConn University', 'Gampel Pavillion', 0, 0);

Insert into ColTeam_Stats
values (2, 'Central Connecticut State University', 40, 30, 0.8, 10),
       (1, 'Northeastern University', 82, 0, 1.00, 1);

insert into HS_Roster
values (1, 1, 'Derek', 'Joyce', 'G', 72, 150, 'Junior', 12),
       (2, 2, 'Lawrence', 'Osher', 'C', 77, 180, 'Senior', 00);

insert into Player
values (1, 'Derek', 'Joyce', 'Junior', 22, 1, 1510, 36, 4.8, 'djoyce@gmail.com'),
       (2, 'Lawrence', 'Osher', 'Senior', 22, 2, 1600, 2, 5.0, 'losher@yahoo.com');

insert into Col_Visits
values (2, '2023-06-09 20:00:00', 1),
       (2, '2023-06-09 20:00:00', 2);

insert into ScoutingReport
values (1, 1, 'Good Shooter, needs to get stronger. High Basketball IQ', 7, 'Ricardo Rincon'),
      (2, 2, 'Knack for getting to the basket. Well worth a division 1 scholarship', 9, 'Ricardo Rincon');

insert into Player_Stats
values (1, 'PG', 22, 19.6, 4.5, 4.6, 1.1, 1.2, .675, .445, .322),
      (2, 'SF', 21, 16.5, 3.5, 7.7, 2.0, 1.5, .635, .448, .334);

insert into Player_Activities
values (1, 'Chess'),
       (2, 'Hiking');

insert into Player_Interests
values (1, 1, 'NU'),
       (2, 2, 'CCSU');

insert into Media
values (1, LOAD_FILE('/path/to/myfile.jpg')),
       (1, LOAD_FILE('/path/to/myfile.png'));

insert into Video
values (1, LOAD_FILE('/path/to/myfile.mp4')),
       (2, LOAD_FILE('/path/to/myfile2.mp4'));

insert into HS_Schedule
values (1, '2023-12-10 19:30:00', 'East Meadow High School', 'East Meadow Gymnasium', 0, 1),
       (1, '2023-07-05 20:30:00', 'Hewlett High School', 'Hewlett Auditorium', 1, 0);

insert into HSTeam_Stats
values (1, 'Franklin High School', 41, 41, 0.5, 5),
       (2, 'Rigdefield High School', 42, 40, 0.51, 4);

insert into HS_Visits
values (1, '2023-12-10 19:30:00', 1),
       (1, '2023-07-05 20:30:00', 2);

insert into HS_Coach
values (1, 'Chris', 'Chambers', 47, 1, 'cchamb6@aol.com'),
       (2, 'Ryan', 'Dust', 31, 2, 'getdust@gmail.com');
