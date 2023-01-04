
# TimeSeries Forecasting with Microservice Architecture using ReactJs and Flask

This is a personal project to implement Microservice Architecture for TimeSeries forecasting of github repo data. This application collects 
following data(commits, release, issues, branches, pull) of githbub repository using the github3.py library in the main flask server. After data
is fully retrived from the github then it is stored in csv files and json files. There are 3 distinct flask server running except for the main flask
server with different timeseries forecasting models i.e.(LSTM, Prophet, Statsmodel). The main flask server sends request to the respective 
forecasting flask servers to generate forecast based on the users request. 

Attach the Architecture Diagram here.




## Architecture

![App Architecture](![alt text](https://github.com/bvedang/React-Flask-Microservice/blob/main/appArchitecture.png?raw=true))


## Tech Stack

**Client:** React, ContextApi, Material UI

**Server:** Flask, CORS, Tensorflow, FB prophet, Statsmodel


## Installation

5 Steps to install this project

Step 1
#### Locate to **React app** directory and open that directory in the termainl. Run the following commands.
```bash
  npm install 
  npm start
```
Step 2
#### Locate to **backends** directory and open that directory in the termainl. Create virtual enviornments and run the following commands.
```bash
  activate virtual env
  pip install -r requirements 
```
Step 3
#### Locate to **fbprophet** directory and open that directory in the termainl. Create virtual enviornments and run the following commands.
```bash
  activate virtual env
  pip install -r requirements 
```
Step 4
#### Locate to **lstmapp** directory and open that directory in the termainl. Create virtual enviornments and run the following commands.
```bash
  activate virtual env
  pip install -r requirements 
```
Step 5
#### Locate to **Statsmodel** directory and open that directory in the termainl. Create virtual enviornments and run the following commands.
```bash
  activate virtual env
  pip install -r requirements 
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/bvedang/React-Flask-Microservice.git
```

Go to the project directory

```bash
  cd React-Flask-Microservice
```

Follow the installation instruction. Open 5 different Terminal/Powershell/CMD

Navigate to **lstmapp** directory in project directory

Terminal/Powershell/CMD : 1 LSTM Flask Server
```bash
  activate virtual env
  python app.py
```
Navigate to **fbprophet** directory in project directory

Terminal/Powershell/CMD : 2 Prophet Flask Server
```bash
  activate virtual env
  python app.py
```
Navigate to **Statsmodel** directory in project directory

Terminal/Powershell/CMD : 3 Statsmodel Flask Server
```bash
  activate virtual env
  python app.py
```
Navigate to **backends** directory in project directory

Terminal/Powershell/CMD : 4 Main Flask Server
```bash
  activate virtual env
  python app.py
```
Navigate to **React app** directory in project directory

Start the ReactJs server

```bash
  npm run start
```

