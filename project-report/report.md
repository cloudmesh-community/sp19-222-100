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

- What: predicting if a hypothetical candidant would win based off of their inputed views array
- Why: to attempt to determine the politcal voting trends of the United States
- Algorithm used: K Nearest Neighbors 

## Requirements

what needed to run:
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
    - https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjZ-4Sr1efhAhUCHqwKHa9ABSwQFjAAegQIBhAC&url=https%3A%2F%2Fwww.ontheissues.org%2F&usg=AOvVaw1Mhc94uff2nsTJNTOn6uF0
    
    - https://transition.fec.gov/pubrec/electionresults.shtml
    
    This page and other Canidates Wikipedia pages
    - https://en.wikipedia.org/wiki/Barack_Obama_2008_presidential_campaign
        

## Implementation

- python framework which contains machine learning code 
- REST api to retreive data and connect python framework with frontend website
- Docker to containerize it all 

## Conclusion

blah

## Work Breakdown

- Gathering data: both 
- Code: J = set up kNN algorithm M = set up trainging and testing data
- Report M = overall outline J = abstract BOTH = review and edits of outline 
