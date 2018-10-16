#语法分析
import nltk
import jieba.posseg as pseg
import jieba
import ast
import fool
s="王健林的儿子是不是王思聪"
from nltk import CFG

def draw_(s):
	s=pseg.cut(s)
	l=[]
	for i in s:
		l.append((i.word,i.flag))
	print(l)

	grammar = r"""
	NP:{<r>?<nr>?<z>?<uj>*<n>}
	{<nr>*}
	{<ns+><v>?}
	{<v><n><uj>?}
	{<m+><eng>?}
	{<NP>?<c>?<NP>*}
	VP:{<v>*<p>*<ns>}
	{<v><NP>}
	{<VP><NP>}
	"""
	cp = nltk.RegexpParser(grammar,loop=2)
	result = cp.parse(l)
	result.draw()
#画语法树
import nltk
import jieba.posseg as pseg
import jieba
import ast
import fool
s="王健林的儿子是不是王思聪"
from nltk import CFG

def draw_(s):
	s=pseg.cut(s)
	l=[]
	for i in s:
		l.append((i.word,i.flag))
	print(l)

	grammar = r"""
	NP:{<r>?<nr>?<z>?<uj>*<n>}
	{<nr>*}
	{<ns+><v>?}
	{<v><n><uj>?}
	{<m+><eng>?}
	{<NP>?<c>?<NP>*}
	VP:{<v>*<p>*<ns>}
	{<v><NP>}
	{<VP><NP>}
	"""
	cp = nltk.RegexpParser(grammar,loop=2)
	result = cp.parse(l)
	result.draw()
def draw_1(s):
	m=s
	l=fool.cut(s)[0]
	print(l)
	p=product_grammar(m)
	grammar = CFG.fromstring("""
	S -> NP L NP|NP vshi NP y|NP L P NP|NP L P NP F|NP vshi R|T vshi R
	NP -> nr nr| nr ude n| nr n|NP ude NP|NP NP|z ude n|a ude n|v ude n|nr|n|b ude|ns ude|ns|ns ude NP|m n|m q n|A\
    |d m|m|NP c NP|NP p NP
	VP -> v NP|v VP
	L ->vshi d vshi
	P ->p|vi p
	F ->f
	T ->t
	R ->r|r NP|r ude NP
	A ->a|d a|m q|d a ude
	"""+p)
	cp= nltk.ChartParser(grammar)
	trees =cp.parse(l)
	for s in trees:
		print(s)
def product_grammar(s):#根据词性构造语法
	l=fool.analysis(s)[0][0]
	k={}
	y=[]
	print(l)
	for i in l:
		if i[1] not in y:
			y.append(i[1])
			k.update({i[1]:[i[0]]})
		else:
			k.update({i[1]:k[i[1]]+[i[0]]})
	g=''
	for i,j in k.items():
		t=i+' ->'
		c=0
		for n in j:
			if len(j)>1 and c<=len(j)-2:
				t+='\''+n+'\''+'|'
			else:
				t+='\''+n+'\''
			c+=1
		g+=t+'\n'
	print('文法:',g)
	return g

#draw_1("赵本山是精彩的演员吗")
product_grammar("赵本山是精彩的演员吗")


