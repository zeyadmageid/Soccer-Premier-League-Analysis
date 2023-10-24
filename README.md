# ⚽🏆 Soccer-Premier-League-Analysis

<img width="568" alt="image" src="https://github.com/zeyadmageid/Soccer-Premier-League-Analysis/assets/52506246/9d16996c-0738-4489-bbb3-151700a426ac">


# Premier League Analysis

Soccer Premier League Analysis from 2014-2019 seasons.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Dashboard](#dashboard)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## About

This project entails an in-depth scrutiny of data pertaining to Premier League teams during the period spanning from 2014 to 2019. Our objective is to meticulously scrutinize the intricate interplay of performance metrics and identify the quintessential factor most tightly entwined with a team's acquisition of points. Furthermore, we embark upon a comprehensive exploration of the epochs of triumphant Premier League managers, discerning the profound influence they exerted upon their respective teams. In this endeavor, we articulate a comprehensive blueprint delineating how nascent managers ought to channel their efforts towards enhancing team performance, and offer insights into how board directors of these teams can efficaciously gauge the effectiveness of their managerial personnel.

## Features

Some features were not included in the analysis due to lack of explanation of the metrics' meanings. The features focused on in this project are:

- Game week
- Date
- Result
- Home/Away
- xG (expected goals)
- scored
- xGA (expected goals againt)
- conceded
- xpts (expected points)
- pts (points)
- npxG (non penalty expected goals)
- npxGA (non penalty expected goals against)
- ppda_coef (Passes Allowed Per Defensive Action, this metric is high for teams which play in a high press manner)
- team name
- season

## Getting Started

Link to dataset: https://www.kaggle.com/datasets/abrarhossainhimself/understat-data-for-teams-players-2014-present

Download the data set which is a zip file containing a csv file for each season which contains a file each team. After extracting the zip file and uploading it to your notebook (in my case I used google drive), everything else will be taken care of. The first section of cells combines together all the csv files for the teams across all seaons into one main spreadsheet. 

### Prerequisites

- Pandas
- Numpy
- Seaborn
- Matplotlib
- glob
- google.colab
- plotly
  
### Installation

Make sure the libraries above are installed before running the notebook in the following format "!pip install library_name. For example, installing pandas would be: !pip install pandas

## Usage

This project could be used to print season statistics, study the correlation nature between different metrics, and analyze the effect of managers on their clubs before and after their tenure. 
<img width="1364" alt="image" src="https://github.com/zeyadmageid/Soccer-Premier-League-Analysis/assets/52506246/b5c3240b-329b-4c5a-aa2f-e072657984d1">
<img width="1630" alt="image" src="https://github.com/zeyadmageid/Soccer-Premier-League-Analysis/assets/52506246/388ea8b4-1c8c-4c2d-ae46-b2156d0971bc">
<img width="783" alt="image" src="https://github.com/zeyadmageid/Soccer-Premier-League-Analysis/assets/52506246/bbd9fb6e-6efb-4e14-8e50-1b75cdb7180c">
<img width="723" alt="image" src="https://github.com/zeyadmageid/Soccer-Premier-League-Analysis/assets/52506246/cefa7cdb-741f-4c37-9b82-2cd5013237ae">


## Dashboard

https://github.com/zeyadmageid/Soccer-Premier-League-Analysis/assets/52506246/c302c3ed-bb49-4f89-92bb-8f07fa961cbe


## Contributing

Others can contribute to this project by adding more recent seasons to the dataset as this dataset only goes up to 2019.

## Acknowledgments

I would like to thank the kaggle user who made the dataset available.

## Contact

email: zhussei@uwo.ca


