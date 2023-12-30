<h1 align="center">🎓Student Performance Indicator📊<br><br>End to End Production Level Application🚀<br><br></h1>

<p align="center"><img src="images/image-1.png" width="700" height="450"></p> 

---

It is a student preformance indicator project implemented in production level.

---

<h3 align="center">Project Organisation</h3>  

```
│  
├── .ebextensions
│   │
│   └── python.config                     <-- we add python configuration to deploy on aws elastic bean stalk
│  
├── .github
│   │
│   └── workflow                          
│       │
│       └── main.yml                      <-- contains yml code to create CI-CD pipeline for github actions
│  
├── artificats                            <-- Contains dataset(train, test and raw) bought in data ingestion and pickle files(preprocessor and model) created during data transformation and model training
│                                             pickle files(preprocessor and model) created during data transformation and model training
│  
├── images                                <-- contains images used in readme file
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
│   │   ├── data_transformation.py        <-- module which takes training and test dataset and then do feature engineering
│   │   │                                     then save preprocessor as pickle file inside artifact folder 
│   │   │
│   │   └── model_trainer.py              <-- module which takes preprocessed training and test data and 
│   │                                         this data is used to train different models and selects best model 
│   │                                         it also perform hyperparameter tuning 
│   │
│   ├── pipeline
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── predict_pipeline.py          <-- module takes the input data given by user as dataframe through flask web application and returns the prediction
│   │   │                                    and also takes data comes from flask application and return data as dataframe
│   │   │
│   │   └── train_pipeline.py
│   │
│   ├── __init__.py
│   │
│   ├── exception.py                     <-- module to display the custom exception
│   │
│   ├── logger.py                        <-- module to create log folder for each execution and log the events whenever required.
│   │
│   └── utils.py                         <-- module to which contians functions that are commonly used.
│   
├── static
│   │
│   └── css                              <-- contains all css files
│   
├── templates                            <-- contains all html files
│
├── .gitignore                           <-- used to ignore the unwanted file and folders
│
├── application.py                       <-- flask web application to take input from user and render output
│
├── Dockerfile                           <-- Contains code to build and run a docker image
│
├── README.md                            <-- used to display the information about the project
│
├── requirements.txt                     <-- text file which contain the dependencies/packages used project 
│                                            also to trigger the setup.py module
│
└── setup.py                             <-- module to package our project
```

---

<h3 align="center">Steps followed to create the project</h3>

1. Create a virtual envirnoment in local device.
2. Setup github repository and clone it to virtual environment.
3. Create 'requirements.txt' file and add common requirements.
4. Create 'setup.py' file and write code to package the project.
5. Create project structure i.e 'src' folder.
6. Write custom exception code in 'exception.py'.
7. Write logging code in 'logger.py'.
8. Understanding problem statement, performing eda and train model in jupyter notebook i.e in 'notebook' folder.
9. Data ingestion 'data_ingestion.py' code to read data from the data source and do train test split and store datasets in artifacts folder use utils to common project function.
10. Data transformation 'data_transformation.py' take trian and test data perform data preprocessing and creates 'preprocessor.pkl' in artifacts folder.
11. Model training and evaluation 'model_trainer.py' and select best model.
12. Add hyperparameter tuning in 'evaluate_model.py' present in utils and creates 'model.pkl' file.
13. Write Prediction pipeline code 'predict_pipeline.py' which takes data coming from user and return prediction.
14. Create a flask web app 'application.py' to take data from user and render prediction use html page and add styling for it.
15. Create an API in 'application.py' and test api using postman.
16. Create '.ebextensions' folder and add python configuration to deploy on AWS EBS(elastic beanstalk).
17. Create '.github' folder and write workflow in 'main.yml' to create a CI-CD pipeline using github actions. 

---

<h3 align="center">Best Practises Implemented</h3>

1. Moduler Programming.
2. Exception Handling.
3. Logging.
4. Comments.
5. Function Documentation (docstring).
6. Organizing Code.

---
