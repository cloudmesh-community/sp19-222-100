# Political Bias and Voting Trends sp19-222-100 sp19-222-96

:warning: in review 

:wave: I really want a discussion on why you think political data can be predicted using AI/ML, provide some resources and discuss why it is important to bridge politics and data driven politics. 

:o: this report is duplicated and should be removed, allso it indicats smaller numbers of people

| Mercedes Olson      Jarod Saxberg 
| mercolso@iu.edu     jsaxberg@iu.edu
| Indiana University  
| hid: sp19-222-96    sp19-222-100
| github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-100/blob/master/project_report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-100/tree/master/project_code)

## Abstract

blah

## Introduction 

Sklearn's K-Nearest Neighbors algorithm was used to train a classifier which
determines if a presidential candidate would win or lose an election based on
their support or opposition to ten issues-healthcare, military, education, 
taxing the wealthy/businesses, women's rights, globalism, gun rights,
infrastructure, minority rights, and immigration. 

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
[@scikit-learn] to perform machine learning on the dataset. Sklearn allows easy
use of many machine learning algorithms. Using their K-Nearest Algorithm is as
simple as using the lines:

```python
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

pred = classifier.predict(x_test)
```

With the use of that code, everything within the scope of this project can be
completed. When users pass their own hypothetical candidate with ten arguments,
the arguments are added to an array that is then passed through the predict
function and the classifier determines if the candidate would win or lose based
on the given arguments. 

### REST API

The REST API allows simple connection between backend python code and a
frontend website/API where users can pass data in and receive it back as a json
formatted object. People can easily access the classifier through the API
without the need to build it and run it on their own. Endpoints are 
developer-designed urls that can be navigated to so users can run the
classifier and other useful features. The basepath is what prefixes all other
endpoints; it can be thought of as a top level directory and all of the
endpoints are files within the directory structure. Below, the basepath and 
endpoints are listed.

BASE PATH:
- /cloudmesh/preselec
  - Prefixes all endpoints; for example, `/cloudmesh/preselec/run/test`.

END POINTS:
- /data/download/\<file\>.csv
  - Downloads the csv data file, named as the argument provided for file.
- /data/show/graph
  - Shows the graph generated from /run/neighbors
- /run/neighbors/\<new\>
  - Runs an analysis that determines the best argument for n_neighbors.
- /run/test/\<new\>
  - Runs an analysis with testing and training sets, also exports a graph.
- /run/custom/\<neighbors\>/\<healthcare\>/\<military\>/\<education\>/\<tax wealthy\>/\<womens rights\>/\<globalism\>/\<gun rights\>/\<infrastructure\>/\<minority rights\>/\<immigration\>
  - Allows user to perform classification with custom arguments.

### Docker

containers

## Dataset

The dataset for this project had to be built from scratch as there were not any
easily accessible dataset with the features desired. On order to create the
dataset, google sheets was used to input data, and then the spreadsheet was
downloaded as a csv file. 

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
