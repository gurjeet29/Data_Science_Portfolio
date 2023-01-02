# Project Name - Superstore Analysis

This is a data visualization project to analyse the sales and the products offered by Superstore store in The United States of America.  

## Dataset Description

The dataset consists of 9994 records, with 5009 unique orders. 

Dataset link ---> https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

### Meta Data

1. Row ID - Unique ID for each row.
2. Order ID - Unique Order ID for each Customer.
3. Order Date - Order Date of the product.
4. Ship Date - Shipping Date of the Product.
5. Ship Mode - Shipping Mode specified by the Customer.
6. Customer ID - Unique ID to identify each Customer.
7. Customer Name - Name of the Customer.
8. Segment - The segment where the Customer belongs.
9. Country - Country of residence of the Customer.
10. City - City of residence of of the Customer.
11. State - State of residence of the Customer.
12. Postal Code - Postal Code of every Customer.
13. Region - Region where the Customer belong.
14. Product ID - Unique ID of the Product.
15. Category - Category of the product ordered.
16. Sub-Category - Sub-Category of the product ordered.
17. Product Name - Name of the Product
18. Sales - Sales of the Product.
19. Quantity - Quantity of the Product.
20. Discount - Discount provided.
21. Profit - Profit/Loss incurred.

## Exploratory Data Analysis

### Overview

* The total sales for Superstore is around $2.3 million with a profit of about $286,400 from 2014 till 2017. Over this period, the total sales, profit and the number of orders have increased steadily with a slight dip in sales in 2015.
   <p align ="center">
  <img src="https://user-images.githubusercontent.com/105280450/198371972-6f7d0dc1-a36b-4ce6-91cc-80d745109b93.png">
  </p>
* Customers belonging to the consumer segment contributed to the highest sales, followed by corporate and then home office.

  <p align ="center">
  <img src="https://user-images.githubusercontent.com/105280450/198065112-49443884-aed7-4e05-877e-f0c583c981c0.png">
  </p>

  
The analysis on the dataset is further segregated into four groups- product analysis, region-wise analysis, customer analysis and trend analysis.

###  1. Product Analysis

* Looking at the categories, the sales and profit from the technology category was the highest. 
 <p align="center">
   <img src= "https://user-images.githubusercontent.com/105280450/198070006-17a3907d-2afb-45b7-9463-cab58f870f80.png">
  </p>

* Although the sales generated from office supplies and furniture are within the range of $720,000 to $745,000, the profit from furniture is quite low (2.49% profit margin). Tables and bookcases are sold at a total loss of $21,199.

   <p align="center">
     <img src= "https://user-images.githubusercontent.com/105280450/198066738-109a8c59-240e-4928-9d25-5ce198e4804c.png">
  </p>
* Next is the supplies sub-category from office supplies generating a loss of 2.55%.
* Products belonging to the technology category contribute to the maximum profit made by the store.

 ###  2. Region-wise Analysis

* The highest sales and profit is contributed by the western region.
* Most of the top 10 states contributing to the total sales either lie on or close to the coast of the country.
  <p align="center">
     <img src= "https://user-images.githubusercontent.com/105280450/198715404-0971ba8f-186c-4d3c-87f8-b692d78d2215.png">
  </p>
  
* From the product analysis, it's clear that the profit from furniture category is the least. On  further categorizing by region, only the central region contributes to the loss. 
 <p align="center">
   <img src= "https://user-images.githubusercontent.com/105280450/198092764-e9ca7b90-8601-4234-b3fe-ec2a54a87002.png" height = 450>
 </p>
  
* Almost for all the regions, the sales of bookcases and tables is in a loss.
  <table>
    <tr>
      <td> <b>Bookcases</b> </td>
      <td> <b>Tables</b> </td>
    </tr>
    
    <tr>
     <td><img src="https://user-images.githubusercontent.com/105280450/198095619-2b9dbca7-91e8-4f9a-9112-0e7023f6028f.png" height = 450></td>
     <td><img src="https://user-images.githubusercontent.com/105280450/198095745-935a67dd-d118-456a-9c4c-e463a1d565ff.png" height = 450></td>
    </tr>
   </table>

### 3. Customer Analysis

* There are 3 customers who are in the top 5 contributing to the highest sales and profit.
* Among the top 5 customers, only one customer- Adrian Barton contributed the maximum sales to office supplies. The remaining four produced the highest sales for         technology products.
   <p align="center">
   <img src= "https://user-images.githubusercontent.com/105280450/198107336-3be63b95-2346-4edb-9bae-d6d96f35962e.png" height= 450>
  </p>
  
### 4. Trend Analysis

* Over a period of four years, the maximum number of orders, sales and profit were made in the last four months. A dip is observed in the first two months of the year.   In the first half of the year, sales and profit are the highest in March.
* By day of the week, maximum orders and sales is made on Mondays and Fridays. The least sales is made on Wednesdays. 

  <p align="center">
   <img src= "https://user-images.githubusercontent.com/105280450/198364375-bc27d6bc-59c2-45af-9784-aea288b7088c.png" height= 450>
  </p>
  
## Conclusion and Inference

1. The overall sales and profit has increased with time. Most of the sales and profit was through techology products, especially phones.
2. More than 50% of the profit is contributed by two states- California and New York. Although Texas made the 3rd highest sales, the store made a loss of 15.12% there ($18.58K in office supplies).
3. The customer producing the highest sales (Sean Miller) also contributed to a loss of 7.91% through the product which made the highest sales.

### Inference drawn from EDA

* It's apparent that furniture products have performed poorly over the four-year period in all the regions. The loss generated from selling bookcases and tables was     the highest for the consumer segment. The store could sell tables along with the chairs as a set, due to the successful sales performance and profit generated from     chairs. Further research is required, perhaps market basket analysis.
* Furthermore, the overall performance of furniture products in the central region has been a downward trend. To avoid this in the future, the store can limit the       losses by investing on products that are more profitable in this region, thereby maintaining their inventory.
* On analyzing the top 5 customers contributing to the highest sales and profit, the store could offer them premium memberships, specific to their needs. This could     help in promoting their business and bring in new customers.
* From trend analysis it has been observed that the overall sales performance of the store has been the best in the last four months of the year. This could be due to   the holiday season in the USA. The performance in the middle of the year is constant but low. The actual reason for this scenario cannot be established currently       from the data. 
* In addition, the sales performance can be further analyzed by studying its trend over a week. Right in the middle of the week, the sales are the least. It's           important to understand the purchasing habits of the customers based on their activity and offer special deals to them that could help in boosting the sales and       profit of the store.
