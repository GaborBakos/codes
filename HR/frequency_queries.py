'''
   You are given  queries. Each query is of the form two integers described below: 
1-  : Insert x in your data structure. 
2-  : Delete one occurence of y from your data structure, if present. 
3-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.


This is a great example for using the collections
'''

from collections import defaultdict
def freq_query(queries):
    ''' Queries is a list of tuples, where first element is 1,2, or 3
        and the second element is the input/output data value or the frequency we are looking for in our array.
    '''
    el_freq = defaultdict(int)  
    freq_count = defaultdict(int)
    ans = []
    for action, data in queries:
        if action == 1:
            if freq_count[el_freq[data]]:
                freq_count[el_freq[data]] -= 1
            el_freq[data] += 1
            freq_count[el_freq[data]] += 1            
        elif action == 2:
            if el_freq[data]:
                freq_count[el_freq[data]] -= 1
                el_freq[data] -= 1
                freq_count[el_freq[data]] += 1
        else:
            # operation 3
            if data in freq_count and freq_count[data]:
                ans.append(1)
            else:
                ans.append(0)
    return ans
