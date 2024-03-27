import os
import pandas as pd
from datetime import date

## specify the directory you saved the data in
LOG_DIR = os.path.join("logs")
LOG_PREFIX = 'predict-'


def update_predict_log(country, y_pred, y_proba, target_date, runtime, model_version, model_version_note, test=False, MODEL_VERSION=0.1):
    """
    update the predict log
    """

    ## print type of log
    print("... updating predict log")
    
    ## get the current date
    today = date.today()
    
    ## name the log file
    log_file = os.path.join(LOG_DIR, "{}-predict-{}-{}.log".format(LOG_PREFIX, today.year, today.month))
    
    ## check if log file exists
    if not os.path.exists(log_file):
        ## create the log file
        with open(log_file, 'w') as outfile:
            outfile.write("date,country,y_pred,y_proba,runtime,model_version,model_note\n")
    
    ## write to the log file
    with open(log_file, 'a') as outfile:
        outfile.write("{},{},{},{},{},{},{}\n".format(
            today, country, y_pred, y_proba, runtime, MODEL_VERSION, model_version_note))
    
    return

def update_train_log(country, date_range, metric, runtime, model_version, model_version_note, test=False, prefix='train-'):
    """
    update the train log
    """

    ## print type of log
    print("... updating train log")
    
    ## get the current date
    today = date.today()
    
    ## name the log file
    log_file = os.path.join(LOG_DIR, "{}-train-{}-{}.log".format(LOG_PREFIX, today.year, today.month))
    
    ## check if log file exists
    if not os.path.exists(log_file):
        ## create the log file
        with open(log_file, 'w') as outfile:
            outfile.write("date,country,date_range,metric,runtime,model_version,model_note\n")
    
    ## write to the log file
    with open(log_file, 'a') as outfile:
        outfile.write("{},{},{},{},{},{},{}\n".format(
            today, country, date_range, metric, runtime, model_version, model_version_note))
    
    return