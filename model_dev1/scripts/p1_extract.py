import pandas as pd

## get data

# original link: https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1
# data download link:
datalink = 'https://data.cdc.gov/api/views/9j2v-jamp/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)

## save as csv to model_dev2/data/raw/leading_deaths
df.to_csv('/home/rahil_shaikh/datasci_9_data_prep/model_dev1/data/raw/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv', index=False)

## save as pickle to model_dev2/data/raw/leading_deaths
df.to_pickle('/home/rahil_shaikh/datasci_9_data_prep/model_dev1/data/raw/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.pk1')