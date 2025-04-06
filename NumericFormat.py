import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
df = pd.read_csv('iris.csv')
label_encoder = LabelEncoder()
df['Species_Label'] = label_encoder.fit_transform(df['species'])
print("Label Encoded Species:\n", df[['species', 'Species_Label']].head())
one_hot_encoder = OneHotEncoder(sparse_output=False)  
species_encoded = one_hot_encoder.fit_transform(df[['species']])
species_df = pd.DataFrame(species_encoded, columns=one_hot_encoder.get_feature_names_out(['species']))
df = pd.concat([df, species_df], axis=1)
print("\nDataset after OneHotEncoding:\n", df.head())
