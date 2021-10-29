<<<<<<< HEAD
import requests,json
import xml.etree.ElementTree as ET 
from xml.dom import minidom
def main(search='0679720219',*args):

  key = '9QfFG2IhANpg4EixwogLA'
  payload = {'q':search, 'key':key}
  res = requests.get(f"https://www.goodreads.com/search/index.xml", params=payload)
  #parse the xml response to a DOM tree
  xmldom = minidom.parseString(res.content)
  #print(xmldom.toprettyxml())
  #get the value of the average rating childNode
  txt = xmldom.getElementsByTagName('average_rating')[0].childNodes[0].nodeValue
  print(txt)
  
    
    
    
   
    
if __name__=='__main__':
  main()
   # parseXML()
=======
import requests,json
import xml.etree.ElementTree as ET 
from xml.dom import minidom
def main(search='0679720219',*args):

  key = '9QfFG2IhANpg4EixwogLA'
  payload = {'q':search, 'key':key}
  res = requests.get(f"https://www.goodreads.com/search/index.xml", params=payload)
  #parse the xml response to a DOM tree
  xmldom = minidom.parseString(res.content)
  #print(xmldom.toprettyxml())
  #get the value of the average rating childNode
  txt = xmldom.getElementsByTagName('average_rating')[0].childNodes[0].nodeValue
  print(txt)
  
    
    
    
   
    
if __name__=='__main__':
  main()
   # parseXML()
>>>>>>> e91c249518180045abfd580520895a5a4e9f2171
