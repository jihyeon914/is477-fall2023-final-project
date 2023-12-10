rule prepare:
    output:
        "data/wine_quality/winequality-red.csv",
        "data/wine_quality/winequality-white.csv",
        "data/wine_quality/winequality.names"
    shell:
        "python scripts/prepare_data.py"
        
        
rule profile:
    input:
        "data/wine_quality/winequality-red.csv",
        "data/wine_quality/winequality-white.csv",
        "data/wine_quality/winequality.names"
    output:
        "profiling/report_red_wine.html",
        "profiling/report_white_wine.html"
    shell:
        "python scripts/profile.py"


rule analyze:
    input:
        "data/wine_quality/winequality-red.csv",
        "data/wine_quality/winequality-white.csv",
        "data/wine_quality/winequality.names"
    output:
        "results/winequality_red_heatmap.pdf",
        "results/winequality_white_heatmap.pdf",
        "results/winequality_red_corr_table.pdf",
        "results/winequality_white_corr_table.pdf"
    shell:
        "python scripts/analysis.py"


rule reproduce: 
    input: 
        "results/winequality_red_heatmap.pdf",
        "results/winequality_white_heatmap.pdf",
        "results/winequality_red_corr_table.pdf",
        "results/winequality_white_corr_table.pdf",
        "profiling/report_red_wine.html",
        "profiling/report_white_wine.html"