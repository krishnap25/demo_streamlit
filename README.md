## Introduction to Streamlit

Streamlit is a user-super-friendly tool to deploy web apps from purely python code. In our case, web apps would
 typically
 consist in visualizations of some experiments that we want people to play with to showcase our research.

####Examples
A personal example of streamlit is https://share.streamlit.io/vroulet/ckn_visualization/interactive_visualization.py
. Other examples can be found at https://streamlit.io/gallery such as https://share.streamlit.io/streamlit/demo-face-gan/.

####Outline
In this introduction, we'll run through
- basic functions of streamlit
- example of an app
- deployment struggles

A great documentation is available at https://docs.streamlit.io/ which I'm drawing most of the examples shown today. 

####Getting started
To start this demo, create the conda environment demo_st, activate it and start rightaway a visualization of your app
 by typing in your console
```
conda env create -f demo_st.yml
conda activate demo_st
streamlit run basic_functions
```
and then open the file `basic_functions.py` with the IDE of your choice.



