# BC3: Instacart Market Basket Analysis 

**Problem type:** Market Basket Analysis

**Submission date:** 12-04-2021 | 11.59pm

## General Context 

Nowadays, understanding the purchasing patterns/behaviors of consumers is a
key task for any retail company. Identifying the relationships between the
different types of products, e.g, complementary, substitute, inferior and
convenience goods, provides the company a wholistic view about its customers
and the portfolio of products it has to offer.

Specifically, market basket analysis is a data mining technique that is used
to inform a retailer about products that are frequently bought together, which
of these are seen as substitutes to one another and customer segmentation. The
retailer uses this information to then optimize the store's layout, develop
cross-promotional programs and develop different marketing strategies for its
customers.
 
## Business Situation 

Instacart is an american company that provides a grocery delivery and pick-up
service via a website or mobile app in the United States and Canada.

Within their platform, users can select items from a wide portfolio of
products, while allowing you to better manage your shopping by speaking with
the personal shopper assigned to you. Your groceries are delivered to you the
same day they are ordered. Jane Doe, one of Instacart's district managers,
described Instacart as follows:

> Whether you shop from meticulously planned grocery lists or let whimsy guide
> your grazing, our unique food rituals define who we are. Instacart, a
> grocery ordering and delivery app, aims to make it easy to fill your
> refrigerator and pantry with your personal favorites and staples when you
> need them. After selecting products through the Instacart app, personal
> shoppers review your order and do the in-store shopping and delivery for
> you.
 
Currently, Instacart uses transactional data to understand which products a
user is likely to buy again, try for the first time, or add to their cart next
during a session. Although, the lack of analytical capabilities hinders
Instacart's ability to take full advantage of this data. Due to the lack of
qualified in-house data scientists, Jane hired an external consultant to
some of the questions they've been struggling to address.

## Metadata

This dataset is a relational set of files describing customers' orders over
time. The dataset is anonymized and contains a sample of 200,000 grocery
orders from more than 100,000 Instacart users. For each user, we provide a few
of their orders, with the sequence of products purchased in each order.
Because the original dataset was too large, the products were grouped by their
types, resulting in a total of 134 generalized products.  We also provide the
week and hour of day the order was placed, and a relative measure of time
between orders.

### File Descriptions

Each entity (customer, product, order, aisle, etc.) has an associated unique
id. Most of the files and variable names should be self-explanatory.

#### departments.csv

Contains a generalized grouping of the products available in the dataset.

```
department_id,department  
1,frozen  
2,other  
3,bakery  
...
```

#### order_products.csv

Contains previous order contents for all customers. 'reordered' indicates that
the customer has a previous order that contains the product. Note that some
orders will have no reordered items.

```
order_id,product_id,add_to_cart_order,reordered  
1934,83,1,1  
1934,37,2,1  
1934,66,3,0  
... 
```

#### orders.csv

This file contains information about each order. 'order_dow' is the day of
week.

```
order_id,user_id,order_number,order_dow,order_hour_of_day,days_since_prior_order  
2539329,1,1,2,08,  
2398795,1,2,3,07,15.0  
473747,1,3,3,12,21.0  
...
```

#### products.csv

```
product_id,department_id,product_name
1,19,Chocolate Sandwich Cookies  
2,13,All-Seasons Salt  
3,7,Robust Golden Unsweetened Oolong Tea  
...
```


## Expected Outcomes

You should aim to provide an overview of Instacart's business as complete as
possible. Jane is particularly interested in the topics below:

- What are the main types of consumer behavior in the business?
- Which types of products should have an extended amount of product offerings?
- Which types of products can be seen as substitutes?
- Which items are complementary?
