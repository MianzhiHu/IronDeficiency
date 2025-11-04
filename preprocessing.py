import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast
import json
import openpyxl
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore, pearsonr
from statsmodels.stats.multitest import multipletests
from var_def import (iron_residual, neuro_residual, behavior_residual, psychopathology_residual, myelin_residual,
                     QSM_residual, brain_volume_residual, iron, QSM, behavior, psychopathology, behavior_old,
                     psychopathology_old, wm)
from utilities import rename_columns, high_corr_checker, process_workbook


# read xlsx file
data = pd.read_excel('./Data/Original_Data/A&M_dataset.xlsx')
wm_data = pd.read_excel('./Data/Original_Data/UT_WM_Integrity_Metrics_Females.xlsx')
questionnaires_dict = pd.read_excel('./Data/Original_Data/A&M_dataset_DICTIONARY.xlsx', sheet_name='Dataset_Dictionary')
questionnaires_totals = pd.read_excel('./Data/Original_Data/A&M_dataset_DICTIONARY.xlsx', sheet_name='Scores')

# define the inclusion and exclusion criteria
choice = "else"
iron_inclusion = False
QSM_inclusion = False
behavioral_inclusion = True
psychopathology_inclusion = True
brain_volume_inclusion = False
wm_inclusion = True
behavioral_exclusion = False
behavioral_exclusion_list = ['Trail_PartA_time', 'Trail_PartA_error_seq', 'TrailsB_Time', 'Trail_PartB_error_seq',
                             'Trail_PartB_error_set', 'Pegboard_Avg_Time', 'Pegboard_Avg_Dropped',
                             'Trail_PartA_time_residual', 'Trail_PartA_error_seq_residual',
                             'TrailsB_Time_residual', 'Trail_PartB_error_seq_residual',
                             'Trail_PartB_error_set_residual', 'Pegboard_Avg_Time_residual',
                             'Pegboard_Avg_Dropped_residual']

# Define the variable lists in a dictionary with their inclusion flags
variables_dict = {
    'iron': (iron_inclusion, iron_residual + iron),
    'QSM': (QSM_inclusion, QSM_residual + QSM),
    'behavioral': (behavioral_inclusion, behavior_residual + behavior),
    'psychopathology': (psychopathology_inclusion, psychopathology_residual + psychopathology),
    'brain_volume': (brain_volume_inclusion, brain_volume_residual),
    'wm': (wm_inclusion, wm)
}

# =============================================================================
#                               Data Cleaning
# =============================================================================
# filter out excluded participants
excluded_iron = data[data['Group_Iron'] == "Excluded"]['Code']
data = data[data['Group_Iron'] != "Excluded"]

# also exlude the participants with high hsCRP
excluded_hsCRP = data[data['High_hsCRP'] == 1]['Code']
data = data[data['High_hsCRP'] != 1]

# remove columns with too many missing values
missing = data.isna().sum().sort_values(ascending=False)
missing_cols = missing[missing > 0.9 * data.shape[0]].index

# Ensure that the columns to be dropped exist in the DataFrame
drop_cols = list(set(missing_cols) & set(data.columns)) + ['Visit']
drop_cols = [col for col in drop_cols if col in data.columns]

data = data.drop(columns=drop_cols)

# detect the missing values and replace all -999 with NaN
data = data.replace(-999.0, np.nan)
data = data.replace(-9999.0, np.nan)

# extract variables of interest
highlighted_cells, reverse_cols, median_cols = process_workbook('./Data/Original_Data/A&M_dataset_DICTIONARY.xlsx')

# store the highlighted variables as variables of interest
variables_of_interest = [cell.value for cell in highlighted_cells]

# select the variables of interest
variables_of_interest = [var for var in variables_of_interest if var in data.columns]

# Exclude variables based on inclusion criteria
for key, (include, vars_list) in variables_dict.items():
    if not include:
        variables_of_interest = [var for var in variables_of_interest if var not in vars_list]
    # in addition, remove the variables to be removed from behavioral data if behavioral data itself is excluded
    if key == 'behavioral' and not behavioral_inclusion:
        variables_of_interest = [var for var in variables_of_interest if var not in behavior_old]
    if key == 'psychopathology' and not psychopathology_inclusion:
        variables_of_interest = [var for var in variables_of_interest if var not in psychopathology_old]


# if there are variables of interest that do not exist in the data, print and store them
missing_vars = [var for var in variables_of_interest if var not in data.columns and var not in drop_cols]

data = data[variables_of_interest]
print(f'Data shape after selecting variables of interest: {data.shape}')

# =============================================================================
# Transform behavioral data
# =============================================================================
if behavioral_inclusion:
    # # aggregate semantic associates
    # data['RAVLT_Semantic_Associates_residual'] = data[['RAVLT_ListA_Sem_Assoc_residual',
    #                                                    'RAVLT_ListB_Sem_Assoc_residual']].mean(axis=1)
    # data['RAVLT_Semantic_Associates'] = data[['RAVLT_ListA_Semantic_Associates',
    #                                           'RAVLT_ListB_Semantic_Associates']].mean(axis=1)
    # data = data.drop(columns=['RAVLT_ListA_Sem_Assoc_residual', 'RAVLT_ListB_Sem_Assoc_residual',
    #                           'RAVLT_ListA_Semantic_Associates', 'RAVLT_ListB_Semantic_Associates'])
    #
    # # aggregate phonemic associates
    # data['RAVLT_Phonemic_Associates_residual'] = data[['RAVLT_ListA_Phon_Assoc_residual',
    #                                                    'RAVLT_ListB_Phon_Assoc_residual']].mean(axis=1)
    # data['RAVLT_Phonemic_Associates'] = data[['RAVLT_ListA_Phonemic_Associates',
    #                                           'RAVLT_ListB_Phonemic_Associates']].mean(axis=1)
    # data = data.drop(columns=['RAVLT_ListA_Phon_Assoc_residual', 'RAVLT_ListB_Phon_Assoc_residual',
    #                           'RAVLT_ListA_Phonemic_Associates', 'RAVLT_ListB_Phonemic_Associates'])

    # aggregate the pegboard data
    data['Pegboard_Avg_Time_residual'] = data[['Pegboard_RH_Time_residual', 'Pegboard_LH_Time_residual']].mean(axis=1)
    data['Pegboard_Avg_Time'] = data[['Pegboard_RH_Time', 'Pegboard_LH_Time']].mean(axis=1)
    data['Pegboard_Avg_Dropped_residual'] = data[['Pegboard_RH_Dropped_residual', 'Pegboard_LH_Dropped_residual']].mean(
        axis=1)
    data['Pegboard_Avg_Dropped'] = data[['Pegboard_RH_Dropped', 'Pegboard_LH_Dropped']].mean(axis=1)

    # # they are all correct, so we discard the total correct columns
    # data['Pegboard_Avg_Correct'] = data[['Pegboard_RH_Total_Correct', 'Pegboard_LH_Total_Correct']].mean(axis=1)

    data = data.drop(columns=['Pegboard_RH_Time_residual', 'Pegboard_LH_Time_residual', 'Pegboard_RH_Dropped_residual',
                              'Pegboard_LH_Dropped_residual', 'Pegboard_RH_Time', 'Pegboard_LH_Time', 'Pegboard_RH_Dropped',
                              'Pegboard_LH_Dropped'])

    # reverse code the new ones
    reverse_cols.extend(['Pegboard_Avg_Time_residual', 'Pegboard_Avg_Dropped_residual',
                         'Pegboard_Avg_Time', 'Pegboard_Avg_Dropped'])

    if behavioral_exclusion:
        # drop pegboard and trail data
        data = data.drop(columns=behavioral_exclusion_list)
        # remove them from the behavioral variable list
        behavior = [var for var in behavior if var not in behavioral_exclusion_list]
        behavior_residual = [var for var in behavior_residual if var not in behavioral_exclusion_list]

    # check for two specific participants
    exlude_participants = ['Z1272', 'Z2324']
    if data['Code'].isin(exlude_participants).any():
        print('Participants to exclude are in the data')
        data = data[~data['Code'].isin(exlude_participants)]
    else:
        print('Participants to exclude are not in the data')

# # =============================================================================
# # Transform questionnaire data for the bifactor model
# # =============================================================================
# if psychopathology_inclusion:
#     if choice == "CBCL":
#         # select only the CBCL columns
#         cbcl_cols = data.columns[data.columns.str.contains('Q')]
#         questionnaires = data[cbcl_cols]
#
#         questionnaires.columns = rename_columns(cbcl_cols)
#
#         # remove designated columns
#         questionnaires = questionnaires.drop(columns=['Q2', 'Q59', 'Q67', 'Q73', 'Q96', 'Q99', 'Q101', 'Q105'])
#
#
#         # reconstruct designated columns
#         def reconstruct(col1, col2, new_col, df, round=True):
#             df[new_col] = (df[col1] + df[col2]) / 2
#             if round:
#                 df[new_col] = df[new_col].round()
#             else:
#                 df[new_col] = df[new_col]
#             df = df.drop(columns=[col1, col2])
#             return df
#
#
#         questionnaires = reconstruct('Q20', 'Q21', 'Destroy', questionnaires, round=False)
#         questionnaires = reconstruct('Q8', 'Q78', 'Inattentive', questionnaires)
#         questionnaires = reconstruct('Q53', 'Q55', 'Overweight', questionnaires)
#
#         uniform_vars = []
#         for col in questionnaires.columns:
#             if len(questionnaires[col].unique()) == 1:
#                 questionnaires = questionnaires.drop(columns=[col])
#                 uniform_vars.append(col)
#                 print(f'Uniform questionnaire item dropped: {col}')
#
#             corr = questionnaires.corr()
#             high_corr = []
#             for i in range(corr.shape[0]):
#                 for j in range(i + 1, corr.shape[0]):
#                     if abs(corr.iloc[i, j]) > 0.85:
#                         high_corr.append((corr.index[i], corr.columns[j]))
#
#             # print the highly correlated variables
#             if high_corr:
#                 print('Highly correlated variables:')
#                 for var in high_corr:
#                     print(f'{var[0]} and {var[1]} are highly correlated, with a correlation of {corr[var[0]][var[1]]}')
#
#     elif choice == "Totals":
#         data = data[questionnaires_totals['ElementName']]
#         col_to_drop = data[data.columns[(data.columns.str.contains('T_SCORE') |
#                                          data.columns.str.contains('total') |
#                                          data.columns.str.contains('Total') |
#                                          data.columns.str.contains('CESD_C_Score') |
#                                          data.columns.str.contains('_pct'))]].columns
#         col_to_drop = col_to_drop[col_to_drop.isin(data.columns)]
#         data = data.drop(columns=col_to_drop)
#         print(data.columns)
#
#         # # check for correlation between the total scores
#         # questionnaires = high_corr_checker(questionnaires)
#         # corr = questionnaires.corr()
#
#         # standardize the data
#         print(f'Current data range: {data.max().max()} - {data.min().min()}')
#         for col in data.columns:
#             # transform the data using min-max scaling
#             data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
#         print(f'Standardized data range: {data.max().max()} - {data.min().min()}')
#
#     else:
#         # remove all the text columns
#         text_cols = questionnaires_dict[questionnaires_dict['ValueRange'].str.contains('Text', na=False)]['ElementName']
#         text_cols = text_cols.str.replace('^CBCL_', '', regex=True)  # to standardize the column names
#         text_cols = text_cols[text_cols.isin(data.columns)]
#         data = data.drop(columns=text_cols)
#
#         # remove all the parent evaluated SCARED columns
#         scaredp_cols = data[data.columns[data.columns.str.contains('SCARED_P')]].columns
#         scaredc_cols = data[data.columns[data.columns.str.contains('SCARED_C')]].columns
#
#         # calculate the correlation between the parent and child SCARED columns
#         scared_corr = []
#         for i, j in zip(scaredp_cols, scaredc_cols):
#             corr = data[i].corr(data[j])
#             scared_corr.append((i, j, corr))
#
#         corr_mean = np.mean([corr[2] for corr in scared_corr])  # 0.5588421650840539
#
#         # # remove the parent SCARED columns
#         # questionnaires = questionnaires.drop(columns=scaredp_cols)
#
#         # # reconstruct the appetite column
#         # for index, row in data.iterrows():
#         #     if row['CDRSR_appetite_type'] == -777:
#         #         data.at[index, 'CDRSR_appetite'] = 0
#         #     elif row['CDRSR_appetite_type'] == 0:
#         #         data.at[index, 'CDRSR_appetite'] = 1 * (row['CDRSR_appetite'] - 1)
#         #     elif row['CDRSR_appetite_type'] == 1:
#         #         data.at[index, 'CDRSR_appetite'] = -1 * (row['CDRSR_appetite'] - 1)
#         #
#         # data = data.drop(columns='CDRSR_appetite_type')

        # # check nan values
        # missing_qn = data.isna().sum().sort_values(ascending=False)
        # missing_qn_var = missing_qn[missing_qn > 0].index
        # if missing_qn_var.any():
        #     for col in missing_qn_var:
        #         print(f'{col} has {missing_qn[col]} missing values')
        # else:
        #     print('No missing values in the questionnaires data')

        # cbcl_cols = questionnaires.columns[questionnaires.columns.str.contains('Q')]
        # questionnaires = questionnaires[cbcl_cols]

        # # check again
        # high_corr_checker(data, checker=True)

        # # finally, standardize the data
        # print(f'Current data range: {questionnaires.max().max()} - {questionnaires.min().min()}')
        # for col in questionnaires.columns:
        #     # transform the data using min-max scaling
        #     questionnaires[col] = (questionnaires[col] - questionnaires[col].min()) / (questionnaires[col].max() -
        #                                                                                questionnaires[col].min())
        # print(f'Standardized data range: {questionnaires.max().max()} - {questionnaires.min().min()}')

        # # rename the columns
        # questionnaires.columns = rename_columns(questionnaires.columns, cbcl_cols=False)

        # # print the column name according to column index
        # for i, col in enumerate(data.columns):
        #     print(f'{i + 1}: {col}')

    # # print the max and min values of the columns
    # for col in data.columns:
    #     # if the column is not a string
    #     if data[col].dtype != 'O':
    #         print(col, data[col].max(), data[col].min())

# =============================================================================
# White matter integrity data
# =============================================================================
if wm_inclusion:
    wm_data = wm_data[['Code'] + wm]
    data = pd.merge(data, wm_data, on='Code', how='left')
# =============================================================================
# Back to general data cleaning
# =============================================================================
# reverse code the variables by subtracting them from the maximum value
for col in reverse_cols:
    print(f'Reverse coding: {col}')
    if col in data.columns:
        data[col] = data[col].max() - data[col]

for col in median_cols:
    if col in data.columns:
        data[col] = abs(data[col] - data[col].median())
        # then do the reverse coding
        data[col] = data[col].max() - data[col]

# print the number of missing values per column
missing = data.isna().sum().sort_values(ascending=False)
print('Missing values per column:')
for col, count in missing.items():
    if count > 0:
        print(f'{col}: {count}')

# keep only psychopathology, behavioral, and wm variables
data = data[psychopathology_residual + behavior_residual + wm + ['Code', 'Sex', 'Age']]

# Remove participants with missing values in wm variables
excluded_wm_missing = data[data[wm].isna().any(axis=1)]['Code']
data = data[~data['Code'].isin(excluded_wm_missing)]
print(f'Data shape after removing participants with missing WM values: {data.shape}')

excluded_behavior_missing = data[data[behavior_residual].isna().any(axis=1)]['Code']
data = data[~data['Code'].isin(excluded_behavior_missing)]
print(f'Data shape after removing participants with missing behavioral values: {data.shape}')

# excluded_psychopathology_missing = data[data[psychopathology_residual].isna().any(axis=1)]['Code']
# data = data[~data['Code'].isin(excluded_psychopathology_missing)]
# print(f'Data shape after removing participants with missing psychopathology values: {data.shape}')

# # drop rows with missing values
# excluded_missing = data[data.isna().any(axis=1)]['Code']
# data = data.dropna()
# print(f'Data shape after dropping missing values: {data.shape}')

# check if the column values are all the same
uniform_vars = []
for col in data.columns:
    if col == 'Sex':
        continue
    if data[col].nunique() == 1:
        # drop the column and print the column name
        data = data.drop(columns=[col])
        uniform_vars.append(col)
        print(f'{col} dropped because all values are the same')

# print the missing variables
print(f'Missing variables: {missing_vars}')

# =============================================================================
# the following code is to prepare data for MATLAB PLS implementation
# =============================================================================
# -----------------------------------------------------------------------------
# prepare for behavioral PLS
# -----------------------------------------------------------------------------
# # convert raw scores to t scores
# for col in data.columns:
#     if col in behavior or col in psychopathology:
#         z_score = zscore(data[col])
#         data[col] = z_score * 10 + 50

# save another copy with renamed columns
data_renamed = data.copy()
i, j, k, l, m = 1, 1, 1, 1, 1
i_, j_, k_, l_ = 1, 1, 1, 1

for col in data_renamed.columns:
    if col in behavior_residual:
        data_renamed.rename(columns={col: f'Behav_{i}'}, inplace=True)
        i += 1
    elif col in behavior:
        data_renamed.rename(columns={col: f'BehavOri_{i_}'}, inplace=True)
        i_ += 1
    elif col in psychopathology_residual:
        data_renamed.rename(columns={col: f'Psych_{j}'}, inplace=True)
        j += 1
    elif col in psychopathology:
        data_renamed.rename(columns={col: f'PsychOri_{j_}'}, inplace=True)
        j_ += 1
    elif col in QSM_residual:
        data_renamed.rename(columns={col: f'QSM_{k}'}, inplace=True)
        k += 1
    elif col in QSM:
        data_renamed.rename(columns={col: f'QSMOri_{k_}'}, inplace=True)
        k_ += 1
    elif col in iron_residual:
        data_renamed.rename(columns={col: f'Iron_{l}'}, inplace=True)
        l += 1
    elif col in iron:
        data_renamed.rename(columns={col: f'IronOri_{l_}'}, inplace=True)
        l_ += 1
    elif col in brain_volume_residual:
        data_renamed.rename(columns={col: f'BrainVol_{m}'}, inplace=True)
        m += 1

# separate into males and females
male = data[data['Sex'] == 1]
male_renamed = data_renamed[data_renamed['Sex'] == 1]
female = data[data['Sex'] == 2]
female_renamed = data_renamed[data_renamed['Sex'] == 2]
print(f'Data shape after cleaning: {data.shape}')

# -----------------------------------------------------------------------------
# Separate the variables into separate DataFrames
# -----------------------------------------------------------------------------
# variables = {
#     'psychopathology': psychopathology_residual,
#     'behavioral': behavior_residual,
#     'QSM': QSM_residual,
#     'iron': iron_residual,
#     'psychopathologyori': psychopathology,
#     'behavioralori': behavior,
#     'QSMori': QSM,
#     'ironori': iron
# }

# Define the initial variables dictionary
all_variables = {
    'psychopathology': psychopathology_residual,
    'behavioral': behavior_residual,
    'QSM': QSM_residual,
    'iron': iron_residual,
    'brain_volume': brain_volume_residual,
    'wm': wm
}

# Create the filtered variables dictionary based on inclusion flags
variables = {key: value for key, value in all_variables.items() if key in variables_dict and variables_dict[key][0]}

for key, vars in variables.items():
    globals()[f'{key}_male'] = male[vars]
    globals()[f'{key}_female'] = female[vars]
    globals()[key] = data[vars]

if __name__ == '__main__':
    # save cleaned data
    data.to_csv('./Data/cleaned_data.csv', index=False)
    data_renamed.to_csv('./Data/cleaned_data_renamed.csv', index=False)
    male_renamed.to_csv('./Data/cleaned_data_male_renamed.csv', index=False)
    female_renamed.to_csv('./Data/cleaned_data_female_renamed.csv', index=False)

    # # test for correlations between brain volume variables and task performance variables
    # corr_df = pd.DataFrame()
    #
    # for brain_var in QSM_residual:
    #     for task_var in psychopathology_residual:
    #         corr, p = pearsonr(female[brain_var], female[task_var])
    #         temp_df = pd.DataFrame({'Brain Iron': [brain_var], 'Psychopathology': [task_var],
    #                                 'Correlation': [corr], 'p': [p]})
    #         corr_df = pd.concat([corr_df, temp_df], ignore_index=True)
    #
    # # adjust the p value for multiple comparisons
    # corr_df['p_adjusted'] = multipletests(corr_df['p'], method='fdr_bh')[1]
    #
    # print(corr_df['Correlation'].mean())
    # print(f'total comparisons: {corr_df.shape[0]}')
    # print(f'significant before adjustment: {corr_df[corr_df["p"] < 0.05].shape[0]}')
    # print(f'significant after adjustment: {corr_df[corr_df["p_adjusted"] < 0.05].shape[0]}')
    #
    # # plot the correlation matrix
    # corr_df = corr_df.pivot(index='Brain Iron', columns='Psychopathology', values='Correlation')
    # plt.figure(figsize=(30, 30))
    # sns.heatmap(corr_df, annot=True, cmap='coolwarm')
    # plt.savefig('./Figures/Brain_Psych_Corr.png', dpi=800)
    # plt.tight_layout()
    # plt.show()

    # save behavioral PLS data
    keys_to_save = [key for key in variables.keys()]

    # Iterate over each key and save corresponding male, female, and combined DataFrames
    for key in keys_to_save:
        for gender in ['male', 'female']:
            var_name = f'{key}_{gender}'
            if var_name in globals():
                df = globals()[var_name]
                df.to_csv(f'./Data/PLS_Data/{var_name}.csv', index=False)  # Save each to a CSV file
                print(f'Saved: {var_name}.csv')

        # Also save the combined (non-gendered) version
        if key in globals():
            df = globals()[key]
            df.to_csv(f'./Data/PLS_Data/{key}.csv', index=False)  # Save the combined version
            print(f'Saved: {key}.csv')

print('Preprocessing done!')