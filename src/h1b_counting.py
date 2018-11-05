
# coding: utf-8

# In[77]:

import sys # run python file and get input output files path


# In[127]:

#[0] xxxx.py
#[1] file_name.csv 
#[2] top_10_occupations.txt
#[3] top_10_states.txt
#[4] column index of visa status
#[5] column index of visa type
#[6] column index of occupation
#[7] column index of state
input_file = sys.argv[1]
output_file_occupations = sys.argv[2]
output_file_states = sys.argv[3]
status = int(sys.argv[4])
visa = int(sys.argv[5])
occupation = int(sys.argv[6])
state = int(sys.argv[7])

"""
#input_file = '../input/H1B_FY_2016.csv'
input_file = '../input/h1b_input.csv'
output_file_occupations = '../output/top_10_occupations.txt'
output_file_states = '../output/top_10_states.txt'
status = 2
visa = 5
#occupation = 20
#state = 38
occupation = 24
state = 50
"""

occupation_dict = {} # store occupation with its certified number
state_dict = {} # store state with its certified number
count = 0 # count total certified number

f = open(input_file) # open csv file
for row in f: # read each row
    data = row.split(';') # csv file seperated by ';'
    if(data[24][0] == '"' and data[24][0] == '"'): # remove strange case(value with "")
        data[24] = data[24][1:-1]
    
    if data[visa].split(' ')[0] in ['H-1B', 'H-1B1','E-3'] and data[status] == 'CERTIFIED': # find target
        count = count + 1 # count number
        
        try:
            occupation_dict[data[occupation]] = occupation_dict[data[occupation]] + 1 # count occupation with its number
        except:
            occupation_dict[data[occupation]] = 1 # zero number before
        try:
            state_dict[data[state]] = state_dict[data[state]] + 1 # count state with its number
        except:
            state_dict[data[state]] = 1 # zero number before


# In[128]:

# sort key in ascending order and value in descending order and get first 10 
occupation_dict_10 = sorted(occupation_dict.items(), key=lambda x: (-x[1], x[0]))[0:10]
state_dict_10 = sorted(state_dict.items(), key=lambda x: (-x[1], x[0]))[0:10]


# In[133]:

f = open(output_file_occupations, 'w+') # open output file
# clean file
f.seek(0)
f.truncate()
# print 1st line
print('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE', file=open(output_file_occupations, 'a'))
# check output lines
if(len(occupation_dict_10) < 10):
    size = len(occupation_dict_10)
else:
    size = 10
# print value in the format
for i in range(size):
    print("{};{};".format(occupation_dict_10[i][0], occupation_dict_10[i][1]) + '%.1f'%(round(100 * occupation_dict_10[i][1] / count, 1)) + '%', file=open(output_file_occupations, 'a'))


# In[134]:

f = open(output_file_states, 'w+') # open output file
# clean file
f.seek(0)
f.truncate()
# print 1st line
print('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE', file=open(output_file_states, 'a'))
# check output lines
if(len(state_dict_10) < 10):
    size = len(state_dict_10)
else:
    size = 10
# print value in the format
for i in range(size):
    print("{};{};".format(state_dict_10[i][0], state_dict_10[i][1]) + '%.1f'%(round(100 * state_dict_10[i][1] / count, 1)) + '%', file=open(output_file_states, 'a'))


# In[ ]:



