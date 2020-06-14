import os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

inputfname = sys.argv[1];
oputfname = os.path.splitext(inputfname)[0];
numpages = int(sys.argv[2]);

inputpdf = PdfFileReader(open(inputfname, "rb"))

i = 0

while i < inputpdf.numPages:
	output = PdfFileWriter()

	for i in range(i, (i+numpages)):
		if i>= inputpdf.numPages:
			i -= 1
			break
		else:
			output.addPage(inputpdf.getPage(i))
    
	with open(oputfname + "-%s.pdf" % (i+1), "wb") as outputStream:
		output.write(outputStream)
	i += 1
