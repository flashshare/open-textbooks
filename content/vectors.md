(Ch:Applets)=

# Including applets

## SVG
{numref}`Figure %s <Fig:Vectors:AdditionPlane>` shows how you can geometrically add two arrows in a plane. The image is a SVG image rendered in the browser.

```{figure} images/Fig-Vectors-AdditionPlane.svg
:name: Fig:Vectors:AdditionPlane

Geometrical interpretation of addition in the plane.
```

## Applet
It is of course much nicer if you can interact with the image. One way of adding interactivity in the browser is through applets. 


```{applet}
:url: https://openla.ewi.tudelft.nl/applet/vectors/3Daddition
:fig: images/Fig-Vectors-3Daddition.svg

Geometrical interpretation of addition for three-dimensional vectors.
```

## Credits
Vector applet developed by Beryl van Gelderen, integration of applet in Jupyter book by Julia van der Kris and Abel de Bruijn, all as part of the [open linear algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/) developed by [PRIME](https://www.tudelft.nl/en/eemcs/the-faculty/departments/applied-mathematics/education/prime/).

## Applets in iframes
The applet can also be included via an iframe:
<iframe src="https://openla.ewi.tudelft.nl/applet/vectors/3Daddition" width="800" height="600" scrolling="auto" allowfullscreen="true"></iframe>

## HTML files as applets

As we can now integrate other HTML files (with their own style sheets and JavaScript), the possibilities are endless. I can for example include this simple website on which you can practice your arithmetic.

```{applet}
:url: https://idemalab.tudelft.nl/rekenapp/
:fig: images/Fig-Vectors-3Daddition.svg

Arithmetic practice.
```

## HTML files as iframes
Alternatively, you can include an external HTML file with an iframe:
<iframe src="https://idemalab.tudelft.nl/rekenapp/" width="800" height="400" scrolling="auto"></iframe>

The upshot of using an iframe is that you can set the following parameters:
- Width in pixels (default is 300)
- Height in pixels (default is 150)
- Loading: either *lazy* (when needed) or *eager* (immediately).
- allowfullscreen
- scrolling: whether to show scrollbars (*true*, *false*, or *auto*).