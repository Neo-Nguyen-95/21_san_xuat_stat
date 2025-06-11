import pandas as pd
from api_repo import APIRepository

course_iid = pd.read_excel('course_iid.xlsx')
course_iid_list = course_iid['course_iid'].to_list()

g6_exercise_iid = pd.read_csv('g6_exercise_iid.csv')
g6_exercise_iid_list = g6_exercise_iid['exercise_iid'].to_list()

g10_exercise_iid = pd.read_csv('g10_exercise_iid.csv')
g10_exercise_iid_list = g10_exercise_iid['exercise_iid'].to_list()

repo = APIRepository()

result = {
    'course_iid': [],
    'exercise_iid': [],
    'links': []
    }


# G6
for course_iid in course_iid_list:
    for exercise_iid in g6_exercise_iid_list:     
        
        try:
            link = repo.get_score_file(course_iid, exercise_iid)
            
            result['course_iid'].append(course_iid)
            result['exercise_iid'].append(exercise_iid)
            result['links'].append(link)
            
        except:
            print('warning!')
   
        
# G10
for course_iid in course_iid_list:
    for exercise_iid in g10_exercise_iid_list:     
      
        try:
            link = repo.get_score_file(course_iid, exercise_iid)
            
            result['course_iid'].append(course_iid)
            result['exercise_iid'].append(exercise_iid)
            result['links'].append(link)
            
        except:
            print('warning!')
        
df_links = pd.DataFrame(result)        
# df.to_excel('links_for_school_collab.xlsx')

df_list = []
for link in df_links['links'].to_list():
    df_temp = pd.read_excel(link)
    df_list.append(df_temp)
    
df_result = pd.concat(df_list)

# df_result.to_excel('student_work_result.xlsx')
