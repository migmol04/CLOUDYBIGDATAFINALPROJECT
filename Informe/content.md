## **Performance Evaluation**

The performance evaluation focuses on analyzing the processing speed and efficiency when handling stock market data using different configurations on cloud infrastructure.

The analysis uses a **test CSV file** with sample stock market data for generating plots and conducting calculations.

---

## **Speed-Up with Different Number of vCPUs and Nodes**

This section examines how the execution time improves when increasing the number of virtual CPUs (vCPUs) and nodes.

A regression analysis is plotted using the data from the test file to visualize the speed-up trend.

---

## **Identified Overheads**

Identifies and analyzes the overheads encountered during data processing, such as:

- **Data Shuffling Overheads**  
- **Network Latency**  
- **I/O Operations Delays**

Overheads are calculated based on execution times derived from the test file.

---

## **Optimizations Done**

This section outlines the optimizations implemented to improve performance, including:

- **Parallel Processing**  
- **Efficient Data Partitioning**  
- **Caching Strategies**  

The optimizations are tested and validated using the sample data file.

---

## **Calculations**

All calculations for speed-up, efficiency, and overheads are performed using the test CSV file.

### Example Formulas:

- **Speed-Up Calculation:**  