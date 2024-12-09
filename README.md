# Big Data Cloud Project: Stock Market Data Analysis

## Table of Contents

1. [Project Description](#project-description)  
2. [Need for Big Data and Cloud](#need-for-big-data-and-cloud)  
3. [Dataset Description](#dataset-description)  
4. [Application Description](#application-description)  
5. [Software Design](#software-design)  
6. [Usage](#usage)  
7. [Performance Evaluation](#performance-evaluation)  
8. [Advanced Features](#advanced-features)  
9. [Conclusions](#conclusions)  
10. [References](#references)  

---

## Project Description

This project aims to solve a Big Data problem by implementing an end-to-end application on the Cloud. The project focuses on analyzing stock market data using Big Data technologies, addressing data collection, processing, and performance optimization on cloud infrastructure.

---

## Need for Big Data and Cloud

### Why Big Data?

- **Volume**: The dataset consists of stock market data over several years, totaling more than 1 GB.  
- **Velocity**: Real-time and historical market data require quick processing for timely analysis.  
- **Variety**: Data includes multiple attributes such as opening price, closing price, and trading volume.  

### Why Cloud?

- **Scalability**: Cloud platforms offer the ability to scale resources as data volume increases.  
- **Cost-Efficiency**: Pay-as-you-go models reduce infrastructure costs.  
- **Performance**: Cloud infrastructure supports distributed computing, allowing faster processing of large datasets.  

---

## Dataset Description

- **Source**: [Kaggle - Stock Market Data](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data)  
- **Acquisition**: Data was downloaded directly from Kaggle.  
- **Content**: The dataset includes stock prices and trading volumes from major companies (e.g., Apple, Google, Microsoft).  
- **Format**: CSV files (not JSON).  
- **Size**: Approximately 1.2 GB.  

### Sample Data Format (CSV)

The dataset is in CSV format, with the following columns:

| Date       | Low       | Open      | Volume   | High      | Close     | Adjusted Close |
|------------|-----------|-----------|----------|-----------|-----------|----------------|
| 18-11-1999| 28.612303 | 32.546494 | 62546380 | 35.765381 | 31.473534 | 27.066582      |
| 19-11-1999| 28.478184 | 30.713518 | 15234146 | 30.758226 | 28.880545 | 24.836662      |
| 22-11-1999| 28.657009 | 29.551144 | 6577870  | 31.473534 | 31.473534 | 27.066582      |
| 23-11-1999| 28.612303 | 30.400572 | 5975611  | 31.205294 | 28.612303 | 24.605980      |
| 24-11-1999| 28.612303 | 28.701717 | 4843231  | 29.998213 | 29.372318 | 25.259573      |
| 26-11-1999| 29.148785 | 29.238197 | 1729466  | 29.685265 | 29.461731 | 25.336472      |
| 29-11-1999| 29.014664 | 29.327612 | 4074751  | 30.355865 | 30.132332 | 25.913176      |
| 30-11-1999| 29.282904 | 30.042917 | 4310034  | 30.713518 | 30.177038 | 25.951620      |
| 01-12-1999| 29.953505 | 30.177038 | 2957329  | 31.071173 | 30.713518 | 26.412981      |

### Note

We will be working **exclusively with CSV files** for this project, as they are straightforward for data analysis tasks and compatible with Big Data tools like Apache Spark and Pandas.

---

## Application Description

### Programming Model

- **Apache Spark**: Used for distributed data processing.  
- **Pandas**: For local data analysis and manipulation.  
- **Python**: Programming language for data processing scripts.  

### Cloud Platform and Infrastructure

- **Google Cloud Platform (GCP)**  
  - **Compute Engine**: Virtual machines with scalable vCPUs.  
  - **Cloud Storage**: For storing large datasets.  
  - **Dataproc**: Managed Spark and Hadoop clusters.  

---
## Usage

### 1. Installation in Local Mode

#### Step 1: Create a Startup Script

In your Cloud Shell, create a file named `spark.sh` with the following content:

```bash
#!/bin/bash
echo export JAVA_HOME=/usr/lib/jvm/default-java >> /etc/profile.d/spark.sh
echo export PATH=\$PATH:/usr/local/spark/bin >> /etc/profile.d/spark.sh
apt-get update
apt-get install -y default-jre python-is-python3
wget https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz
tar xzf spark-3.5.3-bin-hadoop3.tgz
mv spark-3.5.3-bin-hadoop3 /usr/local/spark
```
#### Step 2: Create a VM Instance with the Startup Script

Run the following command to create a VM instance in GCP:

```bash
gcloud compute instances create spark-local --zone=europe-southwest1-a \
--machine-type=e2-standard-4 --metadata-from-file startup-script=spark.sh
```

### 2. Local Job Submission

#### Step 1: SSH into the VM
Start your VM clicking SSH

#### Step 2: Verify Spark Installation

Check if Spark is correctly installed:

```bash
pyspark
```
### 3. Local Job Submission

#### Step 1: Upload Files to the VM

Upload all the files from this repository to the VM

#### Step 2: Submit a Local Spark Job

Execute the following command in the VM to submit a local Spark job:

```bash
spark-submit main.py A.csv output
```

#### Step 3: Check the Output

Wait for the command to complete and check its output. When the command finishes, list the output folder (containing one file per reducer task):

```bash
ls output
```

View the content of the output files:

```bash
cat output/*
```

