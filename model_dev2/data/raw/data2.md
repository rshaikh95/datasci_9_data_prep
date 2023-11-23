Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States

https://catalog.data.gov/dataset/drug-overdose-death-rates-by-drug-type-sex-age-race-and-hispanic-origin-united-states-3f72f/resource/48eb6490-5709-43f3-ae4a-3c7d3a4b0c2c

Data on drug overdose death rates, by drug type and selected population characteristics

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

can we predict the year of drug overdose based on drug overdose rate in the US?

Dependent: year Independent: Drug overdose rate