#This readme file describes what altius_enformer.py is for and how it can be used. This model essentially predicts how a particular region contributes to the expression of a transcription start site, or TSS. It does this by centering the prediction window on a region described in the ROIs.csv file, then finds transcription start sites within 50 kb of the center of that region. For each transcription site, the program will predict the contributions within that region to the transcription start site. These scores are found in the ROI_X_scored_positions_TSS_Y.bed files.


Inputs: 

ROIs.csv = positions of regions of interest
pos_report.csv = complete list of transcription start sites across all chromosomes
targets_human.txt = doc containing list of cells that one can use to predict for (CD8+ cells are line 4760)
model_path = you must download and correct the path of the model in the script (near the top) (see the paper for details)
genome.fa = fasta file containing the entire genome, see paper for details

Outputs:

ROI_contribution_scores_X.bed = bed file containing scores for each 128-bp position (contributions scores are relevant to the ROI provided)
ROI_local_transcripts_X.bed = bed file containing local transcripts to the ROI
ROI_X_scored_positions_TSS_Y.bed = contribution scores for the TSS Y (references the TSS in local transcripts file from top to bottom) with respect to the ROI X (X being the index for the ROIs in ROIs.csv). Scores are given per 128 bp section.

How to use:
1. Ensure all the required packages are installed. See requirements.txt.
2. Make sure the model is installed and change the path in the altius_enformer.py file.
3. After activating the environment, run "python3 altius_enformer.py".
4. Create predictions folder by type "mkdir predictions" in the local directory.
5. The program will ask you if you are going to look for variants, type N. The variant app still needs work.
6. When prompted for which line of targets_human.txt you want to use, type 4760.
7. Find your files in the predictions folder after completion.




