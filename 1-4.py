#1.1
# #vitvlit simboloebs winadadebashi
# a = str(input("sheikvanet winadadeba"))
# print("simobloebis raodenoba winadadebashi aris" + str(len(a)))

#1.2
# # vaertebt or sityvas
# a = str(input("sheiyvanet nebismieri sityva"))
# b = str(input("sheiyvanete meore nebismieri sityva"))
# c = (a+b)
# print (c)

#1.3
# #vitvlit konkretuli asobgeris raodenobas sityvashi
# a = str(input("sheiyvanet striqoni"))
# print(a.count("a"))

#1.4
#sheyvanil sityvebs valagebt simboloebis raodenobis mixedvit zrdadobit
# m=[]
# for i in range (1,4):
#     a = str(input("sheikvanet xilis saxeoba"))
#     m.append(a)
# m.sort(reverse=False)
# for i in m:
#     print(i)

#1.5
#vitvlit isev simboloebs ogond konkretuli raodenobis zgvarit // viyenebt .count
# a = str("სწავლის ძირი მწარე არის, კენწეროში გატკბილდების")
# print(a[0:20])
# print(a.count("ს"))

#1.9
#vcvlit is , were it winadadebashi // viyenebt .replace
# a = str("“Hello, this is example of string. Please, write this text and do some exercises")
# print (a.replace("is","were") )

#1.10
#vitvlit sityvebis raodenobas winadadebashi // viyenebt .split
# a = str("“Hello, this is example of string. Please, write this text and do some exercises")
# b = len(a.split())
# print("sityvebis raodenobaa",b)

#1.11
#vbechdavt sheyvanil winadadebas shebrunebulad
# m=[]
# a = str("have a nice day")
# for i in a:
#     m.append(i)
# m.reverse()
# for i in m:
#     print(i)

#1.12
# a = input("input your name + .")
# b = input("input your surname")
# e = "@gau.edu.ge"
# print(a+b+e)

#1.13
# x=str(input("name"))
# y=str(input("last name"))
# print("{}.{}@edu.ge".format(x,y))




#1.14-1.16
import numpy as np
# a=np.array([1,2,3])
# b=np.random.randint(21, size=3)
# print(a+b)
# print(a*b)

#1.15-1.17
# a = np.array(([1,2,3],[4,5,6]))
# b = np.random.randint(10, size=(2,3))
# print(a)
# print(b)
# print(a+b)
# print(a*b)

#1.18
#ori matricis gamravleba
# x=np.random.randint(10, size=(3,3))
# print (x)

#1.19
#3x3 matrica 0-dan 10mde shualedit
# a = np.random.uniform(0,10, (3,3))
# print(a)

#1.20
# x=np.random.randint(10, size=(10,10))
# print(x)
# y=int(input("del->"))
# print(np.delete(x,y,axis=1))
#1.21
# x=np.random.randint(10, size=(10,10))
# print(x)
# x[x==0]=1
# print(x)
