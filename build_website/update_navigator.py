import re
import os

def updateNav(websitePath):
  navPath = '../block_nav.html'

  # Compile regex
  navigator = re.compile('<nav>.*</nav>', re.DOTALL)

  ## Open websites and put their content in string variables
  websiteObject = open(websitePath, 'r')
  website = websiteObject.read()

  navObject = open(navPath, 'r')
  nav = navObject.read()

  ## Sub
  isNav = navigator.search(website)
  if isNav:
    return navigator.sub(nav, website)
  else:
    return website
    
  navObject.close()
  websiteObject.close()

if __name__ == '__main__':
  rootDir = "/home/rolando/Documents/rolandomunoz.github.io/"
  fileList = os.listdir(rootDir)
  for ifile in fileList:
    if ifile.endswith('.html') and not ifile.startswith('block_'):
      filePath= os.path.join(rootDir, ifile)
      html_text= updateNav(filePath)
      f = open(filePath, 'w')
      f.write(html_text)
      f.close()        
  print('Done!')
'''  for root, dirs, files in os.walk(rootDir):
    for ifile in files:
      if filePath.endswith('.html'):

'''
