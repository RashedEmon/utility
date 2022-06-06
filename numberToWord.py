quantityTag = ["","thousand","million","billion","trilion"]
numberDictonary1={
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
}
numberDictonary2={
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}



def resizing(amount:str):
    length = len(amount)
    if length%3 != 0:
        zeroToAdd = length%3
        for _ in range(zeroToAdd,3):
            amount="0"+amount
    return amount




def stringToArray(amount):
    i = len(amount)
    amountArr = []
    while(i >= 0):
        amountArr.insert(0,amount[i-3:i])
        i=i-3
    return amountArr[1:]
    


def covertNumberToWord(string):
    word=""

    if string[0] != "0":
        word=word+numberDictonary1[string[0]]+" hundred"
        
    if string[1] != "0":
        if string[1] == "1":
            if string[0] == "0":
                word = word + numberDictonary1[string[1:3]]
            else:
                word = word + " and "+ numberDictonary1[string[1:3]]
            return word
        else:
            if string[2] == "0":
                word=word+" and "+numberDictonary2[string[1]]
                return word
            else:
                if string[0] == "0":
                    word=word+""+numberDictonary2[string[1]]+"-"+numberDictonary1[string[2]]
                else:
                    word=word+" and "+numberDictonary2[string[1]]+"-"+numberDictonary1[string[2]]
                return word
    else:
        if string[2] == "0":
            return word
        else:
            if string[0] == "0":
                return word + " "+ numberDictonary1[string[2]]
            else:
                return word + " and "+ numberDictonary1[string[2]]
            
            
        
    return word
    

    
def numberToWord(amountArr):
    amountArr.reverse()
    word=[]
    for i in range(0,len(amountArr)):
        temp=covertNumberToWord(amountArr[i])
        if temp != "":
            if i==0:
                word.append(temp+quantityTag[i])
            else:
                word.append(temp+" "+quantityTag[i])
            
    word.reverse()
    result=""
    for item in word[:-1]:
        result+=item+","
    return result+word[len(word)-1]
    
t=3
while t>0:
    amount = input()
    if "$" in amount:
        amount = amount[:-1]
    arr=[]
    afterPoint = ""
    if "." in amount:
        arr = amount.split(".")
        amount=resizing(arr[0])
        l = len(arr[1])
        temp="1"
        for _ in range(0,l):
            temp+="0"
        afterPoint += " & "+arr[1]+"/"+temp+ " USD only"
    else:
        amount=resizing(amount)
    
    
    amountArr = stringToArray(amount)
    
    print(numberToWord(amountArr)+afterPoint)
    t-=1




#52758368.01$
#586981000.52$
#1000000000.100$
