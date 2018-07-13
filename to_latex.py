

def getDict(fname_keyMap):
	list0 = []
	for l0 in open(fname_keyMap,"r"):
		l0 = l0.rstrip()
		list0.append(l0)

	dic0 = {} 
	il = 0
	while(1):
		if il >= len(list0):
			break;
		key = list0[il]
		num = int(list0[il+1])
		print("key:",key,"num:",num)
		list2 = list0[il+2:il+2+num]
		il += num+2
		dic0[key] = list2

	print(dic0)
	return dic0

def convLatex(fname_txt, dic0):
	list0 = []
	for l0 in open(fname_txt,"r"):
		l0 = l0.rstrip()
		if l0.find("\\ section {")==0:
			list0.append("\\section{"+l0[11:])
			continue
		if l0.find("\\ subsection {")==0:
			list0.append("\\subsection{"+l0[14:])
			continue
		if l0.find("\\ subsubsection {")==0:
			list0.append("\\subsubsection{"+l0[17:])
			continue
		if l0.find("\\ title {")==0:
			list0.append("\\title{"+l0[9:])
			continue
		if l0.find("\\ author {")==0:
			list0.append("\\author{"+l0[10:])
			continue

		while(1):			
			is_Cap = False
			ibeg = l0.find("zzz")
			if ibeg == -1:
				ibeg = l0.find("Zzz")
				is_Cap = True
			if ibeg == -1:
				list0.append(l0)
				break;
			key = l0[ibeg:ibeg+9]
			if is_Cap: 
				key = "z" + key[1:9]
			val = dic0[key]
			if len(val)==1 :
				l0 = l0[0:ibeg]+val[0]+l0[ibeg+9:]
			else:
				for lv in val:
					list0.append(lv)
				break

	f = open('main_en1.tex', 'w')
	for l0 in list0:
		f.write(l0+"\n")
	f.close()






if __name__ == "__main__":
	dic0 = getDict("keyMap.txt")	
	convLatex("fromGoogleTrans.txt", dic0)