
# Import necessary libraries and modules
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
import logging
import mlflow

# Define the main function for the script
def main():
    """Main function of the script."""

    # Define command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="path to input data")
    parser.add_argument("--test_train_ratio", type=float, required=False, default=0.25)
    parser.add_argument("--train_data", type=str, help="path to train data")
    parser.add_argument("--test_data", type=str, help="path to test data")
    args = parser.parse_args()

    # Start an MLflow run for logging
    mlflow.start_run()

    # Print the arguments passed to the script
    print(" ".join(f"{k}={v}" for k, v in vars(args).items()))

    # Load input data from the specified path
    print("input data:", args.data)
    credit_df = pd.read_csv(args.data, header=1, index_col=0)

    # Log metrics about the loaded dataset
    mlflow.log_metric("num_samples", credit_df.shape[0])
    mlflow.log_metric("num_features", credit_df.shape[1] - 1)

    # Split the dataset into training and testing sets
    credit_train_df, credit_test_df = train_test_split(
        credit_df,
        test_size=args.test_train_ratio,
    )

    # Save the training and testing datasets to the specified paths
    credit_train_df.to_csv(os.path.join(args.train_data, "data.csv"), index=False)
    credit_test_df.to_csv(os.path.join(args.test_data, "data.csv"), index=False)

    # End the MLflow run
    mlflow.end_run()

# Check if the script is being run directly
if __name__ == "__main__":
    main()
