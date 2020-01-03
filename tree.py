import requests
from bs4 import BeautifulSoup

def getChildrenLinks(iGen, aLinks):
    print "GEN #" + str(iGen) + " " + str(len(aLinks)) + " links";
    iGen = iGen + 1
    if iGen > 2: #safegaurd to not explode us
        return 0
    oHTML = requests.get(sRootUrl) # get HTML for the given link
    oSoup = BeautifulSoup(oHTML.content, 'html.parser')
    # for oLink in oSoup.find_all('a'):
    #     print sLink
    #     print oLink.get('href')
    #     iLinks = iLinks + getChildrenLinks(iGen + 1, oLink.get('href'))
    getChildrenLinks(iGen, oSoup.find_all('a'))
    
    
# def getChildrenLinks(iGen, sLink):
#     iLinks = 0 # initialize links for this generation to 0
#     # iGen = iGen + 1
#     if iGen > 2: #safegaurd to not explode us
#         return 0
#     oHTML = requests.get(sRootUrl) # get HTML for the given link
#     oSoup = BeautifulSoup(oHTML.content, 'html.parser')
#     for oLink in oSoup.find_all('a'):
#         print sLink
#         print oLink.get('href')
#         iLinks = iLinks + getChildrenLinks(iGen + 1, oLink.get('href'))
#     print "GEN #" + str(iGen) + " " + str(iLinks) + " links";

sRootUrl = ["https://en.wikipedia.org/wiki/Main_Page"];
getChildrenLinks(0, aLinks)

