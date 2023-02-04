# starlet-certificate

Use this repo to generate certificates for [Starlet](https://bit.ly/ME-starlet)

The code has been tested on Python 3.9.13
1. Begin by installing the dependencies using pip install -r requirements.txt
2. Run [cert-pdf.py](cert-pdf.py)
3. You will obtain a pdf named test-cert.pdf


To run with custom inputs, change the values in the main function. The parameters to createpdf function is in the order (name,firm,category) where category is the type of participant (attendee,mentor,speaker, etc). 

The code is WIP and works only for the name field. The code doesn't handle long field issues yet.

* Template folder - Stores the certificate templates 
* Fonts folder - Stores the fonts in .ttf format
