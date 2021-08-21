import os,time
filedir_0 = '/volume1/surveillance/xiaomi_camera_videos/'
for a in os.listdir(filedir_0):
    filedir_1 = filedir_0 + a + '/'
    for b in os.listdir(filedir_1):
        if len(b) == 9:
            delete_dir = b + '/'
            os.system("rm -rf %s" %(delete_dir,))
        if len(b) == 10 and int(time.strftime("%Y%m%d", time.localtime())) > int(b[:-2]):
            filedir_2 = filedir_1 + b + '/'
            filedir_3 = filedir_2[:-3] + '/'
            if not os.path.exists(filedir_3):
                os.mkdir(filedir_3)
            os.system("cd %s; find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy %s.mkv; mv %s.mkv %s ; rm -rf %s" %(filedir_2,b,b,filedir_3,filedir_2))
#没有排序
    for c in os.listdir(filedir_1):
        if len(c) == 8:
            filedir_4 = filedir_1 + c + '/'
            os.system("find *.mkv | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy %s.mkv; mv %s.mkv /volume1/surveillance/xiaomi_camera_videos/allvideo/; rm -rf %s" %(c,c,filedir_4))
            #没有排序