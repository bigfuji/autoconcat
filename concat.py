#coding:utf-8
import os,time
#需要修改为通用路径，并且需要创建allvideo目录
filedir_0 = '/volume1/surveillance/xiaomi_camera_videos/'
if not os.path.exists(filedir_0 + 'allvideo' + '/'):
    os.mkdir(filedir_0 + 'allvideo' + '/')
#处理之前错误的mkv格式
for a in os.listdir(filedir_0):
    #以字符串数判断是否为摄像头文件夹
    if len(a) == 12:
        #摄像机目录
        filedir_1 = filedir_0 + a + '/'
        for b in os.listdir(filedir_1):
            #删除此前错误文件夹
            if len(b) == 9:
                delete_dir = filedir_1 + b + '/'
                os.system("rm -rf %s" %(delete_dir,))
            try:
                #确定其为原始录像文件夹，并且非当天文件夹
                if len(b) == 10 and int(time.strftime("%Y%m%d", time.localtime())) > int(b[:-2]):
                    #原始录像文件夹绝对路径
                    filedir_2 = filedir_1 + b + '/'
                    #天录像文件夹绝对路径
                    filedir_3 = filedir_2[:-3] + '/'
                    if not os.path.exists(filedir_3):
                        os.mkdir(filedir_3)
                    #处理排序文件，合成，删除原始录像文件夹
                    os.system("cd %s; ls -1v|sort -V|sed 's/^/file\ /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy %s.mkv; mv %s.mkv %s ; rm -rf %s" %(filedir_2,b,b,filedir_3,filedir_2))
            except Exception as e:
            #排除可能出现的错误，继续执行
                pass
            continue
        for c in os.listdir(filedir_1):
            #确定其为天录像文件夹
            if len(c) == 8:
                #天录像文件夹绝对路径
                filedir_4 = filedir_1 + c + '/'
                os.system("cd %s; ls -1v|sort -V|sed 's/^/file\ /' > fl.txt; ffmpeg -f concat -i fl.txt -c copy %s.mkv; mv %s.mkv %s; rm -rf %s" %(filedir_4,c+'_'+a,c+'_'+a,filedir_0 + 'allvideo' + '/',filedir_4))