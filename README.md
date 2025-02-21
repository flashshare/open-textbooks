# Open textbooks demonstration

Demonstration of an open textbook made with [Jupyter Books](https://jupyterbook.org/intro.html).

## Installation
To install jupyter books, use pip:
pip install jupyter-book
(For this demo we used version 0.15.0; you may have to replace pip by pip3 on newer installs).

## Building a Jupyter Book
To build a jupyter book, run:
jb buid *foldername*

## Structure of your LaTeX document
If you convert from a LaTeX document with the latex-to-markdown script, your LaTeX document must contain only content; essentially, that's the part you normally put between \begin{document} and \end{document}. I strongly recommend putting the content part in separate files per chapter, as having separate Markdown files per chapter is the easiest way to generate a correct table of contents in the HTML view.

## Including exercises
For the exercises, we use the package sphinx-exercise, which is not included by default, so you also need
pip install sphinx-exercise
(For this demo we used version 0.4.0)

You also need to activate the package in _config.yml,
by adding (under sphinx: extra_extensions:) sphinx_exercise

To make the exercises have lists with letters rather than numbers for the parts of the exercise, add the following custom css to the subfolder _static of your book folder:
```{code}
/* Making list items labeled by letters rather than numbers. */
.exercise.admonition ol {
  list-style-type: lower-alpha;
}
```
or manually add the same to exercise.css after your book is built.

### Exercises from a LaTeX source
Exercises have to be part of a (sub)section called Problems. Exercises are then part of a \begin{enumerate}...\end{enumerate} list, with one problem per item.

To process exercises correctly, *any* exercise that has sub-parts must be in a separate file, included via an \input{} in your LaTeX document. You can (recommended, not necessary) also include a separate file with all problems via a single \input{} statement after \section{Problems}, i.e.
```{code}
\section{Problems}
\input{path/to/your/problemsfile}
```

*TODO* solution example.