import boto3
import csv
from datetime import datetime


aws_access_key = 'AKIARMW5TT7OLIRAMPZZ'
aws_secret_key = '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'
bucket_name = 'desafbucket'
raw_zone = 'Raw'
data_source = 'Local'
data_format = 'CSV'
data_spec = 'Movies'
data_spec2 = 'Series'
current_date = datetime.now().strftime("%Y/%m/%d")
file_name = 'movies.csv'
file_name2 = 'series.csv'

move = open(file_name, "rb")
serie = open(file_name2, "rb")

s3 = boto3.client('s3', aws_access_key_id=aws_access_key,
                  aws_secret_access_key=aws_secret_key)

s3.upload_file(file_name, bucket_name,
               f"{raw_zone}/{data_source}/{data_format}/{data_spec}/{current_date}/movies.csv")
s3.upload_file(file_name2, bucket_name,
               f"{raw_zone}/{data_source}/{data_format}/{data_spec2}/{current_date}/series.csv")
