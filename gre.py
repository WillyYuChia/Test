import requests
from bs4 import BeautifulSoup as bs



############### rename books ##################

# '''



url = 'https://realpython.com/python-requests/'

getSoup(url)

print


# '''




############### rename books ##################

'''
import os
import os.path as op

name = 'test{}.pdf'
for a in range(10):
	if op.exists(name.format(a)):
		original_name = name.format(a)
		new_name = 'Futures&OptionMarket{}.pdf'.format(a)
		os.rename(original_name, new_name)

'''


############### download online pdf ##################
'''
import math
import os
import pprint as pp
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bSoup
import cv2

from fpdf import FPDF
import urllib
import inspect

def getContent(url):
	page = requests.get(url)
	return page.content

def getSoup(url):
	return bSoup(getContent(url), 'html.parser')

image_url = 'http://online.anyflip.com/xetl/tjvj/files/mobile/{}.jpg'

# image = urllib.urlopen(image_url).read()


image_list = []

last_page = 624
num_page = 100
num_book = 7
for book in range(num_book):
	pdf = FPDF()
	for page in range(num_page):
		a = page + book*num_page + 1
		if a>last_page:
			break
		print('Progress: page {}'.format(a))
		curr = '00{}.jpg'.format(a)
		try:
			image = getContent(image_url.format(a))
			with open(curr, 'wb+') as i:
				i.write(image)
			# pp.pprint(inspect.getmembers(i))
			pdf.add_page()
			pdf.image(curr, 0, 0, 210)
		except:
			print('page {}: blank!'.format(a))
		finally:
			os.remove(curr)
	pdf.output('test{}.pdf'.format(book), 'F')
	print('Book{} done!'.format(book))
print('All over!!!')

# print(cv2.imread('001.jpg').shape)
'''



############### playing with modules ##################
'''
import sys
import os.path as pt

if len(sys.argv)>1:
	name = sys.argv[1]
else:
	print('no input file path')

filePath = 'GRE_VOCAB/GRE3000_30.txt'

if not pt.isfile(filePath):
	print('this is not a valid path')
else:
	print('a file is found')

if not pt.exists(filePath):
	print('no such file')
else:
	print('file found')


# opening files this way ensures that the operator helps us close() the file safely after usage
with open('GRE_VOCAB/GRE3000_3.txt', 'r') as f:
	l = f.readline()
	print(l)

try:
	f = open('GRE_VOCAB/GRE3000_2.txt', 'r')
	line = f.readline()
	print(line)
except:
	print('file does not exist')
finally:
	f.close()


import re

string = 'i am a cute little boy, butccc i am a little bit fat. however, i am on my way to being fit!'
p = re.compile('[b-f]+')
li = p.finditer(string)
# for a in li:
# 	print(a)

from collections import Counter

data_set = """Welcome to the world of Geeks!
This portal has been created to provide well written well 
thought and well explained solutions for selected questions 
If you like Geeks for Geeks and would like to contribute 
here is your chance You can write article and mail your article
 to contribute at geeksforgeeks org See your article appearing on 
the Geeks for Geeks main page and help thousands of other Geeks."""

split_it = data_set.split()
Counter = Counter(split_it)
most_occurred = Counter.most_common(4)
# print(most_occurred)


'''




############### getting highlight news ##################
'''

import math
import pprint
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bSoup

def getContent(url):
	page = requests.get(url)
	return page.content

def getSoup(url):
	return bSoup(getContent(url), 'html.parser')

common_words = {
	'url': 'https://en.wikipedia.org/wiki/Most_common_words_in_English',
	'class': 'extiw'
}
common_words['soup'] = getSoup(common_words['url'])

common_words['content'] = common_words['soup'].find_all(class_=common_words['class'])

for a in range(len(common_words['content'])-2):
	print(common_words['content'][a].text)

classes = [
'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor',
'gs-c-promo nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-o-primary-promo gs-u-display-inline-block gs-u-clearfix gs-u-float-right@m gs-u-ml0 gs-c-promo--flex',
'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor',
]
most_read = 'nw-c-most-read__items gel-layout gel-layout--no-flex'
most_read_item = 'gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs'
BBC = getSoup('https://www.bbc.com/news')
targetClass = classes[0]
# news = bbc.find_all(class_=targetClass)
popular_news = BBC.find(class_=most_read).find_all(class_=most_read_item)
print(len(popular_news))
for top in popular_news:
	print(top.text)
# for info in news:
# 	print(info.text)
# for c in classes:
# 	bbc_lines = bbc.find_all(class_=c)
# 	for line in bbc_lines:
# 		print(line.text)

# recursiveFind(cnn, 'cd__headline-text')
# for sec in cnn:
# 	try:
# 		print(len(sec))
# 		headline = sec.find_all('cd__headline-text')
# 		# print(headline)
# 	except:
# 		print('nothing')

# title = cnn.find_all('div', 'cd__wrapper')
# print(title)
# print(cnn.find_all(class_='js no-flash geolocation websockets localstorage webworkers no-touchevents fontface supports textshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox csstransforms3d no-mobile no-phone no-tablet mobilegradea no-gdpr no-ios no-android no-iospre10 no-iemobile no-ieunsupported no-ie11unsupported no-ie no-edge'))

'''




############### adusting the format (aborted) ##################
'''
import math
import pprint
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bSoup
import os.path
from pathlib import Path

folder = 'GRE_VOCAB'
name = 'GRE3000_{}.txt'
newline = '\n'
tab = '\t'
space = ' '
# def fixFormat(file):

def greName(direc, file, num):
	return '{}/{}'.format(direc, file.format(num))

def openFile_read(path):
	if Path(path).exists():
		return open(path, 'r')
	else:
		return None

def openFile_write(path):
	if Path(path).exists():
		return open(path, 'r')
	else:
		return None

def closeFile(f):
	if f!=None:
		f.close()
newFile = ''
f = openFile_read(greName(folder, name, 1))
lines = f.readlines()
for l in lines:
	firstChar = l[0]
	if firstChar==tab:
		line.replace('=', ';')
	elif firstChar!=newline:
		l[0] = firstChar.upper()
	newFile = newFile + l

# for a in range(1):
# 	print(f.readlines())


# for a in range(30):
# 	path = '{}/{}'.format(folder, name.format(a))
# 	if Path(path).exists():
# 		fixFormat(path)
'''





############### digging out GRE 3000 vocabulary and the definitions ##################
'''
import math
import pprint
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bSoup

def getContent(url):
	page = requests.get(url)
	return page.content

def getSoup(url):
	return bSoup(getContent(url), 'html.parser')

def getVocabulary(url):
	soup = getSoup(url)
	words = soup.find_all('li', class_='entry learnable')
	vocabulary = []

	for word in words:
		vocab = word.text.split()[0]
		vocabulary.append(vocab)
	return vocabulary

def getDefinition(word):
	url = 'https://www.dictionary.com/browse/{}?s=t'.format(word)
	soup = getSoup(url)
	explanation = None
	try:
		sections = soup.find(class_='css-1urpfgu e16867sm0').find_all(class_='one-click-content css-1p89gle e1q3nk1v4')
		meanings = []
		for sec in sections:
			defi = sec.text
			if defi[0]==' ':
				continue
			meanings.append(defi)

		examples = []
		for a in range(len(meanings)):
			m = meanings[a]
			m = m.split('\n')[0]
			full = m.split(':')
			full[0] = full[0].replace(';', '=', 1)
			full[0] = full[0].replace(';', ',')
			if len(full)>1:
				full[1] = full[1].replace(';', '; ')
			for s in range(len(full)):
				full[s] = full[s].strip()
				if full[s][-1]=='.':
					full[s] = full[s][:-1]
					meanings[a] = full[s]

			if len(full)>1:
				meanings[a] = full[0]
				full[1] = full[1][0].lower() + full[1][1:len(full[1])]
				examples.append(full[1])

		definition = ''
		for a in meanings:
			definition = definition+a+'; '
		definition = definition[:-2]
		sentences = ''

		Word = word[0].upper() + word[1:len(word)]

		for a in range(len(examples)):
			sentences = sentences + '\te.g. {}\n'.format(examples[a])

		explanation = ('{} - {}\n'+sentences).format(Word, definition)
	except:
		explanation = '{} -  ???'.format(word)
	return explanation

def writeDef(num, defi):
	file = 'GRE_VOCAB/GRE3000_{}.txt'.format(num//100+1)
	f = None
	if num%100==0:
		f = open(file, 'w+')
		f.write('GRE3000 - {}~{}'.format(num+1, num+100) + '\n\n\n')
	else:
		f = open(file, 'a')
	f.write(defi+'\n')
	if num%10==9:
		f.write('~~~ {} ~~~'.format(num+1) + '\n\n')
	f.close()


def fillDefs(start, vocab):
	for a in range(start, len(vocab)):
		defi = getDefinition(vocab[a])
		writeDef(a, defi)

def makeVocab(start, url):
	vocab = getVocabulary(url)
	fillDefs(start, vocab)


pp = pprint.PrettyPrinter(indent=2)
url_vocab = 'https://www.vocabulary.com/lists/94175'

print(getDefinition('animate'))

makeVocab(0, url_vocab)
'''







############### printing out GRE 300 vocabulary from a website ##################
'''
import pprint		# adusting print format
import requests		# getting web information
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bSoup

# getting page with requests module
url = 'https://www.vocabulary.com/lists/94175'
# url = 'https://www.google.com'
page = requests.get(url)
content = page.content

# pp = pprint.PrettyPrinter(indent=2)
soup = bSoup(content, 'html.parser')

words = soup.find_all('li', class_='entry learnable')
# print(words[0].text.split())
# pp.pprint(words)
vocabulary = []

for word in words:
	vocab = word.text.split()[0]
	vocabulary.append(vocab)

for a in range(len(vocabulary)):
	word = vocabulary[a]
	vocabulary[a] = word[0].upper()+word[1:len(word)]

# pp.pprint(vocabulary)

for a in range(11):
	f = open('GRE_VOCAB/gre{}.txt'.format(a), 'w+')
	f.write('GRE3000 - {0}~{1}\n\n'.format(a*300+1, a*300+300))
	for s in range(300):
		num = 300*a+s
		if num<len(vocabulary):
			f.write(vocabulary[300*a+s]+' - \n')
			f.write('\te.g. \n\n')
		else:
			break

	f.close()
'''








############### trying to get an iPhone on shopee ##################
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium import webdriver
import unittest
import time

driver = webdriver.Safari()
driver.get('https://shopee.tw/NARUKO-%E8%8C%B6%E6%A8%B9%E6%8A%97%E7%97%98%E7%B2%89%E5%88%BA%E5%AF%B630ml-i.28944793.454821444')
buyBtn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-solid-primary.btn--l.YtgjXY")
# buy.click()
buySection = driver.find_element(By.CLASS_NAME, '_2O0llP')
# print(buySection, buyBtn)
touches = TouchActions(driver)
touches.move(10, 20)
touches.perform()
# actions = ActionChains(driver)
# # actions.move_to_element(buySection)
# actions.click(buyBtn)
# actions.perform()
# print(buyBtn)
'''






def getContent(url):
	page = requests.get(url)
	return page.content

def getSoup(url):
	return bs(getContent(url), 'html.parser')


