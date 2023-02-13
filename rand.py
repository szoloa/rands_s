from random import randint as rand

class rands:
    kay_1 = ('a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

    kay_2 = ('1','2','3','4','5','6','7','8','9','0')

    kay_3 = ('!','@','#','?','*','&','%','$')
    @staticmethod
    def rand_single(s):
        if s == 1:
            return rands.kay_1[rand(0,len(rands.kay_1)-1)]
        if s == 2:
            return rands.kay_2[rand(0,len(rands.kay_2)-1)]    
        if s == 3:
            return rands.kay_3[rand(0,len(rands.kay_3)-1)]

    @staticmethod
    def rand_range(length):
        string = ''
        for i in range(length):
            # string += rands.rand_single(rand(1,3))
            x = rand(1,len(rands.kay_1)+len(rands.kay_2)+len(rands.kay_3))
            if(x<len(rands.kay_1)):
                string += rands.rand_single(1)
            elif(x<len(rands.kay_1)+len(rands.kay_2)):
                string += rands.rand_single(2)
            else :
                string += rands.rand_single(3)
        return string

if __name__ == '__main__' :
    print(rands.rand_range(16))