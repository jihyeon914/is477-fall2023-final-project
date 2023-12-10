import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

winequality_red_df = pd.read_csv('data/wine_quality/winequality-red.csv', delimiter=";")
winequality_white_df = pd.read_csv('data/wine_quality/winequality-white.csv', delimiter=";")

red_corr = winequality_red_df.corr()

plt.figure(figsize=(16, 12))

sns.heatmap(red_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f', annot_kws={"size": 10})

directory = 'results'
#if not os.path.exists(directory):
#    os.makedirs(directory)

red_heatmap_pdf_path = os.path.join(directory, 'winequality_red_heatmap.pdf')
with PdfPages(red_heatmap_pdf_path) as pdf_red:
    pdf_red.savefig()
    
    
    
red_corr_table_pdf_path = os.path.join(directory, 'winequality_red_corr_table.pdf')
fig, ax = plt.subplots(figsize=(10, 8))
table_red = pd.plotting.table(ax, red_corr.round(2), loc='center', colWidths=[0.2]*len(red_corr.columns))
table_red.auto_set_font_size(False)
table_red.set_fontsize(8)
table_red.scale(1.2, 1.2)
ax.axis('off')
plt.savefig(red_corr_table_pdf_path, bbox_inches='tight')
plt.close() 

print("Red Wine Heatmap plot and table successfully saved to winequality_red_heatmap.pdf file.")

white_corr = winequality_white_df.corr()

plt.figure(figsize=(16, 12))

sns.heatmap(white_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f', annot_kws={"size": 10})

white_heatmap_pdf_path = os.path.join(directory, 'winequality_white_heatmap.pdf')
with PdfPages(white_heatmap_pdf_path) as pdf_white:
    pdf_white.savefig()
    
    
white_corr_table_pdf_path = os.path.join(directory, 'winequality_white_corr_table.pdf')
fig, ax = plt.subplots(figsize=(10, 8))
table_white = pd.plotting.table(ax, white_corr.round(2), loc='center', colWidths=[0.2]*len(white_corr.columns))
table_white.auto_set_font_size(False)
table_white.set_fontsize(8)
table_white.scale(1.2, 1.2)
ax.axis('off')
plt.savefig(white_corr_table_pdf_path, bbox_inches='tight')
plt.close()


print("White Wine Heatmap plot and table successfully saved to winequality_white_heatmap.pdf file.")
