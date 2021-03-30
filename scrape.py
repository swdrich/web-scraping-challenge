def scrape():

    scrape_dict = {}

    # Import dependencies
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup as bs
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape Nasa Mars News
    nasa_url = "https://redplanetscience.com/"
    browser.visit(nasa_url)
    html = browser.html
    nasa_soup = bs(html, 'html.parser')

    # Scrape top news article
    results = nasa_soup.find('div', class_="list_text")
    news_title = results.find('div', class_="content_title").text
    news_teaser = results.find('div', class_="article_teaser_body").text
    print(news_title)
    scrape_dict.update({"news_title": news_title})
    print(news_teaser)
    scrape_dict.update({"news_teaser": news_teaser})

    # Scrape JPL Mars Images
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)
    html = browser.html
    jpl_soup = bs(html, 'html.parser')

    # Get Mars image link
    results = jpl_soup.find('img', class_="headerimage fade-in")["src"]
    print(results)

    # Create full image link
    featured_image_url = f'{jpl_url}{results}'
    print(featured_image_url)
    scrape_dict.update({"featured_image_url": featured_image_url})

    # Mars Facts
    facts_url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(facts_url)

    # Create Mars / Earth df
    mars_earth_df = tables[0]

    # Set indices
    # Columns
    mars_earth_df.columns = mars_earth_df.iloc[0]
    mars_earth_df = mars_earth_df.drop(mars_earth_df.index[0])
    mars_earth_df
    # Index
    mars_earth_df = mars_earth_df.set_index(mars_earth_df.iloc[:,0])
    mars_earth_df = mars_earth_df.drop(labels="Mars - Earth Comparison", axis=1)
    mars_earth_df

    # Create html table from data
    mars_html = mars_earth_df.to_html()
    mars_html = mars_html.replace("\n", "")
    scrape_dict.update({"mars_html": mars_html})

    # Mars Hemisphere Images
    guss_url = "https://marshemispheres.com/"
    browser.visit(guss_url)

    # Get links to images
    html = browser.html
    guss_soup = bs(html, "html.parser")
    results = guss_soup.find_all('div', class_='description')

    url_list = []

    for result in results:
        url_dict = {}
        link = result.find('a')
        title = result.find('h3').text
        img_url = link['href']
        url_dict.update({"title": title})
        url_dict.update({"img_url": img_url})
        url_list.append(url_dict)

    scrape_dict.update({"url_list": url_list})    
    # Close browser
    browser.quit() 