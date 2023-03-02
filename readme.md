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

## Unit tests

Some unit tests have been writtent in the "tests" directory. 

Why testing only the function `update_element_from_list` ?

* in a real project, more elements would be candidate for tests but in this case, time was limited
* `update_element_from_list` is a typical tricky, error-prone function that is also easy to test (pure)
* the majority of the remaining code would need validation tests (including, up to the UI)

```bash
python -m pytest tests/test_nodes.py
============================================================================================================ test session starts ============================================================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/manu/projects/sandbox/dash
plugins: dash-2.8.1
collected 7 items                                                                                                                                                                                                                           

tests/test_nodes.py .......                                                                                                                                                                                                           [100%]

============================================================================================================= 7 passed in 0.02s =============================================================================================================
```

> Note: this requires `pytest` package to be installed

## Caveats
There are still a few things to explore:

* Graph viewer is not fully responsive: the height does not get smaller when window is resized, only the width adapts
* Improve style using bootstrap
* Use a Form for the menu, finding how to deactivate default browser behaviour with the Button


