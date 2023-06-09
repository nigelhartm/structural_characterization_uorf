#!/bin/sh
python format_fasta.py Araport11_5_utr_20220914.fasta
python format_fasta.py Araport11_cds_20220914.fasta
python check_noatcg.py formatted_Araport11_cds_20220914.fasta
python check_noatcg.py formatted_Araport11_5_utr_20220914.fasta
python clean_fasta.py formatted_Araport11_cds_20220914.fasta
python check_noatcg.py formatted_Araport11_cds_20220914.fasta
python filter_longest_version.py formatted_Araport11_5_utr_20220914.fasta
python randomize_seq.py longest_formatted_Araport11_5_utr_20220914.fasta 2
python randomize_seq.py formatted_Araport11_cds_20220914.fasta 2
python find_uorf.py longest_formatted_Araport11_5_utr_20220914.fasta formatted_Araport11_cds_20220914.fasta
python find_uorf.py random1_longest_formatted_Araport11_5_utr_20220914.fasta random1_formatted_Araport11_cds_20220914.fasta
python find_uorf.py random2_longest_formatted_Araport11_5_utr_20220914.fasta random2_formatted_Araport11_cds_20220914.fasta
python get_stats_uorf.py uORF_longest_formatted_Araport11_5_utr_20220914.txt+uORF_random1_longest_formatted_Araport11_5_utr_20220914.txt+uORF_random2_longest_formatted_Araport11_5_utr_20220914.txt
python nt_to_aa.py uORF_longest_formatted_Araport11_5_utr_20220914.txt
python nt_to_aa.py uORF_random1_longest_formatted_Araport11_5_utr_20220914.txt
python nt_to_aa.py uORF_random2_longest_formatted_Araport11_5_utr_20220914.txt
python nt_to_aa.py formatted_Araport11_cds_20220914.fasta
python nt_to_aa.py random1_formatted_Araport11_cds_20220914.fasta
python nt_to_aa.py random2_formatted_Araport11_cds_20220914.fasta
python get_stats_peptide.py aa_formatted_Araport11_cds_20220914.fasta+aa_uORF_longest_formatted_Araport11_5_utr_20220914.txt+aa_random1_formatted_Araport11_cds_20220914.fasta+aa_uORF_random1_longest_formatted_Araport11_5_utr_20220914.txt+aa_uORF_random2_longest_formatted_Araport11_5_utr_20220914.txt
python plot_stats_peptide.py
python get_stats_peptide.py aa_formatted_Araport11_cds_20220914.fasta+aa_random1_formatted_Araport11_cds_20220914.fasta+aa_random2_formatted_Araport11_cds_20220914.fasta
python plot_stats_peptide.py
python get_stats_peptide.py aa_uORF_longest_formatted_Araport11_5_utr_20220914.txt+aa_uORF_random1_longest_formatted_Araport11_5_utr_20220914.txt+aa_uORF_random2_longest_formatted_Araport11_5_utr_20220914.txt
python plot_stats_peptide.py
python get_stats_peptide.py aa_formatted_Araport11_cds_20220914.fasta+aa_uORF_longest_formatted_Araport11_5_utr_20220914.txt
python plot_stats_peptide.py
python get_stats_peptide.py aa_formatted_Araport11_cds_20220914.fasta+aa_uORF_longest_formatted_Araport11_5_utr_20220914.txt
python cdsuorf_plot_stats_peptide.py
python pick_uorfid.py uORF_longest_formatted_Araport11_5_utr_20220914.txt equal 0
python pick_uorfid.py uORF_longest_formatted_Araport11_5_utr_20220914.txt equal 1
python pick_uorfid.py uORF_longest_formatted_Araport11_5_utr_20220914.txt equal 2
python pick_uorfid.py uORF_longest_formatted_Araport11_5_utr_20220914.txt greater 0
python pick_uorfid.py uORF_longest_formatted_Araport11_5_utr_20220914.txt greater 1
python pick_uorfid.py uORF_longest_formatted_Araport11_5_utr_20220914.txt greater 2
python plot_uORF_amount.py
python show_stats.py
