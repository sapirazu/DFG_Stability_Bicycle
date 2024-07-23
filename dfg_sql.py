import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1995",
    database="dfg"
)

mycursor = db.cursor()

#CREAT DATABASE
# mycursor.execute("CREATE DATABASE DFG")
# # DELETE TABLE
# mycursor.execute("DROP TABLE TrainingSegments")
# mycursor.execute("DROP TABLE TraineeTrainings")
# mycursor.execute("DROP TABLE Trainee")
# mycursor.execute("DROP TABLE Training")

# CREATE TABLE
# mycursor.execute("""
# CREATE TABLE Trainee (
#     traineeID INT PRIMARY KEY,
#     traineeName VARCHAR(50),
#     gender TINYINT,
#     height SMALLINT,
#     weight SMALLINT,
#     diagnosis VARCHAR(255)
# );
# """)

mycursor.execute("""
CREATE TABLE Training (
    trainingTypeID INT PRIMARY KEY AUTO_INCREMENT,
    trainingName VARCHAR(50),
    trainingTime TINYINT,
    description VARCHAR(255)
);
""")

mycursor.execute("""
CREATE TABLE TrainingSegments (
    SegmentID INT PRIMARY KEY AUTO_INCREMENT,
    trainingTypeID INT,
    FOREIGN KEY (trainingTypeID) REFERENCES Training(trainingTypeID),
    segmentTime TINYINT,
    perturbationType TINYINT,
    frequency TINYINT DEFAULT 0,
    degree TINYINT,
    power TINYINT
);
""")

mycursor.execute("""
CREATE TABLE TraineeTrainings (
    trainingNumID INT PRIMARY KEY AUTO_INCREMENT,
    traineeID INT,
    FOREIGN KEY (traineeID) REFERENCES Trainee(traineeID),
    trainingTypeID INT,
    FOREIGN KEY (trainingTypeID) REFERENCES Training(trainingTypeID)
);
""")

mycursor.execute("""
CREATE TABLE TrainingAngleResults (
    trainingNumID INT,
    FOREIGN KEY (trainingNumID) REFERENCES TraineeTrainings(trainingNumID),
    time INT,
    shoulder FLOAT(5,3),
    LR_back FLOAT(5,3),
    FB_back_flat FLOAT(5,3),
    system_pitch INT,
    system_roll INT
);
""")


# trainee
# mycursor.execute("CREATE TABLE Trainee (traineeID int PRIMARY KEY, traineeName VARCHAR(50), gender tinyint, "
#                  "height smallint, weight smallint, diagnosis VARCHAR(255))")
# training
# mycursor.execute("CREATE TABLE Training (trainingTypeID int PRIMARY KEY AUTO_INCREMENT, trainingName VARCHAR(50),"
#                  "trainingTime tinyint, description VARCHAR(255))")
# training segments
# mycursor.execute("CREATE TABLE TrainingSegments (SegmentID int PRIMARY KEY AUTO_INCREMENT,"
#                  " trainingTypeID int, FOREIGN KEY(trainingTypeID) REFERENCES Training(trainingTypeID),"
#                  " segmentTime tinyint, perturbationType tinyint, frequency tinyint DEFAULT 0, degree tinyint,"
#                  " power tinyint)")
# # # trainee trainings
# mycursor.execute("CREATE TABLE TraineeTrainings (trainingNumID int PRIMARY KEY AUTO_INCREMENT,"
#                  " traineeID int, FOREIGN KEY(traineeID) REFERENCES Trainee(traineeID),"
#                  " trainingTypeID int, FOREIGN KEY(trainingTypeID) REFERENCES Training(trainingTypeID))")

# # trainee angle data

# mycursor.execute("CREATE TABLE TrainingAngleResults (trainingNumID int,"
#                  " FOREIGN KEY(trainingNumID) REFERENCES TraineeTrainings(trainingNamID),"
#                  " time int, shoulder float(3,3), L-R back float(3,3), F-B back flat(3,3),"
#                  " system pitch int, system roll int")
# # trainee angle data
# mycursor.execute("CREATE TABLE TrainingPosResults (trainingNumID int,"
#                  " FOREIGN KEY(trainingNumID) REFERENCES TraineeTrainings(trainingNamID),"
#                  " time int, all the pos joints")


# c1 = "SELECT trainingID FROM Training WHERE name = (%s)"
# # c3 = "INSERT INTO TrainingSegments (tID) VALUES (%s)"
# mycursor.execute(c1, ("sv",))

# # GET THE DATA IN TUPLE
# t_name = mycursor.fetchone()
# print(t_name)

# INSERT ROWS
# line = "INSERT INTO Trainee (traineeID, traineeName, gender, height, weight, diagnosis) VALUES (%s, %s, %s, %s, %s, %s)"
# val = [(205915358, "Shoval sade", 0, 152, 51, "she is malca"),
#        (205915359, "Shir bm", 0, 160, 55, "she is exelent"),
#        (205915357, "Matan cs", 1, 180, 70, "he is my boyfriend")]
# mycursor.executemany(line, val)
# db.commit()

# line = "INSERT INTO Training (traineeID, trainingTime, description) VALUES (%s, %s, %s)"
# val = [(205915358, 3, "Roll perturbations\n3 min, P every 30 sec\nEasy level"),
#        (205915359, 2, "Roll perturbations\n2 min, P every 30 sec\nEasy level")]
# # val = [("shalom", 10, "Roll perturbations\n10 min, P every 30 sec\nEasy level")]
# mycursor.executemany(line, val)
# db.commit()

# 'Roll: L-R (random)' -1
# 'Pitch: B-F (random)' -2
# 'Roll & Pitch (random)' -3
# 'Left' -4
# 'Right' - 5
# 'Forward'-6
# 'Backward' -7

# line = "INSERT INTO TrainingSegments (trainingTypeID, segmentTime, perturbationType, frequency, degree, power)" \
#        " VALUES (%s, %s, %s, %s, %s, %s)"
# val = [(1, 1, 5, 30, 8, 1), (1, 1, 4, 30, 8, 1),
#        (2, 1, 1, 30, 8, 3)]
# mycursor.executemany(line, val)
# db.commit()

# line = "INSERT INTO Trainee (traineeName) VALUES (%s)"
# val = ("Sade",)
# mycursor.execute(line, val)
# db.commit()

# # DELETE COLUMN
# mycursor.execute("ALTER TABLE Training DROP name")

# # DELETE ROW
# line = "DELETE FROM TraineeTrainings WHERE traineeID = (%s)"
# mycursor.execute(line, (205915358,))
# mycursor.execute("DELETE FROM Trainee WHERE traineeID = 205346851")
# db.commit()

# # CHANGE COLUMN NAME
# mycursor.execute("ALTER TABLE TrainingSegments CHANGE name new_name TYPE")
# # CHOSE SPECIFIC VAL IN THE SAME ROW
# mycursor.execute("SELECT description FROM Training WHERE name = 'Roll easy'")

# id = open("trainingID.txt", "r")
# trainingID = id.readline()
# print(trainingID)
# id.close()
# lineT = "SELECT * FROM TrainingSegments WHERE trainingTypeID = (%s)"
# mycursor.execute(lineT, (trainingID,))

# trainingTime = mycursor.fetchone()
# print(trainingTime)
# # SELECT ALL ROWS OF THE TABLE
# mycursor.execute("SELECT * FROM TrainingSegments")
# mycursor.execute("SELECT * FROM Training")
# mycursor.execute("SELECT * FROM Trainee")
# SHOW TABLE
# mycursor.execute("SHOW TABLES")
# # JOINTS
# mycursor.execute("SELECT * FROM Training INNER JOIN TrainingSegments ON Training.trainingID = "
#                  "TrainingSegments.trainingID WHERE Training.trainingID = 1")

# mycursor.execute("ALTER TABLE TrainingSegments CHANGE power power smallint")
#
# mycursor.execute("SELECT LAST(traineeID) FROM Trainee")
# SELECT fields FROM table ORDER BY id DESC LIMIT 1;
# mycursor.execute("SELECT MAX(trainingNumID) FROM TraineeTrainings")
# trainingNum = mycursor.fetchone()
# print(trainingNum)
# for row in trainingTable:
#     st = row[2]
#     print(st)
# for row in trainingTable:
#     print(row)
# for x in mycursor:
#     print(x)



# # DELETE TABLE
# mycursor.execute("DROP TABLE Training")
# mycursor.execute("DROP TABLE Training")

# CREATE TABLE
# # training
# mycursor.execute("CREATE TABLE Training (trainingTypeID int PRIMARY KEY AUTO_INCREMENT, traineeID int,"
#                  "FOREIGN KEY(traineeID) REFERENCES Trainee(traineeID), trainingTime tinyint, description VARCHAR(255))")
# # training segments
# mycursor.execute("CREATE TABLE TrainingSegments (SegmentID int PRIMARY KEY AUTO_INCREMENT,"
#                  " trainingTypeID int, FOREIGN KEY(trainingTypeID) REFERENCES Training(trainingTypeID),"
#                  " segmentTime int, perturbationType VARCHAR(50), frequency int DEFAULT 0, degree smallint,"
#                  " power VARCHAR(10))")
# trainee
# mycursor.execute("CREATE TABLE Trainee (traineeID int PRIMARY KEY, traineeName VARCHAR(50), gender tinyint, "
#                  "height smallint, weight smallint, diagnosis VARCHAR(255))")
# # trainee trainings
# mycursor.execute("CREATE TABLE TraineeTrainings (trainingNumID int PRIMARY KEY AUTO_INCREMENT,"
#                  " traineeID int, FOREIGN KEY(traineeID) REFERENCES Trainee(traineeID),"
#                  " trainingTypeID int, FOREIGN KEY(trainingTypeID) REFERENCES Training(trainingTypeID))")

# # trainee angle data
# mycursor.execute("CREATE TABLE TrainingAngleResults (trainingNumID int,"
#                  " FOREIGN KEY(trainingNumID) REFERENCES TraineeTrainings(trainingNamID),"
#                  " time int, shoulder float(3,3), L-R back float(3,3), F-B back flat(3,3), left hand flat(3,3)"
#                  " right hand flat(3,3), system pitch int, system roll int")
# # trainee angle data
# mycursor.execute("CREATE TABLE TrainingPosResults (trainingNumID int,"
#                  " FOREIGN KEY(trainingNumID) REFERENCES TraineeTrainings(trainingNamID),"
#                  " time int, all the pos joints")


# c1 = "SELECT trainingID FROM Training WHERE name = (%s)"
# # c3 = "INSERT INTO TrainingSegments (tID) VALUES (%s)"
# mycursor.execute(c1, ("sv",))

# # GET THE DATA IN TUPLE
# t_name = mycursor.fetchone()
# print(t_name)

# INSERT ROWS
# line = "INSERT INTO Training (trainingName, trainingTime, description) VALUES (%s, %s, %s)"
# # val = [("Roll easy", 10, "Roll perturbations\n10 min, P every 30 sec\nEasy level"),
# #        ("Pitch easy", 10, "Pitch perturbations\n10 min, P every 40 sec\nEasy level"),
# #        ("Roll and Pitch easy", 10, "Roll and Pitch perturbations\n10 min, P every 30 sec\nEasy level")]
# val = [("shalom", 10, "Roll perturbations\n10 min, P every 30 sec\nEasy level")]
# mycursor.executemany(line, val)
# db.commit()

# 'Roll: L-R (random)' -1
# 'Pitch: B-F (random)' -2
# 'Roll & Pitch (random)' -3
# 'Left' -4
# 'Right' - 5
# 'Forward'-6
# 'Backward' -7

# line = "INSERT INTO TrainingSegments (trainingTypeID, segmentTime, perturbationType, frequency, degree, power)" \
#        " VALUES (%s, %s, %s, %s, %s, %s)"
# val = [(1, 2, 5, 30, 4, 1), (1, 2, 4, 30, 4, 1), (1, 4, 1, 30, 6, 1),
#        (2, 2, 7, 40, 4, 1), (2, 2, 6, 40, 4, 1), (2, 2, 1, 30, 6, 1),
#        (3, 2, 1, 30, 4, 1), (3, 2, 1, 30, 4, 1), (3, 2, 1, 30, 6, 1), (3, 2, 1, 30, 6, 1)]
# mycursor.executemany(line, val)
# db.commit()

# line = "INSERT INTO Trainee (traineeName) VALUES (%s)"
# val = ("Sade",)
# mycursor.execute(line, val)
# db.commit()

# # DELETE COLUMN
# mycursor.execute("ALTER TABLE Training DROP name")

# # DELETE ROW
# mycursor.execute("DELETE FROM Training WHERE trainingID = 6")
# db.commit()

# # CHANGE COLUMN NAME
# mycursor.execute("ALTER TABLE TrainingSegments CHANGE name new_name TYPE")
# # CHOSE SPECIFIC VAL IN THE SAME ROW
# mycursor.execute("SELECT description FROM Training WHERE name = 'Roll easy'")
# # SELECT ALL ROWS OF THE TABLE
# mycursor.execute("SELECT * FROM TrainingSegments")
# mycursor.execute("SELECT * FROM Training")
# mycursor.execute("SELECT * FROM Trainee")
# SHOW TABLE
# mycursor.execute("SHOW TABLES")
# # JOINTS
# mycursor.execute("SELECT * FROM Training INNER JOIN TrainingSegments ON Training.trainingID = "
#                  "TrainingSegments.trainingID WHERE Training.trainingID = 1")

# mycursor.execute("ALTER TABLE TrainingSegments CHANGE power power smallint")
#
# mycursor.execute("SELECT LAST(traineeID) FROM Trainee")
# trainingTable = mycursor.fetchall()
# for row in trainingTable:
#     print(row)
# print(trainingTable)
# for x in mycursor:
#     print(x)