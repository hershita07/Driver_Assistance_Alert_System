from sqlite3 import Timestamp
from paramiko import SSHClient
import time
import smtplib
import numpy as np
import telepot
import pandas as pd
import csv
# from datetime import datetime
# current_Date = datetime.now()
########################### TELEGRAM CODE ####################################
token = '5321925220:AAFDs-7abkYehncXazfBVLnfKMncObJMwI8'  # telegram token
receiver_id1 = 1010187491  # https://api.telegram.org/bot<TOKEN>/getUpdates
receiver_id2 = 920295260  # Akshay sir
receiver_id3 = 520788165  # Hershita

bot = telepot.Bot(token)

# bot.sendMessage(receiver_id1, 'hello') # send a activation message to telegram receiver id
# bot.sendMessage(receiver_id2, 'hello i am a bot ')
# bot.sendPhoto(receiver_id, photo=open('test_img.png', 'rb')) # send message to telegram
################################################################################
# Connect
client = SSHClient()
client.load_system_host_keys()
client.connect('192.168.20.102', username='guest', password='cdac@123')

# Run a command (execute PHP interpreter)
stdin, stdout, stderr = client.exec_command('date')
date = stdout.read().decode("utf8")
print(date)
date2 = date.split(' ')

if date2[1] == 'Jan':
    month = '01'
elif date2[1] == 'Feb':
    month = '02'
elif date2[1] == 'Mar':
    month = '03'
elif date2[1] == 'Apr':
    month = '04'
elif date2[1] == 'May':
    month = '05'
elif date2[1] == 'Jun':
    month = '06'
elif date2[1] == 'Jul':
    month = '07'
elif date2[1] == 'Aug':
    month = '08'
elif date2[1] == 'Sep':
    month = '09'
elif date2[1] == 'Oct':
    month = '10'
elif date2[1] == 'Nov':
    month = '11'
elif date2[1] == 'Dec':
    month = '12'
else:
    print("Invalid month")

if len(date2[2]) == 1:
    dt = date2[2].zfill(2)
else:
    dt = date2[2]

data = dt+month+date2[-1]


##############################**ACCESSING DATABASE**###################################################
# import mysql.connector

# def insert_varibles_into_table(Seqno, OBU_ID, RSU_ID,GPS_LAT,GPS_LONG,SPEED, Acc_x, Acc_y, Acc_z, Gyro_x, Gyro_y, Gyro_z,UTCTIME,UTCDATE):
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='V2X',
#                                              user='testuser',
#                                              password='Nitish@22')
#         cursor = connection.cursor()
#         mySql_insert_query = """INSERT INTO OBUDATA (Seqno, OBU_ID, RSU_ID,GPS_LAT,GPS_LONG,SPEED, Acc_x, Acc_y, Acc_z, Gyro_x, Gyro_y, Gyro_z,UTCTIME,UTCDATE)
#                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s) """

#         record = (Seqno, OBU_ID, RSU_ID,GPS_LAT,GPS_LONG,SPEED, Acc_x, Acc_y, Acc_z, Gyro_x, Gyro_y, Gyro_z,UTCTIME,UTCDATE)
#         cursor.execute(mySql_insert_query, record)
#         connection.commit()
#         print("Record inserted successfully into OBUDATA Table")

#     except mysql.connector.Error as error:
#         print("Failed to insert into MySQL table {}".format(error))

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
##########################################################################################


while(1):
    stdin, stdout, stderr = client.exec_command('tail -10 /home/guest/data_logs/data.csv')
    out = stdout.read().decode("utf8")
    time.sleep(4)
    # out2 = out2.remove('''""''')

    print(out)
    with open('/var/www/html/data_raw.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([out])

    with open('/var/www/html/data_raw.csv', 'r') as file:
        filedata = file.read()
        filedata = filedata.replace('''"''', '')

    with open('/var/www/html/data.csv', 'w') as file:
        file.write(filedata)

    df = pd.read_csv('/var/www/html/data.csv', header=None)
    # current_Date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    # df["timestamp"] = current_Date #adding time stamp

    df.rename(columns={0: 'string', 1: 'RSU_id', 2: 'OBU_ID', 3: 'bb', 4: 'string length', 5: 'TIME', 6: 'GPS_RECV', 
    7: 'LAT', 8: 'LONG', 9: 'SPEED', 10: 'TRACK', 11: 'Ax',12: 'Ay',13: 'Az',
    14: 'Gx', 15: 'Gy', 16: 'Gz', 17: 'UTCDATE', 18: 'SEQNO', 19: 'X',20:'Y',21:'Z',22:'EMR_STATUS',23:'timestamp',24:'CHECKSM'}, inplace=True)

    
    # df["timestamp"] = current_Date #adding time stamp
    # current_Date = datetime.now()

    print(df)
    df.to_csv('/var/www/html/data3.csv', index=False)

    

stdin.close()
stdout.close()
stderr.close()

client.close()
