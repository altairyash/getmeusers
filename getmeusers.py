import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

file_list = os.listdir('pdf/')
f2 = open('users.txt','w')

for i in file_list:
	fp = open(f'pdf/{i}', 'rb')
	parser = PDFParser(fp)
	doc = PDFDocument(parser)
	s = doc.info[0]
	f2.write(s["Creator"].decode("utf-8") + '\n')
