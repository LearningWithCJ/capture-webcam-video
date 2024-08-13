#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/Carl-Johnson1976
# Telegram: t.me/LearningWithCJ
#

import cv2



dst_path = "D:/your_file_name.avi"
cam = cv2.VideoCapture(0)

if cam.isOpened(): # check webcam is available or not

    resolution = (640, 480)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30
    out = cv2.VideoWriter(dst_path, codec, fps, resolution)

    time = 10 # in seconds
    num_frames = time * fps

    for i in range(num_frames):
        ret, frame = cam.read()
        out.write(frame)

    cam.release()
    out.release()