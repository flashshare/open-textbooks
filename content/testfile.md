# Tensors

## Introduction
Notes from a course on differential geometry, converted directly from LaTeX.

(sec:oneforms)=
## One-forms


(sec:oneformdef)=
### Linear maps

All tensors are (multi)linear *maps*<sup>[^1]</sup> that are linear in all their arguments, of vectors to numbers. The simplest such linear maps are linear functions of vectors to real numbers. These maps are ubiquitous enough that they have their own name: they are known as *one-forms*. In mathematical notation, a one-form&nbsp;$\phi$ is a map from a vector space&nbsp;$V$ ($V$ could for example be $\mathbb{R}^n$, or $\mathbb{C}$, or a subset of either) to the real (or possibly complex) numbers, which we'd write as:

$$
\phi : V \to \mathbb{R},
$$ (defoneform)

which means that we have defined a function that assigns a real number, denoted $\phi(\bm{v})$, to any vector $\bm{v} \in V$. By definition, our function $\phi$ is linear, so we have, for any real numbers $a$ and $b$ and any two vectors $\bm{v}, \bm{w} \in V$:

$$
\phi(a \bm{v} + b \bm{w}) = a \phi(\bm{v}) + b \phi(\bm{w}).
$$ (oneformlinearity)

In particular, we can write any vector $\bm{v}$ as a linear combination of basis vectors<sup>[^2]</sup>, $\bm{v} = v^i \bm{e}_i$. Substituting this expansion into the definition of the one-form an exploiting its linearity, we find

$$
\phi(\bm{v}) = \phi\left(v^i \bm{e}_i\right) = v^i \phi(\bm{e}_i).
$$ (oneformexpansion)

The numbers $\phi(\bm{e}_i)$ are independent of the vector chosen, they only change if you choose a new basis for $V$. To characterize the one-form, all we need to know are these numbers. In analogy with the components of the vectors, we call them the components of the one-form, given by

$$
\phi_i = \phi(\bm{e}_i),
$$ (oneformcomponents)

so we can also write the map $\phi(\bm{v})$ as

$$
\phi(\bm{v}) = \phi_i v^i.
$$ (oneformexpansion2)


### A basis for one-forms
Equation&nbsp;{eq}`oneformcomponents` shows that a one-form acting on an $n$-dimensional vector space $V$ with basis&nbsp;$\{\bm{e}_i\}$ can be characterized by specifying $n$ numbers&nbsp;$\phi_i$, just like the components of a vector $\bm{v}$ in that vector space can be characterized by specifying the $n$ numbers&nbsp;$v^i$. Both the $\phi_i$ and the $v^i$ depend on the choice of basis&nbsp;$\{\bm{e}_i\}$ for $V$. The similarity between the vectors and one-forms suggests that we might also construct a basis for the one-forms, which is indeed the case: we simply take the $n$ one-forms that map a vector $\bm{v}$ onto each of its components. Perhaps somewhat confusingly, these basis one-forms are denoted $\mathrm{d}x^i$:

$$
\mathrm{d}x^i(\bm{v}) = v^i.
$$ (defbasisoneform)

Note that in particular

$$
\mathrm{d}x^i(\bm{e}_j) = \delta_j^i.
$$ (basisoneformbasisvector)

By multiplying both sides of&nbsp;{eq}`defbasisoneform` with $\phi_i$ and summing, we see that these functions are indeed a basis for the one-forms, as we have:

$$
\phi(\bm{v}) = \phi_i v^i = \phi_i \mathrm{d}x^i(\bm{v}).
$$

Suppose now that we have two one-forms, $\phi$ and $\psi$. Given their expansions in terms of the basis, it is almost trivial to show that any linear combination $a \phi + b \psi$ (with $a, b \in \mathbb{R}$) also defines a one-form:

$$
a \phi(\bm{v}) + b \psi(\bm{v}) = a \phi_i v^i + b \psi_i v^i = (a \phi_i + b \psi_i) v^i = \chi_i v^i = \chi(\bm{v}),
$$ (oneformlinearcombinations)

where the one-form $\chi$ is characterized by the numbers $\chi_i = a \phi_i + b \psi_i$.

What we have shown above, is that the *collection* of all one-forms on an $n$-dimensional vector space $V$ with basis $\{\bm{e}_i\}$ also forms a vector space. This vector space of one-forms is known as the *dual* vector space $V^*$ with basis $\{\mathrm{d}x^i\}$.

### A one-on-one correspondence between one-forms and vectors
If the vector space $V$ has an inner product $\langle\cdot \,, \cdot\rangle$ defined on it, we can use that inner product to construct a collection of one-forms. For any vector $\bm{u} \in V$ we can define a unique one-form $\phi_{\bm{u}}$ by

$$
\phi_{\bm{u}}(\bm{v}) = \langle\bm{u} \,, \bm{v}\rangle.
$$ (innerproductoneform)

Equation&nbsp;{eq}`innerproductoneform` defines a one-form because the inner product is linear in both its arguments, and thus in particular in $\bm{v}$; therefore $\phi_{\bm{u}}(\bm{v})$ is also linear in $\bm{v}$. If the basis vectors are orthogonal, we get the basis one-forms by picking the basis vectors for $\bm{u}$:

$$
\phi_{\bm{e}_i}(\bm{v}) = \langle\bm{e}_i \,, \bm{v}\rangle = v^i = \mathrm{d}x^i(\bm{v}).
$$ (innerproductoneformbasis)

Note that equation&nbsp;{eq}`innerproductoneformbasis` does not hold generally. For a basis that is not orthogonal, we would pick up extra components of $\bm{v}$ in the second equality. On the other hand, if the basis is orthonormal (i.e., all basis vectors are orthogonal and they are all of unit length), we find a one-to-one correspondence between the components of $\phi$ and those of $\bm{u}$:

$$
\phi_{\bm{u}}(\bm{v}) = \langle\bm{u} \,, \bm{v}\rangle = u^i v^j \langle\bm{e}_i \,, \bm{e}_j\rangle = u^i v^j \delta_{ij} = u_i v^j = \phi_i v^j,
$$ (orthonormalinnerproduct)

and because the last equality must hold for any choice of $\bm{v}$, we get $u_i = \phi_i$. We'll return to equation&nbsp;{eq}`orthonormalinnerproduct` later. For now, we note that in Cartesian coordinates, the condition of orthonormal basis vectors is met. Therefore, in these coordinates, we can not only construct a one-form from every vector, but in fact *identify* every one-form with a vector. You've seen this (unwittingly, no doubt) many times before, when you wrote the 'standard' inner product (also known as the dot product) as the product of a row and a column vector. In two dimensions, that would give

$$
\langle\bm{u} \,, \bm{v}\rangle = \begin{pmatrix}u_1\,, u_2\end{pmatrix} \begin{pmatrix}v^1 \\ v^2\end{pmatrix} = u_1 v^1 + u_2 v^2 = u_i v^i.
$$

Note that we used lower indices for the components of $\bm{u}$ here, to indicate that they are components of the row-vector representation (or, equivalently, the one-form representation) of the vector. In Cartesian coordinates, these components are identical to the column-vector ones, so you may wonder what we've gained by this whole discussion, as you already knew about inner products and row vectors. The answer is that Cartesian coordinates are special: in general, the 'row-vector' and 'column-vector' components are not equal. We'll see many examples of such cases soon.

Because of the correspondence between one-forms and vectors, one-forms are also known as co-vectors. The components $\phi_i$ (or $u_i$) of the one-forms are known as the *covariant* components, and their basis $\{\mathrm{d}x^i\}$ as the covariant basis. The components $v^i$ of the 'ordinary' vector $\bm{v}$ are known as the *contravariant components* (these are the ones you're used to think of as the components of a vector) and the corresponding basis $\{\bm{e}_i\}$ is known as the contravariant basis<sup>[^3]</sup>.

We've seen that for every vector we can define a corresponding one-form. It's easy to see that for a vector space with an orthogonal basis, this construction gives us all one-forms possible on that space: equation&nbsp;{eq}`innerproductoneformbasis` then gives us the basis one-forms, and all others are simply linear combinations. That result also holds for a general basis. The easiest way to see that is that you can always construct an orthogonal basis from any basis through the Gram-Schmidt process. From that orthogonal basis, you can find the basis one-forms, and re-construct all other one-forms. This one-to-one correspondence between a vector space with an inner product and the one-forms acting on it is known as the Riesz Lemma:
```{prf:theorem} Riesz Lemma
For a vector space $V$ with an inner product $\langle\cdot \,, \cdot\rangle$ defined on it, the collection of one-forms defined by $\phi_{\bm{u}}(\cdot) = \langle\bm{u} \,, \cdot\rangle$ for $\bm{u} \in V$ gives the complete dual space $V^*$ of one-forms on $V$.
```


(sec:oneformgeometry)=
### A geometric interpretation of one-forms

We have a simple geometric interpretation of vectors: objects with both a magnitude and a direction, that we usually draw as arrows. Given the close relation between vectors and one-forms, we may expect there to be a similar geometric interpretation of one-forms, and indeed one exists. It is somewhat elusive though (at least it was to me initially), because, if you're trained in thinking in Cartesian coordinate systems, they are hard to distinguish from vectors. The distinction is significant though, and to see it, we should move away from the comfort of Cartesian coordinates. To develop our intuition, we're going to work in two dimensions only (so we can easily draw pictures). We'll label the Cartesian coordinates $x$ and $y$ (or $x^1$ and $x^2$, for summing), with basis vectors $\bm{\hat{f}}_1$ and $\bm{\hat{f}}_2$ (to distinguish from the more general $\{\bm{e}_i\}$). We can then define a different set of coordinates $u$ and $v$ (or $\{u^i\}$ for summing) by expressing them as (not necessarily linear) functions of the Cartesian coordinates; we can also invert these functions to get the Cartesians back in terms of the $\{u^i\}$:

```{math}
:label: coordinatetransform
\begin{alignat*}{2}
u^1 &= u = u(x,y) & \qquad\qquad & x^1 = x = x(u,v) \\
u^2 &= v = v(x,y) & \qquad\qquad & x^2 = y = y(u,v)
\end{alignat*}
```

We can now define a new set of basis vectors $\{\bm{e}_i\}$ pointing in the direction in which $u$ and $v$ increase:

$$
\bm{e}_1 = \bm{e}_u = \begin{pmatrix} \frac{\partial x}{\partial u} \\ \frac{\partial y}{\partial u}\end{pmatrix}, \qquad
\bm{e}_2 = \bm{e}_v = \begin{pmatrix} \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial v}\end{pmatrix}.
$$ (coordinatetransformtangentbasis)

You have likely seen this construction before for the basis vectors in polar coordinates. Let's calculate them to illustrate: we have $r = \sqrt{x^2 + y^2}$ and $\theta = \arctan(y/x)$, or inversely $x = r \cos \theta$ and $y = r \sin\theta$, which gives:

$$
\bm{e}_r = \begin{pmatrix} \cos\theta \\ \sin \theta \end{pmatrix}, \qquad 
\bm{e}_\theta = \begin{pmatrix} -r\sin\theta \\ r\cos \theta \end{pmatrix}.
$$ (polarcoordstangentbasis)

Note that these basis vectors are orthogonal but not orthonormal - to get the 'standard' polar basis vectors we'd have to normalize $\bm{e}_\theta$. As the polar coordinates still define an orthogonal basis, let's also illustrate with an example where that is not the case. If we take $u = x$ and $v = x+y$, then $x = u$ and $y = v-u$, and we get

$$
\bm{e}_u = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad 
\bm{e}_v = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.
$$ (nonorthogonalcoordstangentbasis)

Choosing the direction in which one of the variables increases is a fine way to find a basis. Geometrically, the resulting basis vectors are the tangent vectors to the lines on which all but one of the variables is constant. There is however another, equally valid way: pick the directions normal to lines (or surfaces, or higher-dimensional meta-surfaces<sup>[^4]</sup>) on which one of the coordinates is constant (see {numref}`fig:coordinatetransformbases`). To find these directions, we take the gradient of each of the transformations:

$$
\bm{e}^1 = \bm{e}^u = \bm{\nabla}u = \begin{pmatrix} \frac{\partial u}{\partial x} \\ \frac{\partial u}{\partial y}\end{pmatrix}, \qquad
\bm{e}^2 = \bm{e}^v = \bm{\nabla}v = \begin{pmatrix} \frac{\partial v}{\partial x} \\ \frac{\partial v}{\partial y}\end{pmatrix}.
$$ (coordinatetransformationnormalbasis)

We can easily calculate what these basis vectors are for our polar coordinates

$$
\bm{e}^r = \begin{pmatrix} \frac{x}{r} \\ \frac{y}{r} \end{pmatrix} = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}, \qquad
\bm{e}^{\theta} = \begin{pmatrix} -\frac{y}{r^2} \\ \frac{x}{r^2} \end{pmatrix} = \begin{pmatrix} -\frac{\sin\theta}{r} \\ \frac{\cos \theta}{r} \end{pmatrix}.
$$ (polarcoordsnormalbasis)

We thus find that while the new basis vectors point in the same direction as the old ones, they don't have the same length. For our non-orthogonal example, the directionality is also quite different:

$$
\bm{e}^u = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad 
\bm{e}^v = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
$$ (nonorthogonalcoordsnormalbasis)

Equations&nbsp;{eq}`coordinatetransformtangentbasis` and {eq}`coordinatetransformationnormalbasis` give us the components of the two bases represented in Cartesian coordinates. We can therefore calculate their (Cartesian) inner product, which, using the chain rule, shows us that they are orthogonal:

$$
\langle\bm{e}^i \,, \bm{e}_j\rangle = \bm{e}^i \cdot \bm{e}_j = \left(\frac{\partial u^i}{\partial x^k}\right) \left(\frac{\partial x^k}{\partial u^j}\right) = \frac{\partial u^i}{\partial u^j} = \delta_j^i.
$$ (basisorthogonality)

We can write any arbitrary vector&nbsp;$\bm{v}$ in&nbsp;$\mathbb{R}^2$ as a linear combination of the basis vectors of either basis:

$$
\bm{v} = v^i \bm{e}_i = v_i \bm{e}^i,
$$ (vectorexpansion)

and by combining equations&nbsp;{eq}`basisorthogonality` and&nbsp;{eq}`vectorexpansion` we find

```{math}
\begin{align*}
\bm{v} \cdot \bm{e}^i &= v^j \bm{e}_j \cdot \bm{e}^i = v^j \delta_j^i = v^i, \\
\bm{v} \cdot \bm{e}_i &= v_j \bm{e}^j \cdot \bm{e}_i = v_j \delta_i^j = v_i,
\end{align*}
```
so we get the components of the vector in either basis by projecting on the basis vector, as usual.

```{figure} images/coordinatesystems.svg
:name: fig:coordinatetransformbases
Contravariant and covariant bases for (a) polar coordinates and (b) a non-orthogonal coordinate system in&nbsp;$\mathbb{R}^2$. The contravariant basis vectors (red and blue) point in the direction in which one of the variables increases and are found by taking derivatives of the coordinate transformations (equation&nbsp;{eq}`coordinatetransformtangentbasis`). The covariant basis vectors (green and orange) point in the direction normal to the (meta)surface on which one of the coordinates is constant, and are found by calculating the gradient of the inverse coordinate transformations. Note that in polar coordinates the basis vectors are orthogonal and the two basis vectors corresponding to the radial direction coincide (red and orange), but that in the non-orthogonal example in (b) the basis vectors are neither orthogonal nor identical in the two bases. However, the vectors from the two sets are still mutually orthogonal, respecting $\langle\bm{e}^i \,, \bm{e}_j\rangle = \delta_j^i$.
```


You will no doubt have noticed that we've used the same notation for the 'tangent-based' basis vectors as we did for the contravariant (or 'regular') basis in the previous sections. Likewise, we've used the same notation for the 'normal-based' basis vectors as those of the covariant or one-form basis introduced before. We've now also seen that they behave in the same manner. Although the basis vectors may not be orthogonal within the basis sets, the two sets are orthogonal to each other (cf. equations&nbsp;{eq}`basisoneformbasisvector` and&nbsp;{eq}`basisorthogonality`). These similarities suggest that there is an identification to be made, and indeed, the tangent-based basis vectors are a contravariant basis, and the normal-based ones its covariant dual. To prove that, we'll need a two-tensor, the metric, which will give us the inner product in the vector spaces with the contravariant and covariant bases. Before we go there however, we'll identify the geometric interpretation of the one-form. Consider an arbitrary (not necessarily linear) function $f$ on $\mathbb{R}^2$, defined in terms of the Cartesian coordinates, so we have $f = f(x,y)$. We can construct a vector-like quantity, the gradient of $f$, out of the derivatives of $f$, which will turn out to be a co-vector, or one-form, rather than an ordinary vector:

```{math}
:label: gradientoneform
\begin{align*}
\bm{\nabla}f &= \frac{\partial f}{\partial x} \bm{\hat{x}} + \frac{\partial f}{\partial y} \bm{\hat{y}} = \frac{\partial f}{\partial u} \left( \frac{\partial u}{\partial x} \bm{\hat{x}} + \frac{\partial u}{\partial y} \bm{\hat{y}} \right) + \frac{\partial f}{\partial v} \left( \frac{\partial v}{\partial x} \bm{\hat{x}} + \frac{\partial v}{\partial y} \bm{\hat{y}} \right)  \\
&= \frac{\partial f}{\partial u} \bm{\nabla}u + \frac{\partial f}{\partial v} \bm{\nabla}v = \frac{\partial f}{\partial u} \bm{e}^u + \frac{\partial f}{\partial v} \bm{e}^v \\
&= \frac{\partial f}{\partial u^i} \bm{e}^i \equiv f_{,i} \bm{e}^i
\end{align*}
```
The components of the gradient of $f$ are thus the components of a co-vector, which we've tentatively identified with a one-form already. In Cartesian coordinates, these components are identical to the components of a regular vector, which is why you're probably used to thinking about gradients as vectors: the direction of steepest increase of a function. That direction however by construction is perpendicular to a meta-surface on which the function is constant - and thus perpendicular to the tangent lines to that meta-surface, which point in the direction that the function will move when a single variable changes. The geometrical interpretation of the one-form is thus similar to the one you're used to from gradients: it corresponds to a direction perpendicular to a meta-surface on which a function is constant, and its magnitude tells you how close together those meta-surfaces are, see {numref}`fig:gradients`.


```{figure} images/gradients2.svg
:name: fig:gradients
Correspondence between gradients and one-forms. The plot shows the contour lines of a function of two variables, i.e., the lines for which the function is constant. The gradient of this function defines a co-vector or one-form on $\mathbb{R}^2$, with a magnitude that corresponds to the local density of contour lines, and a direction perpendicular to those contour lines.
```


## The metric tensor
Before we can complete the proof of the assertion that, for a vector space with an inner product, the one-forms of {numref}`sec:oneformdef` and the co-vectors of {numref}`sec:oneformgeometry` are one and the same, we need a way to calculate inner products in an arbitrary coordinate system. To do so, we need a new construct, the *metric tensor*. The metric tensor is an example of a two-tensor, which means that it is a map of two vectors onto a real number, and linear in each of its components. We define the metric tensor as the map of two vectors $\bm{v}, \bm{w} \in V$ on their inner product:

$$
g(\bm{v}, \bm{w}) = \langle\bm{v} \,, \bm{w}\rangle.
$$ (defmetrictensor)

Note that the metric tensor itself does not depend on the choice of coordinates: the inner product of two vectors is always the same, independent of the basis we work in. Geometrically, the inner product of two vectors is the length of the projection of one on the other - a number that should not depend on whether you choose to work in, say, Cartesian or polar coordinates.

The *representation* of the metric depends strongly on the basis however, just like the representation of a vector and a one-form depend on the basis chosen. Because the inner product (and all two-tensors) are linear in each component, given a basis, we can find a unique set of numbers that characterizes the tensor, using the same trick we used to find the components of a one-form. We have:

$$
g(\bm{v}, \bm{w}) = \langle\bm{v} \,, \bm{w}\rangle = v^i w^j \langle\bm{e}_i \,, \bm{e}_j\rangle \equiv v^i w^j g_{ij},
$$ (metriccomponents)

so the components of the metric are simply given by the inner products of the basis vectors: $g_{ij} = \langle\bm{e}_i \,, \bm{e}_j\rangle$.

In equation&nbsp;{eq}`metriccomponents`, we used the 'canonical' contravariant basis to express our vectors. Of course, following the geometric interpretation of {numref}`sec:oneformgeometry`, we could also have expressed our vectors in the covariant basis, which would give us a different set of numbers for the representation of the metric:

$$
g(\bm{v}, \bm{w}) = \langle\bm{v} \,, \bm{w}\rangle = v_i w_j \langle\bm{e}^i \,, \bm{e}^j\rangle \equiv v_i w_j g^{ij},
$$ (covariantmetriccomponents)

or $g^{ij} = \langle\bm{e}^i \,, \bm{e}^j\rangle$. We call $g_{ij}$ the covariant representation of the metric, and $g^{ij}$ its contravariant one.

There's no reason to stop here - what if we take the contravariant representation for one vector, and the covariant one for the other? In the case of the metric, this gives us a very useful relation:

```{math}
\begin{align*}
g(\bm{v}, \bm{w}) = \langle\bm{v} \,, \bm{w}\rangle &= v_i w^j \langle\bm{e}^i \,, \bm{e}_j\rangle = v_i w^j \delta_j^i = v_i w^i,\\
&= v^i w_j \langle\bm{e}_i \,, \bm{e}^j\rangle = v^i w_j \delta_i^j = v^i w_i,
\end{align*}
```

so we get

$$
v^i w^j g_{ij} = v^i w_i = v_i w^i = v_i w_j g^{ij}.
$$ (metricrelations)

Now equation&nbsp;{eq}`metricrelations` holds for arbitrary vectors $\bm{v}$ and $\bm{w}$. From the first equality we can therefore read off that we have

$$
w_i = g_{ij} w^j,
$$ (loweringindex)

and by the third equality we have

$$
w^i = g^{ij} w_j.
$$ (raisingindex)

The components of the metric tensor can thus be used to relate the covariant and contravariant components of a vector to each other directly. The operations described by equations&nbsp;{eq}`loweringindex` and&nbsp;{eq}`raisingindex` are colloquially referred to as to 'lowering' and 'raising' the index of the components, and they are one reason why the metric is extremely useful. In Cartesian (or any orthonormal) coordinates, the components of the metric are given by the Kronecker delta, $g_{ij} = \delta_{ij}$, and by equations&nbsp;{eq}`loweringindex` and&nbsp;{eq}`raisingindex`, the covariant and contravariant components of vectors in such coordinates are thus identical.

By combining equations&nbsp;{eq}`loweringindex` and&nbsp;{eq}`raisingindex`, we also find a direct relation between the two representations of the metric:

$$
w_i = g_{ij} w^j = g_{ij} g^{jk} w_k \quad \Rightarrow \quad g_{ij} g^{jk} = \delta_i^k,
$$ (metricinverse)

so the two representations of the metric are each other's inverse.

Incidentally, equation&nbsp;{eq}`metricrelations` also completes the proof that the one-forms and co-vectors from {numref}`sec:oneforms` are one and the same. We already found that for every one-form, we can find a unique vector&nbsp;$\bm{u}$ such that the one-form is identical to taking the inner product with that vector, i.e., $\phi_{\bm{u}}(\bm{v}) = \langle\bm{u} \,, \bm{v}\rangle$. Equation&nbsp;{eq}`metricrelations` shows that the components, $\phi_i$ of the one-form are then identical to the covariant components of $\bm{u}$.

Finally, the metric gets its name from the fact that we can use it to calculate lengths. The length of a vector does not depend on the chosen coordinate system, but within such a system, it can be calculated by taking the inner product of the representation of the vector with itself. Because the metric is the representation of the two-tensor that corresponds to the inner product, it can be used to measure the length of a vector, and we have:

$$
\|\bm{v}\|^2 = \langle\bm{v} \,, \bm{v}\rangle = v^i v^j g_{ij} = v_i v_j g^{ij}.
$$


(sec:twotensors)=
## General two-tensors

A *two-tensor* is a map of two vectors onto a real number, that is linear in each of its arguments. It is a direct generalization of the one-form defined in equation&nbsp;{eq}`defoneform`:

$$
\chi: V \times V \to \mathbb{R},
$$ (deftwotensor)

so we assign a real number $\chi(\bm{v}, \bm{w})$ to any *pair* of vectors $\bm{v}, \bm{w} \in V$. The metric tensor $g(\bm{v}, \bm{w})$ is an example of a two-tensor.

We can find a coordinate representation of a general two-tensor $\chi$ in complete analogy as that of a one-form (see equation&nbsp;{eq}`oneformcomponents`) by considering its action on the basis vectors of $V$. By bilinearity of $\chi$ we have

$$
\chi(\bm{v}, \bm{w}) = v^i w^j \chi(\bm{e}_i, \bm{e}_j) \equiv v^i w^j \chi_{ij},
$$ (twotensorcovariantrepresentation)

which defines the covariant representation (or covariant components) of $\chi$.

### Tensor product and two-tensor basis
One way to construct a two-tensor is as the product of two one-forms. If $\phi$ and $\psi$ are one-forms, then we can define a two-tensor $\chi = \phi \otimes \psi$ by simply taking the product of the values of the two one-forms:

$$
\chi(\bm{v}, \bm{w}) = (\phi \otimes \psi)(\bm{v}, \bm{w}) = \phi(\bm{v}) \cdot \psi(\bm{w}).
$$ (deftensorproduct)

In other words, we simply have the first one-form act on the first argument, and the second one-form on the second argument, and multiply the result. The tensor product of $\phi$ and $\psi$ is linear in each of the arguments because $\phi$ and $\psi$ are linear themselves.

If $\chi$ is the tensor product of two one-forms, its components become the products of the components of the two one-forms:

$$
\chi(\bm{v}, \bm{w}) = v^i w^j \chi_{ij} = \phi(\bm{v}) \cdot \psi(\bm{w}) = v^i \phi(\bm{e}_i) \cdot w^j \psi(\bm{e}_j) = v^i w^j \phi_i \psi_j,
$$ (tensorproductcomponents)

and because&nbsp;{eq}`tensorproductcomponents` holds for any pair of vectors ($\bm{v}, \bm{w}$), we have $\chi_{ij} = \phi_i \psi_j$.

We can construct a basis for the two-tensors from the basis of the one-forms, by taking tensor products of the one-form basis functions. We have:

$$
(\mathrm{d}x^i \otimes \mathrm{d}x^j)(\bm{v}, \bm{w}) = \mathrm{d}x^i(\bm{v}) \cdot \mathrm{d}x^j(\bm{w}) = v^i w^j,
$$ (twotensorbasis)

and after multiplying both sides of equation&nbsp;{eq}`twotensorbasis` with $\chi_{ij}$ we find that

$$
\chi(\bm{v}, \bm{w}) = v^i w^j \chi_{ij} = \chi_{ij} (\mathrm{d}x^i \otimes \mathrm{d}x^j)(\bm{v}, \bm{w}),
$$ (twotensorbasisexpansion)

for an arbitrary two-tensor&nbsp;$\chi$, so the tensor products $(\mathrm{d}x^i \otimes \mathrm{d}x^j)$ of the one-form bases form a basis for the two-tensors.

### Symmetry and wedge product
The tensor product defined in equation&nbsp;{eq}`deftensorproduct` is not symmetric if $\phi$ and $\psi$ are different one-forms. A general two-tensor is not symmetric if its action on two vectors $\bm{v}$ and $\bm{w}$ depends on their order. We can however always define a symmetric and an antisymmetric part of any two-tensor, in an almost tautological way:

```{math}
\begin{align*}
\chi(\bm{v}, \bm{w}) &= \chi^\mathrm{s}(\bm{v}, \bm{w}) + \chi^\mathrm{a}(\bm{v}, \bm{w}),\\
\chi^\mathrm{s}(\bm{v}, \bm{w}) &= \frac12 \left[ \chi(\bm{v}, \bm{w}) + \chi(\bm{w}, \bm{v})\right], \\
\chi^\mathrm{a}(\bm{v}, \bm{w}) &= \frac12 \left[ \chi(\bm{v}, \bm{w}) - \chi(\bm{w}, \bm{v})\right].
\end{align*}
```

The component representations of the symmetric and antisymmetric part of $\chi$ follow in the same way from the representation of $\chi$. They occur so often that they have their own notation: $(ij)$ for the symmetrized part, and $[ij]$ for the antisymmetrized part:

```{math}
\begin{align*}
\chi_{ij} &= \chi_{(ij)} + \chi_{[ij]}, \\
\chi_{(ij)} &= \frac12 \left( \chi_{ij} + \chi_{ji} \right), \\
\chi_{[ij]} &= \frac12 \left( \chi_{ij} - \chi_{ji} \right).
\end{align*}
```


(Anti)symmetric products of one-forms can also be defined, again in the fully analog way. The symmetric product is indicated by&nbsp;$\odot$ and given by

$$
(\phi \odot \psi)(\bm{v}, \bm{w}) = \frac12 \left[ \phi(\bm{v}) \cdot \psi(\bm{w}) + \phi(\bm{w}) \cdot \psi(\bm{v}) \right].
$$ (defsymmetrictensorproduct)

The symmetric product is rarely used, but you may encounter its antisymmetric counterpart frequently. It is known as the *wedge product*, denoted by $\wedge$, and defined as

$$
(\phi \wedge \psi)(\bm{v}, \bm{w}) = \phi(\bm{v}) \cdot \psi(\bm{w}) - \phi(\bm{w}) \cdot \psi(\bm{v}).
$$ (defwedgeproduct)

Note the absence of the factor&nbsp;$\frac12$ in the definition of the wedge product. Tensors that are fully antisymmetric in any two indices are known as *forms*; the wedge product between two one-forms defines a two-form. Unsurprisingly, you can define a basis for the two-forms by taking wedge products of the one-form bases, in complete analogy with the basis of the two-tensors. We denote the basis elements as $\mathrm{d}x^i \wedge \mathrm{d}x^j$, with the wedge product as defined in equation&nbsp;{eq}`defwedgeproduct`. Note in particular that the wedge product of a one-form with itself is zero; if $V$ is an $n$-dimensional space (say $\mathbb{R}^n$), there are therefore not $n^2$ but only $\frac12 n(n-1)$ nonzero basis two-forms. In particular, in one dimension, there are no basis two-forms, in two dimensions there is only one, and in three dimensions there are three.

The presence of the three basis two-forms in $\mathbb{R}^3$ is why we can define a cross product between vectors in&nbsp;$\mathbb{R}^3$; as you may know, the result of the cross product between two vectors is not a vector but a pseudovector, as it does not change under mirror reflections. More properly, the components of the cross product are actually the components of a two-form.

### Tensors as maps of vectors to vectors
You may be tempted to write the components of a two-tensor as a matrix; after all, we have a collection of numbers $\chi_{ij}$ with two indices. A matrix however is a (linear) map from vectors to vectors. There is a subtle difference, which we can illustrate by considering the object we get when we fix one of the arguments of the tensor $\chi$. For fixed $\bm{w} \in V$, we get a map from the vectors to the real numbers:

$$
\chi(\cdot, \bm{w}) : V \to \mathbb{R},
$$ (tensortooneform)

defined as $\chi(\bm{v}, \bm{w})$ for any $\bm{v} \in V$. $\chi(\cdot, \bm{w})$ thus defines a one-form, just like $\phi_{\bm{u}}(\bm{v}) = \langle\bm{u} \,, \bm{v}\rangle$ defined one; indeed the one-form $\phi_{\bm{u}}(\cdot)$ is just a special case of equation&nbsp;{eq}`tensortooneform` for which $\chi$ is the metric tensor.

Now we've seen in {numref}`sec:oneforms` that there is a one-to-one correspondence between one-forms and vectors: the one-form $\phi_{\bm{u}}(\cdot)$ corresponds with the vector&nbsp;$\bm{u}$. Their components are related via the metric tensor, as expressed in equations&nbsp;{eq}`loweringindex` and&nbsp;{eq}`raisingindex`. There is therefore also a vector that corresponds to the one-form $\chi(\cdot, \bm{w})$. The components of this one-form are given by $\chi_{ij}w^j$; unsurprisingly, the components of the corresponding vector are given by raising the free index&nbsp;$i$ with the metric, which gives a vector $\bm{u}$ with components

$$
u^k = g^{ik} \chi_{ij} w^j.
$$ (twotensorvectormap)

Now if we vary the vector&nbsp;$\bm{w}$ in equation&nbsp;{eq}`twotensorvectormap`, the resulting vector will also change - linearly, because the equation is linear. Equation&nbsp;{eq}`twotensorvectormap` thus gives us a linear map from vectors to vectors, whose components are given by

$$
\chi^k_j = g^{ik} \chi_{ij}.
$$ (deftensorlinearmapcomponents)

Note that if the tensor $\chi$ is not symmetric, it matters on which of its entries we have it act. In equation&nbsp;{eq}`deftensorlinearmapcomponents` we've chosen to act on the second entry of $\chi(\cdot, \cdot)$; had we chosen the first one, we'd have raised the other component, and arrived at $\chi^k_i = g^{jk} \chi_{ij}$.

The components of $\chi^k_j$ (and $\chi^k_i$) *do* form a matrix in the sense that you're used to: they map vectors onto vectors. Because of the identification of vectors and one-forms, we can thus interpret a two-tensor as either a map of two vectors onto a real number (as we usually do with the metric, representing the inner product map), but also as a map from vectors to vectors. Note that in general the *representations* of the tensor are different: the former corresponds to the covariant representation $\chi_{ij}$, while the latter corresponds to the 'mixed' representation $\chi^k_j$. Many texts treat the representations as the tensors. In that language, the covariant representation is called a $(0, 2)$ tensor, and the mixed representations are called $(1, 1)$ tensors. That is confusing the representation with the abstract object though - just like a vector is more than the set of numbers that represent it, a tensor is more than a set of numbers: it is a multi-linear map, with various representations corresponding to various uses.

Finally, we could use the two-tensor also as a map of two one-forms (or equivalently, two co-vectors) onto a real number, or of one one-form onto another, or even of one one-form (/co-vector) and one vector onto a real number. Representations for all of these can be gotten easily by the same construction that gave us the covariant representation. For example, the contravariant representation $\chi^{ij}$ of the tensor $\chi$ (in which we interpret it as the map of two co-vectors onto a real number) is given by

$$
\chi(\bm{v}, \bm{w}) = v_i w_j \chi(\bm{e}^i, \bm{e}^j) \equiv v_i w_j \chi^{ij}.
$$ (twotensorcontravariant)

It won't surprise you that the contravariant representation is referred to as the $(2, 0)$ one, nor that it is related to the other representations through the metric. We have:

$$
\chi^{kl} = g^{lj} \chi^k_j = g^{ik} g^{jl} \chi_{ij},
$$ (twotensormetricrelations)

where we have to take care to preserve the order of the indices if $\chi$ is not symmetric.

(sec:tensorcoordtransforms)=
### Tensors and coordinate transformations

In {numref}`sec:oneformgeometry` we introduced the idea of constructing a basis (two bases, actually, the contravariant and covariant ones) based on a coordinate transformation. Such a basis is known as a *coordinate basis*, and turns out to be very convenient to work with. Two examples are given in {numref}`sec:oneformgeometry`; an example of a basis that is not a coordinate basis is the 'regular' polar basis in which the basis vectors have been normalized: you cannot write these as the derivatives of some function of $\mathbb{R}^2$ onto itself.

We know that the components of the representation of a tensor (a concept that we now also understand to include one-forms and vectors) change as we go from one basis to the next, but we haven't yet discussed how to relate them. For coordinate bases, this is easy, as we can simply express the change as a linear transformation based on the Jacobian of the transformation function. To see how this works, suppose we have two sets of coordinates, which we'll denote by $\{u^i\}$ and $\{u^{i'}\}$, or 'unprimed' and 'primed'<sup>[^5]</sup>. For both of these coordinate systems, we have functions $x^i(\{u^i\})$ and $x^i(\{u^{i'}\})$ that map them back to Cartesian coordinates, exactly like in equation&nbsp;{eq}`coordinatetransform`. We can also define contravariant and covariant bases for each system, following equations&nbsp;{eq}`coordinatetransformtangentbasis` and&nbsp;{eq}`coordinatetransformationnormalbasis`:

```{math}
:label: primedunprimedbases
\begin{alignat*}{2}
\bm{e}_i &= \frac{\partial \bm{x}}{\partial u^i}, &\qquad \bm{e}_{i'} &= \frac{\partial \bm{x}}{\partial u^{i'}},\\
\bm{e}^i &= \bm{\nabla} u^i, &\qquad \bm{e}^{i'} &= \bm{\nabla} u^{i'},
\end{alignat*}
```

where $\bm{x}$ is the vector with components $x^i$ in Cartesian coordinates. Since both the primed and unprimed coordinate systems are related to the Cartesians through a coordinate transformation, they are related to each other, and we can express the primed basis vectors in terms of the unprimed ones using the chain rule:

```{math}
:label: primedunprimedbasistransforms
\begin{align*}
\bm{e}_{i'} &= \frac{\partial \bm{x}}{\partial u^{i'}} = \frac{\partial \bm{x}}{\partial u^j} \frac{\partial u^j}{\partial u^{i'}} \equiv \Lambda^j_{i'} \bm{e}_j,\\
\bm{e}^{i'} &= \bm{\nabla} u^{i'} = \frac{\partial u^{i'}}{\partial u^j} \bm{\nabla} u^j \equiv \Lambda^{i'}_j \bm{e}^j,
\end{align*}
```

so the basis vectors are related through the Jacobian matrices of partial derivatives, $\Lambda^j_{i'} = \partial u^j/\partial u^{i'}$ for the contravariant basis, and its inverse $\Lambda^{i'}_j = \partial u^{i'}/\partial u^j$ for the covariant basis<sup>[^6]</sup>. The components of vectors and co-vectors / one-forms transform in the exact opposite way as their respective basis vectors, as we can see easily by expressing them in the two bases. For the contravariant components of a vector&nbsp;$\bm{v}$ we have

$$
\bm{v} = v^j \bm{e}_ji = v^{i'} \bm{e}_{i'} = v^{i'} \Lambda^j_{i'} \bm{e}_j,
$$ (vectorcoordinatetransform)

so we can read off that

$$
v^{i'} = \Lambda^{i'}_j v^j,
$$ (vectorcontravariantcomponenttransform)

and similarly we find for the contravariant components that

$$
v_{i'} = \Lambda^j_{i'} v_j.
$$ (vectorcovariantcomponenttransform)


As you may have guessed, we can use the linearity of a two-tensor in each of its components to now also write down the transformation rules for the components of such a tensor in any representation. Perhaps unsurprisingly, it will pick up two transformation matrices, one per component. For our generic tensor $\chi$ with covariant components $\chi_{ij}$ in the unprimed and $\chi_{i'j'}$ in the primed coordinates, we find

$$
\chi(\bm{v}, \bm{w}) = \chi_{kl} v^k w^l = \chi_{i'j'} v^{i'} w^{j'} = \chi_{i'j'} \Lambda^{i'}_k v^k \Lambda^{j'}_l w^l,
$$ (twotensorcoordinatetransform)

so

$$
\chi_{i'j'} = \Lambda^k_{i'} \Lambda^l_{j'} \chi_{kl}.
$$ (twotensorcovariantcomponenttransform)

The transformations of components of other representations can be found in a completely analogous manner.

### Tensor eigenvalues, diagonalization, and invariants
Because two-tensors can be interpreted as linear maps from vectors to vectors, they are (in this representation) identical to matrices, and all the machinery of linear algebra can be applied to them. In particular, we can find the eigenvalues and eigenvectors of a two-tensor in the $(1, 1)$ representation, which are defined in the usual way:

$$
\chi^k_j v^j = \lambda v^k,
$$ (tensoreigenvalues)

where $\bm{v} = v^k \bm{e}_k$ is the eigenvector corresponding to the eigenvalue&nbsp;$\lambda$. If the tensor (and thus its $(1, 1)$ matrix representation) is symmetric, the eigenvalues are real, and the tensor can be diagonalized by a coordinate transformation to a basis of eigenvectors (see {numref}`sec:tensorcoordtransforms`).

Like for vectors, the components of a tensor depend on the choice of coordinates, but there are also a number of characteristics (like the length of the vector) that are independent of the choice of coordinates. You're likely familiar with two examples from linear algebra: the trace and the determinant of  a matrix. The trace directly translates to tensors, as we now have a matrix representation: it is the sum of all the eigenvalues, which equals the sum of the diagonal elements *in the $(1, 1)$ representation of the tensor*. The trace can also be calculated from the other representations, but then requires the metric to first transform it to the $(1, 1)$ matrix form. We have

$$
\mathrm{Tr}(\chi) = \chi^i_i = g^{ik} \chi_{ik} = g_{ik} \chi^{ik}.
$$ (tensortrace)

Likewise, we can calculate the determinant of the matrix representation, which implies that in the other representations, we get correction factors that depend on the metric. We have

$$
\mathrm{det}(\chi) = \mathrm{det}(\chi^k_j) = \mathrm{det}(g^{ik}\chi_{ij}) = \mathrm{det}(g_{jl}\chi^{kl}).
$$ (tensordeterminant)


To prove that the eigenvalues of a two-tensor, or functions of those eigenvalues (such as the trace and determinant) are independent of the choice of coordinates, we consider a generic two-tensor $\chi$ in a matrix representation in some basis. The tensor has a characteristic polynomial

$$
P(\lambda) = \det(\chi - \lambda I),
$$ (charpolynomial)

where $I$ is the identity tensor. First we'll prove that this polynomial is independent of the choice of basis. Therefore, let's apply a similarity transform to $\chi$, which gives $\chi' = \Lambda^{-1} \chi \Lambda$. The characteristic polynomial of the transformed matrix is given by

```{math}
:label: charpolynomialinvariance
\begin{align*}
P'(\lambda) &= \det(\chi' - \lambda I) = \det(\Lambda^{-1} \chi \Lambda - \lambda I) = \det[\Lambda^{-1} ( \chi - \lambda I) \Lambda] \\
&= \det(\Lambda^{-1}) \det(\chi - \lambda I) \det(\Lambda) = P(\lambda),
\end{align*}
```
where we used that the determinant of a product is the product of the determinants ($\det(\chi\psi) = \det(\chi)\det(\psi)$), and that the determinant of the inverse of a matrix is the inverse of the matrix's determinant ($\det(\Lambda^{-1}) = 1/\det(\Lambda)$). Equation&nbsp;{eq}`charpolynomialinvariance` shows that the characteristic polynomial is invariant under coordinate transformations. Note that so far we have made no assumptions on the number of dimensions of $\chi$. If the number of dimensions equals two, we can easily express the characteristic polynomial in terms of the elements of $\chi$:

$$
P(\lambda) = \det(\chi - \lambda I) = \lambda^2 - \lambda \mathrm{Tr}(\chi) + \det(\chi).
$$ (charpolynomial2D)

Now as the characteristic polynomial is invariant for any value of $\lambda$, the coefficients of the various powers of $\lambda$ in equation&nbsp;{eq}`charpolynomial2D` must also be invariant, which shows that the trace and determinant of $\chi$ are invariant. As we can express the eigenvalues of $\chi$ in terms of the trace and determinant, those must be invariant as well.

In three dimensions, in addition to the trace and determinant of $\chi$, we find that the sum of the minors of $\chi$ (the determinants of the matrices you get when crossing out a row and the corresponding column) is also invariant, which again gives us the invariance of the eigenvalues. This sum of minors is not necessarily the easiest invariant to work with, so instead we can pick another quantity. A commonly used one is the trace of $\chi^2$ (i.e., the sum of the squares of all components), which of course can be expressed as a linear combination of the three invariants we already found.


### Higher-order tensors
The concepts of this section extend trivially to higher-order tensors. $n$-tensors are multilinear maps of $n$ vectors to real numbers. They can be represented by objects with $n$ indices, with a mix of covariant and contravariant components, depending on your needs. These component representations are related to each other through the metric, and can be transformed from one coordinate system to another through multiplication with $n$ Jacobian matrices. Tensors may be symmetric or antisymmetric in some or all of their arguments (and consequently, their components in the corresponding indices). In particular, $n$-forms are fully antisymmetric in all arguments by construction. Therefore, if your vector space has $n$ dimensions, there is essentially (up to multiplication with a scalar) only one $n$-form, and no forms of degree larger than $n$.

## Covariant differentiation
(sec:covariantderivatives)=
### Connections and covariant derivatives

Unlike Cartesian coordinates, in a general curvilinear coordinate system the basis vectors change in orientation and length as you move through space. This property can be very convenient for expressing physical quantities that respect the same symmetries as your chosen coordinate system (e.g., the radially outward direction is easier to specify in polar than in Cartesian coordinates), but it also means that the components of a vector will change if you move the vector to a different spot. Moreover, all coordinate systems, vectors and tensors may be fields, i.e., functions of position, such as the temperature (scalar field) and wind (vector field) at any point on Earth at a given time. We'll often want to know how these quantities change as we move from one position to the next, i.e., we'll want to calculate their derivatives, but we'll typically only be interested in the actual changes in the abstract vector or tensor, not in the change due to a particular choice of coordinates. In this section we'll find a way of doing that, which is known as the *covariant derivative*: the derivative of the object independent of the choice of coordinates.

To illustrate, let's consider a vector field $\bm{v}$ expressed as a function of a coordinate system $\{u^i\}$, and suppose we want to know how $\bm{v}$ changes if we vary the $j$th coordinate (e.g., we want to know how the wind changes as we move south). To calculate this quantity, we express $\bm{v}$ in the coordinate basis&nbsp;$\{\bm{e}_i\}$ defined by $\{u^i\}$ as usual, $\bm{v} = v^i \bm{e}_i$, and take the derivative of each of the components of $\bm{v}$, which gives us

$$
\frac{\partial \bm{v}}{\partial u^j} = \frac{\partial v^i}{\partial u^j} \bm{e}_i + v^i \frac{\partial \bm{e}_i}{\partial u^j},
$$ (vectorderivative)

so in addition to the partial derivative of $v^i$, we'll get an extra term due to the change of the basis vector $\bm{e}_i$. Since the derivative of a vector is another vector, we can express the components of $\partial \bm{e}_i / \partial u^j$ in the basis $\{\bm{e}_i\}$ again, through

$$
\frac{\partial \bm{e}_i}{\partial u^j} = \Gamma^k_{ij} \bm{e}_k.
$$ (defChristoffelsymbols)

Equation&nbsp;{eq}`defChristoffelsymbols` defines the *connections* or *Christoffel symbols* $\Gamma^k_{ij}$, which, for any fixed value of $i$, map the basis vectors $\bm{e}_k$ on the derivatives of the basis vectors. We'll find explicit expressions for the Christoffel symbols in terms of the metric in {numref}`sec:Christoffelsymbols`. Using the Christoffel symbols, we can express the derivative of $\bm{v}$ as another vector:

$$
\frac{\partial \bm{v}}{\partial u^j} = \left[ \frac{\partial v^k}{\partial u^j} + v^i \Gamma^k_{ij} \right] \bm{e}_k.
$$ (vectorderivative2)

Note that in equation&nbsp;{eq}`vectorderivative2` we re-labeled the index of the components of $\bm{v}$ in the first term. The vector whose components are given by the terms in square brackets on the right hand side of equation&nbsp;{eq}`vectorderivative2` is called the *covariant derivative* of the vector&nbsp;$\bm{v}$. Following standard practice, we will denote partial derivatives of vector and tensor components in a given coordinate system with a comma (so $v^k_{,j} = \partial v^k / \partial u^j$) and covariant derivatives with a semicolon ($v^k_{;j}$), so we have for the components of the covariant derivative:

$$
v^k_{;j} = v^k_{,j} + v^i \Gamma^k_{ij}.
$$ (covariantvectorderivative)

Note that in Cartesian coordinates, the Christoffel symbols are all identically zero, and thus the covariant derivative equals the ordinary partial derivative. Also note that equations&nbsp;{eq}`vectorderivative2` and&nbsp;{eq}`covariantvectorderivative` define a new vector for each value of&nbsp;$j$.

If we can take covariant derivatives of vectors, it stands to reason that we should also be able to do so of one-forms (which are in the end related one-on-one to the vectors). As a one-form&nbsp;$\phi$, when acting on a vector, gives us a scalar $\phi(\bm{v})$ (i.e., a number, not a vector) which is independent of the basis, the covariant derivative of the one-form will equal its partial derivative. The same however does not hold for the components $\phi_i$, as those are dependent on the choice of basis. Unsurprisingly, the components of the covariant derivative of a one-form $\phi$ will also contain a Christoffel symbol. To find an expression for them, we simply take the derivative of the full one-form, and expand in a basis:

```{math}
:label: oneformcovariantderivativederivation
\begin{align*}
\frac{\partial \phi(\bm{v})}{\partial u^j} = \frac{\partial \phi_k v^k}{\partial u^j} &= \phi_k v^k_{,j} + \phi_{k,j} v^k \\
&= \phi_k v^k_{;j} + \phi_{k;j} v^k = \phi_k v^k_{,j} + \phi_k v^i \Gamma^k_{ij} + \phi_{k;j} v^k,
\end{align*}
```

where we used, when going from the first to the second line, that the covariant and partial derivatives of the scalar $\phi(\bm{v})$ are the same. Comparing the last term of equation&nbsp;{eq}`oneformcovariantderivativederivation`B with the last of {eq}`oneformcovariantderivativederivation`A, we can read off (after some relabeling) that we can define, as the covariant derivative of $\phi$, a new one-form with components

$$
\phi_{k;j} = \phi_{k,j} - \phi_i \Gamma^i_{kj}.
$$ (oneformcovariantderivative)


The extension of the covariant derivative to two-tensors is trivial: we simply repeat the construction in equation&nbsp;{eq}`oneformcovariantderivativederivation` for a two-tensor $\chi(\bm{v}, \bm{w})$, which will give us an extra term with a Christoffel symbol for each of the vectors, so the covariant derivative of $\chi$ defines a new two-tensor with components

$$
\chi_{kl;j} = \chi_{kl,j} - \chi_{il} \Gamma^i_{kj} - \chi_{ki} \Gamma^i_{lj}.
$$ (twotensorcovariantderivative)

Likewise, extensions to the $(1, 1)$ and $(2, 0)$ representation of $\chi$ follow readily:

```{math}
:label: twotensorcovariantderivative11
\begin{align*}
\chi^k_{l;j} &= \chi^k_{l,j} + \chi^i_l \Gamma^k_{ij} - \chi^k_i \Gamma^i_{lj}, \\
\chi^{kl}_{;j} &= \chi^{kl}_{,j} + \chi^{il} \Gamma^k_{ij} + \chi^{ki} \Gamma^l_{ij}.
\end{align*}
```

(sec:Christoffelsymbols)=
### Christoffel symbols

The Christoffel symbols are defined by equation&nbsp;{eq}`defChristoffelsymbols`; although they can in principle be calculated from this equation for any basis by expressing the derivatives of the basis in the basis itself, it would be helpful to have a faster way of getting them. Fortunately, we can find the Christoffel symbols directly from the derivatives of the metric, as we'll see below in equation&nbsp;{eq}`Christoffelmetric`. To derive this expression, we first note that the Christoffel symbols are symmetric in their lower indices, because, by symmetry of the partial derivatives, we have for any coordinate basis

$$
\frac{\partial \bm{e}_i}{\partial u_j} = \frac{\partial^2 \bm{x}}{\partial u_j \partial u_i} = \frac{\partial^2 \bm{x}}{\partial u_i \partial u_j} = \frac{\partial \bm{e}_j}{\partial u_i},
$$

so $\Gamma^k_{ij}\bm{e}_k = \Gamma^k_{ji}\bm{e}_k$, and we have

$$
\Gamma^k_{ij} = \Gamma^k_{ji}.
$$ (Christoffelsymmetry)

Now by taking the derivative of (the covariant representation of) the metric, $g_{ij} = \langle\bm{e}_i \,, \bm{e}_j\rangle$, and using the definition&nbsp;{eq}`defChristoffelsymbols` of the Christoffel symbols, we get

```{math}
:label: metricderivativeChristoffel
\begin{align*}
\partial_k g_{ij} &= \langle\partial_k\bm{e}_i \,, \bm{e}_j\rangle + \langle\bm{e}_i \,, \partial_k\bm{e}_j\rangle = \langle\Gamma^l_{ik}\bm{e}_l \,, \bm{e}_j\rangle + \langle\bm{e}_i \,, \Gamma^l_{jk}\bm{e}_l\rangle \\
&= \Gamma^l_{ik} g_{lj} + \Gamma^l_{jk} g_{il}.
\end{align*}
```
In equation&nbsp;{eq}`metricderivativeChristoffel` we can cyclicly permute the indices to also get

```{math}
:label: metricderivativeChristoffel2
\begin{align*}
\partial_i g_{jk} &= \Gamma^l_{ji} g_{lk} + \Gamma^l_{ki} g_{jl}, \\
\end{align*}
```

```{math}
:label: metricderivativeChristoffel3
\begin{align*}
\partial_j g_{ki} &= \Gamma^l_{kj} g_{li} + \Gamma^l_{ij} g_{kl}.
\end{align*}
```
Adding equations&nbsp;{eq}`metricderivativeChristoffel` and&nbsp;{eq}`metricderivativeChristoffel2` and subtracting&nbsp;{eq}`metricderivativeChristoffel3`, we get, after some rewriting in which we use the symmetry of both $g_{ij}$ and $\Gamma^k_{ij}$,

$$
2 \Gamma^l_{ik} g_{lj} = \partial_k g_{ij} + \partial_i g_{jk} - \partial_j g_{ki}.
$$ (metricderivativeChristoffel4)

We can now isolate the Christoffel symbols by contracting<sup>[^7]</sup> both sides with $g^{jm}$. After re-labeling the indices this gives us the desired expression:

$$
\boxed{\Gamma^k_{ij} = \frac12 g^{kl} \left( \partial_i g_{lj} + \partial_j g_{il} -\partial_l g_{ij} \right).}
$$ (Christoffelmetric)

Incidentally, the Christoffel symbols as given in equation&nbsp;{eq}`Christoffelmetric` are sometimes referred to as the Christoffel symbols of the second kind; the Christoffel symbols of the first kind are defined as $\Gamma_{ijk} = g_{il}\Gamma^l_{jk}$, which can be used to calculate the partial derivatives of the metric from the Christoffel symbols:

$$
\partial_k g_{ij} = \Gamma_{ijk} + \Gamma_{jik}.
$$ (Christoffelfirstkindmetric)


### Covariant derivative of the metric
You may have noticed that while we used the Christoffel symbols to calculate covariant derivatives in {numref}`sec:covariantderivatives`, the expressions in {numref}`sec:Christoffelsymbols` for the Christoffel symbols themselves involve the ordinary partial derivatives of the metric. That makes sense: the Christoffel symbols are defined as the connection between the basis vectors and their partial derivatives, so we'd expect partial derivatives there; they show up in the covariant derivative to correct for the fact that the basis vectors have nonvanishing partial derivatives. Nonetheless, we can still calculate the covariant derivative of the metric tensor. Fortunately, as we'll see, it is always zero, in any coordinate system.

One easy way to assert the vanishing of the covariant derivative of the metric is to use the fact that tensor equations are invariant under coordinate transformations: if the covariant derivative of the metric is zero in one coordinate system, it has to be zero in all. There is a special coordiante system in which the calculation of the covariant derivative of the metric is trivial: Cartesian coordinates, as there the metric is simply the identity, and its covariant derivative (equal to the partial derivative in Cartesian coordinates) identically vanishes.

Alternatively, we can simply calculate the covariant derivative of the metric, using equation&nbsp;{eq}`twotensorcovariantderivative` for a general two-vector and equation&nbsp;{eq}`Christoffelfirstkindmetric` for the partial derivative of the metric, which gives us

```{math}
\begin{align*}
g_{ij;k} &= \Gamma_{ijk} + \Gamma_{jik} - g_{lj} \Gamma^l_{il} - g_{il} \Gamma^l_{jk}, \\
&= g_{il}\Gamma^l_{jk} + g_{jl} \Gamma^l_{ik} - g_{lj} \Gamma^l_{ik} - g_{il} \Gamma^l_{jk},
\end{align*}
```
or, by symmetry of both the metric and $\Gamma^l_{ik}$,

$$
\boxed{g_{ij;k} = 0.}
$$ (metriccovariantderivative)


(sec:curvature)=
## Curvature


### Geodesics
Geodesic: generalization of straight line in Euclidean space (shortest path between two points).
Straight line $\Leftrightarrow$ tangent vectors all point in the same direction.
Tangent vector of a line parametrized by arclength $s$ and given by $\bm{r}(s)$ is

$$
\bm{\hat{t}}(s) = \frac{\mathrm{d}\bm{r}}{\mathrm{d}s} = \dot{\bm{r}}(s).
$$

These tangent vectors have unit length by construction. The change of the tangent vector is given by its derivative; for a straight line we thus have $\dot{\bm{\hat{t}}}(s) = 0$. If we express the components of $\bm{t}$ in an arbitrary (contravariant) coordinate basis, this equation gives:

$$
0 = \frac{\mathrm{d}\bm{\hat{t}}}{\mathrm{d}s} = \frac{\mathrm{d}(t^i \bm{e}_i)}{\mathrm{d}s} = \dot{t}^i \bm{e}_i + t^i \dot{\bm{e}}_i = \dot{t}^i \bm{e}_i + t^i (\partial_j \bm{e}_i) \dot{x}^j = \dot{t}^i \bm{e}_i + t^i (\Gamma^k_{ij} \bm{e}_k) \dot{x}^j,
$$

so, by re-labeling indices, we have that for a straight line in arbitrary coordinates

$$
\left(\dot{t}^i + \Gamma^i_{jk} t^j \dot{x}^k \right) \bm{e}_i = 0.
$$ (geodesictangent)

Substituting back $t^i = \dot{x}^i$ in equation&nbsp;{eq}`geodesictangent`, we get

$$
\frac{\mathrm{d}^2 x^i}{\mathrm{d}s^2} + \Gamma^i_{jk} \frac{\mathrm{d}x^j}{\mathrm{d}s} \frac{\mathrm{d}x^k}{\mathrm{d}s} = 0,
$$ (geodesicequation)

for the tangent vector to a straight line. 


(sec:Riemanntensor)=
### Riemann tensor

If the world were flat, and thus a Euclidean space, walking first west for a distance&nbsp;$x$ and then south for a distance&nbsp;$y$ would put you at the same spot as when you'd walk south for a distance&nbsp;$y$ first and then west for a distance&nbsp;$x$. On a curved world, like our (roughly) spherical planet, this is clearly not the case, if the distances are large enough: if you start on the equator, go west first for $6371\;\mathrm{km}$ (Earth's radius) and then go south by another&nbsp;$6371\;\mathrm{km}$, you end up in quite a different spot then when you'd have gone south first, as in that case the circle of latitude (on which you travel east/west) is much shorter than at the equator. This discrepancy is due to two effects, one which originates in the choice of coordinates (we're attempting a square grid on a spherical surface if we use an east/west and north/south coordinate frame), the other in the fact that the space itself is curved.

Notwithstanding our poor choice of coordinates, the example above shows that you can determine the curvature of your local space purely from measurements in that space; we don't need to go to the moon to discover that the earth is round. In general, the curvature of your object may not be constant though, so we'd better find a local measure rather than considering global distances. Unsurprisingly, this local measure is the second derivative, which you can see from considering the curvature of a line: the first derivative gives you the direction of the tangent, the second derivative tells you how quickly the tangent changes, which is a measure of curvature.

Naturally, we want to disentangle actual curvature from effects due to the choice of coordinates when calculating the curvature of our space. We therefore will use the covariant derivative. Differentiating the covariant derivative of a one-form (equation&nbsp;{eq}`oneformcovariantderivative`) once again, we find<sup>[^8]</sup>

```{math}
:label: oneformcovariantsecondderivative
\begin{align*}
\phi_{i;jk} &= \partial_k (\phi_{i;j}) - (\phi_{m;j}) \Gamma^m_{ik} - (\phi_{i;m}) \Gamma^m_{jk}  \\
&= \partial_k \partial_j \phi_i - \partial_k \left( \phi_l \Gamma^l_{ij} \right) - \left(\partial_j \phi_m - \phi_l \Gamma^l_{mj}\right) \Gamma^m_{ik} - \left(\partial_m \phi_i - \phi_l \Gamma^l_{im} \right) \Gamma^m_{jk}.
\end{align*}
```
We find that unlike for partial derivatives, when taking the covariant second derivative, the order of the differentiation matters - just like the order of travel mattered for our thought experiment on earth. The difference between the two answers is a measure for the curvature, which we can now calculate easily by swapping $j$ and $k$ in&nbsp;{eq}`oneformcovariantsecondderivative` and subtracting, which gives

```{math}
:label: oneformcovariantsecondderivativecurvature
\begin{align*}
\phi_{i;jk} - \phi_{i;kj} &= {R^l}_{ijk} \phi_l, \\
\end{align*}
```

```{math}
:label: Riemanntensorcomponents
\begin{align*}
{R^l}_{ijk} &= \partial_j \Gamma^l_{ik} - \partial_k \Gamma^l_{ij} + \Gamma^l_{mj} \Gamma^m_{ik} - \Gamma^l_{mk} \Gamma^m_{ij}.
\end{align*}
```
Equation&nbsp;{eq}`Riemanntensorcomponents` defines the $(1, 3)$ representation of the *Riemann tensor* (also known as the curvature tensor or the Riemann-Christoffel tensor), which measures the curvature of space. Fortunately, in physics, we will almost never need the full tensor, not even in general relativity. Moreover, it has a number of symmetries, reducing the $n^4$ (with $n$ the dimension of the underlying vector space) components to $n^2(n^2-1)/12$ independent ones; and in flat space, all components vanish.

One symmetry of the Riemann tensor follows from cyclicly permuting its covariant components, which gives

$$
{R^l}_{ijk} + {R^l}_{jki} + {R^l}_{kij} = 0,
$$ (Riemanncyclicidentity)

as you can check easily. Second, we can lower the contravariant component to produce a fully covariant representation of our four-tensor (interpreted, as usual, as the map of four vectors onto a real number), $R_{ijkl} = g_{im} {R^m}_{jkl}$, for which we can find an explicit expression in terms of the metric and Christoffel symbols:

$$
R_{ijkl} = \frac12 \left[ \partial_l \partial_i g_{jk} - \partial_l \partial_j g_{ik} + \partial_k \partial_j g_{il} - \partial_k \partial_i g_{jl} \right] - g^{mn} \left[ \Gamma_{mik} \Gamma_{njl} - \Gamma_{mil} \Gamma_{njk} \right].
$$ (RiemannmetricChristoffel)

From equation&nbsp;{eq}`RiemannmetricChristoffel`, we can read off one symmetry and two antisymmetries of $R_{ijkl}$:

```{math}
:label: Riemannsymmetry
\begin{align*}
R_{ijkl} &= - R_{jikl}, \\
R_{ijkl} &= - R_{ijlk}, \\
R_{ijkl} &= R_{klij}.
\end{align*}
```

Finally, we have the *Bianchi identity* for the covariant derivatives of the Riemann tensor

$$
{R^l}_{ijk;m} + {R^l}_{ikm;j} + {R^l}_{imj;k} = 0.
$$ (Bianchiidentity)


(sec:Ricci)=
### Ricci tensor, Ricci scalar, and Einstein tensor

From the first antisymmetry of the Riemann tensor, equation&nbsp;{eq}`Riemannsymmetry`A, we can read off that the 'contraction' of the first and the second index of the $(1, 3)$ representation (i.e., summing over all cases when $i=j$) gives zero:

$$
{R^i}_{ijk} = 0.
$$

Contracting the first and third index however does not in general give zero, but instead the components of a new two-tensor, known as the *Ricci tensor*, of which the covariant representation is given by:

$$
R_{ij} = {R^k}_{ikj}.
$$ (defRiccitensor)

By equation&nbsp;{eq}`Riemannsymmetry`C, the Ricci tensor is symmetric in its two arguments, and by the antisymmetry property&nbsp;{eq}`Riemannsymmetry`A, the contraction of the first and fourth index of the Riemann tensor just gives $-R_{ij}$. Likewise, other contractions give zero or the Ricci tensor as well, so the Ricci tensor is the only nontrivial contraction of the Riemann tensor.

We can further contract the two indices of the Ricci tensor to arrive at the *Ricci scalar* or *curvature scalar*

$$
R = R^i_i = g^{ij} R_{ij} = g^{ij} g^{kl} R_{kilj},
$$ (defRicciscalar)

which is simply the trace of the Ricci tensor, see equation&nbsp;{eq}`tensortrace`.

Rather than contracting two components of the Riemann tensor, one can also contract the Bianchi identity&nbsp;{eq}`Bianchiidentity`, which leads to an expression for the contravariant components of a tensor that has a vanishing contraction with its covariant derivative. The derivation takes a page and is not so relevant here, but as you may encounter the tensor again in a physics context, it is nice to see how it is related to the Ricci tensor and scalar, in their contravariant representation. This new tensor is known as the *Einstein tensor*, with components given by

$$
G^{ij} = R^{ij} - \frac12 g^{ij} R.
$$ (defEinsteintensor)

The Einstein tensor is evidently symmetric; by construction, the contraction with its covariant derivative vanishes: ${G^{ij}}_{;j}=0$. It occurs in the basic set of equations of general relativity, the Einstein field equations, which state that curvature originates from energy (including mass):

$$
G^{\mu\nu} = 8 \pi T^{\mu\nu},
$$ (Einsteinequation)

where the Greek indices are understood to sum over four-dimensional spacetime, and $T^{\mu\nu}$ is the contravariant representation of the stress-energy tensor. Incidentally, as the contraction of the covariant derivative of the Einstein tensor vanishes, so must that of the stress-energy tensor, so we get ${T^{\mu\nu}}_{;\nu} = 0$, which gives conservation of both energy and momentum.

(sec:surfaces)=
### Curvature of surfaces

Surfaces deserve special attention, if only because we encounter them so often. We define a surface as a space with two dimensions<sup>[^9]</sup>, possibly (but not necessarily) embedded in a higher-dimensional (usually three-dimensional) space. As asserted in {numref}`sec:Riemanntensor`, the Riemann tensor of a surface will have only $2^2 (2^2-1)/12 = 1$ independent component; as indeed you can check easily, of the 16 components of the Riemann tensor of a surface, by the (anti)symmetry condition&nbsp;{eq}`Riemannsymmetry`, 12 are zero, and the remaining four satisfy $R_{1212} = R_{2121} = -R_{1221} = -R_{1221}$. The free parameter of course will be the Ricci scalar, which, as a scalar, is independent of the choice of coordinates. We can use these observations to write down a simple form for the Riemann tensor of a surface. After all, if we know the value of $R_{1212}$ (which itself is determined by the value of the free parameter $R$), we can find all other components. Because the other components follow from symmetry arguments, it follows that the Riemann tensor of a surface is some multiple of any other tensor that satisfies the same symmetries (and thus also has only one free parameter). We can easily construct such a tensor from the metric. We conclude that we can write

$$
R_{ijkl} = f(R) \left( g_{ik}g_{jl} - g_{il}g_{jk} \right),
$$ (Riemanntensorsurface)

where $f(R)$ is a scalar function of the Ricci scalar $R$, and (as you again can check easily) the right-hand side of equation&nbsp;{eq}`Riemanntensorsurface` satisfies the symmetrie&nbsp;{eq}`Riemannsymmetry` of the Riemann tensor. To find $f(R)$, we simply contract the Riemann tensor in equation&nbsp;{eq}`Riemanntensorsurface` with $g^{ik}$ to find the Ricci tensor for a surface:

$$
R_{jl} = g^{ki} R_{ijkl} = f(R) g^{ki} \left( g_{ik}g_{jl} - g_{il}g_{jk} \right) = f(R) \left( 2 g_{jl} - g_{jl} \right) = f(R) g_{jl},
$$

where we used that in two dimensions, the trace of the metric is two. For the Ricci scalar, we now find

$$
R = g^{jl} R_{jl} = f(R) g^{jl} g_{jl} = 2 f(R).
$$

We can thus read off that $f(R) = \frac12 R$. This quantity is known as the *Gaussian curvature* of the surface, usually denoted by a capital $K$. The fact that this curvature is intrinsic to the surface (i.e., does not depend on an embedding in a higher-dimensional space) was discovered by Gauss; he considered this result so special that he called it his 'remarkable theorem' ('theorema egregius'). Another theorem, known as the Gauss-Bonnet theorem, tells us that the Gaussian curvature is a topological quantity: if we integrate over a closed surface, the value of the Gaussian curvature will only depend on the genus of the surface:

$$
\oint K \mathrm{d}A = 2 \pi \chi = 4 \pi (1-g),
$$ (GaussBonnet)

where $\chi$ is the Euler characteristic of the surface, given by $\chi = 2(1-g)$ where $g$, the genus, simply counts the number of holes. Indeed, for a sphere of radius $a$ we obtain $K = 1/a^2$, and the integral of $K$ over the whole sphere equals $4 \pi$ ($g=0$); for a torus we have $g=1$ and the integral of $K$ (now not constant on the surface) vanishes.

We cite van Kampen&nbsp;{cite}`van1992stochastic`, and multiple sources&nbsp;{cite}`van1992stochastic,zia2009making`, just to see how that'll work out.





(app:formaldefinitions)=
## Appendix: Formal definitions


### Algebra
#### Groups
A *group* $G$ is a set with an operation&nbsp;$\cdot$ defined on it, satisfying the following four axioms:
1. (Closedness) If $a, b \in G$, then $a \cdot b \in G$ and $b \cdot a \in G$.
1. (Existence of a unit element) There is an element $e \in G$ such that $e \cdot g = g \cdot e = g$ for all $g \in G$.
1. (Associativity) For any $a, b, c \in G$, we have $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
1. (Existence of an inverse) For every $a \in G$, there exists an element $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$.

A group&nbsp;$G$ for which $a \cdot b = b \cdot a$ for all $a, b \in G$ is called a *commutative* or *abelian* group; the operation of a commutative group is often denoted by a plus sign.

**Examples** of groups are the symmetries of geometrical objects, the collection of all permutations of $n$ elements, the integers under addition (with zero as the unit element), the real numbers under addition, the real numbers except zero under multiplication, and the collection of all rotations in $n$ dimensions (known as the matrix group $SO(n)$).

A *subgroup* of a group is a subset of the elements of a group that also forms a group.

#### Rings
A *ring* $R$ is a set with two operations defined on it, usually called addition, $+$, and multiplication, $\cdot$, satisfying the following three conditions:
1. The ring is a commutative group under the addition operation (with a unit element denoted $0$).
1. The ring is associative under multiplication and contains a multiplicative unit element (denoted $1$).
1. (Distrubitivity) For any $a, b, c \in R$ we have $a \cdot (b + c) = a \cdot b + a \cdot c$.


An **example** of a ring is the collection of integers&nbsp;$\mathbb{Z}$ with the usual addition and multiplication operations.

#### Fields
A *field* $F$ is a ring for which each element except the identity of addition, also has a multiplicative inverse; the field is therefore a group under both addition and multiplication, with the added condition of distrubitivity.

**Examples** of fields are the sets&nbsp;$\mathbb{Q}$, $\mathbb{R}$ and&nbsp;$\mathbb{C}$ of rational, real and complex numbers, with their usual addition and multiplication. There are also finite fields $\mathbb{F}_p$ for any prime number $p$, consisting of the integers modulo&nbsp;$p$, where any operation that carries an element outside the set ${0, 1, \ldots, p-1}$ we add or subtract $p$ such that we return to the set (akin to the definition of angles modulo $2\pi$). For example, the field $\mathbb{F}_5$ consists of the elements ${0, 1, 2, 3, 4}$; we have $1 + 2 = 3$, $2 + 3 = 5 = 0$, $2 \cdot 2 = 4$, $2 \cdot 3 = 6 = 1$, and so on. It is easy to prove that this set satisfies all conditions of a field, with $2$ and $3$ being each other's additive inverse (as well as $1$ and $4$), and $2$ and $3$ also being each other's multiplicative inverse, with $4$ the multiplicative inverse of itself.

There are also non-prime finite fields, but constructing them takes a bit more work. (Mathematical) fields should not be confused with physical scalar, vector, or tensor fields, which are functions of a position in space (or spacetime), e.g. the velocity $\bm{v}(\bm{x})$ of a fluid in steady-state flow.


### Linear algebra
#### Vector spaces
A *vector space* $V$ over a field $F$ (usually $\mathbb{R}$ or $\mathbb{C}$) is a collection of objects (usually called vectors) with two operators defined on them: addition $+$ between vectors, and scalar multiplication $\cdot$ between the elements of the field and those of the vector space. The operations satisfy the following eight conditions:
1. (Existence of a unit element) There exists an element $\bm{0} \in V$ such that $\bm{0} + \bm{v} = \bm{v} + \bm{0} = \bm{v}$ for all $\bm{v} \in V$.
1. (Associativity of addition) For any $\bm{u}, \bm{v}, \bm{w} \in V$, we have $(\bm{u} + \bm{v}) + \bm{w} = \bm{u} + (\bm{v} + \bm{w})$.
1. (Commutativity of addition) For any $\bm{u}, \bm{v} \in V$, we have $\bm{u} + \bm{v} = \bm{v} + \bm{u}$.
1. (Existence of additive inverse) For every $\bm{v} \in V$, there exists an element $-\bm{v}$ such that $\bm{v} + (-\bm{v}) = (-\bm{v}) + \bm{v} = \bm{0}$.
1. (Identity of scalar multiplication) For every $\bm{v} \in V$, we have $1 \cdot \bm{v} = \bm{v}$, where $1$ is the unit element of multiplication of $F$.
1. (Compatibility) For all $a, b \in F$ and $\bm{v} \in V$, we have $a \cdot (b \cdot \bm{v}) = (a \cdot b) \cdot \bm{v}$.
1. (Distributivity of vector addition) For all $a \in F$ and $\bm{u}, \bm{v} \in V$, we have $a \cdot (\bm{u} + \bm{v}) = a \cdot \bm{u} + a \cdot \bm{v}$.
1. (Distributivity of scalar multiplication) For all $a, b \in F$ and $\bm{v} \in V$, we have $(a + b) \cdot \bm{v} = (a \cdot \bm{v}) + (b \cdot \bm{v})$.


**Examples** are the well-known vector spaces $\mathbb{R}^n$ and $\mathbb{C}^n$.

#### Norm and metric
A *norm* is a function that assigns a length to any vector in a vector space $V$. Formally, if $V$ is a vector space over a field&nbsp;$F$, then the norm is a function $||\cdot||: V \to [0, \infty)$ satisfying, for all $\bm{v}, \bm{w} in V$ and $s \in F$:
1. (Positive definiteness) $||\bm{v}|| \geq 0$, and $||\bm{v}|| = 0$ if and only if $\bm{v} = \bm{0}$.
1. (Absolute homogeneity) $|| s \bm{v}|| = |s| ||\bm{v}||$, with $|s|$ the absolute value of $s$.
1. (Triangle inequality) $||\bm{v} + \bm{w}|| \leq ||\bm{v}|| + ||\bm{w}||$.


A closely related concept is a *metric*, which is a function that gives a distance between each pair of elements of a set. Formally, if&nbsp;$X$ is a set, then a metric is a function $d : X \times X \to [0, \infty)$ satisfying, for all $x, y, z \in X$:
1. ('Identity of indiscernables') $d(x,y) = 0$ if and only if $x=y$.
1. (Symmetry) $d(x,y) = d(y,x)$.
1. (Triangle inequality) $d(x,y) \leq d(x, z) + d(z,y)$.


Any norm on a vector space defines a metric through $d(\bm{v}, \bm{w}) = ||\bm{v} - \bm{w}||$.

**Examples** include the Euclidean metric (distance between two points in space is calculated using the Pythagorean theorem), the discrete metric, where $d(x,y) = 0$ if ($x=y$) and $d(x,y) = 1$ if $x \neq y$, and the taxicab (or Manhattan) metric, which is the number of steps you have to do on a square grid to get from point $p$ to point $q$. For real vectors $\bm{p}$ and $\bm{q}$, the taxicab metric is defined as

$$
d_1(\bm{p}, \bm{q}) = \sum_{i=1}^n |p_i - q_i| = ||\bm{p} - \bm{q}||_1,
$$

whereas the Euclidean metric is defined as

$$
d_2(\bm{p}, \bm{q}) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2} = ||\bm{p} - \bm{q}||_2.
$$

The taxicab and Euclidean metric are also known as the $L^1$ and $L^2$ norm, respectively (hence the subscripts). In analogy, we can define $L^n$ norms for any positive integer $n$.

A metric allows us to distinguish between points that are 'close' and points that are 'far apart'. We can therefore also define the concept of a *converging sequence*: a sequence of points which, as we progress through the sequence, get ever-closer to a given point (the limit of the sequence). Perhaps counter-intuitively, the limit of a converging sequence need not be part of the space on which we have defined the norm. The easiest example is probably an irrational number (say $\sqrt{2}$ or $\pi$) for the space of rationals&nbsp;$\mathbb{Q}$: we can easily construct a sequence of fractions that converges to $\pi$ (namely $3, 31/10, 314/100, 3141/1000, 31415/10000, \ldots$), but $\pi$ itself cannot be written as a fraction.

A space that contains all the limit points of all converging sequences in that space is called *complete*. As we've just seen, $\mathbb{Q}$ is not complete, but $\mathbb{R}$ is (it is by definition, as we define $\mathbb{R}$ as the smallest complete space that contains&nbsp;$\mathbb{Q}$). A space with a metric is called a metric space; a complete metric space is called a *Banach space*.

#### Inner product
An *inner product* is a function defined on a vector space $V$ that maps two elements of the space to the underlying field $F$: $\langle \cdot, \cdot \rangle : V \times V \to F$, satisfying, for all $\bm{u}, \bm{v}, \bm{w} \in V$ and $s \in F$:
1. (Linearity) $\langle \bm{u} + \bm{v}, \bm{w} \rangle = \langle \bm{u}, \bm{w} \rangle + \langle \bm{v}, \bm{w} \rangle$, $\langle \bm{u}, \bm{v} + \bm{w} \rangle = \langle \bm{u}, \bm{w} \rangle + \langle \bm{u}, \bm{v} \rangle$, and $s \langle \bm{u}, \bm{v} \rangle = \langle \bm{u}, s \bm{v} \rangle = \langle s^* \bm{u}, \bm{v} \rangle$, where $s^*$ is the complex conjugate of $s$.
1. (Symmetry) $\langle \bm{u}, \bm{v} \rangle = \overline{\langle \bm{v}, \bm{u} \rangle}$.
1. (Positive definiteness) $\langle \bm{v}, \bm{v} \rangle > 0$ if $\bm{v} \neq \bm{0}$.

Given an inner product, we can define a metric: for $\bm{p}, \bm{q} \in V$, define

$$
d(\bm{p}, \bm{q}) = \sqrt{\langle \bm{p}-\bm{q}, \bm{p}-\bm{q} \rangle}.
$$

A complete inner product space (i.e., a vector space with an inner product defined on it) is known as a *Hilbert space*.

The best known **example** of an inner product is the *dot product* on $\mathbb{R}^n$, defined as 

$$
\langle \bm{v}, \bm{w} \rangle = \bm{v} \cdot \bm{w} = \sum_{i=1}^n v_i w_i.
$$

The corresponding metric is of course the Euclidean one.




## Last section
We will try an itemized list.
- Apples
- Strawberries
- Oranges


And include a nice {numref}`table:areasecondmoment`.
```{table} Second moment of the area for some common cross-sectional shapes.
:name: table:areasecondmoment
| Shape | Second moment of the area |
| :--- | :--: |
| Massive cylinder, radius&nbsp;$R$ | $\frac{\pi}{4} R^4$ |
| Hollow cylinder, radius&nbsp;$R$, thickness&nbsp;$d$|  $\pi R^3 d$ |
| Massive square, side&nbsp;$a$ | $\frac{1}{12} a^4$ |
```

## References
```{bibliography}
:style: unsrt
:filter: docname in docnames
```

[^1]: The word 'map' is essentially synonymous to 'function' in the mathematical literature; there are books that restrict 'function' to functions of numbers, or 'map' to linear maps, and so on, but there isn't a universally accepted distinction.

[^2]: We'll use the Einstein summation convention: we implicitly assume any repeated index is summed over, unless explicitly stated otherwise.

[^3]: There is no easy way to remember the difference between the names, except perhaps that a covector has covariant components / basis. One very silly mnemonic I once encountered is that the *co*variant components have their index be*low* (same 'o' in 'co' and 'low'). It is so silly it is surely now also stuck in your head. Make of it what you will.

[^4]: A meta-surface in $n$-dimensional space is an $n-1$ dimensional object. In two dimensions, it's a line, in three dimensions, a surface, in four dimensions, a volume, and so on.

[^5]: The notation with a prime on the index is fairly standard, though some authors prefer using a bar over the index. You can only sum over an index if occurs either twice with or twice without a prime; to avoid confusion, it is best to not mix primed and unprimed versions of the same letter in an equation.

[^6]: The fact that the two transformations are each other's inverse, i.e., that $\Lambda^j_{i'} \Lambda^{i'}_k = \delta^j_k$, follows directly from the chain rule, as you can easily check for yourself by writing out the sum.

[^7]: The term 'contracting with the metric' is used for the operation 'multiplying with the metric and summing over the relevant indexes'. On the left-hand side of equation&nbsp;{eq}`metricderivativeChristoffel4`, we get $\Gamma^l_{ik} g_{lj} g^{jm} = \Gamma^l_{ik} \delta_l^m = \Gamma^m_{ik}$, isolating the Christoffel symbol. You can also 'contract' two indexes (always an upper and a lower one) of a single tensor or product of two tensors, 'contracting' then means that you sum over those indexes, see e.g. equation&nbsp;{eq}`defRiccitensor`.

[^8]: Note that while for every value of $j$ the components $\phi_{i;j}$ define a new one-form, we can also define a two-tensor with components $\phi_{i;j}$. To calculate the second derivative of $\phi$, we want the derivative with respect to $u^k$ for every value of $j$, so the easiest thing to do is to take the covariant derivative of the tensor with components $\phi_{i;j}$, hence the two Christoffel symbols in the first line of equation&nbsp;{eq}`oneformcovariantsecondderivative`.

[^9]: A surface can be embedded in an arbitrary space with dimension larger than two, but itself always has two dimensions. A hypersurface is a subspace with dimension $n-1$ embedded in a space with dimension $n$. A surface is thus a hypersurface in 3D.

