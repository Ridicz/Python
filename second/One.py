x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
# kod jest poprawny

for i in "qwerty": if ord(i) < 100: print i
# kod nie jest poprawny

for i in "axby": print ord(i) if ord(i) < 100 else i
# kod jest poprawny
