import pandas as pd
import numpy as np
import semopy as sem
from semopy import Model, calc_stats, semplot
from preprocessing import data, psychopathology, behavioral

# Define the model
model = '''
# Latent variables
psychopathology =~ CBCL_AnxDep_residual + CBCL_WthdrDep_residual + CBCL_SomaComplt_residual + CBCL_SocProbs_residual + CBCL_ThtProbs_residual + CBCL_AttenProbs_residual + CBCL_RuleBreak_residual + CBCL_AgresBehav_residual + CBCL_DSM_DepProb_residual + CBCL_DSM_AnxProb_residual + CBCL_DSM_SomaProb_residual + CBCL_DSM_AttenDef_residual + CBCL_DSM_OppDefProb_residual + CBCL_DSM_CondProb_residual + CBCL_Scale_SluggCog_residual + CBCL_Scale_ObsesComp_residual + CBCL_Scale_StressProb_residual + CBCL_Activities_residual + CBCL_Social_residual + CBCL_edu_residual + SCARED_C_GAD_residual + SCARED_C_PanicD_residual + SCARED_C_SocialPhob_residual + SCARED_C_SchoolPhob_residual + SCARED_C_SeparationAnx_residual + CESD_C_Somatic_residual + CESD_C_Depressed_residual + CESD_C_Positive_residual + CESD_C_Interpersonal_residual + CDRSR_SCORE_residual + PARS_total_residual

cognitive_performance =~ CPT_HITS_R_residual + CPT_OMI_R_residual + CPT_COM_R_residual + CPT_HRT_R_residual + CPT_VAR_R_residual + CPT_DPR_R_residual + CPT_C_R_residual + CPT_PRS_R_residual + CPT_BLKCH_R_residual + CPT_ISICH_R_residual + CPT_HRTSD_R_residual + WASI_Vocab_Raw_residual + WASI_Matrix_Raw_residual + RAVLT_ListA_Correct_Rec_residual + RAVLT_ListA_Intru_ListB_residual + RAVLT_Semantic_Associates + RAVLT_Phonemic_Associates + Stroop_WordColor_Read_residual + Stroop_WordColor_ColRec_residual + Stroop_WordColor_InkRec_residual + Trail_PartA_time_residual + Trail_PartA_error_seq_residual + TrailsB_Time_residual + Trail_PartB_error_seq_residual + Trail_PartB_error_set_residual + Pegboard_Handedness_residual + Pegboard_RH_Time_residual + Pegboard_RH_Dropped_residual + Pegboard_RH_Total_Corr_residual + Pegboard_LH_Time_residual + Pegboard_LH_Dropped_residual + Pegboard_LH_Total_Corr_residual + NEURO_DIGIT_Forward_residual + NEURO_DIGIT_Backward_residual + NEURO_DIGIT_Sequencing_residual + NEURO_DDT_kvalue_residual

body_iron =~ Ferritin_ngperml_residual + Hemoccue_Hb_residual

brain_iron =~ f_iron_l_Pu_mean_residual + f_iron_r_Pu_mean_residual + f_iron_l_Cd_mean_residual + f_iron_r_Cd_mean_residual + f_iron_l_GP_mean_residual + f_iron_r_GP_mean_residual

myelination =~ f_myelin_r_Pu_mean_residual + f_myelin_l_Pu_mean_residual + f_myelin_r_Cd_mean_residual + f_myelin_l_Cd_mean_residual + f_myelin_r_GP_mean_residual + f_myelin_l_GP_mean_residual

# Structural equation
brain_iron ~ body_iron
myelination ~ brain_iron + body_iron
psychopathology ~ body_iron + brain_iron + myelination
cognitive_performance ~ body_iron + brain_iron + myelination + psychopathology
'''

# Fit the model
# remove the first three columns
data_male = data[data['Sex'] == 1]
data_female = data[data['Sex'] == 2]
data = data.iloc[:, 3:]

fa = sem.efa.explore_pine_model(psychopathology, levels=2)
print(fa)



# model = Model(model)
# print(model.fit(data))
# stats = calc_stats(model)
# res = model.inspect()
#
# # plot the model
# g = semplot(model, 'model.png')