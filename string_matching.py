i=input
s=i()
p=i()
import re
print( len(re.findall('(?={0})'.format(re.escape(p)), s)) )

