#Abhishek Gupta (ag4cb@virginia.edu)

import json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def visualize_categories(restaurants):
    categories = Counter(sorted([category for restaurant in restaurants for category in restaurant['categories']]))
    index = np.arange(len(categories))+0.5
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(index, tuple(categories.values()), width=width)

    ax.set_ylabel('Number of Category')
    ax.set_title('Categories of restaurants in Charlottesville')
    ax.set_xticks(index+width)
    ax.set_xticklabels(tuple(categories.keys()), rotation=90)
    plt.subplots_adjust(bottom=0.4)
    plt.tight_layout()
    plt.show()

def visualize_prices(restaurants):
    prices = Counter(sorted([restaurant['price'] for restaurant in restaurants]))
    total = sum(prices.values())
    sizes = [float(x)/total*100 for x in prices.values()]
    labels = prices.keys()
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def main():
    restaurants = None
    with open("../scrapeyelp/restaurants.json") as f:
        restaurants = json.load(f)
    visualize_categories(restaurants)
    visualize_prices(restaurants)

if __name__ == '__main__':
        main()
