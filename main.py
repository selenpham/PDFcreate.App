from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P",unit = "mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
# print(type(pdf))
df = pd.read_csv("topics.csv")

pdf.add_page()  
pdf.set_font(family = "arial", style="B", size =18)
pdf.cell(w=0, h=12,txt= "This is my notebook", align="C", ln=1, border=1)


for index, row in df.iterrows():

    # for i in range(row["Pages"]):
    #     pdf.add_page()

    pdf.add_page()  

# set the header
    pdf.set_font(family = "arial", style="B", size =12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12,txt= row["Topic"], align="L", ln=1)

    for y in range(20,298,10):
        pdf.line(10,y,200,y)

#Set the footer
    pdf.ln(265)
    pdf.set_font(family = "arial", style="B", size =8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10,txt= row["Topic"], align="R")


    for i in range(row["Pages"]-1):
        pdf.add_page()
# set header
        pdf.set_font(family = "arial", style="B", size =12)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12,txt= row["Topic"], align="L", ln=1)
        for y in range(20,298,10):
            pdf.line(10,y,200,y)

# set footer

        pdf.ln(265)
        pdf.set_font(family = "arial", style="B", size =8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10,txt= row["Topic"], align="R")

pdf.output("ouput.pdf")