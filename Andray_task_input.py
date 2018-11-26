# File format:  student_id          nnnnnnnn
#               account_created     year-month-day
#               last_active	        year-month-day
#               balance_usd	        $nnn.nn
#               language_id         ss

import datetime

# Function to find the most active or the most lazy student
# Reason is max or min between 'account_created' and 'last_active'
# separated by 'language_id'
def activ_stud(lang = '', reason = ''):
    # Check input format
    if (type(lang) == str) and (lang != ''):
        selected_lang = lang
    else:
        selected_lang = input("Select language, please: ")

    # Select comparision reason
    if reason == '':
        reason = input("Select reason, please: ") 

    if reason == 'min':
        reason_val = float('inf')
    elif reason == 'max':
        reason_val = 0
    else: 
        raise Exception("Incorrect reason")
    
    # Input file processing
    s_result = []
    with open('4_vera.tsv') as f:
        for line_number, line_data in enumerate(f):
            if line_number == 0:
                continue
            student_id, account_created, last_active, balance, language_id = line_data.rstrip('\n').split('\t')
            
            if language_id == selected_lang:
                python_date_start = datetime.datetime.strptime(account_created, '%Y-%m-%d')
                python_date_end = datetime.datetime.strptime(last_active, '%Y-%m-%d')
                active_day = python_date_end - python_date_start
                
                active_days_num = int(active_day.days) 
                s = [student_id, account_created, last_active, active_days_num, balance, language_id]
                
                if reason == 'min':
                    if active_days_num < reason_val:
                        reason_val = active_days_num
                        s_result = s
                else:        #max
                    if active_days_num > reason_val:
                        reason_val = active_days_num
                        s_result = s

    if len(s_result) == 0:
        print ("No students with selected language")         
    else:
        print(reason, 'in', selected_lang.title(), ': ', s_result)

# Test function 

#1 - became useless becouse we never used languages values in function           
languages = ['ru','jp','en','sp']
activ_stud(languages)

#2
activ_stud('ru')

#3
activ_stud('jp', 'max')

#4
activ_stud()
