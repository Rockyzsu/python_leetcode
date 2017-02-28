# -*-coding=utf-8-*-
__author__ = 'Rocky'
def findWords( words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    kb={'q':['q','w','e','r','t','y','u','i','o','p'],
        'a':['a','s','d','f','g','h','j','k','l'],
    'z':['z','x','c','v','b','n','m']}

    rList=[]
    qRow= kb['q']
    aRow= kb['a']
    zRow= kb['z']
    for w in words:
        w=w.lower()
        i=0
        l=len(w)

        if w[0] in qRow:
            row=qRow
        if w[0] in aRow:
            row=aRow
        if w[0] in zRow:
            row=zRow

        #row=kb[w[0]]
        for i in range(len(w)):
            if w[i] not in row:
                break
            else:
                if i==l-1:
                    rList.append(w)
    return rList
words=["Hello", "Alaska", "Dad", "Peace"]
rList=findWords(words)
print rList