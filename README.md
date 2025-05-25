# Sleep-Disorder
This project focuses on analyzing sleep health and lifestyle data to detect potential sleep disorders using machine learning techniques. It involves data preprocessing, visualization, model building, and evaluation.

📂 Dataset
The dataset used is Sleep_health_and_lifestyle_dataset.csv containing features related to sleep patterns, lifestyle habits, and health indicators for individuals.

🧰 Tech Stack
Python
Pandas, NumPy – Data handling and manipulation
Matplotlib, Seaborn – Data visualization
Scikit-learn – Machine learning (model building, evaluation)
Pickle – Model serialization

📊 Features in the Dataset
Some key features include:
Sleep Duration
Sleep Quality
Physical Activity Level
Stress Level
BMI Category
Blood Pressure
Occupation
Gender
Age

🛠️ Project Workflow
Data Loading and Cleaning
Handled missing values
Encoded categorical variables using LabelEncoder and OneHotEncoder
Exploratory Data Analysis (EDA)
Plotted correlation heatmaps, histograms, and count plots
Visualized patterns between lifestyle factors and sleep disorders
Model Training
Split the dataset using train_test_split()
Trained a RandomForestClassifier to detect sleep disorders
Model Evaluation
Achieved model accuracy using accuracy_score
Saved the trained model using pickle for future inference

🎯 Objective
The main objective is to leverage machine learning to classify individuals with potential sleep disorders based on lifestyle and health-related factors, aiding in early intervention and awareness.
