import random 
import string


def getKey():
	s = 'zzz'
	for i in xrange(6):
		s = s+random.choice(string.ascii_lowercase)
	return s

def beginCode(u0):
	if u0.find("\\begin{equation}")==0: return 0
	if u0.find("\\begin{figure}")==0 : return 1
	if u0.find("\\begin{eqnarray}")==0: return 2
	if u0.find("\\begin{tcolorbox}")==0: return 3
	return -1

def endCode(u0):
	if u0.find("\\end{equation}")==0: return 0
	if u0.find("\\end{figure}")==0 : return 1
	if u0.find("\\end{eqnarray}")==0: return 2
	if u0.find("\\end{tcolorbox}")==0: return 3
	return -1

def convert(fname):
	list_line = []
	for l0 in open(fname, 'r'):
		l0 = l0.rstrip()		
		u0 = l0.decode('utf-8')
		list_line.append(u0)

	icode = -1;
	list_Out = []
	list_Tmp = []
	list_Map = []
	for i in xrange(len(list_line)):
		u0 = list_line[i]
		if beginCode(u0) != -1 and icode == -1:
			icode = beginCode(u0)
		if endCode(u0) == icode and icode != -1:
			icode = -1
			list_Tmp.append(u0)
			key = getKey()
			list_Tmp.insert(0,str(len(list_Tmp)))	
			list_Tmp.insert(0,key)
			list_Map.append(list_Tmp)
			list_Tmp = []
			list_Out.append(key)
			continue
		if icode != -1:
			list_Tmp.append(u0)
			continue

		while 1:
			ibeg = u0.find("$")
			if ibeg == -1:
				break;
			else:	
				iend = u0.find("$",ibeg+1)		
				if iend == -1:
					print(u0)
				assert iend != -1
				u1 = u0[0:ibeg]
				u2 = u0[iend+1:]
				eqn = u0[ibeg:iend+1]
				key = getKey()
				list_Map.append([key,"1",eqn])
				u0 = u1+key+u2

		if u0.find("\\usepackage")==0 or \
		 u0.find("\\geometry")==0 or \
		 u0.find("\\newcommand")==0 or \
		 u0.find("\\begin{document}")==0 or\
		 u0.find("\\tableofcontents")==0 or\
		 u0.find("\\maketitle")==0 or\
		 u0.find("\\documentclass")==0 or\
		 u0.find("\\end{document}")==0:
			key = getKey()
			list_Out.append(key)
			list_Map.append([key,"1",u0])
			continue

		list_Out.append(u0)

	f = open('toGoogleTrans.txt', 'w')
	for u0 in list_Out:
		s0 = u0.encode('utf-8')
		f.write(s0+"\n")
	f.close()

	f = open("keyMap.txt", "w")
	for imap in xrange(len(list_Map)):
		list0 = list_Map[imap]
		for l0 in list0:
			print(l0)
			f.write(l0+"\n")






if __name__ == "__main__":
	convert("main_en.tex")