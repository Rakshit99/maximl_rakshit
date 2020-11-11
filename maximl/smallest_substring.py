from collections import defaultdict   

def smallestSubstring(s): 
    n = len(s) 
    distCount = len(set([x for x in s])) 
  
    count, start, finalStart, minWin = 0, 0, -1, n
    countList = defaultdict(lambda: 0)

    for i in range(n): 
        countList[s[i]] += 1
 
        if countList[s[i]] == 1: 
            count += 1
  
        if count == distCount: 
            while countList[s[start]] > 1:   
                countList[s[start]] -= 1
                start += 1
  
            curWin= i - start + 1
            if minWin > curWin: 
                minWin = curWin 
                finalStart = start
    
    return minWin 
      
s1 = "rgdhfjghk"
print("Length of smallest substring having maximum number of characters '"+ s1+ "' :")
print(smallestSubstring(s1))