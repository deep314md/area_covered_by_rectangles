
ret = [(3,3,6,5),(4,4,6,6),(4,3,7,5),(4,2,8,5),(4,3,8,6),(9,0,11,4),(9,1,10,6),(9,0,12,2),(10,1,13,5),(12,4,15,6),(14,1,16,5),(12,1,17,2)]

def calculate(ret):
    import hashlib
    if ret == [] : return 0
    ln = len(ret)
    result = []

    def hash_list(lst):
        res = []
        for x in range(lst[0], lst[2], 1):
            for y in range(lst[3], lst[1], -1):
                point = ' '.join([str(x),str(y)])
                res.append( hashlib.sha256(point.encode('utf-8')).hexdigest()[:10] )
        return res

    result = []
    for i in range(0,ln):
            lst = ret[i]
            for el in hash_list(lst):
                if el not in result:
                    result.append(el)

    return len(result)

print(calculate(ret))