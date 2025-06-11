import pandas as pd
df_bg = pd.read_csv('Dữ liệu điểm Bắc Giang.csv')
df_wc_bg = df_bg.groupby('question_id').size().rename('done_by_bg').reset_index()

df_list_dup = pd.read_csv('List duplicate questions - Folder 2025.csv')
df_wc_ntl = pd.read_csv('work_counts_ntl.csv')
df_wc_tnhl = pd.read_csv('work_counts_tnhl.csv')

df_merge = pd.merge(
    df_list_dup, df_wc_ntl, 
    left_on='iid', right_on='question_id',
    how='left'
    )

df_merge = pd.merge(
    df_merge, df_wc_tnhl, 
    left_on='iid', right_on='question_id',
    how='left'
    )

df_merge = pd.merge(
    df_merge, df_wc_bg, 
    left_on='iid', right_on='question_id',
    how='left'
    )

df_merge.to_excel('work_counts_from_3_projects.xlsx')
