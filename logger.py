from datetime import datetime
import sys
import os
import re
'''
This is the logger class of type singleton. It will log by default to the directory set under the config.json file.
If the log directory does not exist, it will be created under the application folder.
'''
class logger(object):

    __instance = None

    #This is the log level for each log message
    logLevel = ["Severe", "Warning", "Info"]

    def __new__(cls, path):
        if logger.__instance is None:
            logger.__instance = object.__new__(cls)
        return logger.__instance

    def __init__(self, path):
        #Create the name of the log file
        date = datetime.now()
        logName = "scraper_logs_" + date.strftime('%d-%m-%Y') + ".txt"
        #Open/create a log file under the current directory with the specified path
        if path is not None:
            #Check if the path value is valid and if it exists
            try:
                os.makedirs(path)
            except OSError:
                if not os.path.isdir(path):
                    raise
            #Try to make or open the log file in the directory
            try:
                __logFile = open(path, "a+")
                #Successfully opened the log file
                return
            except IOError as e:
                print "There was an error opening the file at location : " + path
                print "IOError({0}): {1}".format(e.errno, e.strerror)
            except :
                print "Unexpected error:", sys.exc_info()[0]
                raise

        #Open a log file under the default location with the date in the name
        print "Attempting to open a new log file at location /logs/" + logName
        try:
            __logFile = open("~/logs"+logName, "a+")
        except IOError:
            print "There was an error opening the file at location : " + logName
            print "IOError ({0}): {1}".format(e.errno, e.strerror)
            raise
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
            #SHUT DOWN THE SERVER???
        #If we have successfully opened the log file, then we can save the value
        self.__logFile = __logFile

    def log(self, level, module, message):
        if logger.__logFile is None:
            raise loggingException("The log file is not open. Please open another log file or check for any errors when opening your log files"
                                    "including read write permssions")
        if logger.logLevel.__contains__(level):
            self.__logFile.writelines("LogLevel : " + level + " | " + datetime.time() + " | Module : " + message)
        else:
            self.__logFile.writelines("Unknown : " + datetime.time() + " " + message)


class loggingException(object):
    pass

