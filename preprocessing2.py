import pandas as pd
import numpy as np
import semopy as sem
from semopy import Model, calc_stats, semplot
from preprocessing import QSM_female, QSM_male, brain_volume_female, brain_volume_male

# calculate the mean QSM values across the left and right hemispheres
QSM_list = [QSM_male, QSM_female]
brain_volume_list = [brain_volume_male, brain_volume_female]

for i, data in enumerate(QSM_list):
    data['Putamen'] = data[['QSM_l_Pu_mean_residual', 'QSM_r_Pu_mean_residual']].mean(axis=1)
    data['Caudate'] = data[['QSM_l_Cd_mean_residual', 'QSM_r_Cd_mean_residual']].mean(axis=1)
    data['Globus Pallidus'] = data[['QSM_l_GP_mean_residual', 'QSM_r_GP_mean_residual']].mean(axis=1)
    # only keep the columns of interest
    data = data[['Putamen', 'Caudate', 'Globus Pallidus']]
    QSM_list[i] = data

for i, data in enumerate(brain_volume_list):
    data['Thalamus'] = data[['Vol_Thalamus_L_resid_norm', 'Vol_Thalamus_R_resid_norm']].mean(axis=1)
    data['Caudate'] = data[['Vol_Caudate_L_resid_norm', 'Vol_Caudate_R_resid_norm']].mean(axis=1)
    data['Putamen'] = data[['Vol_Putamen_L_resid_norm', 'Vol_Putamen_R_resid_norm']].mean(axis=1)
    data['Pallidum'] = data[['Vol_Pallidum_L_resid_norm', 'Vol_Pallidum_R_resid_norm']].mean(axis=1)
    data['Hippocampus'] = data[['Vol_Hippocampus_L_resid_norm', 'Vol_Hippocampus_R_resid_norm']].mean(axis=1)
    data['Amygdala'] = data[['Vol_Amygdala_L_resid_norm', 'Vol_Amygdala_R_resid_norm']].mean(axis=1)
    data['Accumbens'] = data[['Vol_Accumbens_L_resid_norm', 'Vol_Accumbens_R_resid_norm']].mean(axis=1)
    # only keep the columns of interest
    data = data[['Thalamus', 'Caudate', 'Putamen', 'Pallidum', 'Hippocampus', 'Amygdala', 'Accumbens']]
    brain_volume_list[i] = data

# save the data
QSM_list[0].to_csv('./Data/PLS_Data/combined_QSM_male.csv', index=False)
QSM_list[1].to_csv('./Data/PLS_Data/combined_QSM_female.csv', index=False)
brain_volume_list[0].to_csv('./Data/PLS_Data/combined_brain_volume_male.csv', index=False)
brain_volume_list[1].to_csv('./Data/PLS_Data/combined_brain_volume_female.csv', index=False)
example_QSM = QSM_list[0]
example_brain_volume = brain_volume_list[0]

