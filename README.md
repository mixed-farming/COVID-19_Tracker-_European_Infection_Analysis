<a name="readme-top"></a>
# COVID-19_Tracker-_European_Infection_Analysis
Tracking Daily COVID-19 Infection Count in European Countries using Hadoop MapReduce and Python
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#descriptions">Description</a>
    </li>
    <li>
      <a href="#steps">Steps</a>
    </li>
    <li>
      <a href="#how-to-run">How to run</a>
    </li>
    <li>
      <a href="#results">Results</a>
      <ul>
        <li>
          <a href="#mapper">Mapper</a>
        </li>
        <li>
          <a href="#reducer">Reducer</a>
          <ul>
            <li><a href="#intermediate-line-graph">Intermediate Line Graph</a></li>
            <li><a href="#sorted-bar-graph">Sorted Bar Graph</a></li>
          </ul>
        </li>
      </ul>
     </li>
    <li>
      <a href="#libraries-used">Libraries used</a>
    </li>
    <li>
      <a href="#source">Source</a>
    </li>
  </ol>
</details>

## Descriptions
The project aims to harness the power of Hadoop MapReduce and Python to track and analyze the daily COVID-19 infection count in European countries. By utilizing the distributed processing capabilities of Hadoop, we can efficiently handle large volumes of data and extract meaningful insights.

<!-- STEPS -->
## Steps
- Collecting reliable COVID-19 data for European countries (WHO here).
- Preparing and formatting data for Hadoop MapReduce.
- Setting up Hadoop(standalone mode here) for distributed processing.
- Implementing MapReduce job in Python.
- Analyzing daily COVID-19 infections in European countries.

<!-- HOW TO RUN -->
## How to run
```
cat data_set.csv | python3 mapper.py | python3 reducer.py
```
The above command processes data from the "data_set.csv" file using a mapper script and a reducer script. It performs a series of sequential operations to transform the data and generate the final output.

<!-- RESULTS -->
## Results
Here are some data visuals of the output obtained:
<!-- MAPPER -->
### Mapper
The mapper script reads data from a CSV file, extracts relevant information, and performs grouping based on location. It calculates the difference in total COVID-19 cases between the first and last recorded dates for each location. <br>
<a href="https://github.com/mixed-farming/COVID-19_Tracker-_European_Infection_Analysis/assets/94393300/6089da46-fc5f-47a8-8f4c-0b0d59125300" target="_blank">Analyzing Mapper 3D plot</a>

<!-- REDUCER -->
### Reducer
The reducer script processes the output from the mapper script and calculates the average daily increase in cases for each location. The results are then displayed and/or saved in JSON
format.
<!-- INTERMEDIATE LINE GRAPH -->
#### Intermediate Line Graph
![reducer](https://github.com/mixed-farming/COVID-19_Tracker-_European_Infection_Analysis/assets/94393300/aa9f4ffe-389c-4083-bb0c-4d9cb545d466)
<!-- SORTED BAR GRAPH -->
#### Sorted Bar Graph
![reducer4](https://github.com/mixed-farming/COVID-19_Tracker-_European_Infection_Analysis/assets/94393300/62dbe8f2-ca16-462b-8ba5-8d39d949524c)

<!-- LIBRARIES -->
## Libraries used
- json
- datetime
- sys
- itertools
- matplotlib
- numpy
- plotly

<!-- SOURCE -->
## Source
- Covid-Data: [Click here](https://github.com/owid/covid-19-data/tree/master/public/data/cases_deaths)
- Hadoop(standalone mode) installation and configuration: [Click here](https://mindmajix.com/installation-and-configuration-in-hadoop#standalone)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
