# define some variables
iron_residual = ['Ferritin_ngperml_residual', 'Hemoccue_Hb_residual']
iron = ['Ferritin_ngperml', 'Hemoccue_Hb']

neuro_residual = ['f_iron_l_Pu_mean_residual', 'f_iron_r_Pu_mean_residual', 'f_iron_l_Cd_mean_residual',
                  'f_iron_r_Cd_mean_residual', 'f_iron_l_GP_mean_residual', 'f_iron_r_GP_mean_residual']

QSM_residual = ['QSM_l_Pu_mean_residual', 'QSM_r_Pu_mean_residual', 'QSM_l_Cd_mean_residual',
                'QSM_r_Cd_mean_residual', 'QSM_l_GP_mean_residual', 'QSM_r_GP_mean_residual']
QSM = ['QSM_l_Pu_mean', 'QSM_r_Pu_mean', 'QSM_l_Cd_mean', 'QSM_r_Cd_mean', 'QSM_l_GP_mean', 'QSM_r_GP_mean']
# wm = ['FA_Splenium_by_QSM', 'FA_Splenium_by_QSM_age', 'FA_SLF_by_QSM', 'FA_SLF_by_QSM_age', 'T1w_T2w_Ratio_BA44']
wm = ['FA_Splenium_by_QSM_age', 'FA_SLF_by_QSM_age']

myelin_residual = ['f_myelin_r_Pu_mean_residual', 'f_myelin_l_Pu_mean_residual', 'f_myelin_r_Cd_mean_residual',
                   'f_myelin_l_Cd_mean_residual', 'f_myelin_r_GP_mean_residual', 'f_myelin_l_GP_mean_residual']

behavior_residual = ['CPT_HITS_R_residual', 'CPT_OMI_R_residual', 'CPT_COM_R_residual', 'CPT_DPR_R_residual',
                     'WASI_Vocab_Raw_residual', 'WASI_Matrix_Raw_residual', 'RAVLT_ListA_Correct_Rec_residual',
                     'RAVLT_ListA_Immed_Re_T1_residual', 'RAVLT_ListB_Immed_Re_T1_residual',
                     'RAVLT_ListA_Delay_Re_T1_residual', 'RAVLT_ListA_Delay_Re_T2_residual',
                     'RAVLT_std_total_learn_residual', 'RAVLT_Learning_Ratio_residual',
                     'RAVLT_T1T5_Difference_residual', 'RAVLT_Early_Learning_residual',
                     'RAVLT_Late_Learning_residual', 'RAVLT_Pro_Interfere_residual', 'RAVLT_Retro_Interfere_residual',
                     'RAVLT_Retention_residual', 'RAVLT_Retrieval_Effic_residual', 'Stroop_WordColor_Read_residual',
                     'Stroop_WordColor_ColRec_residual', 'Stroop_WordColor_InkRec_residual',
                     'Trail_PartA_time_residual', 'Trail_PartA_error_seq_residual', 'TrailsB_Time_residual',
                     'Trail_PartB_error_seq_residual', 'Trail_PartB_error_set_residual', 'Pegboard_Avg_Time_residual',
                     'Pegboard_Avg_Dropped_residual', 'NEURO_DIGIT_Forward_residual', 'NEURO_DIGIT_Backward_residual',
                     'NEURO_DIGIT_Sequencing_residual', 'NEURO_DDT_kvalue_log_residual']

behavior = ['CPT_HITS_R', 'CPT_OMI_R', 'CPT_COM_R', 'CPT_DPR_R', 'WASI_Vocab_Raw', 'WASI_Matrix_Raw',
            'RAVLT_ListA_Correct_Recognition', 'RAVLT_ListA_Immed_Recall_Trial1', 'RAVLT_ListB_Immed_Recall_Trial1',
            'RAVLT_ListA_Delay_Recall_Trial1', 'RAVLT_ListA_Delay_Recall_Trial2', 'RAVLT_std_total_learn',
            'RAVLT_Learning_Ratio', 'RAVLT_T1T5_Difference', 'RAVLT_Early_Learning', 'RAVLT_Late_Learning',
            'RAVLT_Proactive_Interfere', 'RAVLT_Retroactive_Interfere', 'RAVLT_Retention', 'RAVLT_Retrieval_Efficiency',
            'Stroop_WordColor_WordRead',
            'Stroop_WordColor_ColorRecognized', 'Stroop_WordColor_InkRecognized', 'Trail_PartA_time',
            'Trail_PartA_error_seq',
            'TrailsB_Time', 'Trail_PartB_error_seq', 'Trail_PartB_error_set', 'Pegboard_Avg_Time',
            'Pegboard_Avg_Dropped', 'NEURO_DIGIT_ForwardScore', 'NEURO_DIGIT_BackwardScore',
            'NEURO_DIGIT_SequencingScore', 'NEURO_DDT_kvalue']

psychopathology_p_residual = ['CBCL_AnxDep_residual', 'CBCL_WthdrDep_residual', 'CBCL_SomaComplt_residual',
                              'CBCL_SocProbs_residual', 'CBCL_ThtProbs_residual', 'CBCL_AttenProbs_residual',
                              'CBCL_RuleBreak_residual', 'CBCL_AgresBehav_residual', 'CBCL_DSM_DepProb_residual',
                              'CBCL_DSM_AnxProb_residual',
                              'CBCL_DSM_SomaProb_residual', 'CBCL_DSM_AttenDef_residual',
                              'CBCL_DSM_OppDefProb_residual',
                              'CBCL_DSM_CondProb_residual', 'CBCL_Scale_SluggCog_residual',
                              'CBCL_Scale_ObsesComp_residual',
                              'CBCL_Scale_StressProb_residual', 'CBCL_Activities_residual', 'CBCL_Social_residual',
                              'CBCL_edu_residual', 'SCARED_C_GAD_residual', 'SCARED_C_PanicD_residual',
                              'SCARED_C_SocialPhob_residual', 'SCARED_C_SchoolPhob_residual',
                              'SCARED_C_SeparationAnx_residual',
                              'SCARED_P_GAD_residual', 'SCARED_P_PanicD_residual', 'SCARED_P_SocialPhob_residual',
                              'SCARED_P_SchoolPhob_residual', 'SCARED_P_SeparationAnx_residual',
                              'CESD_C_Somatic_residual',
                              'CESD_C_Depressed_residual', 'CESD_C_Positive_residual', 'CESD_C_Interpersonal_residual',
                              'CDRSR_SCORE_residual', 'PARS_total_residual']

psychopathology_residual = ['CBCL_AnxDep_residual', 'CBCL_WthdrDep_residual', 'CBCL_SomaComplt_residual',
                            'CBCL_SocProbs_residual', 'CBCL_ThtProbs_residual', 'CBCL_AttenProbs_residual',
                            'CBCL_RuleBreak_residual', 'CBCL_AgresBehav_residual', 'CBCL_Activities_residual',
                            'CBCL_Social_residual', 'CBCL_edu_residual', 'SCARED_C_Total_residual',
                            'SCARED_P_Total_residual', 'CESD_C_Score_residual',
                            'CDRSR_SCORE_residual', 'PARS_total_residual']


psychopathology = ['CBCL_AnxDepSCORE', 'CBCL_WthdrDepSCORE', 'CBCL_SomaCompltSCORE', 'CBCL_SocProbsSCORE',
                   'CBCL_ThtProbsSCORE', 'CBCL_AttenProbsSCORE', 'CBCL_RuleBreakSCORE', 'CBCL_AgresBehavSCORE',
                   'CBCL_Activities_Score', 'CBCL_SocialSCORE', 'CBCL_eduSCORE', 'SCARED_C_Total_Score',
                   'SCARED_P_Total_Score', 'CESD_C_Score', 'CDRSR_SCORE', 'PARS_total']


brain_volume_residual = ['Vol_Thalamus_L_residual', 'Vol_Caudate_L_residual', 'Vol_Putamen_L_residual',
                         'Vol_Pallidum_L_residual', 'Vol_Hippocampus_L_residual', 'Vol_Amygdala_L_residual',
                         'Vol_Accumbens_L_residual', 'Vol_Thalamus_R_residual', 'Vol_Caudate_R_residual',
                         'Vol_Putamen_R_residual', 'Vol_Pallidum_R_residual', 'Vol_Hippocampus_R_residual',
                         'Vol_Amygdala_R_residual', 'Vol_Accumbens_R_residual', 'Vol_eTIV_residual']

# define the variables that need to be transformed and then removed from the data
behavior_old = ['RAVLT_ListA_Sem_Assoc_residual', 'RAVLT_ListB_Sem_Assoc_residual', 'RAVLT_ListA_Semantic_Associates',
                'RAVLT_ListB_Semantic_Associates', 'RAVLT_ListA_Phon_Assoc_residual', 'RAVLT_ListB_Phon_Assoc_residual',
                'RAVLT_ListA_Phonemic_Associates', 'RAVLT_ListB_Phonemic_Associates', 'Pegboard_RH_Time_residual',
                'Pegboard_LH_Time_residual', 'Pegboard_RH_Dropped_residual', 'Pegboard_LH_Dropped_residual',
                'Pegboard_RH_Time', 'Pegboard_LH_Time', 'Pegboard_RH_Dropped', 'Pegboard_LH_Dropped',
                'Pegboard_LH_Total_Corr_residual', 'Pegboard_RH_Total_Corr_residual', 'Pegboard_LH_Total_Correct',
                'Pegboard_RH_Total_Correct']
psychopathology_old = ['SCARED_P_GAD_residual', 'SCARED_P_PanicD_residual', 'SCARED_P_SocialPhob_residual',
                       'SCARED_P_SchoolPhob_residual', 'SCARED_P_SeparationAnx_residual', 'SCARED_P_GAD_Score',
                       'SCARED_P_PanicD_Score', 'SCARED_P_SocialPhob_Score', 'SCARED_P_SchoolPhob_Score',
                       'SCARED_P_SeparationAnx_Score']


