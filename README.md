# Deployment_credit_card_payment_defaults

ML Production Pipeline with Python SDK v2 &amp; MLFlow in Azure


# Azure Machine Learning Pipeline Deployment

This repository contains code for deploying a machine learning pipeline in Azure Machine Learning. The pipeline consists of several components for data preparation and model training, and it ultimately deploys the trained model as an online endpoint.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Data Preparation](#data-preparation)
  - [Model Training](#model-training)
  - [Online Endpoint Deployment](#online-endpoint-deployment)
  - [Testing the Endpoint](#testing-the-endpoint)
- [Clean Up](#clean-up)

## Prerequisites
Before using this code, make sure you have the following prerequisites in place:

- [Azure Machine Learning Workspace](https://azure.microsoft.com/en-us/services/machine-learning/): You must have an Azure Machine Learning workspace set up.

## Project Structure
The project is organized as follows:

- `main.py`: The main script that defines and deploys the Azure Machine Learning pipeline.
- `components/`: Directory containing the component scripts and YAML definitions for data preparation and model training.
- `dependencies/`: Directory containing the Conda environment YAML file.
- `deploy/`: Directory containing a sample request JSON for testing the deployed endpoint.

## Usage

### Authentication
Before running the code, ensure that you have the appropriate Azure credentials set up for authentication. The code uses Azure Identity to authenticate, and it falls back to interactive sign-in if necessary.

### Data Preparation
The data preparation component is defined in `data_prep.py`, and it handles the preprocessing of the data. It splits the data into training and testing datasets and logs metrics using MLflow.

### Model Training
The model training component is defined in `train.py`. It trains a machine learning model, registers the model to the Azure Machine Learning workspace, and saves it to a file.

### Online Endpoint Deployment
The code deploys the trained model as an online endpoint. It creates an online endpoint with a unique name and deploys the latest version of the registered model.

### Testing the Endpoint
You can test the deployed online endpoint using the provided sample request JSON in the `deploy/` directory. The script in `main.py` demonstrates how to invoke the endpoint with sample data.

## Clean Up
After you've finished using the resources, don't forget to clean up:

- You can uncomment and use the `ml_client.online_endpoints.begin_delete()` method to delete the online endpoint when it's no longer needed.

Feel free to customize this README to provide additional information and context specific to your project. This documentation should help users understand how to use and maintain your Azure Machine Learning pipeline deployment.
