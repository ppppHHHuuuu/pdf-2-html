import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('thanh123400', '74959ed09d7ba61d68f3e194ce6db180')

    # run the conversion and write the result to a file
    client.convertFileToFile('./pdf.html', 'test_css_together.pdf')

except pdfcrowd.Error as why:
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
    raise