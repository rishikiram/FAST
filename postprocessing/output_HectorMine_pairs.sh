#!/bin/bash

python parse_results.py -d ../data/waveformsCDY/fingerprints/ -p candidate_pairs_CDY_EHZ -i ../data/global_indices_HM/CDY_EHZ_idx_mapping.txt 
python parse_results.py -d ../data/waveformsRMM/fingerprints/ -p candidate_pairs_RMM_EHZ -i ../data/global_indices_HM/RMM_EHZ_idx_mapping.txt 
python parse_results.py -d ../data/waveformsCPM/fingerprints/ -p candidate_pairs_CPM_EHZ -i ../data/global_indices_HM/CPM_EHZ_idx_mapping.txt 
python parse_results.py -d ../data/waveformsHEC/fingerprints/ -p candidate_pairs_HEC_BHE -i ../data/global_indices_HM/HEC_BHE_idx_mapping.txt 
python parse_results.py -d ../data/waveformsHEC/fingerprints/ -p candidate_pairs_HEC_BHN -i ../data/global_indices_HM/HEC_BHN_idx_mapping.txt 
python parse_results.py -d ../data/waveformsHEC/fingerprints/ -p candidate_pairs_HEC_BHZ -i ../data/global_indices_HM/HEC_BHZ_idx_mapping.txt 
python parse_results.py -d ../data/waveformsGTM/fingerprints/ -p candidate_pairs_GTM_EHZ -i ../data/global_indices_HM/GTM_EHZ_idx_mapping.txt 
python parse_results.py -d ../data/waveformsRMR/fingerprints/ -p candidate_pairs_RMR_EHZ -i ../data/global_indices_HM/RMR_EHZ_idx_mapping.txt 
python parse_results.py -d ../data/waveformsTPC/fingerprints/ -p candidate_pairs_TPC_EHZ -i ../data/global_indices_HM/TPC_EHZ_idx_mapping.txt 
