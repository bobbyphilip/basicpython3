import math
def solve():
    '''
        8
   A --------B
    |       |
  8 |       | 8
    |       |
   D---------C
        8 

    Shortest Path connecting all 4 points of square of side 8. Total length should be less than 22
    '''
    SEMIWIDTH = 4
    HEIGHT = 8

    wlist = [ x * 0.1 for x in range(1, SEMIWIDTH*10+1)]
    hlist = [ x * 0.1 for x in range(1, HEIGHT*10+1)]
    res = [100,0,0,0]
    for h1 in hlist:
        h2 = HEIGHT-h1
        for w in wlist:
            connect = SEMIWIDTH-w
            hyp1 =(math.sqrt((h1*h1)+(w*w)))
            hyp2 =(math.sqrt((h2*h2)+(w*w)))

            len = hyp1*2+hyp2*2+connect*2
            if len<=22:
                if len<res[0]:
                    res[0]=len
                    res[1]=w
                    res[2] = h1
                    res[3] = h2
    print("Final answer is ",res)

if __name__ == '__main__':
    solve()
