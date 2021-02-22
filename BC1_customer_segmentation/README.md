# BC1: Wonderful Wines of the World 

**Problem type:** Customer Segmentation

**Submission date:** 01-March-2021 | 11.59pm

## General Context

Finding new customers is vital in every industry. The process for finding new
customers begins by learning as much as possible from the existing customers.
Understanding current customers allow organizations to identify groups of
customers that have different product interests, different market
participation, or different response to marketing efforts.

Market segmentation, the process of identifying customers’ groups, makes use
of geographic, demographic, psychographic, and behavioral characteristics of
customers. By understanding the differences between the different segments,
organizations can make better strategic choices about opportunities, product
definition, positioning, promotions, pricing, and target marketing.

## Business Situation

Wonderful Wines of the World (WWW) is a 7-year-old enterprise that seeks out
small, unique wineries around the world and brings their wines to its
customers. Its mission is to delight its customers with well-made, unique, and
interesting wines that would never travel far beyond their points of origin.

WWW sells wines through catalogs and a web site, and ten small stores in major
cities around the USA. Customers can purchase at the stores, by telephone
(after looking at the catalog), or on the web site. Several hundred selections
are available in each new catalog, sent every 6 weeks.

Through aggressive promotion in wine and food magazines, WWW now has 350,000
customers in its database. Most customers are highly involved in wine,
entertain frequently, and have sufficient money to indulge their passion for
wine. WWW sometimes offers wine accessories as well – wine racks, cork
extractors, etc.

WWW is trying to make use of the database it started about 4 years ago. So
far, it has simply mass-marketed everything. All customers get the catalog,
and there are no loyalty programs or attempts to identify target markets for
cross-selling opportunities. Now, WWW wants to “get smart” about its database,
and start differentiating customers, and developing more focused programs.

WWW has provided a sample of 10,000 customers from its active database. These
are all customers who have purchased something from WWW in the past 18 months
(after 18 months with no purchase, a person is eliminated from the active
database). It was these 20,000 randomly-selected people who were sent the test
promotion for the silver-plated cork extractor.

## Metadata

| Name     | Values         | Statistics         | Meaning                                                      |
|----------|----------------|--------------------|--------------------------------------------------------------|
| CUSTID   | 1001-10000     | customer ID number |                                                              |
| DAYSWUS  | 550-1250       | mean=899           | number of days as a customer                                 |
| AGE      | 18-78          | mean=48            | customer’s age or imputed age                                |
| EDUC     | 12-20          | mean=16.7          | years of education (may be imputed)                          |
| INCOME   | $10K-$140K     | mean=$70K          | household income (may be imputed)                            |
| KIDHOME  | 0, 1           | 42%                | 1=child under 13 lives at home                               |
| TEENHOME | 0, 1           | 47%                | 1=child 13-19 years lives at home                            |
| FREQ     | 1-56           | mean=15            | number of purchases in past 18 mo.                           |
| RECENCY  | 0-550          | mean=62            | number of days since last purchase                           |
| MONETARY | $6-$3052       | mean=$623          | total sales to this person in 18 mo.                         |
| LTV      | -$178 to $1791 | mean=$209          | Lifetime value of the customer                               |
| PERDEAL  | 0-100%         | mean=32%           | % purchases bought on discount                               |
| DRYRED   | 0-100%         | mean=50%           | % of wines that were dry red wines                           |
| SWEETRED | 0-100%         | mean= 7%           | % sweet or semi-dry reds                                     |
| DRYWH    | 0-100%         | mean=29%           | % dry white wines                                            |
| SWEETWH  | 0-100%         | mean= 7%           | % sweet or semi-dry white wines                              |
| DESSERT  | 0-100%         | mean= 7%           | % dessert wines (port, sherry, etc.)                         |
| EXOTIC   | 0-100%         | mean=17%           | % very unusual wines                                         |
| WEBPURCH | 0-100%         | mean=42            | % of purchases made on website                               |
| WEBVISIT | 0-10           | mean= 5            | average # visits to website per month                        |
| SMRACK   | 0, 1           | 8%                 | 1=bought the small wine rack $50                             |
| LGRACK   | 0, 1           | 7%                 | 1=bought the large wine rack $100                            |
| HUMID    | 0, 1           | 8%                 | 1=bought wine cellar humidifier $75                          |
| SPCORK   | 0, 1           | 6.8%               | 1=silver-plated cork extractor $60                           |
| BUCKET   | 0, 1           | 1%                 | 1=bought silver wine bucket $150                             |
| ACCESS   | 0, 4           | mean=0.25          | number of accessories (not SPCORK)                           |
| COMPLAIN | 0, 1           | 1%                 | 1=made a complaint in last 18 mo.                            |
| MAILFRND | 0, 1           | 10%                | 1=appears on a purchased list of “mail friendly” customers   |
| EMAILFRD | 0, 1           | 5%                 | 1=appears on a purchased list of “e-mail friendly” customers |

## Additional remarks

**Note:** DRYRED + SWEETRED + DRYWH + SWEETWH + DESSERT = 100%

Notice the data was stored in a XLSX file. There may be some intricacies when
reading this file type using Python, feel free to modify/delete rows and/or
columns before you read it with Python. Make sure the data is being
imported properly and that you remove (before or after converting it to a
pandas data frame) any irrelevant rows/columns you may find.

## Expected outcomes

1. Explore the data and identify the variables that should be used to segment customers.
2. Identify customer segments
    * Justify the number of clusters you chose (taking in consideration the business use).
    * Use dimensionality reduction techniques to speed-up model development
        (don't forget you should be able to interpret and explain your results
        to non-technical managers).
3. Suggest business applications for the findings.
