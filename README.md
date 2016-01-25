# YelpScraper
Scrape the 100 most popular restaurants in Charlottesville from Yelp and analyze the data

This project uses the Scrapy library to parse the 100 most popular restaturants from Yelp's Charlottesville page.
Then, after storing the result as a json file, the data is visualized using the Matplotlib library.

#Installing

Install the requirements using pip:

```
pip install -r requirements.txt
```

#Running

To run the spider and generate the data as a json file:

'''
scrapy crawl yelp -o filenamehere.json
'''

The previous run of this spider generated a restaurants.json file (already included).

Lastly, to visualize the data and view the figures that it produces, cd into the visualizeyelp directory and run:

'''
python visualize.py
'''

The figures (already included) that this will generate compare the different categories of food and their pricyness.

DISCLAIMER: The spider works as of this commit but may stop functioning if Yelp's website layout changes drastically
