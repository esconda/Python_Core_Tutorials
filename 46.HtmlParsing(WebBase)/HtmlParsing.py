# Author: Burak Dogancay
from multiprocessing.sharedctypes import Value
from turtle import title
from bs4 import BeautifulSoup
from pyquery import PyQuery

def htmlParsing():
  myData = """
  <ul>
    <li class="item">item1</li>
    <li class="item">item2</li>
    <li class="item">item3</li>
  </ul>
  """
  soup = BeautifulSoup(myData,"html.parser")
  
  for item in soup.select("li.item"):
    print(item.get_text())
    
def beatSoupFunc():
  data = """
  <div>
    <label>Name:</label>
    John Smith
  </div>
  """
  
  soup = BeautifulSoup(data, "html.parser")
  label = soup.find("label", text="Name:")
  print("--BEAUTIFUL SOUP EXAMPLE--")
  print(label.text)
  print(label.next_sibling.strip())
  print("---------------------")
    
def pyQueryExample():
  html = """
  <h1>Sales</h1>
  <table id="table">
  <tr>
    <td>Burak</td>
    <td>32</td>
  </tr>
  <tr>
    <td>Yunus Emre</td>
    <td>28</td>
  </tr>
  <tr>
    <td>Koray</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Melih</td>
    <td>25</td>
  </tr>
  </table>
  """
  
  doc = PyQuery(html)
  title = doc('h1').text()
  print("--ATTRIBUTE KEYS--")
  print("H1 attribute is :", title)
  print("---------------------")
  
  rows = doc('#table > tr')
  print("--ATTRIBUTE KEYS--")
  for row in rows:
    name = PyQuery(row).find('td').eq(0).text()
    value = PyQuery(row).find('td').eq(1).text()
    print("%s\t %s" % (name, value))
  print("---------------------")
  
  
def main():
  htmlParsing()
  pyQueryExample()
  beatSoupFunc()
  #writingSubprocess()


if __name__ == '__main__':
    main()