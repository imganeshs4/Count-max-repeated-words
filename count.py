filename= input("Enter the file name : ")

fhand=open(filename,'r')
strings=fhand.read()
words=strings.split()

counts=dict()
lists=list()

for word in words:
  counts[word]=counts.get(word,0)+1

for key,value in counts.items():
	lists.append((value,key))

lists.sort(reverse=True)

for value,key in lists[:10]:
	print(key,' : ',value)
