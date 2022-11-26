from bs4 import BeautifulSoup
import requests

url = "https://a-z-animals.com/animals/african-bullfrog/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")


s = soup.select_one('#single-animal-text > figure.wp-block-image.size-large > img')


print(s.get("src"))