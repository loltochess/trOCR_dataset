import pandas as pd

df1 = pd.read_csv('labels_background_renamed.txt', header=None, engine='python')
df1[['file_name', 'text']] = df1[0].str.split(' ', n=1, expand=True)
df1.drop(columns=[0], inplace=True)
df1['text'] = df1['text'].str.strip()

df2 = pd.read_csv('labels_basic_renamed.txt', header=None, engine='python')
df2[['file_name', 'text']] = df2[0].str.split(' ', n=1, expand=True)
df2.drop(columns=[0], inplace=True)
df2['text'] = df2['text'].str.strip()

df3 = pd.read_csv('labels_blur_1_renamed.txt', header=None, engine='python')
df3[['file_name', 'text']] = df3[0].str.split(' ', n=1, expand=True)
df3.drop(columns=[0], inplace=True)
df3['text'] = df3['text'].str.strip()

df4 = pd.read_csv('labels_blur_2_renamed.txt', header=None, engine='python')
df4[['file_name', 'text']] = df4[0].str.split(' ', n=1, expand=True)
df4.drop(columns=[0], inplace=True)
df4['text'] = df4['text'].str.strip()

train_df = pd.concat(
    [df1, df2, df3, df4],
    ignore_index=True
)

train_df.to_csv("train_end.txt")

train_df.sample(20)