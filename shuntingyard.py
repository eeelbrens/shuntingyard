'''
First, a little bit of context:
Shunting yard algorithm is an algorithm devised by Edsger Dijkstra for converting ordinary infix mathematical operators into postfix (or RPN, the acronym for Reverse Polish Notation).
For example, you would 
This algorithm makes it easier for machines to calculate math operations since it's closer to machine language. In fact, HP used it in its earliest calculators in the 70s (e.g. HP-35 and HP-45).
It also eliminates the need for brackets, since 
Of course it's way more intuitive and easier for everyone to write math expressions in infix, but shunting yard is waaaaay too intriguing to ignore :)
And so I made this implementation. Keep in mind, I'm still a CS/DS Major college freshman, and I didn't try to implement more complex data types than lists, soooo this is a very basic implementation for now.
Read this guide on how the algorithm functions first: https://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
Don't worry, I'll try to guide you through the code comments as much as I can. Enjoy!
'''

instr = input("Shunting yard algorithm python implementation (and calculator).\nMade by eeelbrens (Abdelrhman Elbrens).\nEnter a string of a CORRECT infix mathematical operation (e.g. 30^2+41*(82/5+33)^4 , A * (B + C * D) + E , e^(i*pi) + 1)\nENTER A CORRECT MATH EXPRESSION TO PREVENT OUTPUT ERRORS.\nSupported operators: + , - , * , / , ^\nOnly positive integers are supported for the time being -_-\nSpaces between numbers or symbols are irrelevant.\nIf the input is purely numeric with no abstract placeholders, the output will be evaluated and the result will be given immediately.\nInput: ")
post = [] # postfix stack
opr = [] # operator stack
templist = [] # useful in combining alphanumeric characters together without converting any entry to another data type

# converting infix to postfix
for i in instr: # here, i'm loading likewise characters/numbers in templist first before adding them to the postfix stack, then following the rest of the shunting yard algorithm rules operator by operator
    if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        templist.append(i)
    if (ord(i)) in [40,41,42,43,45,47,94]: # supported operators' ascii characters are listed here in order. the characters in order are: ["(" ,")","*","+","-","/","^"]
        post.append("".join(templist)) # this is where they get added to the postfix stack. also occuring on line 44
        templist = []
        if ord(i) in [40,94]: # ["(","^"] since ( can be added without checking any conditions and "^" is right associative
            opr.append(i)
        if ord(i) in [42,43,45,47] :
            if len(opr) == 0: # to prevent out of index access. while loop can only work with an existing operator in the operator stack. also applied in line 34
                opr.append(i)
            else:
                while ((ord(i) in [43,45]) and (ord(opr[-1]) in [42,43,45,47,94])) or ((ord(i) in [42,47]) and (ord(opr[-1]) in [42,47,94])): # precedence logic for ["+","-","*","/"], justified in boolean terms using ascii codes :)
                    temp = opr.pop()
                    post.append(temp)
                    if len(opr) == 0: ## referenced in line 28
                        break
                opr.append(i)
        if(ord(i) == 41): # [")"]
            while opr[-1] != "(":
                temp = opr.pop()
                post.append(temp)
            opr.pop()
        if post[-1] == "": # array cleaner of join effect
            post.pop()
post.append("".join(templist)) ## referenced in line 23
for i in reversed(opr):
    post.append(i)

# at this point, postfix stack is ready to be processed!
# but first, we need to check if the whole output is numeric or not so that we can determine if we can evaluate the output
testlist = []
for i in post:
    if i not in ["+","-","*","/","^"]:
        testlist.append(i)
numerictag = ("".join(testlist)).isnumeric()

# printing post as space-separated output
for i in post:
    if i != "":
        print(i, end = " ")
    else:
        post.remove(i)
print()

# now, we can calculate any detected valid numeric expression after its numeric evaluation
postc = [] # basically, follow the rpn calculation one by one and place them yet on another stack
r = 0
if numerictag:
    for i in post:
        if i in ["+","-","*","/","^"]: # here it's safe for me to use if directly since it's guaranteed that there are at least two numbers in the beginning of the stack
            b = postc.pop()
            a = postc.pop()
            ch = i
            if(ch == "+"):
                r = a+b
            elif(ch == "-"):
                r = a-b
            elif(ch == "*"):
                r = a*b
            elif(ch == "/"):
                r = a/b
            elif(ch == "^"):
                r = a**b
            postc.append(r)
        else:
            postc.append(int(i))
    print("Valid numerical math expression detected! Evaluated at: ", end = "")
    print(r)
