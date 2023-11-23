import pandas as pd

datalink = 'https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)

## save as csv to model_dev2/data/raw/leading_deaths
df.to_csv('/home/rahil_shaikh/datasci_9_data_prep/model_dev2/data/raw/Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States.csv', index=False)

## save as pickle to model_dev2/data/raw/leading_deaths
df.to_pickle('/home/rahil_shaikh/datasci_9_data_prep/model_dev2/data/raw/Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States.pk1')