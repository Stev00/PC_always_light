import pyautogui,time,datetime

def main():
    print("Start.")
    n=1
    start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')
    end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '21:59', '%Y-%m-%d%H:%M')
    pyautogui.FAILSAFE = False
    while True:
        xingqi = datetime.datetime.now().weekday() + 1
        now_time = datetime.datetime.now()
        if start_time < now_time < end_time and 1 <= xingqi <= 6:
            x1,y1 = pyautogui.position()
            time.sleep(30)
            x2,y2 = pyautogui.position()
            if x1-x2 == 0 and y1-y2 == 0:
                pyautogui.press('up')
                if n%20==0:
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                n+=1
            else:
                if n%20==0:
                    print('.')
                n+=1
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'waiting time...')
            time.sleep(600)     
if __name__ == '__main__':
    main()
