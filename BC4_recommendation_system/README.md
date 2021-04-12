# BC4: ManyGiftsUK recommender system

**Problem type:** Recommender System

**Submission date:** 03-05-2021 | 11:59 pm

## General Context 

Recommender systems have become a very important part of the retail industries by providing decision-making support to its customers. Several studies such as Iyengar and Lepper (2000) have proved that when faced with easy choices, customers tend to buy more. Given the number of possible choices available, especially for online shopping, having some extra guidance on these choices can really make a difference and lead to an increase in sales. As an example, 35% of Amazon sales come from recommendations. Moreover, recommender systems are a useful alternative to search algorithms since they help users discover items they might not have found otherwise.

Recommender systems usually make use of either or both collaborative filtering and content-based filtering. Collaborative filtering approaches build a model from a user's past behavior (items previously purchased or selected and/or numerical ratings given to those items) as well as similar decisions made by other users. It relies solely on user/ item interaction data. In the opposite side, content-based filtering relies on item attribute data and it uses this kind of data to recommend items with similar properties to the ones a user has liked in the past. Modern recommender systems typically combine one or more approaches into a hybrid system.

There are two kinds of user/ item interaction data available: explicit and implicit.
- Explicit: A score, such as a rating or a like
- Implicit: Not as obvious in terms of preference, such as a click, view, or purchase

The most common example of explicit data discussed is movie ratings, which are given on a numeric scale. We can easily see whether a user enjoyed a movie based on the rating provided. The problem, however, is that most of the time, people don’t provide ratings at all, so the amount of explicit data available is quite scarce. Sometimes we get access to data about certain interactions between users and items that give us some degree of certainty on whether a user likes an item - this is what we call implicit data. With implicit data, the more interactions a user has with a item, the more certain we are about its preference. A common example might be viewing a product in Amazon website or even purchasing it.

## Business Situation 

ManyGiftsUK is a UK-based and registered non-store online retailer with some 80 members of staff. The company was established in 1981 mainly selling unique all-occasion gifts. For years in the past, the merchant relied heavily on direct mailing catalogues, and orders were taken over phone calls. It was only 2 years ago that the company launched its own web site and shifted completely to the web. Since then the company has maintained a steady and healthy number of customers from all parts of the United Kingdom and the world, and has accumulated a huge amount of data about many customers. The company also uses Amazon.co.uk to market and sell its products. 

With this new data the company expects to build a recommender system that is able to facilitate user choices by recommending items the user likes and improve user experience when making purchases on its website. A particular challenge is the cold start problem - how can we suggest relevant items to new customers?

The customer transaction dataset held by the merchant has 8 variables as shown below, and it contains all the transactions occurring between 01/12/2010 and 09/12/2011. Over that particular period, there were 25900 valid transactions in total, associated with 4070 unique items and 4372 customers from 38 different countries. The dataset has 541909 instances, each for a particular item contained in a transaction. Also it is important to note that many of ManyGiftsUK customers are wholesalers.

## Metadata

| Name                        | Meaning                                                                                                                                                        |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InvoiceNo                   | Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation.    |
| StockCode                   | Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.                                                            |
| Description                 | Product (item) name. Nominal.                                                                                                                                  |
| Quantity                    | The quantities of each product (item) per transaction. Numeric.                                                                                                |
| InvoiceDate                 | Invoice Date and time. Numeric, the day and time when each transaction was generated.                                                                          |
| UnitPrice                   | Unit price. Numeric, Product price per unit in pounds.                                                                                                         |
| CustomerID                  | Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.                                                                        |
| Country                     | Country name. Nominal, the name of the country where each customer resides.                                                                                    |


## Expected Outcomes

1. Explore the data and build models to answer the problems:
    1. Recommender system: the website homepage offers a wide range of products the user might be interested on
    2. Cold start: offer relevant products to new customers
2. Implement adequate evaluation strategies and select an appropriate quality measure
3. In the deployment phase, elaborate on the challenges and recommendations in implementing the recommender system

## References

Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating: Can one desire too much of a good thing?. Journal of personality and social psychology, 79(6), 995.

Hu, Y., Koren, Y., & Volinsky, C. (2008). Collaborative filtering for implicit feedback datasets. 2008 Eighth IEEE International Conference on Data Mining, 263–272.
