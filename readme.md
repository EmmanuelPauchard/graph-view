# Graph Viewer and editor

This is a sample application to test Dash. The application displays a graph and a few fields to update the graph's nodes.

## Live view

This application is visible on Azure:
https://graph-app-emmanuelp.azurewebsites.net/


## Screenshot

![Sceenshot](/img/screenshot.png)


## Dependencies
See [requirements.txt](requirements.txt).

This application is made with [Dash](https://plotly.com/dash/)

## Installation and Usage
```python
pip install -r requirements.txt
python run.py
```

## Architecture
Each web component is divided into a module:
* Inputs: handle inputs, label and update Button
* Graph_Viewer: the Cytoscape graph canvas
* App: wrapper class

![Packages](/img/packages.png)

![Classes](/img/classes.png)


## Caveats
There are still a few things to explore:

* Graph viewer is not fully responsive: the height does not get smaller when window is resized, only the width adapts
* Improve style using bootstrap
* Use a Form for the menu, finding how to deactivate default browser behaviour with the Button


