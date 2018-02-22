# #AllTheFilters

To run on Mac:
`$ python3 filtergram.py`

To run on Windows:
`$ python filtergram.py`

A sample image ([brooklyn.jpg](brooklyn.jpg)) has been included for testing purposes.


## Contents

This project is split into the following parts:

* [Part 1](part1): Setting Up The Basics
    * In `filters.py`, students write the `load_img()` and `save_img()` functions.
    * In `filtergram.py`, students test out their filters library by loading and saving an image. (The saved image will look identical to the source image, since no filters have been applied yet!)
* [Part 2](part2): Building Your First Filter
    * In `filters.py`, students write the `obamicon()` filter.
    * In `filtergram.py`, students apply their Obamicon filter to an image.
* [Part 3](part3): Creating Your Own Custom Filter
    * In `filters.py`, students write their own custom filter. Actual student filters may vary, based on student interest.
    * In `filtergram.py`, students apply their new filter to an image. You can apply multiple filters to the same image!
* [Part 4](part4): Putting It All Together
    * Students use the `filters.py` created by the teacher, which consolidates all the custom filters built by the entire class. Actual student filters may vary, based on student interest.
    * In `filtergram.py`, students apply a variety of filters to an image.

Each folder contains the two following files:

* `filtergram.py`
    * This program will create a new image called "recolored.jpg" in the current directory.
* `filters.py`
    * This program contains functions defined by students, including wrappers for Pillow functions and custom image filter functions.