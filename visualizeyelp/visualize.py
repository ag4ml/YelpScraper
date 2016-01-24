#Abhishek Gupta (ag4cb@virginia.edu)

import json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def visualize_categories(restaurants):
    categories = Counter(sorted([category for category in restaurant['categories'] for restaurant in restaurants]))
    index = np.arange(len(categories))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = plt.bar(index, tuple(categories.values()), width)
    plt.xlabel('Categories')
    plt.ylabel('Number of Category')
    plt.title('Categories of restaurants in Charlottesville')
    plt.xticks(index + width, tuple(categories.keys()))
    plt.show()



def main():
    restaurants = None
    with open("../scrapeyelp/restaurants.json") as f:
        restaurants = json.load(f)
    visualize_categories(restaurants)
    #visualize_prices(restaurants)

if __name__ == '__main__':
        main()
