import gcalc

def header():
    print \
""" 
 Google Calculator Shell 
 -----------------------
 Ctrl+C to quit
 """

if __name__=='__main__':
    header()
    g = gcalc.GCalc()
    while True:
        print "GC >> ",
	query = raw_input()
	print g.calc(query)
