import pandas as pd

data = pd.read_csv('intelligentGuessingDataSet.csv', encoding='latin-1')


def return_pattern(string, where):
    if string[0] == where[0]:
        pattern_found = string[0]
    else:
        pattern_found = ''
    for i in range(len(string),1,-1):
        length_of_pattern = len(pattern_found)
        occurance = where.count(string[:i]) 
        if occurance ==1 and len(string[:i])>=length_of_pattern:
            pattern_found = string[:i]
        
        if ' ' in string:
            strings = string.split(' ')
            pattern_found = ''
            part1=''
            for string in strings:
                if string in where:
                    part1 +=' '+string
            pattern_found = part1[1:]
            
    return pattern_found

def give_pattern(fname,lname,email):
    initial = email[:email.index('@')]
    for_fname = return_pattern(fname,initial)
    for_lname = return_pattern(lname,initial)
    
    final_pattern_f = ''
    final_pattern_l = ''
    
    if for_fname != '':
        if len(for_fname) == 1:
            final_pattern_f+= '<1>'
        elif for_fname == fname:
            final_pattern_f+= '<11>'
        else:
            s = len(for_fname)
            form = '<11-f'+str(s)+'l>'
            final_pattern_f+= form
            
        initial = initial.replace(for_fname, final_pattern_f)
        
    if for_lname != '':
        if len(for_lname) == 1:
            final_pattern_l+= '<2>'
        elif for_lname == lname and ' ' not in for_lname:
            final_pattern_l+= '<22>'
        elif ' ' in for_lname:
        
            names = for_lname.split(' ')
            one = '<20>'
            two = '<21'
            
            merged = one+two
            
            initial = initial.replace(names[0], one)
            initial = initial.replace(names[1], two)
             
        else:
            s = len(for_lname)
            form = '<22-f'+str(s)+'l>'
            final_pattern_l+= form
        initial = initial.replace(for_lname, final_pattern_l)
    return initial


print(give_pattern('ian','ian ditullio','ian.ditullio@gmail.com'))