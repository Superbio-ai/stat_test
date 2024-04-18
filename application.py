import argparse
import pandas as pd
import logging

from app.summary_stats import generate_summary_stats
from app.stat_tests import hypothesis_tests

if __name__ == "__main__":
    
    import os
        
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--data", help="Name of file uploaded to container, which contains data", type=str, required=True, default='data.csv'
    )
    parser.add_argument(
        "-s", "--sample1", help="Name of column containing sample1 (or only sample)", type=str, required=True
    )
    parser.add_argument(
        "-s2", "--sample2", help="Name of column containing sample2 (optional)", type=str, required=False, default=None
    )
    parser.add_argument(
        "-m", "--missing_treatment", help="Either drop rows with missing data, or replace missing data with mean of each column", type=str, required=False, default='drop'
    )
    parser.add_argument(
        "-g", "--summary_stats", help="Specify summary stats to generate, if needed (can specify specific type, or whole suite)", type=str, required=True, default='suite'
    )
    parser.add_argument(
        "-h", "--hypothesis_tests", help="Specify hypothesis tests to run, if needed (can specify specific type, or whole suite)", type=str, required=True, default='suite'
    )
    parser.add_argument(
        "-o", "--output_folder", help="Output directory for model, predictions and fit metrics", type=str, required=False, default='output/'
    )
    args = parser.parse_args()
    
    if not os.path.exists('/data/' + args.output_folder):
        # Create the directory
        os.makedirs('/data/' + args.output_folder)
    
    #data is mount point
    data = pd.read_csv('/data/' + args.data)
    
    generate_summary_stats(data = data, s1 = args.sample1, s2 = args.sample2, missing_treatment = args.missing_treatment, output = args.output_folder)
    logging.info("Summary stats generated")
    
    hypothesis_tests(data = data, s1 = args.sample1, s2 = args.sample2, missing_treatment = args.missing_treatment, output = args.output_folder)
    logging.info("Hypothesis tests run")
    
    #monte_carlo(data = data, s1 = args.sample1, s2 = args.sample2, missing_treatment = args.missing_treatment, output = args.output_folder)
    logging.info("Monte carlo sampling tests run")
    
    #transformations(data = data, s1 = args.sample1, s2 = args.sample2, missing_treatment = args.missing_treatment, output = args.output_folder)
    logging.info("Transformations applied")
    
    #sampling(data = data, s1 = args.sample1, s2 = args.sample2, missing_treatment = args.missing_treatment, output = args.output_folder)
    logging.info("Data sampled")