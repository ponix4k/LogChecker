#/usr/bin/python3
from datetime import datetime,timedelta
import yaml

def get_settings():
    with open("settings.yaml","r") as file:
        settings = yaml.full_load(file)
        return settings

def get_yesterday():
    today = datetime.now()
    yesterday = (today - timedelta(days=1)).strftime('%Y%m%d')
    return yesterday

def count_errors_in_log(file_path):
    errorcount = 0
    print(file_path)
    with open(file_path,"r",encoding="utf-8") as log:
        for line in log:
            if "error" in line.lower():
                errorcount +=1
    return errorcount

def has_finished(file_path):
    finished = False
    with open(file_path,"r",encoding="utf-8")as log:
        for line in log:
            if "finished" in line.lower():
                finished = True
    return finished

def check_logs(logs,log_dir):
    yesterday = get_yesterday()
    for log in logs:
        logPath = "{0}{1}{2}.log".format(log_dir,log,yesterday)
        print("there are {0} errors in {1}".format(count_errors_in_log(logPath),log))
        with open("dailylog.log"+a)

        if has_finished(logPath) == True:
            print("{0} run has finished".format(log))
        else:
            print ("{0} run is incomplete".format(log))

#def write_to_dailylog():

def main():
    settings = get_settings()
    logs = settings["logs"]
    log_dir = settings["logdir"]
    check_logs(logs,log_dir)

if __name__ == "__main__":
    main()