import pandas as pd

from sklearn.model_selection import train_test_split
import os
from tqdm import tqdm

data = []
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/1_구어체(1).xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/1_구어체(2).xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/2_대화체.xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/3_문어체_뉴스(1).xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/3_문어체_뉴스(2).xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/3_문어체_뉴스(3).xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/3_문어체_뉴스(4).xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/4_문어체_한국문화.xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/5_문어체_조례.xlsx'))
data.append(pd.read_excel('datasets/origin_kor2eng_corpus/6_문어체_지자체웹사이트.xlsx'))

total_data = pd.DataFrame(columns=['KOR', 'ENG'])

for d in tqdm(data):
    total_data = total_data.append(d[['원문', '번역문']].rename(columns={'원문':'KOR', '번역문':'ENG'}))


train_df, val_df = train_test_split(total_data, test_size = 0.3, random_state=1234)
val_df, test_df = train_test_split(val_df, test_size=0.3, random_state=1234)

path = './datasets/korNeng_corpus'
os.makedirs(path, exist_ok=True)

total_data.to_csv(path + '/korneng.csv', index=None, encoding='utf-8-sig')

train_df.to_csv(path + '/train_data.csv', index=None, encoding='utf-8-sig')
val_df.to_csv(path + '/validation_data.csv', index=None, encoding='utf-8-sig')
test_df.to_csv(path + '/test_data.csv', index=None, encoding='utf-8-sig')