:warning: in review 

:wave: I really want a discussion on why you think political data can be predicted using AI/ML, provide some resources and discuss why it is important to bridge politics and data driven politics. 

# Political Bias and Voting Trends sp19-222-100 sp19-222-96

| Mercedes Olson      Jarod Saxberg 
| mercolso@iu.edu     jsaxberg@iu.edu
| Indiana University  Indiana University
| hid: sp19-222-96    sp19-222-100
| github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-100/blob/master/project_report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-100/tree/master/project_code)

## Abstract

blah

## Introduction 

The goal of this project was to predict if a hypothetical candidate would win based off of what idea and views they supported for a specific ten issues. The issues include if the candidate supported healthcare, increase in spending on military, education, increase taxes on the wealthy, supporting women rights, globalism, gun rights, increase in infrustructure, minoity rights, and immigration. The reason behind this was to try and determine the political voting trends of the United States. The algorithm used was K Neareest Neighbor and the implimentation will later be discussed. 

:wave: avoid phrases like the goal of this project. 

## Requirements

what is needed to run:
- Docker within itself will download needed python libraries found from inside requirements.txt

## Design

The design of this project is quite simple for people to use. From a high-level
perspective, all a user needs to do is build a docker container and proceed to
the endpoints defined. To break this down, the project is split up into three 
parts: the python code containing the machine learning logic, the REST API 
connecting the python code to a website that can be navigated to, and a docker
container that houses all of the files necessary for the project. Below each
part will be discussed in more detail.

### Python

This project makes use of sklearn's K-Nearest Neighbors algorithm
[@scikit-learn] to perform machine learning on the dataset. 

### REST API

- BASE PATH:
- /cloudmesh/preselec

- END POINTS:
- /data/<file>.csv
- /run/neighbors
- /run/test
- /run/custom/<neighbors>/<healthcare>/<military>/<education>/<tax wealthy>/<womens rights>/<globalism>/<gun rights>/<infrastructure>/<minority rights>/<immigration>

### Docker

containers

## Dataset

- took csv file and uploaded to website 
- presidential candidate from the years 1988 to 2016 with party  
- top 4 year year both with percent and number of votes 
- array of 0 and 1 (best for k nearest neighbors) that say if they support the 10 topics
- for the Keywords/Label array each element correlates with the topics 
    - example is 0 for 3rd element means they do not support education 
    - example is 1 for 5th element means they do support womens right and pro choice 
- Websites we got data from 
    - https://www.ontheissues.org/default.htm
    
    - https://transition.fec.gov/pubrec/electionresults.shtml
    
    This page and other Canidates Wikipedia pages
    - https://en.wikipedia.org/wiki/Barack_Obama_2008_presidential_campaign
- note bias and limitations while creating dataset which can affect results
    
## Results

- accuracy (f1 score, precision, recall, etc)
- possibly run lasso algorithm to see which features are the most/least impactful

## Discussion

- discussion on how political data can apply to AI/ML, especially in today's time (polarization makes AI/ML easier)
- importance of making the connection/application

## Conclusion

- reiterate results and accuracy, future endeavors/predictions (if any) 

## Work Breakdown

- Gathering data: both 
- Code: J = set up kNN algorithm M = set up trainging and testing data
- Report M = overall outline J = abstract BOTH = review and edits of outline 
