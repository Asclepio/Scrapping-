
# Asegurate de instalar beatifulsoup y request
pip install beautifulsoup4
pip install requests

import requests
from bs4 import BeautifulSoup

# Usar el modulo requests , usamos la funcion  "get"
# Acceder al sitio web
# argumento de la funcion es "get:
result = requests.get("https://www.google.com/")

# Para asegurarse de que puede ingresar al sitio, debe tener como respuesta
# 200 OK response:

print(result.status_code)

# Poder revisar el HTTP header del sitio:
print(result.headers)

# For more information on HTTP headers and the information
# one can obtain from them, you may consult:
# https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

# Now, let us store the page content of the website accessed
# from requests to a variable:
src = result.content
#print (src)

# Now that we have the page source stored, we will use the
# BeautifulSoup module to parse and process the source.
# To do so, we create a BeautifulSoup object based on the
# source variable we created above:
soup = BeautifulSoup(src, 'lxml')

# Now that the page source has been processed via Beautifulsoup
# we can access specific information directly from it. For instance,
# say we want to see a list of all of the links on the page:
links = soup.find_all("a")
print(links)
print("\n")

# Perhaps we just want to extract the link that has contains the text
# "About" on the page instead of every link. We can use the built-in
# "text" function to access the text content between the <a> </a>
# tags.
for link in links:
  if "About" in link.text:
       print(link)
       print(link.attrs['href']
