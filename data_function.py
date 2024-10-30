import mysql.connector
from mysql.connector import RefreshOption
import openpyxl



class Segment:
    def __init__(self, segment_ID, time, speed, angle, exercise_ID,direction):
        self.segment_ID = segment_ID
        self.time = time
        self.speed = speed
        self.angle = angle
        self.exercise_ID = exercise_ID
        self.direction = direction

class exercise:
    def __init__(self, exercise_ID, exercise_name, description, time):
        self.exercise_ID = exercise_ID
        self.exercise_name = exercise_name
        self.description = description
        self.time = time





def connect_myc():
    db = mysql.connector.connect(
     host="localhost",
    user="root",
    passwd="1995",
    database="dfg"
    )
    refresh = RefreshOption.LOG
    db.cmd_refresh(refresh)
    myc = db.cursor()
    return db, myc


def get_exercise_progrems(myc, exercise_ID): # get the exercise progrems from the database

    myc.execute( f"SELECT * FROM exercise_sement WHERE exercise_ID = {exercise_ID} ORDER BY segment_time")    
    myresult = myc.fetchall()
    Segment_list = []
    for row in myresult:
        s = Segment(row[0], row[1], row[2], row[3], row[4], row[5])
        Segment_list.append(s)
        #print("ID", segment.segment_ID,"time", segment.time,"speed", segment.speed,"angle", segment.angle,"exercise_ID",  segment.exercise_ID,"direction",  segment.direction)
    myc.execute( f"SELECT * FROM exercise_progrems WHERE exercise_ID = {exercise_ID}")
    myresult = myc.fetchall()

    exercise_progrem = exercise(myresult[0][0], myresult[0][1], myresult[0][2], myresult[0][3])
    print("ID", exercise_progrem.exercise_ID,"name", exercise_progrem.exercise_name,"description", exercise_progrem.description,"time",  exercise_progrem.time)

    return Segment_list, exercise_progrem



def calibrate_body_angle(sheet):
    # take all the angel of the body from the exel file and calculate the average
    shoulder = []
    torso_RL = []
    torso_BF = []
    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=2, max_col=4, values_only=True):
        shoulder.append(row[0])
        torso_RL.append(row[1])
        torso_BF.append(row[2])
    # calculate the average of the angel
    shoulder_avg = sum(shoulder) / len(shoulder)
    torso_RL_avg = sum(torso_RL) / len(torso_RL)
    torso_BF_avg = sum(torso_BF) / len(torso_BF)
    return shoulder_avg, torso_RL_avg, torso_BF_avg


def create_chart(sheet):
        #create the chart in the excel file time will be the x axis and the angel will be the y axis
    chart = openpyxl.chart.LineChart()
    chart.style = 13
    chart.y_axis.title = "Angel"
    chart.x_axis.title = "Time"
    chart.title = "Angel over time"
    data = openpyxl.chart.Reference(sheet, min_col=2, min_row=1, max_row=sheet.max_row, max_col=6)
    chart.add_data(data, titles_from_data=True)
    sheet.add_chart(chart, "F1")
