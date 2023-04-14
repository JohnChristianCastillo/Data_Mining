"""
people with higher incomes (>50k) are more likely to accept the special promotion offer 10%
for people with lower lower income (<=50k) only 5% accept the special promotion offer

people with high income, on average, gives us 980 euro in profit
while people with lower income costs us 310 euro on average

sending a special promotion offer costs 10 euro per package

two .xlsx files are provided, "01_existing-customers.xlsx" which contains whether or not the person exceeds 50k income 
and "01_potential-customers.xlsx" which does not contain data about income
both of the files contains the following attributes:
1. age
2. workclass
3. education: highest level of education achieved by an individual
4. education-num: highest level of educationa chieved in numerical form (an integer greater than 0)
5. marital-status: marital status of an individual
6. occupation: general type of occupation of an individual
7. relationship: representa what this individual is relative to others
8. race
9. sex
10. capital-gain: capital gains for an individual (integer greater than or equal to 0)
11. capital-loss: capital losses for an individual (integer greater than or equal to 0)
12. hours-per-week: the hours an individual has reported to work per week continuous
13. native-country: country of origin for an individual
lastly, "01_existing-customers.xlsx" contains the extra attribute:
14. the label: whether or not an individual makes more than 50k a year

Solve this problem (provide the list of people to send the promotion to) and give an estimate of the profit you expect when sending the promotion to the people you selected.
The goal is to maximize the revenue

make use of the library: sklearn
first use decision trees to solve this problem
"""
import pandas as pd

# read the data
existing_customers = pd.read_excel("01_existing-customers.xlsx")
potential_customers = pd.read_excel("01_potential-customers.xlsx")

