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
    browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html 
    soup = bs(html, "html.parser") 

    link = soup.find('div', class_='default floating_text_area ms-layer')
    image_url = link.a.attrs['data-fancybox-href']
    mars_data["featured_image_url"] = 'https://www.jpl.nasa.gov/' + image_url

    #  Get Mars weather
    browser = init_browser()
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    marsweather = weather.text
    mars_data["mars_weather"] = marsweather.replace('\n', '')

     #  Get Hemisphere images
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    link = soup.find('div', class_='downloads')
    mars_data["cerberus_url"] = link.a.attrs['href']

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    link = soup.find('div', class_='downloads')
    mars_data["schiaparelli_url"] = link.a.attrs['href']

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    link = soup.find('div', class_='downloads')
    mars_data["syrtis_major_url"] = link.a.attrs['href']

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    link = soup.find('div', class_='downloads')
    mars_data["valles_marineris_url"] = link.a.attrs['href']
    
     #  Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

#if __name__ == "__main__":
#    print(scrape())




