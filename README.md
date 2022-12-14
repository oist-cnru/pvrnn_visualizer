# pvrnn_visualizer
## Some tools to aid visualization of common tasks in PVRNN

Sometimes it may be time consuming to access and then plot specific variables that are saved when we run PVRNN. These variables are saved in various 
locations, under various formats, and we might want to plot them or analyze them in various ways. 

These scripts require us just to input the paths to the variables of interests (regardless of format), specify the units we might want to see plotted, 
and indicate some information about the primitive transitions. It can be finished in about one minute. 
This Python module can so far do two things:
- A .CSV file including all the specified units from the chosen variables is automatically saved. This kind of file has been very useful recently, 
at least for some of us. We would open it in Excel or an analogous application, with which we could have some flexibility to look at several variables 
grouped together.
- The variables of interest can be plotted and aligned to each other. Vertical lines indicate the primitive (or chunks of primitives) switches. 
See one example below, from prior generation using my own data. The black, vertical lines separate the primitive chunks:  

![image](https://user-images.githubusercontent.com/89183135/207508658-2ef06994-d793-4178-a52e-a785f739f084.png)

##Dependencies

In requirements.txt file.




