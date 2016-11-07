from datetime import datetime
'''
This is the logger class of type singleton. It will log by default to the directory set under the config.json file
'''
class logger(object):

    __instance = None

    #This is the log level for each log message
    logLevel = ["Severe", "Warning", "Info"]

    def __new__(cls, path):
        if logger.__instance is None:
            logger.__instance = object.__new__(cls)
            logger.__instance(path)
        return logger.__instance

    def __init__(self, path):
        #Open a lof file under the specified path
        if path is not None:
            try:
                __logFile = open(path, "a+")
                #Successfully opened the log file
                return
            except IOError:
                print "There was an error opening the file at location : " + path
                print "Exception : " + IOError.message

        #Open a log file under the default location with the date in the name
        date = datetime.date()
        logName = "scraper_logs_" + date + ".txt"
        print "Attempting to open a new log file at location ~/logs/" + logName
        try:
            __logFile = open("~/logs"+logName, "a+")
        except IOError:
            print "There was an error opening the file at location : " + logName
            print "Exception : " + IOError.message
            raise
            #SHUT DOWN THE SERVER???
        #If we have successfully opened the log file, then we can save the value
        self.__logFile = __logFile

    def log(self, logLevel, module, message):
        if logger.__logFile is None:
            raise loggingException("The log file is not open. Please open another log file or check for any errors when opening your log files"
                                    "including read write permssions")
        if logger.logLevel.__contains__(logLevel):
            self.__logFile.writelines("LogLevel : "logLevel + " | " + datetime.time() + " | Module : " + message)
        else:
            self.__logFile.writelines("Unknown : " + datetime.time() + " " + message)


class loggingException(object):
    pass

