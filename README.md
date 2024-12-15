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

## Software Design

### Architectural Design

The project follows a modular architecture, organized into different components for clarity and maintainability:

#### Main Processing Module

- **`main.py`**: The entry point for running different Spark jobs based on the specified operation.  
  - **Functionality**: Initializes the Spark session and dispatches the job to the appropriate module.

#### Processing Modules

- **`AveragePrice.py`**: Contains functions for calculating the average closing price per year.
- **`DataOrganization.py`**: Functions for reorganizing the dataset to improve data structure.
- **`InvertedIndex.py`**: Functions for creating an inverted index of the maximum closing prices.
- **`advanced_analysis.py`**: Provides advanced analytics on the dataset.

#### Visualization Modules

Located in the `plotFunctions` folder, these scripts generate plots for each analysis:

- **`AveragePricePlot.py`**  
- **`dataorgPlot.py`**  
- **`invertedindexplot.py`**  
- **`advanceplot.py`**  

#### Results

Results and visualizations are saved in the `Results` folder, organized by analysis type:

- **`Results/AveragePrice`**  
- **`Results/dataorg`**  
- **`Results/invertedIndex`**  
- **`Results/advanced_analysis`**  

### Code Baseline

The code is written in **Python** and uses **Apache Spark** for distributed data processing. The baseline structure includes:

- **Spark Job Dispatcher**: `main.py`
- **Individual Spark Jobs**: `AveragePrice.py`, `DataOrganization.py`, `InvertedIndex.py`, `advanced_analysis.py`
- **Helper Scripts**: Visualization scripts in `plotFunctions`
- **Tests**: Sample data file `A.csv` in the `Tests` folder

### Dependencies

The following dependencies are required:

#### Python Libraries

- **`pyspark`**: For distributed data processing.
- **`pandas`**: For local data manipulation.
- **`matplotlib`**: For generating visualizations.
- **`numpy`**: For numerical operations.

#### Apache Spark

- **Spark 3.x with Hadoop 3.x**.

#### Google Cloud SDK

- **`gcloud`**: For interacting with Google Cloud services.

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
spark-submit main.py A.csv output operation
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

### 4. Dataproc Cluster Creation

Execute the following command in the Cloud Shell to create a Dataproc cluster:

```bash
gcloud dataproc clusters create mycluster --region=europe-southwest1 \
--master-machine-type=e2-standard-4 --master-boot-disk-size=50 \
--worker-machine-type=e2-standard-4 --worker-boot-disk-size=50 \
--enable-component-gateway
```
### 5. Job Submission to the Cluster
Upload all the files from the spark folder of this repository to the Cloud Shell.

Execute the following command in the Cloud Shell to create a Dataproc cluster:

```bash
BUCKET=gs://BUCKET_NAME
gcloud dataproc jobs submit pyspark --cluster mycluster \
--region=europe-southwest1 main.py -- $BUCKET/input $BUCKET/output operation
```
### Possible Values for `operation`

The `operation` parameter can take the following values:

- **`average_price`**: Calculate the average closing price per year.  
- **`data_organization`**: Reorganize the dataset for better structure.  
- **`inverted_index`**: Create an inverted index of the maximum closing prices.  
- **`advanced_analysis`**: Perform advanced analytics on the dataset.  

Wait for the job to be completed, check its output and check the output files with the following commands:

```bash
gcloud storage ls $BUCKET/output
gcloud storage cat $BUCKET/output/* | more

```

## Performance Evaluation

## Description

This analysis compares the execution time of a Spark operation in two scenarios:

1. **Sequential Execution** with 1 executor.
2. **Parallel Execution** with 2 executors and 2 cores per executor.

The operation executed is `average_price` using the following script.

---

## Bash Commands Used

### Sequential Execution

```bash
BUCKET=gs://finalprojectcloud
spark-submit main.py $BUCKET/forbes2000/csv $BUCKET/AveragePriceTest average_price
```

### Parallel Execution

```bash
spark-submit --num-executors 2 --executor-cores 2 main.py $BUCKET/forbes2000/csv $BUCKET/AveragePriceTest average_price
```

![Sequential Execution](./Screenshots/tiempo1.png)


![Parallel Execution](./Screenshots/tiempo2.png)

## Speedup Calculation

The speedup is calculated using the formula:

$\text{Speedup} = \frac{\text{Sequential Time}}{\text{Parallel Time}}$

- **Sequential Time**: 113.80 seconds  
- **Parallel Time**: 81.86 seconds  

**Speedup Calculation**

$\text{Speedup} = \frac{113.80}{81.86} \approx 1.39$

## Summary

| **Configuration**        | **Time (s)** | **Speedup** |
|---------------------------|--------------|-------------|
| 1 executor, 1 core       | 113.80       | 1.00        |
| 2 executors, 2 cores     | 81.86        | 1.39        |
---

## Advanced Features

### Tools and Platforms explained in Class

- **Apache Spark on Google Cloud Dataproc**: Leveraging managed Spark clusters on Dataproc for seamless distributed processing, which provides scalability, ease of deployment, and integration with other GCP services.
- **Google Cloud Storage (GCS)**: Using GCS buckets to store and retrieve large datasets efficiently, ensuring high availability and durability.
- **Dataproc Component Gateway**: Facilitating access to interfaces like Spark  and Hadoop Distributed File System (HDFS) for monitoring and managing jobs.

### Advanced Functions and Techniques

- **Inverted Index Implementation**: Creating an inverted index of the maximum closing prices to enable efficient lookup and querying of stock data.
- **Advanced Analysis Module**: Performing trend analysis and advanced computations beyond basic statistical measures.
- **Regression Analysis**: Using regression techniques to identify trends and patterns in the dataset, visualized using `matplotlib`.

### Techniques to Mitigate Overheads

- **Data Partitioning**: Implementing efficient partitioning in Spark to distribute the workload evenly across the cluster and reduce data shuffling.
- **Lazy Evaluation**: Taking advantage of Spark's lazy evaluation to optimize execution plans and avoid unnecessary computations.

### Challenging Implementation Aspects

- **Cluster Resource Management**: Balancing resource allocation (vCPUs, memory) within Google Cloud quotas while maintaining performance.
- **Distributed Data Processing**: Handling large datasets and ensuring data consistency across nodes in the cluster.

---

## Conclusions

### Goals Achieved

- **End-to-End Implementation**: Successfully built an end-to-end Big Data application for stock market data analysis on Google Cloud Platform using Apache Spark.
- **Distributed Processing**: Achieved efficient processing of a large dataset (over 1 GB) by leveraging the distributed computing capabilities of Spark and Dataproc.
- **Multiple Analyses**: Implemented various analyses, including:
  - **Average Closing Price**: Calculation of average closing prices per year.
  - **Data Organization**: Reorganization of data for better structure and usability.
  - **Inverted Index**: Creation of an inverted index to facilitate efficient lookups.
  - **Advanced Analysis**: Performed trend analysis and other advanced computations.

### Improvements Suggested

- **Resource Optimization**: Fine-tuning Spark configurations and resource allocation to mitigate quota limitations and improve processing speed.
- **Error Handling**: Adding more robust error handling and logging to improve fault tolerance.
- **Scalability**: Exploring further scaling options for larger datasets beyond the current 1.2 GB limit.

### Lessons Learnt

- **Cloud Resource Management**: Managing quotas and resources in Google Cloud Platform is essential for ensuring smooth job execution.
- **Distributed Computing Challenges**: Understanding data partitioning, shuffling, and caching is key to optimizing Spark jobs.
- **Visualization**: Generating visualizations for large datasets requires careful handling of memory and file storage.

### Future Work

- **Real-Time Analysis**: Extending the application to handle real-time stock market data streams using Spark Streaming.
- **Machine Learning Integration**: Incorporating machine learning models for predictive analysis of stock prices.
- **Dashboard Creation**: Building an interactive dashboard for visualizing the analysis results dynamically.

### Interesting Insights

- **Market Trends**: Analysis revealed fluctuations and trends in stock prices over the years, which can be valuable for investors.
- **Performance Gains**: Distributed processing significantly reduced the time required to analyze large datasets compared to single-node processing.
---
## References 
- **Source Dataset**: [Kaggle - Stock Market Data](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data)
- **Apache Spark Documentation**: [Apache Spark](https://spark.apache.org/docs/latest/)
- **Google Cloud Dataproc Documentation**: [Google Cloud Dataproc](https://cloud.google.com/dataproc/docs)
- **Pandas Documentation**: [Pandas](https://pandas.pydata.org/docs/)
- **Matplotlib Documentation**: [Matplotlib](https://matplotlib.org/stable/contents.html)
- **Google Cloud SDK Reference**: [gcloud CLI](https://cloud.google.com/sdk/gcloud)

## Authors:
- **Miguel Ángel Molina de la Rosa**
- **Santiago Ochoa de Zabalegui Velasco**


