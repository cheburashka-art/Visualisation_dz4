import zipfile, xml.etree.ElementTree as ET, json, os, glob, re
from datetime import datetime, timedelta
root=os.getcwd(); z=zipfile.ZipFile(os.path.join(root,'df.xlsx')); ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
sh=ET.fromstring(z.read('xl/worksheets/sheet1.xml')); rows=sh.findall('.//m:row',ns)
def cell(c):
 v=c.find('m:v',ns); inline=c.find('m:is',ns)
 if inline is not None: return ''.join(t.text or '' for t in inline.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'))
 return v.text if v is not None else ''
def excel_date(v):
 try: return (datetime(1899,12,30)+timedelta(days=float(v))).strftime('%Y-%m-%d')
 except: return ''
raw=[]
for r in rows[1:]:
 vals=[cell(c) for c in r.findall('m:c',ns)]
 if len(vals)>=13:
  raw.append({'order':vals[0],'date':excel_date(vals[1]),'status':vals[2],'created':vals[3],'delivered':vals[4],'address':vals[5],'name':vals[6],'category':vals[7],'price':float(vals[8] or 0),'discountPrice':float(vals[9] or 0),'discount':float(vals[10] or 0),'quantity':float(vals[11] or 0),'total':float(vals[12] or 0)})
json.dump(raw,open(os.path.join(root,'data.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
manifest={}
for f in glob.glob(os.path.join(root,'items','*')):
 base=os.path.basename(f)
 if base.startswith('.') or base.startswith('._'): continue
 m=re.match(r'(\d+)_',base)
 if m: manifest.setdefault(m.group(1), 'items/'+base)
json.dump(manifest,open(os.path.join(root,'images.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print('rows',len(raw),'images',len(manifest))
print('date',raw[0]['date'],'sample',raw[0]['name'])
