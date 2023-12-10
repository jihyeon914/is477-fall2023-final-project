from ydata_profiling import ProfileReport
import pandas as pd
import os

winequality_red_df = pd.read_csv('data/wine_quality/winequality-red.csv', delimiter=";")
winequality_white_df = pd.read_csv('data/wine_quality/winequality-white.csv', delimiter=";")

profile_red = ProfileReport(winequality_red_df, title="Profiling Report - Red Wine")
profile_white = ProfileReport(winequality_white_df, title="Profiling Report - White Wine")

directory = 'profiling'
#if not os.path.exists(directory):
#    os.makedirs(directory)

profile_red.to_file(os.path.join(directory, "report_red_wine.html"))
profile_white.to_file(os.path.join(directory, "report_white_wine.html"))

print("Profile reports successfully saved under profiling folder")
 
 