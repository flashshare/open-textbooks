---
jupytext:
    formats: md:myst
    text_representation:
        extension: .md
        format_name: myst
kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

(ch:Jupyterquiz)=
# Jupyter quiz

We'll use a Jupyter quiz for testing our knowledge.
Source: [Jupyter quiz](https://pypi.org/project/jupyterquiz/#description). $ $

% BUG: if there is no math rendered at all before the quiz, there won't be proper math rendering in the quiz. Unfortunately a hidden tag will not resolve this issue, but the math can be placed anywhere on the page, and it can just be a space (hence the space with dollars.).

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
git_path="https://raw.githubusercontent.com/jmshea/jupyterquiz/main/examples/"
# display_quiz(git_path+"questions.json")
display_quiz("questions.json")
```

