# Visualizing real-time aircraft data with Python and Matplotlib
Analyzing and visualizating real-time aircraft data can offer insights into condition-based maintenance needs, sensor anomaly detection, and accident/incident analysis.

Following an aviation accident, for example, investigators attempt to recover the flight data recorder (FDR) that contains raw data recorded prior to the accident. If the FDR is recovered and salvageable, the data are extracted and analyzed in an attempt to determine what preceeded the accident and what actions the crew took. For example, the FDR may show a meaningful discrepancy between sensors.

## Objective
This program uses Python, specifically Pandas and Matplotlib, to plot a real-time data series such as FDR data in a user-friendly way. Each data source is plotted as a separate subplot in a vertically stacked series of plots. This is akin to figures seen in Accident Reports and allows comparisons to be made between different sensors ([example1](http://avherald.com/img/lionair_b38m_pk-lqp_jakarta_181029_knkt_data_1.jpg), [example2](https://avherald.com/img/ethiopian_b38m_et-avj_190310_7.jpg)).

## Installing and Running
This program was built with Python 3.7 using Anaconda (installer: https://www.anaconda.com/distribution/). An environment file (environment.yml) is also provided to install the necessary dependencies.
