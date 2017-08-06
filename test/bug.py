from ete3 import Tree
from treematcher import TreePattern

a = Tree('(( (((A,B)p5, X)p6, Y)p7, (Z, (W, (C, D)p1)p2)p3)p4 , E)root;', format=1)
print a.get_ascii()
b = TreePattern(" ((A, B)+)p7 ; ")
print b.write()

#nod = (a&'p4')
#pat = (b&'A')

#print nod
#print pat

#pat.set_controller()
#res = pat.is_local_match(nod, None)
#print res

lala = b.find_match(a, maxhits=None)
print "match: "
for i in lala: print i



#b = TreePattern(" (((A, B)@)*), (E)@^; ")
#b = TreePattern(" ((C)+); ")
#print b
#for i in b.find_match(a, maxhits=None): print i
