# partition the pubmed mesh data into a 90%-10% split
# this is not stratified on anything

import pandas as pd
from sklearn.model_selection import train_test_split

root = "/project/rcde/datasets/pubmed/mesh_50k/"
df = pd.read_csv(root + "pubmed_multi_label_text_classification_dataset_processed.csv")
print(len(df))

df_train, df_test = train_test_split(df, test_size=0.1, random_state=42)

df_train.abstractText.to_csv(root + "splits/train.txt", index=None, header=False)
df_test.abstractText.to_csv(root + "splits/test.txt", index=None, header=False)