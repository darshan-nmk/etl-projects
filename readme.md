# IBM Data Engineering – ETL Projects  

![Python](https://img.shields.io/badge/python-3.7%2B-blue)  
![Pandas](https://img.shields.io/badge/pandas-1.x-green)  
![Status](https://img.shields.io/badge/status-active-success)  
![License](https://img.shields.io/badge/license-MIT-lightgrey)  

This repository contains my hands-on **ETL (Extract, Transform, Load) projects** completed as part of the **IBM Data Engineering Professional Certificate (Coursera)**.  

---

## 📂 Project Structure  

```
ETL_IBM/
│
├── etl_cars/  
│   ├── etl_cars.py          # Task 1 – Extract & Load car dataset  
│   ├── used_car_prices1.json  
│   ├── used_car_prices1.xml  
│   ├── used_car_prices2.json  
│   ├── used_car_prices2.xml  
│   ├── used_car_prices3.json  
│   └── used_car_prices3.xml  
│
├── etl_people/  
│   ├── etl_people.py        # Task 2 – Extract, Transform & Load people dataset  
│   ├── source1.json  
│   ├── source1.xml  
│   ├── source2.json  
│   ├── source2.xml  
│   ├── source3.json  
│   └── source3.xml  
│
└── readme.md
```

---

## 📝 Project Tasks  

### 🔹 Task 1 – Cars Dataset  
- Extract data from **CSV, JSON, XML** files.  
- Consolidate into a single DataFrame.  
- Load results into `transformed_data.csv`.  
- Log each ETL step into `log_file.txt`.  

### 🔹 Task 2 – People Dataset  
- Extract data from **CSV, JSON, XML** files.  
- Transform:
  - Convert height from **inches → meters**.  
  - Convert weight from **pounds → kilograms**.  
- Load results into `transformed_data.csv`.  
- Log each ETL step into `log_file.txt`.  

---

## ⚙️ Requirements  

- Python 3.7+  
- Libraries:  
  ```bash
  pip install pandas
  ```

(Other libraries like `xml.etree.ElementTree` and `glob` are built-in with Python.)

---

## ▶️ Running the Projects  

### Task 1 – Cars ETL
```bash
cd ETL_IBM/etl_cars
python etl_cars.py
```

### Task 2 – People ETL
```bash
cd ETL_IBM/etl_people
python etl_people.py
```

---

## 📊 Sample Logs  

Each ETL run generates `log_file.txt`, for example:

```
2025-Sep-04-14:20:05, ETL Job Started
2025-Sep-04-14:20:05, Extract phase Started
2025-Sep-04-14:20:06, Extract phase Ended
2025-Sep-04-14:20:06, Transform phase Started
2025-Sep-04-14:20:06, Transform phase Ended
2025-Sep-04-14:20:07, Load phase Started
2025-Sep-04-14:20:07, Load phase Ended
2025-Sep-04-14:20:07, ETL Job Ended
```

---

## 🎯 Learning Outcomes  
- Practice working with **different data formats (CSV, JSON, XML)**.  
- Understand **ETL pipelines**.  
- Implement **logging** for reproducibility.  
- Apply **data transformation logic** (unit conversions).  

---

## 📌 Author  
👤 **Nagamanikandan S**  
