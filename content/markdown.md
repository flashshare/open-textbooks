(ch:markdown)=
# Content in MarkDown

## Basic text

The simplest content one can put in a book is plain text. Sections containing only text and images can be incorporated in Jupyter books through MarkDown files. MarkDown files are plain text files with a few extra's. These extra's include (demonstrated where feasible):
* (sub)section headers,
* hyperlinks,
* bulleted and numbered lists,
* **bold** and *italic* text,
* footnotes<sup>[^1]</sup>,
* block quotes,
* inline images (e.g. the MarkDown logo below).

![Image](images/markdownlogo.png)

Many modern plain text editors have a MarkDown writing mode; there are also editors with a split screen setting that allow you to see your text with MarkDown codes and the final result side by side.

The basic version of MarkDown used in Jupyter Books is specified at [CommonMark](https://commonmark.org); they offer an [overview](https://commonmark.org/help/) of the basic options.

## MyST
Sometimes plain text is all you need. But you may want more. In particular, you may want to break up long pieces of text not just with subsections, but with blocks containing tips, notes, exercises, or background information. And you may want to create internal references to allow your readers to jump quickly to a given section. Therefore, Jupyter books uses an extension of MarkDown called MyST (Markedly Structured Text).

Creating a note (or exercise, tip, or any other block) in MyST is easy.
```{note}
This is a note
```
Most 'what you see is what you get' MarkDown editors will not recognize the code block, but it will be recognized by the Jupyter book software that generates your website. The [VSCode](https://code.visualstudio.com/) editor with [MyST Markdown extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) does recognize and preview-render various MyST features, and is my editor of choice, also because it supports many other languages and has integrated version control with git.

```{tip}
To see how I made this tip, download the MarkDown file using the link at the top right of the page.
```

```{warning}
Too many special blocks may make your book unreadable.
```

```{exercise} MarkDown files
:class: dropdown
Try making a MarkDown file yourself. Note how this exercise 'folds out'. This setting can be turned on or off centrally in the configuration file of your book, or locally per block (which is what I've done here).
```

## HTML

As the pages of our book will eventually become webpages, it stands to reason that HTML directives will be recognized, and they are. I advise against their use, unless you have no alternative, as it makes converting your text to a nicely formatted printed version harder. One example I have found useful is the non-breaking space; the HTML&nbsp;command for that is `&nbsp;`, which also allows me to show how you prevent text from being parsed. I've put a non-breaking space between 'HTML' and 'command' on the previous line; they should stay together no matter what you do to the browser window. It's not hard to remember the command: the letters simply make up 'non-breaking space'.

## Equations

The extended version of MarkDown that we use for our Jupyter books allows us to incorporate $\LaTeX$. All the standard LaTeX features are available, such as inline symbols ($x$) and equations

$$
\phi(a \bm{v} + b \bm{w}) = a \phi(\bm{v}) + b \phi(\bm{w}).
$$ (oneformlinearity1)

The number of equation {eq}`oneformlinearity1` is not a MarkDown feature; if you look at this page in a MarkDown 'what you see is what you get' editor, you'll see the label I used to refer to it.

Multiple equations can be aligned nicely. Unfortunately, unlike in LaTeX, we can't give these equations separate numbers, but they can have a joint number:

$$
\begin{align*}
a &= b \\
c &= d
\end{align*}
$$ (allignedequations)

Typesetting matrix equations also works just like in LaTeX, for example

$$
\begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix} \begin{pmatrix} 1 \\ 1\end{pmatrix} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}.
$$


We can also combine LaTeX with blocks again, for instance to highlight a theorem:
```{prf:theorem} Riesz Lemma
For a vector space $V$ with an inner product $\langle\cdot \,, \cdot\rangle$ defined on it, the collection of one-forms defined by $\phi_{\bm{u}}(\cdot) = \langle\bm{u} \,, \cdot\rangle$ for $\bm{u} \in V$ gives the complete dual space $V^*$ of one-forms on $V$.
```

## Figures and tables

While figures and tables can be included directly in MarkDown, it is better to include them using blocks, as these allow us to include captions and references. Figures can be both bitmap and vector images; when available, vector images are recommended, as they are scale-free. For example, {numref}`fig:vectorimageexample` shows an SVG image.

```{figure} images/Cell_membrane_detailed_diagram_en.svg
:name: fig:vectorimageexample
Cartoon of the plasma membrane of a cell, consisting of a bilayer of lipids with a large number of embedded and associated proteins. On the intracellular side, the plasma membrane is supported by the cytoskeleton. On the extracellular side, it can face an extracellular fluid or extracellular tissue. Image created by [Mariana Ruiz](https://commons.wikimedia.org/wiki/User:LadyofHats), obtained from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cell_membrane_detailed_diagram_en.svg), public domain.
```

We can also include tables, as shown in&nbsp;{numref}`table:areasecondmoment2`.
```{table} Second moment of the area for some common cross-sectional shapes.
:name: table:areasecondmoment2
| Shape | Second moment of the area |
| :--- | :--: |
| Massive cylinder, radius&nbsp;$R$ | $\frac{\pi}{4} R^4$ |
| Hollow cylinder, radius&nbsp;$R$, thickness&nbsp;$d$|  $\pi R^3 d$ |
| Massive square, side&nbsp;$a$ | $\frac{1}{12} a^4$ |
```

## References
What is a good scientific text without references? So let's cite a paper&nbsp;{cite}`zia2009making` and a book&nbsp;{cite}`van1992stochastic`.

NB: The use of a bibliography requires the use of the `docutils` package, but [not every version is compatible with jupyter-book](https://jupyterbook.org/en/stable/content/citations.html). The error is a bug in docutils `0.18` and `0.19`. Unfortunately, the recommended version `0.17.1` does not run smoothly if you use the latest version of python (`3.12` or higher), and the newer version `0.20` doesn't work (yet) with JupyterBook. With `python 3.12`, there's a fix: use docutils `0.18.1`, and put an extra `<div>` before the bibliography (see the source file of this document), as that fixes the bug.

<div>

```{bibliography}
:style: unsrt
:filter: docname in docnames
```

[^1]: Footnotes should of course be used sparingly in every text, and especially in websites. Nonetheless, they may come in handy and it's good to know that you can use them.