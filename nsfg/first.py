'''
Created on 2013. 1. 19.

@author: pragma0924
'''
import survey

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

# Count the number of live births
live_birth_records = [record for record in table.records if record.birthord != 'NA']
print 'Number of live births', len(live_birth_records)

# identify the first babies
first_and_others = {'first': [], 'others': []}
for record in live_birth_records:
    if record.birthord == 1:
        first_and_others['first'].append(record)
    else: 
        first_and_others['others'].append(record)
        
print '# of first: %s, # of others: %s' % (len(first_and_others['first']), len(first_and_others['others']))