import sys
import os
import scipy.io as sio
import numpy as np
import pandas as pd
from scipy.stats import norm
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from var_def import QSM_residual, iron_residual, brain_volume_residual, psychopathology_residual

# add path to the PLS results
result_dir = os.path.abspath('C:/Users/zuire/OneDrive/桌面/胡勉之/Texas A&M University/IronDeficiency/MATLAB/Result')
sys.path.append(result_dir)

# read original data
data = pd.read_csv('./Data/cleaned_data.csv')

print(pearsonr(data['Ferritin_ngperml_residual'], data['Hemoccue_Hb_residual']))


def get_pls_results(lv_path, boot_ratio_path, var_names, method='fdr_bh', p=.05):

    # define the path
    lv_path = os.path.join(result_dir, lv_path)
    boot_ratio_path = os.path.join(result_dir, boot_ratio_path)

    # read lv_vals file
    lv_vals = sio.loadmat(lv_path)

    # read bootstrap ratio file
    boot_ratio = sio.loadmat(boot_ratio_path)

    u1 = lv_vals['u1'][:, 0]
    boot_ratio = boot_ratio['bsrs1']

    # combine the data with their respective columns
    result = np.column_stack((u1, boot_ratio))

    # name the columns
    df = pd.DataFrame(result, columns=['u1', 'boot_ratio'])

    # calculate the p values according to the boot_ratio
    df['p_value'] = 2 * (1 - norm.cdf(abs(df['boot_ratio'])))

    # adjust the p values for multiple comparisons
    df['p_value_adjusted'] = multipletests(df['p_value'], method=method)[1]

    # if boot_ratio is greater than 1.96, then the corresponding u1 value is significant
    df['significant'] = abs(df['p_value_adjusted']) < p

    # add the variable names to the DataFrame as the first column
    df.insert(0, 'Variable', var_names)

    return df


# get the results
neuro_iron_results = get_pls_results('PLS_Behav_neuro~iron_lv_vals.mat',
                                     'PLS_Behav_neuro~iron.mat',
                                     iron_male)

neuro_iron_all_results = get_pls_results('PLS_Behav_neuro_all~iron_lv_vals.mat',
                                            'PLS_Behav_neuro_all~iron.mat',
                                            iron_male)

QSM_iron_results = get_pls_results('PLS_Behav_female_QSM~iron149_lv_vals.mat',
                                      'PLS_Behav_female_QSM~iron149.mat',
                                   iron_residual)

QSM_neuro_results = get_pls_results('PLS_Behav_female_brainv_QSM_lv_vals.mat',
                                            'PLS_female_brainv~QSM~iron.mat',
                                       brain_volume_male)

brain_volume_iron_results = get_pls_results('PLS_Behav_female_brainv~iron_lv_vals.mat',
                                            'PLS_Behav_female_brainv~iron.mat',
                                       iron_residual)

brain_volume_QSM_results = get_pls_results('PLS_Behav_female_brainv~QSM_lv_vals.mat',
                                            'PLS_Behav_female_brainv~QSM.mat',
                                       QSM_residual)

brain_volume_combined_QSM_results = get_pls_results('PLS_Behav_female_brain_volume~QSM_lv_vals.mat',
                                            'PLS_Behav_female_brain_volume~QSM.mat',
                                       example_QSM)

psychopathology_iron_results = get_pls_results('PLS_Behav_female_psychopathology~iron_lv_vals.mat',
                                                    'PLS_Behav_female_psychopathology~iron.mat',
                                                iron_residual)

psychopathology_QSM_results = get_pls_results('PLS_Behav_female_psychopathology~QSM_lv_vals.mat',
                                                'PLS_Behav_female_psychopathology~QSM.mat',
                                              QSM_residual)

psychopathology_brainv_results = get_pls_results('PLS_Behav_female_psychopathology~brainv_lv_vals.mat',
                                                'PLS_Behav_female_psychopathology~brainv.mat',
                                              brain_volume_residual)

cogsummary_iron_results = get_pls_results('PLS_Behav_female_behav~iron_lv_vals.mat',
                                            'PLS_Behav_female_behav~iron.mat',
                                            iron_residual)

cogsummary_QSM_results = get_pls_results('PLS_Behav_male_behav~QSM_lv_vals.mat',
                                            'PLS_Behav_male_behav~QSM.mat',
                                            QSM_residual)

cogsummary_psychopathology_results = get_pls_results('PLS_Behav_female_behav~psychopathology_lv_vals.mat',
                                                        'PLS_Behav_female_behav~psychopathology.mat',
                                                        psychopathology_residual)

cogsummary_myelin_results = get_pls_results('PLS_Behav_cogsummary~myelin_lv_vals.mat',
                                            'PLS_Behav_cogsummary~myelin.mat',
                                            myelin_male)

cogsummary_brainv_results = get_pls_results('PLS_Behav_female_behav~brainv_lv_vals.mat',
                                            'PLS_Behav_female_behav~brainv.mat',
                                            brain_volume_residual)
cogsummary_brainv_results = cogsummary_brainv_results[cogsummary_brainv_results['significant'] == True]

myelin_neuro_results = get_pls_results('PLS_Behav_myelin~neuro_lv_vals.mat',
                                        'PLS_Behav_myelin~neuro.mat',
                                       neuro_male)


# plot the results
sns.set_theme(style='whitegrid')
sns.set_context('talk')
plt.figure(figsize=(15, 15))
cogsummary_psychopathology_results['u1'] = cogsummary_psychopathology_results['u1'] * -1
sns.barplot(x='u1', y='Variable', data=cogsummary_psychopathology_results, hue='significant')
plt.xlabel('Correlation Strength')
plt.ylabel('')
plt.tight_layout()
plt.savefig('./Figures/PLS_Cog_Psychopathology_all.png', dpi=600)
plt.show()

