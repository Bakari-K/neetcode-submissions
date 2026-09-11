class Solution:

    def encode(self, strs: List[str]) -> str:
        mystring = ""
        for string in strs:
            for char in string:
                mystring = mystring + str(ord(char)) + ' '
            mystring = mystring + '-1' + ' '
        print(mystring)
        return mystring

    def decode(self, s: str) -> List[str]:
        strs = []
        mylist = s.split()
        print(mylist)
        curstring = ""
        for val in mylist:
            if val != '-1':
                curstring = curstring + chr(int(val))
            else:
                strs.append(curstring)
                curstring = ""
        return strs

