from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import csv
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter, A4
from tqdm import tqdm
import numpy as np
from PIL import Image

pdfmetrics.registerFont(TTFont('Roboto', 'fonts\Roboto-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Robotomono', 'fonts\RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Ember-bold', 'fonts\AmazonEmber_Bd.ttf'))
packet = io.BytesIO()


# def rearrange_field(full_field, end, name_check):
#     if name_check==1:
#         dynamic_variable =6
#     else:
#         dynamic_variable =5
#     field_list = full_field.strip().split(" ")
#     field_size_list =[]
#     field_rearrange_list=[]
#     field_choose_len =0
#     temp_field=""
#     for field in field_list:
#         # print("field",field)
#         field_choose_len+=len(field)+1
#         # print("field len check",field_choose_len)
#         if field:
#             if field_choose_len*dynamic_variable< end:
#                 if field == field_list[len(field_list)-1]:
#                     # print("inside if if")
#                     if field == field_list[0]:
#                         temp_field+=field
#                     else:
#                         temp_field+=" "+field
#                     temp_field=temp_field.strip()
#                     # print("temp_field",temp_field)
#                     field_rearrange_list.append(temp_field)
#                     field_size_list.append(len(temp_field))
#                     temp_field=""
#                     field_choose_len=0

#                 else:
#                     # print("inside if else")
#                     temp_field+=" "+field
#                     temp_field=temp_field.strip()
#             else:
#                 if field == field_list[len(field_list)-1]:
#                     # print("inside else if")
#                     field_rearrange_list.append(temp_field)
#                     field_size_list.append(len(temp_field))
#                     field_rearrange_list.append(field)
#                     field_size_list.append(len(field))

#                 else:
#                     # print("inside else")
#                     field_rearrange_list.append(temp_field)
#                     field_size_list.append(len(temp_field))
#                     temp_field = field
#                     field_choose_len=len(field)+1

#     print("field_rearrange,field_size",field_rearrange_list,field_size_list)
#     return field_rearrange_list



# create a new PDF with Reportlab
def createpdf(full_name, full_firm, category):

    packet = io.BytesIO()

    start = 150
    end = 570

    full_name = full_name.upper()
    full_firm = full_firm.upper()



    '''
    Role rearrange -> form groups of role that could fit in one line

    Possible approach - 1) decrease size of whole text to fit into single line

                        2) split the text to fit into multiple lines
    Example: Consultant System Administration
    Expected Outcome: Consultant System
                      Administration 

    ''' 


    cert_pagesize=((2000,1414))    
    can = canvas.Canvas(packet, pagesize=cert_pagesize)
    recent_offset = 0
    # for i,name in enumerate(name_list):
    can.setFont('Ember-bold', 30)
    x_pos = start + abs((end-start)/2 - len(full_name)*15)
    # print(x_pos,len(full_name))
    print("full name",full_name)
    can.drawString(x_pos+30, 290, full_name)
    
    # firm_rearrange_list = rearrange_field(full_firm,end,0)

    # for i,firm in enumerate(firm_rearrange_list):

    #     can.setFont('Roboto', 8)
    #     can.setFillColorRGB(0.09765625,0.16796875,0.247)
    #     if i==0:
    #         can.drawString(8, recent_offset-13-13-(i*10), firm)
    #         last_offset = recent_offset-13-13-(i*10)
    #     else:
    #         can.drawString(8, recent_offset-26-(i*8), firm)


    can.save()
   

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # read your existing PDF
    if category.lower() == "attendee":
        existing_pdf = PdfFileReader(open("template\\attendee.pdf", "rb"))

    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0) 
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)

    # finally, write "output" to a real file
    outputStream = open("test-cert.pdf", "wb")
    output.write(outputStream)
    outputStream.close()



if __name__=="__main__":
    createpdf("Siddharth Shivkumar","Cochin University of Science and Technology","attendee")
    
    
    # with open('attendees_details_second_round.csv', 'r') as readFile:
    #     reader = csv.reader(readFile)
    #     l = 0
    #     for i,row in enumerate(reader):
    #         print("################# processing",i,"################")
    #         if l!=0:
    #             name = row[0] #this is the name of the individual
    #             category = row[2] #this is the category of the individual
    #             firm = row[1] #this is the firm of the individual
    #             if name:
    #                 createpdf(name,firm,category)
            

    #         l+=1
