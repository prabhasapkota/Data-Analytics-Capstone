# Data-Analytics-Capstone

# Machine Learning Insights for Sustainable Agriculture: Land Use and Farm Inputs
* Author: Prabha Sapkota
* GitHub: https://github.com/prabhasapkota/Data-Analytics-Capstone
* Overleaf: https://www.overleaf.com/project/671945ef3b8ceee7ec59c2e3

# Goals of the Research:
The goal of this research is to leverage machine learning techniques on Global
Food and Agricultural Statistics datasets to uncover insights into fertilizer application, land management and aiming to optimize agricultural productivity while promoting sustainable resource use and minimizing environmental impact.This research will use Kaggle datasets about the Global Food and Agriculture Statistics. This dataset was kindly published by the United Nation on the UNData
site 

# Phases of the Research
![alt text](<images/Phases of the Research.png>)

# Getting Started
* Begin by creating a folder to house your information.
* This folder should contain all data that was found and will eventually be where you store the notebook.
* For organizational purposes, all data has been stored in the Data folder.
* After getting the data and performing cleaning operations, create a virtual environment within your repository.
* Type python -m venv .venv in your terminal to setup a virtual environment.
* To activate the virtual environment type .venv\Scripts\activate in the terminal.
* After creating the virtual environment use pip install -r requirements.txt in the terminal.
* Once there, type jupyter lab in the terminal. If a browser does not automatically pop up, use CTRL + Click on the link provided.

# Data Collection 
Data was downloaded directly from Kaggle Datasets in csv format. You can find the original datasets here http://data.un.org/Explorer.aspx. The datasets are downloaded directly from Kaggle in csv format. Each file has a table format with rows and columns where each row represents a unique record and each column represents a different data attribute (e.g., country, year, element, value). After that, datatsets are uploaded in the VS Code and then pushed to GitHub repository.

# Data Cleaning
The three datasets i.e. Population indices, land and fertilizer had missing values in critical fields such year and value. I used the \verb|dropna()| method in pandas to remove rows with missing data. The value field is numerical and central to analysis for these three datasets, while year is essential for any temporal trends. Including rows with missing data in these fields could lead to incomplete or misleading analysis, so it’s safer to exclude them, which has been identified and removed by running Python script within VsCode. In addition to this, the year column is  set to an integer format across all datasets. Python script was ran to check for duplicate. Duplicates was found only for production datasets which was dropped. After handling the missing values, checking integer format and identifying and dropping duplicates, the  cleaned datasets has been saved separately as you can see in GitHub repository \url{https://github.com/prabhasapkota/Data-Analytics-Capstone}. 
![alt text](images/Production_indices.png)
![alt text](images/land_data.png)
![alt text](images/fertilizers_data.png)

# Data attributes and records
After the cleaning process the three datasets has following rows and columns:
* Fertilizers datasets: 102124 rows and 8 columns
* Land datasets: 104659 rows and 8 columns
* Production datasets: 311634 rows and 8 columns

# Exploratory Data Analysis
The EDA for this project was performed at Jupyter Notebook within VS Code which can be found at \url{http://localhost:8888/lab/workspaces/auto-V/tree/capstone.ipynb}. The cleaned datasets was loaded in the notebook and following steps were carried out.

## Initial Data Inspection
The initial data inspection was conducted to quickly understand the structure , contents and quality of each dataset. For this  each dataset was loaded, checked the first few rows (\verb|head()|), data types, and column names, Assessed the dataset dimensions (number of rows and columns) to get a sense of the dataset size and Identified missing values in each column and calculated missing value counts to understand potential data quality issues. 
![alt text](<images/Initial Data Inspection.png>)

## Initial Descriptive Statistics 
For second step descriptive statistics was calculated such as mean, median, minimum, maximum, and standard deviation for each dataset’s numerical columns (\verb|value|, representing production indices, land area, or fertilizer quantity).
Summarized count, unique, top, and frequency values for categorical columns (country or area, category and element) to understand their variability and most common entries. 
![alt text](<images/Production Indices Dataset.png>)
![alt text](<images/Land Use Dataset.png>)
![alt text](<images/Fertilizer Use Dataset.png>)


## Initial Data Distribution for Numerical Columns
The objective was to assess the spread and shape of numerical data to identify trends, potential outliers, and skewness. For this histograms were generated for numerical columns in each dataset to visualize data distributions. 
![alt text](<images/Graphs for production indices datasets.png>)
![alt text](<images/Graphs For Fertilizer Datasets.png>)
![alt text](<images/Graphs for Land Use Datasets.png>)

## Initial Data Distribution for Categorical Columns
Histograms were generated for numerical columns in each dataset to visualize data distributions.
![alt text](images/Graphs.png)

## Initial Data Preparation or Data Pre-processing
Data types were converted where needed, especially ensuring the year column was an integer for each dataset. Missing values were handled by imputing average values or dropping rows where critical values were missing. Duplicate rows were identified and removed to maintain data quality, particularly in the production indices dataset where duplicates were found.
![alt text](<images/Output after Data preprocessing.png>)

## Initial Storytelling and Presentation
The initial EDA across the three datasets provided critical insights into trends, patterns, and distributions. 
* Production Indices
The data indicates variability in agricultural production indices across different countries and years. Categories such as "Crops" and "Livestock" showed distinct trends over time. Top-producing countries demonstrate consistent growth, but variability exists in smaller economies.
![alt text](<images/Visualizations for Production Datasets.png>)

* Land Use
The majority of land use categories, such as "Agricultural Land" and "Forest Land," display clear regional patterns. The relationship between land use categories and production indices suggests opportunities to optimize land utilization. Temporal trends reveal shifts in land use patterns, potentially linked to policy changes or climate factors.
![alt text](<images/Visualizations for Land Use Datasets.png>)

* Fertilizer Use
Fertilizer use varies significantly by country and category. Nitrogen-based fertilizers dominate usage in most regions.
There’s a noticeable increase in fertilizer usage in emerging economies over the analyzed period, potentially driving productivity gains. Outlier analysis identified certain countries with extreme levels of fertilizer application, warranting further investigation.
![alt text](<images/Visualizations for Fertilizer Datasets.png>)

* Visual Presentation Highlights:
The EDA was supported by impactful visualizations that reveal the underlying structure of the data.
* Line Plots
Time-series visualizations of fertilizer usage and production indices showcased trends and seasonality. Adjustments to x-axis ticks ensured clarity for datasets with extensive temporal data.
* Bar Charts
Categorical distributions revealed the dominance of specific categories, such as "Crops" in production indices and "Agricultural Land" in land use.
* Box Plots
Insights into variations across countries highlighted disparities in land use efficiency, fertilizer application, and production capabilities.
* Story Telling
The findings from the EDA were contextualized within the broader narrative of sustainable agriculture: 
Patterns in land use and fertilizer application point to opportunities for policy interventions to minimize waste and improve sustainability.
Temporal trends highlight the impact of global efforts to enhance agricultural efficiency through technological advancements and resource management.

## Predictive Analysis
Predictive Analysis was carried out by performing following steps:
1. Load and Inspect the Data
![alt text](<images/Load and Inspect the Data.png>)
2. Merge Datasets
![alt text](<images/Merge Datasets.png>)
3. Feature Engineering 
![alt text](<images/Feature Engineering.png>)
4. Train-Test Split
![alt text](<images/Train-Test Split.png>)

### Goal 1: Optimize Farm Input Usage
Used a regression model to predict productivity based on fertilizer and land use.
Prior to use a regressison model merged datasets was checked for NaN or infinite values, and NaNs were filled with the median value of each column. Then values were clipped to a reasonable range to address any outliers or excessively large values that could distort the model's learning process. This clipping ensured that extreme values did not overly influence the model while retaining meaningful data followed by checking for Large Numerical values. After preprocessing, a regression model was trained to predict agricultural productivity (value-prod) using features such as fertilizer use, land use, and engineered variables like lagged productivity and interaction terms. The model's performance was evaluated using Mean Absolute Error (MAE) and R-squared metrics (R²). The Mean Absolute Error (MAE) of 102,387.80 indicates a relatively low average prediction error, suggesting that the model’s predictions are close to the actual values, especially if the productivity values are large. The R-squared (R²)value of 0.99 shows that the model explains 99 percentage of the variance in productivity, indicating an excellent fit. This high R² suggests that the model effectively captures the relationship between farm inputs (fertilizer and land use) and agricultural output.
![alt text](<images/Code and outputs for Goal 1.png>)

### Goal 2: Identify Sustainable Land Use Practices
The main idea was to classify the land use practices as 'sustainable' and 'unsustainable'. The first step taken was to identify and remove the NaN values. The model was trained using Random Forest classifier. the model initially showed a high accuracy score, which raised concerns about potential overfitting. 
![alt text](<images/Initial Code for Goal 2.png>)
![alt text](<images/Output 1.png>)
To address this and improve the model’s generalization ability, several steps were taken, Duplicate records were identified in both the training and test sets, which can introduce bias and affect model training. Removing these duplicates ensures that the model is trained on unique, relevant data. After handling the duplicates, the model was re-trained, and its performance was evaluated again. After removing duplicates and retraining the model, the accuracy reduced to a more realistic \textbf{0.52}. The model performed better at identifying unsustainable practices than sustainable ones, as seen in the classification report. The cross-validation scores showed slight fluctuations but remained consistent, suggesting the model’s performance is stable.
![alt text](<images/Re-trained Model.png>)
![alt text](<images/Output after re-training the model.png>)

### Goal 3: Forecast Sustainable Agriculture Productivity
To forecast sustainability for goal 3, the process began by preparing the dataset, ensuring the year column was converted to a datetime format for time-series modeling. The next step involved building a time-series forecasting model using historical productivity data. The model was optimized using the L-BFGS-B method, a widely used optimization technique for unconstrained problems, which minimized the loss function and fine-tuned the model parameters. After optimization, the historical and forecasted productivity values were plotted, with historical data shown in blue and forecasted data in red, to visually display the predictions over time. The forecast results were provided as predicted values for future years, offering insights into potential trends in agricultural productivity. 
![alt text](<images/Code for Goal 3.png>)
![alt text](images/Forcast.png)