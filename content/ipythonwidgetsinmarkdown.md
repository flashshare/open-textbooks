# Simple exercises

Jupyter books allow for the inclusion of [ipywidgets](https://jupyterbook.org/en/stable/interactive/interactive.html#ipywidgets), small interactive HTML elements, which can be used for making simple exercises that are generated and checked fully within the book. Here we'll illustrate with a very basic addition exercise; just type your answer in the box and the system will tell you whether you got it right, and if so, will generate a new exercise.

```{code-cell} ipython3
:tags: [remove-input]

# Import ipywidgets and the display method from ipython.
import ipywidgets as widgets
from IPython.display import display

# Array with two numbers to add. We put them in an array so that we can address (and change) the numbers from our checkanswer function.
x = np.array([np.random.randint(1,11), np.random.randint(1,11)])

# A widget element: simple textbox, we use the description to set the problem.
getanswer = widgets.Text(description = f"{x[0]} + {x[1]} = ")

# Second widget element: submit button.
returnbutton = widgets.Button(description = 'check')

# Third widget element, now a simple label, just displaying text. For now it's empty, we'll set its value when an answer has been given.
assessment = widgets.Label()

# Display both the textbox (with the problem text), the submit button, and the (empty) answer label.
display(widgets.HBox([getanswer, returnbutton]))
display(assessment)

# Function to check the given answer; the parameter passed is the event handle.
def checkanswer(b):
    # Verify that the answer is not empty and is an integer; if neither, just do nothing.
    if ((getanswer.value != '') and (getanswer.value.isnumeric())):
        answer = int(getanswer.value)
        # Actually check the answer. If correct, say so in the label (with the exercise just solved) and generate a new problem. If wrong, only set the label.
        if (x[0] + x[1] == answer):
            assessment.value = f'correct: {x[0]} + {x[1]} = {answer}'
            x[0] = np.random.randint(1,11)
            x[1] = np.random.randint(1,11)
            getanswer.description = f"{x[0]} + {x[1]} = "
            getanswer.value = ''
        else:
            assessment.value = 'wrong'

# Event listener that gets activated if the user hits return in the textbox.
getanswer.on_submit(checkanswer)

# Event listener that gets activated if the user clicks the submit button.
returnbutton.on_click(checkanswer)

```

Let's test if things are running with a very basic slider.

```{code-cell} ipython3
:tags: [remove-input]

import ipywidgets as widgets
widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
```
