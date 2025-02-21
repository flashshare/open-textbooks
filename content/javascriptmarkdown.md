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
# Using JavaScript in your MarkDown pages

Unfortunately browsers don't have decent support for running Python yet. However, they all support JavaScript, which can help us spice things up. Below are a few examples on how to make JavaScript work in your JupyterBook

Source: [Two ways to use JavaScript in Jupyter Notebook](https://comp.reachingfordreams.com/en/blog/17-javascript-in-jupyter-notebook-magic-node)

The 'two ways' a via Node.js and via a 'magic', which essentially converts a Python block into a JavaScript one (or one of a range of other options, including HTML and SVG). One can however also use the IPython library (much the same effect as the magic) or run an external JavaScript file.

## Basic example: Dynamically fill a block
In this example, we create a HTML element, then fill it with a list of numbers at runtime.

```{code-cell} ipython3
:tags: [remove-input]
%%html
<div id="javasciptId"></div>
```

```{code-cell} ipython3
:tags: [remove-input]
%%javascript

var selected = document.getElementById("javasciptId");
var numbers = new Array();
numbers[1]=33;
numbers[2]=44;
numbers[3]=55;
numbers[4]=66;
numbers[5]=77;
selected.innerHTML = "<b>Numbers</b>";
selected.innerHTML += "<ul>";
var num=0;
var sum=0;
var average=0;
for(var i in numbers){
    selected.innerHTML += "<li>Figure "+i+": "+numbers[i];
    num++;
    sum=sum+numbers[i];
}
selected.innerHTML += "</ul>";
var average = Math.round(sum/num);
selected.innerHTML += "Average number is "+average;
```

## Button example
```{code-cell} ipython3
:tags: [remove-input]
%%html
<div id="clickbait"><button id="clickbaitbutton">Click me!</button></div>
<div id="javasciptId3"></div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script language="javascript">
//var clickbaitbutton = document.getElementById("clickbait");
$(".clickbait button").on("click", function(event) {
    var selected = document.getElementById("javasciptId3");
    selected.innerHTML += "You clicked!";
    $(".javascriptId3").append("You clicked!")
});
</script>
```

```{code-cell} ipython3
:tags: [remove-input]
%%javascript
var clickbaitbutton = document.getElementById("clickbait");
clickbaitbutton.on("click", function(event) {
    var selected = document.getElementById("javasciptId3");
    selected.innerHTML += "You clicked!";
});
```

## Drawing example
There is a much-used visualization library for JavaScript called D3. We can invoke it for drawing. Note that we still make a HTML element to put the drawing in (which we don't need if our file is a Jupyter notebook).

```{code-cell} ipython3
:tags: [remove-input]
%%javascript
require.config({ 
     paths: { 
     d3: 'https://d3js.org/d3.v5.min'
}});
```

```{code-cell} ipython3
%%javascript
(function(element) {
    require(['d3'], function(d3) {   
        var data = [1, 2, 4, 8, 4, 2, 1]

        var svg = d3.select(element.get(0)).append('svg')
            .attr('width', 500)
            .attr('height', 200);
        svg.selectAll('circle')
            .data(data)
            .enter()
            .append('circle')
            .attr("cx", function(d, i) {return 65 * (i + 1);})
            .attr("cy", function(d, i) {return 100 + 40 * (i % 2 - 1);})
            .style("fill", "#f7e80c")
            .transition().duration(2000)
            .attr("r", function(d) {return 2*d;})
        ;
    })
})(element);
```