from random import randint as rand

# rands((int)lens).string to return a length = lens random string
class rands:
    kay = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            '1','2','3','4','5','6','7','8','9',
            '0','!','@','#','?','*','&','%','$']
    
    def __rand_single(self):
        return self.kay[rand(1,len(self.kay)-1)]
    
    def __rand_range(self,function):
        string = ''
        for i in range(self.lens):
            string += function()
        self.string = string
    
    def __rand_sigle_nonerepeat(self):
        delkayinfo = rand(1,len(self.kay)-1)
        delkay = self.kay[delkayinfo]
        del self.kay[delkayinfo]
        return delkay

    def __init__(self,lens,function = 0) -> None:
        self.lens = lens
        if(function == 0):
            self.__rand_range(self.__rand_sigle_nonerepeat)
        elif function == 1:
            self.__rand_range(self.__rand_single)
        else :
            self.__rand_range(function)
if __name__ == '__main__':
    print(rands(16).string)