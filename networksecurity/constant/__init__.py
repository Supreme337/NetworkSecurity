import pandas as pd
import numpy as np
import os 
import sys

"""Defining common constant variables for training pipeline"""
TARGET_COLUMN="Result"
ARTIFACT_DIR: str ="Artifacts"
FILE_NAME: str ="phishingData.csv"
PIPELINE_NAME: str ="NetworkSecurity"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

"""Data Ingestion related constant start with DATA_INGESTION VAR NAME"""
DATA_INGESTION_COLLECTION_NAME:str="NetworkSecurity"
DATA-INGESTION_DATABASE_NAME:str:="Harsh"
DATA_INGESTION_DIR_NAME:"data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2