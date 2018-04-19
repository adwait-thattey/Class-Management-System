import utilities

#class chromosome_ka_baap :
if True :
    course_durations = dict()
    #import constants.file_paths["data_utilities"] :
    
    course_iterator = utilities.get_all_courses()
    I = next(course_iterator)
    while I:
        L = list()
        L.append(I.professor)
        L.append(I.no_of_classes_per_week)
        course_durations[I.id] = list(L)
        try:
            I = next(course_iterator)
        except StopIteration :
            break

    print(course_durations)            


# class chromosome :
#     ''' A class that contains 1 chromosome for genetic algorithms '''
#     def __init__(self) :
#         timeline = list(None)*10*6
#         for i in range(len(timeline)) :
#             if (i%4) :
#                 timeline[i] = "Break"
        
#         course_time = dict()


