from rich import print

# def opo(row):
#     # aaa = f'''
#     #     <tr>
#     #         <td><input type="number" name="table_2_col-1_row-{row}" id="table_2_col-1_row-{row}"></td>
#     #         <td><input type="number" name="table_2_col-2_row-{row}" id="table_2_col-2_row-{row}"></td>
#     #     </tr>
#     # '''
#     aaa = f'''
#         <tr>
#             <td><input type="number" name="table_3_col-1_row-{row}" id="table_3_col-1_row-{row}"></td>
#             <td><input type="number" name="table_3_col-2_row-{row}" id="table_3_col-2_row-{row}"></td>
#             <td><input type="number" name="table_3_col-3_row-{row}" id="table_3_col-3_row-{row}"></td>
#         </tr>
#     '''
#     return aaa
# for i in range(1, 18):
#     print(opo(i))

import aspose.words as aw

# Load the document from disk
doc = aw.Document("result.docx")

# Enable round-trip information
saveOptions = aw.saving.HtmlSaveOptions()
# saveOptions.export_roundtrip_information = True 
saveOptions.export_roundtrip_information = False


# Save the document as HTML
doc.save("result.html", saveOptions)
# doc.save("result.pdf", saveOptions)


textdelstart = r'<p style="margin-top:0pt; margin-bottom:10pt; line-height:115%; font-size:12pt"><span style="font-weight:bold; color:#ff0000">Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.</span></p>'
testdelend = r'<p style="margin-top:0pt; margin-bottom:10pt; line-height:115%; font-size:12pt"><span style="font-weight:bold; color:#ff0000">Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/</span></p>'
imagedell = r'<div><div style="clear:both"><p style="margin-top:0pt; margin-bottom:10pt"><span style="height:0pt; display:block; position:absolute; z-index:-65537"><img src="result.001.png" width="576" height="314" alt="" style="margin-top:239.45pt; position:absolute" /></span><span>&#xa0;</span></p></div>'

with open("result.html", "r", encoding='utf-8') as file:
    text = file.read()
    text = text.replace(textdelstart, '')
    text = text.replace(testdelend, '')
    text = text.replace(imagedell, '')
    text = text.replace('><', '>\n<')
    file.close()
with open("result.html", "w", encoding='utf-8') as file:
    file.write(text)
    file.close()
        

