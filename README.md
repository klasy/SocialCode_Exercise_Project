# SocialCode_Exercise_Project
SocialCode Test Project

First of all I should say that this is just a project created for the only purpose to satisfy the test task from SocialCode.

=====================================================================================
0. Introduction.

The task is:
  Create a Python / Django web application which provides a single api (/analyze-image) which accepts an image file and returns recognized text in the image. For example in the attached image 'cbsnews' would be returned as plain text (or in a json struct). Image recognition quality is not whats being tested here, just find a library or tool which can perform the analysis and output data that you can wrap in an api.

=====================================================================================

1. Dependencies:
    - pytesser as a tool to analyse the image and get a text line out of it. According to it's README it also has dependencies. Please, read carefully to install all the libraries for jpeg, png and fonts before installing the Python Imaging Library (PIL).
    So before installing pytesser:
      + install all the image related libraries mentioned in "Prerequisites." chapter of README file of pytesser project;
      + install Python Imaging Library;
      + install pytesser;
    Notes: please, make sure you read "Interdependency with HarfBuzz" of docs/INSTALL* file of freetype library.

======================================================================================

2. 
