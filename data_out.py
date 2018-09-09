import pandas as pd
import numpy as np

from settings import Settings
from data_functions import if_fuc

ai_settings = Settings()

print(ai_settings.business_type)
print(ai_settings.distribution_column)
print(ai_settings.staff_exceptions)

#read row data and dataclean
deposit_detail = pd.read_excel('deposit_detail.xlsx', 'Sheet1',
    converters = {'业务子类型': str, '客户代码2': str})
deposit_detail = pd.DataFrame(deposit_detail)
deposit_detail = deposit_detail.loc[deposit_detail['业务子类型'].isin(
    ai_settings.business_type)]

#delete rows where customer name not in settings
criterion = lambda row: row['员工名称'] not in ai_settings.staff_exceptions
deposit_detail = deposit_detail[deposit_detail.apply(criterion,
    axis='columns')]

#select column for compute according to settings
selected_dataframe = deposit_detail[ai_settings.distribution_column]

#group by customer id
group_2 = selected_dataframe.loc[:,['客户代码2','分成后季日均']]
group_2 = group_2.groupby('客户代码2').sum()
grouped_data = pd.merge(selected_dataframe, group_2, on='客户代码2', how='left')

group_1 = selected_dataframe.loc[:,['客户代码2','分成后年日均']]
group_1 = group_1.groupby('客户代码2').sum()
grouped_data = pd.merge(grouped_data, group_1, on='客户代码2', how='left')

group_3 = selected_dataframe.loc[:,['客户代码2','余额分成比率']]
group_3 = group_3.groupby('客户代码2').sum()
grouped_data = pd.merge(grouped_data, group_3, on='客户代码2', how='left')

#aplly if condition function
grouped_data['out'] = grouped_data.apply(lambda x: if_fuc(
    col_if_s=x.分成后季日均_y, col_if_y=x.分成后年日均_y,
    col_if_ye=x.余额分成比率_y, col_compute_s=x.分成后季日均_x,
    col_compute_y=x.分成后年日均_x, col_compute_ye=x.余额分成比率_x), axis=1)

#output data to excel and print this version
grouped_data.to_excel('data_out.xlsx','Sheet1')
print("Release version: data_out_1.1")