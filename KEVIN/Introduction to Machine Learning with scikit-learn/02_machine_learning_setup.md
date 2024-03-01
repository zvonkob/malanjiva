# Setting up Python for Machine Learning: scikit-learn and Jupyter Notebook

Lesson 2 from [Introduction to Machine Learning with scikit-learn](https://courses.dataschool.io/courses/introduction-to-machine-learning-with-scikit-learn)

**Note:** Since the video recording, the official name of the "IPython Notebook" was changed to "Jupyter Notebook". However, the functionality is the same.

## Agenda

- What are the benefits and drawbacks of scikit-learn?
- How do I install scikit-learn?
- How do I use the Jupyter Notebook?
- What are some good resources for learning Python?

![scikit-learn algorithm map](images/02_sklearn_algorithms.png)

## Benefits and drawbacks of scikit-learn

### Benefits:

- **Consistent interface** to Machine Learning models
- Provides many **tuning parameters** but with **sensible defaults**
- Exceptional **documentation**
- Rich set of functionality for **companion tasks**
- **Active community** for development and support

### Potential drawbacks:

- Harder (than R) to **get started with Machine Learning**
- Less emphasis (than R) on **model interpretability**

### Further reading:

- Ben Lorica: [Six reasons why I recommend scikit-learn](https://www.oreilly.com/content/six-reasons-why-i-recommend-scikit-learn/)
- scikit-learn authors: [API design for machine learning software](https://arxiv.org/pdf/1309.0238v1.pdf)
- Data School: [Should you teach Python or R for data science?](https://www.dataschool.io/python-or-r-for-data-science/)

![scikit-learn logo](images/02_sklearn_logo.png)

## Installing scikit-learn

**Option 1:** [Install scikit-learn library](https://scikit-learn.org/stable/install.html) and dependencies (NumPy and SciPy)

**Option 2:** [Install Anaconda distribution](https://www.anaconda.com/products/individual) of Python, which includes:

- Hundreds of useful packages (including scikit-learn)
- IPython and Jupyter Notebook
- conda package manager
- Spyder IDE

![Jupyter logo](images/02_jupyter_logo.svg)

## Using the Jupyter Notebook

### Components:

- **IPython interpreter:** enhanced version of the standard Python interpreter
- **Browser-based notebook interface:** weave together code, formatted text, and plots

### Installation:

- **Option 1:** [Install the Jupyter notebook](https://jupyter.readthedocs.io/en/latest/install.html) (includes IPython)
- **Option 2:** Included with the Anaconda distribution

### Launching the Notebook:

- Type **jupyter notebook** at the command line to open the dashboard
- Don't close the command line window while the Notebook is running

### Keyboard shortcuts:

**Command mode** (gray border)

- Create new cells above (**a**) or below (**b**) the current cell
- Navigate using the **up arrow** and **down arrow**
- Convert the cell type to Markdown (**m**) or code (**y**)
- See keyboard shortcuts using **h**
- Switch to Edit mode using **Enter**

**Edit mode** (green border)

- **Ctrl+Enter** to run a cell
- Switch to Command mode using **Esc**

### IPython, Jupyter, and Markdown resources:

- [nbviewer](https://nbviewer.jupyter.org/): view notebooks online as static documents
- [IPython documentation](https://ipython.readthedocs.io/en/stable/)
- [Jupyter Notebook quickstart](https://jupyter.readthedocs.io/en/latest/content-quickstart.html)
- [GitHub's Mastering Markdown](https://guides.github.com/features/mastering-markdown/): short guide with lots of examples

## Resources for learning Python

- [Codecademy's Python course](https://www.codecademy.com/learn/learn-python): browser-based, tons of exercises
- [DataQuest](https://www.dataquest.io/): browser-based, teaches Python in the context of data science
- [Google's Python class](https://developers.google.com/edu/python/): slightly more advanced, includes videos and downloadable exercises (with solutions)
- [Python for Everybody](https://www.py4e.com/): beginner-oriented book, includes slides and videos

## Comments or Questions?

- Email: <kevin@dataschool.io>
- Website: https://www.dataschool.io
- Twitter: [@justmarkham](https://twitter.com/justmarkham)

© 2021 [Data School](https://www.dataschool.io). All rights reserved.
