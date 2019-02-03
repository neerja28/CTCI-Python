# Data structures
# str: a = '' (empty), a = "" (empty), a = 'Hello'
# bytes: a = b'' (empty), a = b"" (empty), a = b'Hello'
# list: a = list() (empty), a = [] (empty), a = [1, 2, 3]
# tuple: a = tuple() (empty), a = (1,) (single item), a = (1, 2, 3), a = 1, 2, 3
# set: a = set() (empty), a = {1, 2, 3}
# dict: a = dict() (empty), a = {} (empty), a = {1:2, 2:4, 3:9}

from collections import Counter
def check_permutation(str1, str2):
    if (len(str1)!= len(str2)):
        return False
    counter = Counter() #dict 
    for c in str1:
        counter[c]+=1 # {a:1, b:1, c:1} 
    for c in str2:
        if counter[c]==0:
            return False
        counter[c]-=1 {a:0, b:0, c:0} 
    return True

check_permutation('abc','cba')
