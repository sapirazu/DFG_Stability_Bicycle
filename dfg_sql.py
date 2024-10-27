import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1995",
    database="dfg"
)

mycursor = db.cursor()

# הכנסת מידע על משתמש
insert_user_query = """
INSERT INTO users (user_id, name, gender, age)
VALUES (%s, %s, %s, %s)
"""
user_data = (209146216, 'roee zehavi', 'm', 26)

# יצירת טבלת משתמש
create_users_table_query = """
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name CHAR(255),
    gender ENUM('m', 'f'),
    age TINYINT
)
"""

# יצירת טבלת אימונים
create_exercise_progrems_table_query = """
CREATE TABLE exercise_progrems (
    exercise_ID INT PRIMARY KEY,
    exercise_name VARCHAR(50),
    description VARCHAR(50),
    time TINYINT
)
"""

# הכנסת מידע על אימון
insert_exercise_query = """
INSERT INTO exercise_progrems (exercise_ID, exercise_name, description, time)
VALUES (%s, %s, %s, %s)
"""
exercise_data = (1, 'gating started', 'first exercise', 10)




# יצירת טבלת היסטורית אימונים
create_exercise_history_table_query = """
CREATE TABLE exercise_history (
    exercise_Number INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    exercise_ID INT,
    score INT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (exercise_ID) REFERENCES exercise_progrems(exercise_ID)
)
"""
#             בחירת ביצוע פעולה- לבחור פעולה ואת להוריד את הערה בשורה למטה
mycursor.execute(create_exercise_history_table_query)
db.commit()
