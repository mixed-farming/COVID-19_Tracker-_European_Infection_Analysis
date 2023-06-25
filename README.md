<a name="readme-top"></a>
# COVID-19_Tracker-_European_Infection_Analysis
Tracking Daily COVID-19 Infection Count in European Countries using Hadoop MapReduce and Python
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#description">Description</a>
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
    <li><a href="#source">Source</a></li>
  </ol>
</details>

<!-- DESCRIPTION -->
## Description
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

<!-- RESULTS -->
## Results
Here are some data visuals of the output obtained:
<!-- MAPPER -->
### Mapper
https://github.com/mixed-farming/COVID-19_Tracker-_European_Infection_Analysis/assets/94393300/850fbcf8-b40e-4e49-b944-123b0c6fd0f4
<!-- REDUCER -->
### Reducer
<!-- INTERMEDIATE LINE GRAPH -->
#### Intermediate Line Graph
![reducer](https://github.com/mixed-farming/COVID-19_Tracker-_European_Infection_Analysis/assets/94393300/aa9f4ffe-389c-4083-bb0c-4d9cb545d466)
<!-- SORTED BAR GRAPH -->
#### Sorted Bar Graph
![reducer4](https://github.com/mixed-farming/COVID-19_Tracker-_European_Infection_Analysis/assets/94393300/62dbe8f2-ca16-462b-8ba5-8d39d949524c)

<!-- SOURCE -->
## Source
Covid-Data: [Click here](https://github.com/owid/covid-19-data/tree/master/public/data/cases_deaths)
Hadoop(standalone mode) Installation and Configuration: [Click here](https://mindmajix.com/installation-and-configuration-in-hadoop#standalone)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
