### Kafka dataset EDA
The goal of this project is to collect the adtech data from kafka platform. This platform allows to create a pipeline to extract the data once at the specific period of time, so what I have extracted the 7 million rows of adtech data to provide the EDA on it.
Guide how to extract the data from this platform using SingleStore database is available [here](https://docs.singlestore.com/cloud/developer-resources/functional-extensions/load-and-analyze-adtech-data/).

After preparing the SingleStore on the local environment, you can extract everything you need from that database using the db.py module.

Also make sure that you have installes every requirements using the following command:

```pip install -r requirements.txt```
