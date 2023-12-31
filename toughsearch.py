
from random import random
import copy
import sys

SIZEX = 30
SIZEY = 30
FILLER = '.'
DUMMY = ' '

HTML_STRING='&#x41;&#x42;&#x43;&#x44;&#x45;&#x46;&#x47;&#x48;&#x49;&#x4a;'+\
'&#x4b;&#x4c;&#x4d;&#x4e;&#x4f;&#x50;&#x51;&#x52;&#x53;&#x54;&#x55;&#x56;'+\
'&#x57;&#x58;&#x59;&#x5a;&period;&#x20;'

FILLER_HTML='&period'

ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ALPHA_HTML=[]
for alpha_char in HTML_STRING.split(';'):
	ALPHA_HTML.append(alpha_char)

#for xchar in ALPHA_HTML:
#	#print(xchar,end=';')
#	print('<br>'+xchar+'</br>')
#sys.exit()
#	ALPHA_HTML=;&NewLine;&#x42;
#	ALPHA=""

def initialize_puzzle():
	global SIZEY
	puzzlex = []
	for doit in range(SIZEX):
		puzzlex.append(DUMMY)

	puzzley = []
	for doit in range(SIZEY):
		puzzley.append(puzzlex.copy())

	#return puzzley 

	# make it a tree
	increment = 0.1
	for y in range(SIZEY):
		for x in range(int(SIZEX/2-increment),int(SIZEX/2+increment)):
			# print(x, end=', ')
			puzzley[y][x] = FILLER
		#print('')
		if increment < SIZEX/2:
			increment +=0.5

	trunk = []
	for trunk_pos in range(SIZEX):
		if trunk_pos > (SIZEX/2-2)-1 and trunk_pos < (SIZEX/2+2) -1:
			trunk.append('#')
		else:
			trunk.append(DUMMY)
	puzzley.append(trunk.copy()) 
	puzzley.append(trunk.copy()) 
	puzzley.append(trunk.copy())
	
	#SIZEY = SIZEY + 3
	
	return puzzley

def html_puzzle(words):
	for liney in words:
		print('            ',end='')
		for letterx in liney:
			if ord(letterx)> 65:
				print(ALPHA_HTML[ord(letterx)-65],end=' ')
			else:
				print('X')
		print('<br>')

def display_puzzle(words):
	for liney in words:
		print('            ',end='')
		for letterx in liney:
			print(letterx,end=' ')
		print('')

def do_word(words, word):
	xloc = int(random()*SIZEX)
	yloc = int(random()*SIZEY)

	#print(f'random: {xloc},{yloc}')

	# decide forward, backward
	# decide u/d, l/r diag l->r or diag r->l
	xdir = 0
	ydir = 0
	# xdir and ydir cannot both be 0
	while (xdir == 0 and ydir == 0):
		xdir = int(random()*3)-1
		ydir = int(random()*3)-1

	#xdir = 0 up/down, 1 L->R, -1 R->L
	#ydir = 0 left/right, 1 U->D, -1 D->U
	#
	xpos = xloc
	ypos = yloc

	xlen = len(word)*xdir
	ylen = len(word)*ydir

	# FIX OUT OF BOUNDS
	#print(f'xloc:{xloc},xlen:{xlen},xdir:{xdir}')
	if xlen + xloc <0:
		xpos = abs(xlen)

	if xlen + xloc >= SIZEX:
		xpos = (SIZEX-1) - abs(xlen)

	if ylen + yloc < 0:
		ypos = abs(ylen)

	if ylen + yloc > SIZEY:
		ypos = (SIZEY-1) - abs(ylen)

	xsave = xpos
	ysave = ypos
		
	# print(f'xloc:{xpos},xlen:{xlen},xdir:{xdir}')

	failed = False
	# TRY THE PLACEMENT
	for placement in range(len(word)):
		# print(f'{xpos},{ypos}')
		if words[xpos][ypos] == FILLER or words[xpos][ypos] ==  word[placement]:
			pass
		else:
			failed = True
		xpos += xdir
		ypos += ydir

	if not failed:
		xpos = xsave
		ypos = ysave

		for placement in range(len(word)):
			if words[xpos][ypos]== word[placement]:
				pass
				# print(f"DOUBLE DOWN! {word}:{word[placement]}{placement}")
			words[xpos][ypos]=word[placement]
			xpos += xdir
			ypos += ydir

	return failed

def place_word(wordy, word):
	failed = True
	while failed:
		failed = do_word(wordy, word)

def fill_puzzle(wordy):
	for y in range(SIZEY):
		for x in range(SIZEX):
			if wordy[x][y] == FILLER:
				letter = ALPHA[int(random()*len(ALPHA))]
				wordy[x][y] = letter

def main():

	global ALPHA

	wordy = initialize_puzzle()

	word_list = []

	word_list.append("MERRY")
	word_list.append("CHRISTMAS")
	word_list.append("JESUS")
	word_list.append("MARY")
	word_list.append("JOSEPH")
	word_list.append("GABRIEL")
	word_list.append("ANGELS")
	word_list.append("SHEPHERDS")

	for word in word_list:
		place_word(wordy, word)

	key = copy.deepcopy(wordy)

	# MAKE ALPHA FILLER JUST THE LETTERE IN THE WORDS
	a_list=[]
	for x in word_list:
		for y in x:
			# print(y,end='')
			if y not in a_list:
				a_list.append(y)
	#print(a_list)

	fill_puzzle(wordy)
	display_puzzle(key)
	print('\n\n\f')
	html_puzzle(wordy)
	#display_puzzle(wordy)

	
	print('\n\n\n')
	spacer = 0
	for word in word_list:
		print('      ', end='')
		print(word, end = '\t')
		spacer += 1
		if spacer > 4:
			spacer = 0
			print('')
	print('')


main()



