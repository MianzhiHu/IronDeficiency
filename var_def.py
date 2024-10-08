# define some variables
iron_residual = ['Ferritin_ngperml_residual', 'Hemoccue_Hb_residual']
iron = ['Ferritin_ngperml', 'Hemoccue_Hb']

neuro_residual = ['f_iron_l_Pu_mean_residual', 'f_iron_r_Pu_mean_residual', 'f_iron_l_Cd_mean_residual',
                  'f_iron_r_Cd_mean_residual', 'f_iron_l_GP_mean_residual', 'f_iron_r_GP_mean_residual']

QSM_residual = ['QSM_l_Pu_mean_residual', 'QSM_r_Pu_mean_residual', 'QSM_l_Cd_mean_residual',
                'QSM_r_Cd_mean_residual', 'QSM_l_GP_mean_residual', 'QSM_r_GP_mean_residual']
QSM = ['QSM_l_Pu_mean', 'QSM_r_Pu_mean', 'QSM_l_Cd_mean', 'QSM_r_Cd_mean', 'QSM_l_GP_mean', 'QSM_r_GP_mean']

myelin_residual = ['f_myelin_r_Pu_mean_residual', 'f_myelin_l_Pu_mean_residual', 'f_myelin_r_Cd_mean_residual',
                   'f_myelin_l_Cd_mean_residual', 'f_myelin_r_GP_mean_residual', 'f_myelin_l_GP_mean_residual']

behavior_residual = ['CPT_HITS_R_residual', 'CPT_OMI_R_residual', 'CPT_COM_R_residual', 'CPT_HRT_R_residual',
                     'CPT_VAR_R_residual', 'CPT_DPR_R_residual', 'CPT_C_R_residual', 'CPT_PRS_R_residual',
                     'CPT_BLKCH_R_residual',
                     'CPT_ISICH_R_residual', 'CPT_HRTSD_R_residual', 'WASI_Vocab_Raw_residual',
                     'WASI_Matrix_Raw_residual',
                     'RAVLT_ListA_Correct_Rec_residual', 'RAVLT_ListA_Intru_ListB_residual',
                     'RAVLT_Semantic_Associates_residual',
                     'RAVLT_Phonemic_Associates_residual', 'Stroop_WordColor_Read_residual',
                     'Stroop_WordColor_ColRec_residual',
                     'Stroop_WordColor_InkRec_residual', 'Trail_PartA_time_residual', 'Trail_PartA_error_seq_residual',
                     'TrailsB_Time_residual', 'Trail_PartB_error_seq_residual', 'Trail_PartB_error_set_residual',
                     'Pegboard_Avg_Time_residual', 'Pegboard_Avg_Dropped_residual', 'NEURO_DIGIT_Forward_residual',
                     'NEURO_DIGIT_Backward_residual', 'NEURO_DIGIT_Sequencing_residual', 'NEURO_DDT_kvalue_residual']

behavior = ['CPT_HITS_R', 'CPT_OMI_R', 'CPT_COM_R', 'CPT_HRT_R', 'CPT_VAR_R', 'CPT_DPR_R', 'CPT_C_R', 'CPT_PRS_R',
            'CPT_BLKCH_R', 'CPT_ISICH_R', 'CPT_HRTSD_R', 'WASI_Vocab_Raw', 'WASI_Matrix_Raw', 'RAVLT_ListA_Correct_Recognition',
            'RAVLT_ListA_Intrusions_ListB', 'RAVLT_Semantic_Associates', 'RAVLT_Phonemic_Associates', 'Stroop_WordColor_WordRead',
            'Stroop_WordColor_ColorRecognized', 'Stroop_WordColor_InkRecognized', 'Trail_PartA_time', 'Trail_PartA_error_seq',
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
                            'CBCL_RuleBreak_residual', 'CBCL_AgresBehav_residual', 'CBCL_DSM_DepProb_residual',
                            'CBCL_DSM_AnxProb_residual',
                            'CBCL_DSM_SomaProb_residual', 'CBCL_DSM_AttenDef_residual', 'CBCL_DSM_OppDefProb_residual',
                            'CBCL_DSM_CondProb_residual', 'CBCL_Scale_SluggCog_residual',
                            'CBCL_Scale_ObsesComp_residual',
                            'CBCL_Scale_StressProb_residual', 'CBCL_Activities_residual', 'CBCL_Social_residual',
                            'CBCL_edu_residual', 'SCARED_C_GAD_residual', 'SCARED_C_PanicD_residual',
                            'SCARED_C_SocialPhob_residual', 'SCARED_C_SchoolPhob_residual',
                            'SCARED_C_SeparationAnx_residual',
                            'CESD_C_Somatic_residual', 'CESD_C_Depressed_residual', 'CESD_C_Positive_residual',
                            'CESD_C_Interpersonal_residual', 'CDRSR_SCORE_residual', 'PARS_total_residual']

psychopathology = ['CBCL_AnxDepSCORE', 'CBCL_WthdrDepSCORE', 'CBCL_SomaCompltSCORE', 'CBCL_SocProbsSCORE',
                   'CBCL_ThtProbsSCORE', 'CBCL_AttenProbsSCORE', 'CBCL_RuleBreakSCORE', 'CBCL_AgresBehavSCORE',
                   'CBCL_DSM_DepProbSCORE', 'CBCL_DSM_AnxProbSCORE', 'CBCL_DSM_SomaProbSCORE', 'CBCL_DSM_AttenDefSCORE',
                   'CBCL_DSM_OppDefProbSCORE', 'CBCL_DSM_CondProbSCORE', 'CBCL_Scale_SluggCogSCORE',
                   'CBCL_Scale_ObsesCompSCORE', 'CBCL_Scale_StressProbSCORE', 'CBCL_Activities_Score',
                   'CBCL_SocialSCORE', 'CBCL_eduSCORE', 'SCARED_C_GAD_Score', 'SCARED_C_PanicD_Score',
                   'SCARED_C_SocialPhob_Score', 'SCARED_C_SchoolPhob_Score', 'SCARED_C_SeparationAnx_Score',
                   'CESD_C_Somatic', 'CESD_C_Depressed', 'CESD_C_Positive', 'CESD_C_Interpersonal',
                   'CDRSR_SCORE', 'PARS_total']
