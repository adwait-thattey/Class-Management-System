import constants
import ../Modules/library/utilities.py
class chromosome_ka_baap :
    course_durations = dict()
    #import constants.file_paths["data_utilities"] :
    
    course_iterator = utilities.get_all_courses();



class chromosome :
    ''' A class that contains 1 chromosome for genetic algorithms '''
    def __init__(self) :
        timeline = list(None)*10*6
        for i in range(len(timeline)) :
            if (i%4) :
                timeline[i] = "Break"
        
        course_time = dict()


