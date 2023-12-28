<h1 align="center">Student Performance Indicator <br>Production Level Application</h1>

It is a student preformance indicator project.

---

<h3 align="center">Project Organisation</h3>  

```
│  
├── notebook
│   │
│   ├── eda.ipynb                         <-- a jupyter notebook where eda is performed for the given dataset
│   │
│   ├── train.ipynb                       <-- a jupyter notebook where model training is done initially for the given dataset
│   │
│   └── data                              <-- contains the data required for project
│   
├── src
│   │
│   ├── components
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── data_ingestion.py             <-- module which reads data from different data source and do train test split
│   │   │                                     then save raw data, train data and test data inside artifact folder 
│   │   │
│   │   ├── transformation.py
│   │   │
│   │   └── model_trainer.py
│   │
│   ├── pipeline
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── predict_pipeline.py
│   │   │
│   │   └── train_pipeline.py
│   │
│   ├── __init__.py
│   │
│   ├── exception.py                     <-- module to display the custom exception
│   │
│   ├── logger.py                        <-- module to create log folder for each execution and log the events whenever required.
│   │
│   └── utils.py
│
├── .gitignore                           <-- used to ignore the unwanted file and folders
│
├── README.md                            <-- used to display the information about the project
│
├── requirements.txt                     <-- text file which contain the dependencies/packages used project 
│                                            also to trigger the setup.py module
│
└── setup.py                             <-- module to package our project
```

---
