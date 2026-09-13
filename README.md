# Social Network Data Processing & Recommendation System

A Pure Python project that processes, transforms, validates, and works with social network data stored in JSON format.

The project was built to strengthen Python fundamentals and understand how raw structured data can be converted into useful and readable information.

## 🚀 Features

* Load and process JSON data
* Display users and their connections
* Convert user/page IDs into names
* Store processed information using file handling
* **People You May Know** recommendation
* **Pages You May Like** recommendation
* Detect and report problems in messy data

## 🧹 Data Validation & Cleaning

The project checks for common data issues such as:

* Inactive users
* Users with no friends
* Users with no liked pages
* Duplicate friends
* Duplicate liked pages
* Self-connections
* Invalid friend IDs
* Invalid page IDs

The detected issues are written to a separate text file as a readable report.

## 🧠 Concepts Used

* Python Lists
* Dictionaries
* Sets
* Loops
* Conditional Statements
* Functions
* List Comprehensions
* `next()`
* JSON Data Handling
* File Handling
* Data Validation
* Data Cleaning
* Data Transformation
* Basic Recommendation Logic

## 🛠️ Built With

**Language:** Python

**Module:** `json` (Python built-in module)

**External Libraries:** None

## 📂 Project Structure

```text
Network-Data-Processing-Recommendation/
│
├── main.py
├── data.json
├── uns_data.json
├── Information.txt
├── messy_data_info.txt
└── README.md
```

## 🔄 Project Workflow

```text
JSON Data
    ↓
Load Data
    ↓
Process & Transform Data
    ↓
Display User & Page Information
    ↓
Generate Recommendations
    ↓
Validate Messy Data
    ↓
Generate Error Report
```

## 🎯 Purpose

The main goal of this project was to strengthen Python and data-processing fundamentals before moving towards more advanced Data Science and Machine Learning concepts.

I intentionally built the project using Pure Python and built-in functionality instead of external libraries, allowing me to focus on understanding the logic behind data processing.

## 📌 Future Improvements

* Improve recommendation logic using mutual connections
* Add recommendation scoring
* Create a simple user interface
* Handle larger datasets efficiently
* Explore Machine Learning-based recommendations
