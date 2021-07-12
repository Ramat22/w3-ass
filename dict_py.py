# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:24:12 2021

@author: win10
"""
 
dict={"brand":"ford",
      "model":"mustang"
      }
x=dict.get("model")
print(x)


dict={"brand":"ford",
      "model":"mustang"
      }
x=dict.items()
print(x)


dict={"brand":"ford",
      "model":"mustang",
      "year":"1956"      
      }
dict.update({"year":2021})
print(dict)



dict={"brand":"ford",
      "model":"mustang",
      "year":"1956"      
      }
dict.pop("model")
print(dict)


dict={"brand":"ford",
      "model":"mustang",
      "year":"1956"      
      }    
for x in dict:
 print(dict[x])



dict={"brand":"ford",
      "model":"mustang",
      "year":"1956"      
      }
mydict = dict.copy()
print(mydict)



myfamily={
   "person1":{"name":"rama",
         "year":"2000"
},
"person2":{"name":"rimu",
         "year":"2002"
}
}
print(myfamily)







