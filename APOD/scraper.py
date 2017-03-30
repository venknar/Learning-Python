import urllib.request
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Download the Basic Content or the Index Page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "APOD_Pictures"
content = urllib.request.urlopen(base_url).read()

# Parse the contents of the Page using the Beautiful Soup.
for link in BeautifulSoup(content, "lxml").findAll("a"):
    href = urljoin(base_url, link["href"])

    # Follow the Link and download the contents in them.
    innerContent = urllib.request.urlopen(href).read()
    # In each page look for the page content that has the image reference.
    for img in BeautifulSoup(innerContent, "lxml").findAll("img"):
        img_href = urljoin(href, img["src"])
        # Downloading the image from the location.
        print("Downloading Image: ", img_href) 
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))