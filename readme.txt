#This readme file describes what altius_enformer.py is for and how it can be used. This model essentially predicts how a particular region contributes to the expression of a transcription start site, or TSS. It does this by centering the prediction window on a region described in the ROIs.csv file, then finds transcription start sites within 50 kb of the center of that region. For each transcription site, the program will predict the contributions within that region to the transcription start site. These scores are found in the ROI_X_scored_positions_TSS_Y.bed files.



Original Publication: Effective gene expression prediction from sequence by integrating long-range interactions, Avsec et al.
Website: https://www.nature.com/articles/s41592-021-01252-x


Inputs: 

ROIs.csv = positions of regions of interest
pos_report.csv = complete list of transcription start sites across all chromosomes
targets_human.txt = doc containing list of cells that one can use to predict for (CD8+ cells are line 4760)
model_path = you must download and correct the path of the model in the script (near the top of altius_enformer.py). Make sure that you also place the variables folder in the local folder of the saved_model.pb. (Location: tfhub.dev/deepmind/enformer/1)
genome.fa = fasta file containing the entire human genome (GRCh38/hg38), uploaded to Google Drive (https://drive.google.com/drive/folder/1rs20eRnR9yqWsuxPWOkQwCI1d4DHh3iQ)

Outputs:

ROI_contribution_scores_X.bed = bed file containing scores for each 128-bp position (contributions scores are relevant to the ROI provided)
ROI_local_transcripts_X.bed = bed file containing local transcripts to the ROI
ROI_X_scored_positions_TSS_Y.bed = contribution scores for the TSS Y (references the TSS in local transcripts file from top to bottom) with respect to the ROI X (X being the index for the ROIs in ROIs.csv). Scores are given per 128 bp sections.


How to run the unit test:
1. Ensure all the required packages are installed. See requirements.txt.
2. Make sure the model is installed and change the path in the altius_enformer.py file.
3. Create predictions folder by typing "mkdir predictions" in the local directory.
4. After activating the environment, run "python3 altius_enformer.py".
5. The program will ask you if you are going to look for variants, type N. The variant app still needs work.
6. When prompted for which line of targets_human.txt you want to use, type 4760 (this points to the CD8+ dataset).
7. Find your files in the predictions folder after completion.
8. The files in the "predictions" folder should match those in "unit_test_predictions" exactly. If this is not the case, contact jrodriguez@altius.org.
9. After confirming the files are the same, change the transcript variable at the top of "altius_enformer.py" to equal "pd.read_csv('pos_report.csv')".
10. Your program should be ready to use! Running the program is about the same as the unit test EXCEPT you will need to supply different ROIs in the ROIs.csv.





