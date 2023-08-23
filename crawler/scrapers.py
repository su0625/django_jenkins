import pandas

url = "https://currencyex.doitwell.tw/tw/"
def recommend():
    dfs = pandas.read_html(url)
    recommend_df = dfs[0]
    recommend_df.columns=[u'種類','推薦','匯率','說明']
    recommend_df.drop([len(recommend_df)-1],inplace=True)
    return recommend_df

def all():
    dfs = pandas.read_html(url)
    all_df = dfs[1]
    all_df.columns=['銀行名稱','銀行現金賣出','銀行現金買入','銀行即期賣出',"銀行即期買入","更新時間"]
    all_df.drop([len(all_df)-1],inplace=True)
    return all_df
