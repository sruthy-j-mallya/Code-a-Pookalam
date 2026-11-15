# Code a Pookalam

A pookalam (the floral carpet made for Onam) drawn with Python code, using the [joy](https://github.com/fossunited/joy) graphics library.

![The finished pookalam drawn by rangoli.py](images/pookalam.png)

## Files

- **rangoli.py**: the finished design. It has nested flowers, a spiral of triangles, a ring, overlapping squares and a border of dots.
- **pookalam.py**: the step-by-step experiments (stage 1 to stage 14) that led to the final design. Each stage calls `show(...)` to draw its own shape.

## How to run

The `show()` function draws SVG output, so the easiest place to run the code is a Jupyter notebook.

1. Install Jupyter and download `joy.py` into this folder. Joy is a single file, not a pip package.

   ```bash
   pip install jupyter
   curl -LO https://github.com/fossunited/joy/raw/main/joy.py
   ```

   > Don't run `pip install joy`. That installs an unrelated package with the same name, and you'll see errors like `NameError: name 'color' is not defined`. If you already installed it, remove it with `pip uninstall joy`.

2. From this folder, start Jupyter and create a new notebook:

   ```bash
   jupyter notebook
   ```

3. In the first cell, import joy:

   ```python
   from joy import *
   ```

4. Paste the contents of `rangoli.py` into the next cell and run it. The pookalam appears below the cell.

To see the experiments, paste one stage at a time from `pookalam.py` (each section starts with a `#stage` comment) and run it the same way.
