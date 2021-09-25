import validators
from bs4 import  BeautifulSoup
import requests as req
from flask import Flask, request, render_template 

# Flask constructor
app = Flask(__name__)   
@app.route('/', methods =["GET", "POST"])
def formaction():
    if request.method == "POST":
       fq = request.form.get("flink")
       return action(fq+"yayayaya")
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()
def validate(url):
  flag=validators.url(url)
  return flag
def identifyBrokenLinks(uniqueExternalLinks):
    errorcodes=[404,408,500,502,503,504]
    count = 0
    length_uniqueExternalLinks = len(uniqueExternalLinks)
    
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

    brokenLinksList = []

    for link in uniqueExternalLinks:
        count = count + 1
        print("Checking external link #",count," out of ",length_uniqueExternalLinks,".")
        try:
          statusCode = req.get(link, headers=user_agent).status_code
          if statusCode in errorcodes:
            brokenLinksList.append(link)
          else:
            pass
        except:
          brokenLinksList.append(link)
    return brokenLinksList


def action(query):
  if query!=None:
    content=req.get(query).text
    soup=BeautifulSoup(content,'lxml')
    linksn=[]
    urls=soup.find_all('a',href=True)
    for url in urls:
      toggler=validate(url['href'])
    if toggler==True:
      linksn.append(url['href'])
    brokelinks=identifyBrokenLinks(linksn)
    return brokelinks
