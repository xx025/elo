from src.inti_seting import con_db
import os

def generatehtmlpage():
    str1='''
    <table style="border-collapse:collapse;word-break:break-all;font-size:14px;width:900px;">
        <tr style="color:#000;background-color:#48a6fb;font-size:18px;">
            <th colspan="4" style="border-color:#000;border-width:1px;border-style:solid;padding:15px;min-width:100px;text-align:center;">
                BeautifulGirlRank</th>
        </tr>
        <tr>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">
                照片</td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">
                编号</td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">
                得分</td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">
                参比次数</td>
        </tr>'''
    con_db.getcon()
    list=con_db.get_all("select pothopath,id,score,comNum from girls order by score desc")
    con_db.close()
    with open("src\index.html", mode='wt', encoding='utf-8') as ff:
        for i in list:
            str2 = '''<tr><td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">
            <img src="file:///{0}" style="width:50px;height: 50px;"></td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">{1}</td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">{2}</td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;min-width:100px;text-align:center;">{3}</td>
            </tr>'''.format(os.path.abspath(i[0]),i[1],int(i[2]),i[3])
            str1+=str2
        ff.write(str1+'''</table>''')
    import webbrowser
    webbrowser.open_new_tab("src\index.html")

