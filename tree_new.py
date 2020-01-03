import requests
import validators
import anytree
import base64
import os
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from bs4 import BeautifulSoup

# def getChildrenLinks(iGen, aLinks):
#     print "GEN #" + str(iGen) + " " + str(len(aLinks)) + " links"
#     iGen = iGen + 1
#     if iGen > 2: #safegaurd to not explode us
#         return 0
#     oHTML = requests.get(sRootUrl) # get HTML for the given link
#     oSoup = BeautifulSoup(oHTML.content, 'html.parser')
#     # for oLink in oSoup.find_all('a'):
#     #     print sLink
#     #     print oLink.get('href')
#     #     iLinks = iLinks + getChildrenLinks(iGen + 1, oLink.get('href'))
#     getChildrenLinks(iGen, oSoup.find_all('a'))
    
    
def getChildrenLinks(iGen, sParentLink, oParentNode):
    iGen = iGen + 1 # in next generation
    if iGen > 2: #safegaurd to not explode us
        return
    oHTML = requests.get(sParentLink) # get HTML for the given link
    oSoup = BeautifulSoup(oHTML.content, 'html.parser') # html for this link
    for oLink in oSoup.find_all('a'):
        print "GEN = " + str(iGen)
        sLink = oLink.get('href')
        print sLink
        if sLink is None:
            continue
        if not validators.url(sLink):
            continue
        if 'https:' not in sLink and 'http:' not in sLink:
            sLink = "https:" + sLink
        oNewParent = Node(sLink, parent=oParentNode)
        getChildrenLinks(iGen, sLink, oNewParent)
        aLinks.append({"iGen": iGen, "sParentLink": sParentLink, "sLink": sLink})

aLinks = []
aLinks.append({"iGen": 0, "sParentLink": None, "sLink": "https://chrisfrew.in"})
oRootNode = Node("https://chrisfrew.in")
getChildrenLinks(0, "https://chrisfrew.in", oRootNode)
    
DotExporter(oRootNode).to_dotfile("chrisfrew.dot") # don't forget to add 'ratio' and other goodies:

# len=3.0;
# ratio=10.0;
# node [shape = circle, fontsize = 6]; # still needs work

