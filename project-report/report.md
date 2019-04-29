# Political Bias and Voting Trends

:warning: in review 

:wave: I really want a discussion on why you think political data can be predicted using AI/ML, provide some resources and discuss why it is important to bridge politics and data driven politics. 

:o: basepath in yaml file not in cloudmesh domain, use cloudmesh/ai/voting, check your code after mods

| Mercedes Olson      Jarod Saxberg 
| mercolso@iu.edu     jsaxberg@iu.edu
| Indiana University  
| hid: sp19-222-96    sp19-222-100
| github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-100/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-100/tree/master/project-code)

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
downloaded as a csv file. After converting the dataset to a cvs file it was then uploaded on to a website. The actual information on the website included the top 4 presidentail candidates, based off total votes and percentage of votes, from the years 1988 to 2016 with their respective parties. After selecting the candidates, the ten topics that were chosen. The topics included if they supported increase in funds for healthcare, increase in militray funding and involvement, increase in funding for education, increasing taxes on the wealthy, women's rights and supporting aborotion, supporting world trade and globalism, not putting restrictions on gun rights, supporting minority rights, and supporting immigration into the US. Each presidential candidate got either a 1 or 0 if they were for it or againt it respectively as that was the best for k nearest neighbors. An example would be if the candidate had a 0 in the 3rd element and 1 in the 5th element they would not support increase in funding for education but they support womens rights and are pro choice. One final thing to take into consideration when making this data is bias and limitations of records can affect the results.   

- Websites we got data from 
    - https://www.ontheissues.org/default.htm
    
    - https://transition.fec.gov/pubrec/electionresults.shtml
    
    This page and other Canidates Wikipedia pages
    - https://en.wikipedia.org/wiki/Barack_Obama_2008_presidential_campaign
    
## Results

- accuracy (f1 score, precision, recall, etc)
- possibly run lasso algorithm to see which features are the most/least impactful

## Discussion

- discussion on how political data can apply to AI/ML, especially in today's time (polarization makes AI/ML easier)
- importance of making the connection/application

## Conclusion

- reiterate results and accuracy, future endeavors/predictions (if any) 

## Work Breakdown

Going through candidates and creating the dataset was an even contriubtion for both contributors. The coding aspect was spilt in a way that Jarod set up the kNN algorithm and Merecedes set up training and testing data. Both working on docker file. The report was broken down in segaments with Mercedes starting and doing the over all outline and Jarod working on the abstact. Both colaborators worked evenly and together editing and finalizing the resport for every section.  

## Specification

```
swagger: "2.0"
info: 
  version: "0.0.1"
  title: "presidential support"
  description: "Attempts to determine how much support a candidate will receive based on their viewpoints"
  termsOfService: "http://swagger.io/terms/"
  license: 
    name: "Apache"
host: "localhost:8080"
basePath: "/"
schemes: 
  - "http"
consumes: 
  - "application/json"
produces: 
  - "application/json"
paths:
  /run/custom/<neighbors>/<hlt>/<mil>/<edu>/<tax>/<wmr>/<glb>/<gnr>/<inf>/<mnr>/<img>:
    get:
      tags:
        - RUN_CUSTOM
      operationId: run.run_custom
      description: "Runs an analysis based on given arguments"
      produces:
        - "application/json"
      responses:
        "200":
          description: "Run custom analysis"
          schema: {}
  /run/test/<new>:
    get:
      tags:
        - RUN_TEST
      operationId: run.run_test
      description: "Runs an analysis based on test/train data from dataset."
      produces:
        - "application/json"
      responses:
        "200":
          description: "Run test analysis"
          schema: {}
  /run/neighbors/<new>:
    get:
      tags:
        - RUN_NEIGHBORS
      operationId: run.neighbors
      description: "Determines best neighbor argument to use for KNN algorithm"
      produces:
        - "application/json"
      responses:
        "200":
          description: "Run neighbor search"
          schema: {}
  /data/download/<output>:
    get:
      tags:
        - DATA
      operationId: data.download
      description: "Downloads data from an external location"
      produces:
        - "application/json"
      responses:
        "200":
          description: "Data info"
          schema: {}
  /data/show/graph:
    get:
      tags:
        - DATA_GRAPH
      operationId: data.graph
      description: "Shows the graph generated from the neighbors endpoint"
      produces:
        - "application/png"
      responses:
        "200":
          description: "Show graph"
          schema: {}
```
