Death rates for suicide, by sex, race, Hispanic origin, and age: United States

https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1

Data on death rates for suicide, by selected population characteristics.

Classification: Identify missing values, Remove outliers, Cleaning column names, Drop unnecessary columns

Identify missing values: use df.replace to remove white space with 0

Remove Outliers: Identify threshold and remove outliers using df_cleaned

Change column names to represent what they contain (STUB_LABEL = Sex)

Since sex and race is combined into 1 column, adjust it to only contain "Male" or "Female" and remove other char

Change Age column to only have mean number instead of range

Clean column names: make them all lower case, remove white spaces and replace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')

Drop Columns: Identify and remove unneccessary columns via df.drop

Replace column for gender with Male or Female and remove other str characters such as race details

Cannot perform other dependent variables without cleaning dataset

can we predict the year of death based on death rate in the US?

Dependent: Year  Independent: Death Rate