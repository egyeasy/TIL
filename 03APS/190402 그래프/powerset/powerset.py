def get_power_set(s):
  power_set=[[]]
  for elem in s:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set


def powersetlist(s):
    r = [[]]

    for e in s:
        temp= [x+[e] for x in r]
        r += temp

    return r


def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result



import collections
def power_set(s):
    q = collections.deque()
    q.appendleft([])
    for elem in reversed(s):
        while True:
            subset = q.pop()
            q.appendleft([elem] + subset)
            q.appendleft(subset)
            if not subset: break
    return list(q)


def powerset1(s):
    x = len(s)
    res = []
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        res = []
        #yield [ss for mask, ss in zip(masks, s) if i & mask]
        for mask, ss in zip(masks, s):
            if i & mask:
                res.append(ss)
        yield res

def powerset2(seq):
    #Returns all the subsets of this set. This is a generator.
    if len(seq) <= 1:
        #return [[], seq]
        yield seq
        yield []
    else:
        res =[]
        for item in powerset2(seq[1:]):
            #res.append(item)
            #res.append([seq[0]]+item)
            yield [seq[0]]+item
            yield item
        #return res

maxsum = 0
for set1 in powerset1([4, 5, 6, 7, 8, 9]):
    if sum(set1) > maxsum:
        maxsum = sum(set1)
print(maxsum)


l = [14, 7, 35, 84]
for x in powerset2(l):
    if sum(x) % 2:
        print(x)

#r = [x for x in powerset2(l)]
#print(r)
print(powersetlist([0,1,2,3,4, 5, 6, 7, 8, 9]))

import time
tSet = [_ for _ in range(1, 21)]

stime = time.time()
s=0
for s1 in powersetlist(tSet):
   s += sum(s1)
print("powersetlist : ",s, end=" ")
etime = time.time()
print(etime-stime)

stime = time.time()
s=0
for s1 in list_powerset(tSet):
   s += sum(s1)
print("list_powerset : ",s, end=" ")
etime = time.time()
print(etime-stime)

stime = time.time()
s=0
for s1 in power_set(tSet):
   s += sum(s1)
print("power_set : ",s, end=" ")
etime = time.time()
print(etime-stime)


stime = time.time()
s = 0
for set1 in powerset1(tSet):
       s += sum(set1)
print("powerset1 : ",s, end=" ")
etime = time.time()
print(etime-stime)


stime = time.time()
s = 0
for set1 in powerset2(tSet):
       s += sum(set1)
print("powerset2 : ",s, end=" ")
etime = time.time()
print(etime-stime)
