# Uncovering the Best Mode of Transport: Travel Time analysis
_Adit Jindal, Ha Dang, Hassan Naveed, Sasan Zohreh_

_CSE 6242 Data and Visual Analytics, Georgia Tech_

_Spring 2023_

_Dr. Duen Horng (Polo) Chau_

## Description
This project aims to uncover the best mode of transport for a given trip. We will be using the NYC Taxi and Limousine Commission (TLC) dataset to analyze the travel time of ride-sharing vehicles vs. yellow taxis. We will be using the Citi Bike NYC to analyze bike travel time.

This project includes two parts: 
- The Front-end is a web application that allows users to input their trip information and get the travel time in minutes from a starting LocationID to an ending LocationID. The Front-end is build using HTML/CSS/JavaScripts with the D3.js libraray. 
- The Back-end is a Flask server that takes in the trip information and a dictionary that maps ending LocationIDs to travel time. The Back-end is built using Flask.

## Installation
### Conda Installation
Make sure you have Conda installed on your local machine. This guideline will use Conda to install necessary packages to run the back-end and front-end in a virtual Conda environment.

To check if you have Conda installed, run the following command in your terminal:
```
conda --version
```
If you do not have Conda installed, please follow the instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Create a Virtual Environment
> **NOTE:** Make sure you are in the directory of the project. The root directory of the project contains the `env.yml` file and `requirements.txt` file that will be used to create the virtual environment.

To create a virtual environment, run the following command in your terminal:
```
conda env create -f env.yml
```

Activate the `datavis_project` environment and install the necessary packages:
```
conda activate datavis_project

pip install -r requirements.txt
```

## Execution

### Run the Back-end
To run the back-end, navigate to the `Back-end` folder and run the following command in your terminal:
```
cd CODE/Back-end
python -m app
```

This will spin up the backend server, and you should get the following output in the terminal
```
Backend starting
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Run the Front-end
To run the front-end, navigate to the `Front-end` folder and run the following command in another terminal window:
```
cd CODE/Front-end

python -m http.server 8000
```

This will spin up the front-end server, and you should get the following output in the terminal
```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...

```

### View the Web Application
Open your browser and navigate to `http://localhost:8000/` to view the web application.
