from bs4 import BeautifulSoup as bs
import requests 
from splinter import Browser
import pandas as pd



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    # Get News Title and News P
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)  

    html = browser.html
    soup = bs(html, "html.parser") 

    title = soup.find('div', class_='content_title').text
    excerpt = soup.find('div', class_='rollover_description_inner').text
    mars_data["news_title"] = title.replace('\n', '')
    mars_data["news_p"] = excerpt.replace('\n', '')

    # Get Featured URL
    #url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    #html2 = browser(url2)
    #soup = bs(html2, "html.parser") 

    #link = soup.find('div', class_='default floating_text_area ms-layer')
    #image_url = link.a.attrs['data-fancybox-href']
    #mars_data["featured_image_url"] = 'https://www.jpl.nasa.gov/' + image_url

    #  Get Mars weather
    #url = 'https://twitter.com/marswxreport?lang=en'
    #html = browser.html
    #soup = bs(html, "html.parser")

    #marsweather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    #mars_weather = marsweather.text

     #  Get Hemisphere images
    #url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'lxml')

     #  Store data in a dictionary
    #mars_data = {"news_title": news_title,
    #    "news_p": news_p,
    #    "featured_image_url": featured_image_url,
    #    "mars_weather": max_temp}

     #  Close the browser after scraping
    #browser.quit()

    # Return results
    return mars_data

if __name__ == "__main__":
    print(scrape())




