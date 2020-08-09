I present here the cartography & data analysis code I developed as part of a project led by Antoine PARENT and Pablo JENSEN, in the context of the IXXI Complexity and Cliometrics team. This project aims to quantify the process of economic polarisation having arguably followed the onset of neoliberal policies since the 1980s, and help expose the causal relations between globalisation and the development of territorial inequalities.

The code is implemented IPython notebooks for easy lisibility and reusability, and is organised in four autonomous modules corresponding to successive steps of our analysis.

## Data processing
This notebook imports the raw data, format them in a way approriate to our analysis, and export the formatted data.

## Cartography
This notebook builds dynamic maps of polarisation in France and exports them in .html format, based on the Folium library (see https://python-visualization.github.io/folium/)

## Polarisation analysis
This notebook analyses the evolution of different measures of socio-economic polarisation in order to assess which are relevant to our analysis

## Causal analysis
This notebook regresses selected measures of polarisation on theoretically relevant data so as to characterise dynamically polarisation in France, based on the statsmodels library (see https://www.statsmodels.org/stable/index.html)

A fuller explanation of the underlying research can be found in the MKDocs website for this project : https://avelguenin.github.io/france-polarisation-code/
