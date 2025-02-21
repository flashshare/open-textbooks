(ch:forces)=
# Conversion example: Forces

This example page is a conversion of chapter 2 of [Mechanics and Relativity](https://textbooks.open.tudelft.nl/textbooks/catalog/book/14), also published (with more exercises) in [Introduction to particle and continuum mechanics](https://interactivetextbooks.tudelft.nl/nb1140/index.html). Links to other chapters of that book appear here in red.

(sec:Newtonslaws)=
## Newton's laws of motion

As described in Chapter 1, classical mechanics is based on a set of axioms, which in turn are based on (repeated) physical observations. In order to formulate the first three axioms, we will need to first define three quantities: the (instantaneous) velocity, acceleration and momentum of a particle. If we denote the position of a particle as $\bm{x}(t)$, indicating a vector<sup>[^1]</sup> quantity with the dimension of length that depends on time, we define its velocity as the time derivative of the position:

$$
\bm{v}(t) = \dot{\bm{x}}(t) = \frac{\mathrm{d}\bm{x}(t)}{\mathrm{d}t}.
$$ (defv)

Note that we use an overdot to indicate a *time* derivative, we will use this convention throughout these notes. The acceleration is the time derivative of the velocity, and thus the second derivative of the position:

$$
\bm{a}(t) = \ddot{\bm{x}}(t) = \frac{\mathrm{d}\bm{v}(t)}{\mathrm{d}t} = \frac{\mathrm{d}^2 \bm{x}(t)}{\mathrm{d}t^2}.
$$ (defa)

Finally the *momentum* of a particle is its mass times its velocity:

$$
\bm{p}(t) = m \bm{v}(t) = m \dot{\bm{x}}(t).
$$ (defp)

We are now ready to give our next three axioms. You may have encountered them before; they are known as Newton's three laws of motion.

```{prf:axiom} Newton's first law of motion
As long as there is no external action, a particle's velocity will remain constant.
```


Note that the first law includes particles at rest, i.e., $\bm{v} = 0$. We will define the general 'external action' as a *force*, therefore a force is now anything that can change the velocity of a particle. The second law quantifies the force:

````{admonition} Isaac Newton (1642-1727)
:class: dropdown
**Isaac Newton** (1642-1727) was a British physicist, astronomer and mathematician, who is widely regarded as one of the most important scientists in history. Newton was a professor at Cambridge from 1667 till 1702, where he held the famous Lucasian chair in mathematics. Newton invented infinitesimal calculus to be able to express the laws of mechanics that now bear his name ({numref}`sec:Newtonslaws`) in mathematical form. He also gave a mathematical description of gravity (equation&nbsp;{eq}`FGrav`), from which he could derive Kepler's laws of planetary motion (<a href="https://interactivetextbooks.tudelft.nl/nb1140/content/generalplanarmotion.html#sec-keplerslaws">Section 6.4</a>). In addition to his work on mechanics, Newton made key contributions to optics and invented the reflection telescope, which uses a mirror rather than a lens to gather light. Having retired from his position in Cambridge, Newton spend most of the second half of his life in London, as warden and later master of the Royal mint, and president of the Royal society.
```{figure} images/portraits/Newton.jpg
---
width: 300
---
Portrait of Isaac Newton by Godfrey Kneller (1689)<sup>[^2]</sup>.
```
````



```{prf:axiom} Newton's second law of motion
If there is a net force acting on a particle, then its instantaneous change in momentum due to that force is equal to that force:

$$
\bm{F}(t) = \frac{\mathrm{d}\bm{p}(t)}{\mathrm{d}t}.
$$ (N2)

```


Now since $\bm{p} = m\bm{v}$ and $\bm{a} = \mathrm{d}\bm{v}/\mathrm{d}t$, if the mass is constant we can also write&nbsp;{eq}`N2` as $\bm{F} = m \bm{a}$, or

$$
\bm{F}(t) = m \ddot{\bm{x}}(t),
$$ (N2b)

which is the form in we will use most. Based on the second law, we see that a force has the physical dimension of a mass times a length divided by a time squared - since this is quite a lot to put in every time, we define the dimension of force as such: $F = MLT^{-2}$. Likewise, we define a unit, the Newton (N), as a kilogram times a meter per second squared: $\mathrm{N} = \mathrm{kg} \cdot \mathrm{m} / \mathrm{s}^2$. Therefore, in principle Newton's second law of motion can also be used to measure forces, though we will often use it the other way around, and calculate changes in momentum due to a known force.

Note how Newton's first law follows from the second: if the force is zero, there is no change in momentum, and thus (assuming constant mass) a constant velocity. Note also that although the second law gives us a quantification of the force, by itself it will not help us achieve much, as we at present have no idea what the force is (though you probably have some intuitive ideas from experience) - for that we will use the force laws of the next section. Before we go there, there is another important observation on the nature of forces in general.

```{prf:axiom} Newton's third law of motion
If a body exerts a force $\bm{F}_1$ on a second body, the second body exerts an equal but opposite force $\bm{F}_2$, on the first, i.e., the forces are equal in magnitude but opposite in direction:

$$
\bm{F}_1 = - \bm{F}_2.
$$ (N3)

```


(sec:forcelaws)=
## Force laws

Newton's second law of motion tells us what a force *does*: it causes a change in momentum of any particle it acts upon. It does not tell us where the force comes from, nor does it care - which is a very useful feature, as it means that the law applies to all forces. However, we do of course need to know what to put down for the force, so we need some rule to determine it independently. This is where the force laws come in.

````{admonition} Robert Hooke (1635-1703)
:class: dropdown
**Robert Hooke** (1635-1703) was a British all-round natural scientist and architect. He discovered the force law named after him in 1660, which he published first as an anagram: 'ceiiinosssttuv', so he could claim the discovery without actually revealing it (a fairly common practice at the time); he only provided the solution in 1678: 'ut tensio, sic vis' ('as the extension, so the force'). Hooke made many contributions to the development of microscopes, using them to reveal the structure of plants, coining the word cell for their basic units. Hooke was the curator of experiments of England's Royal Society for over 40 years, combining this position with a professorship in geometry and the job of surveyor of the city of London after the great fire of 1666. In the latter position he got a strong reputation for his hard work and great honesty. At the same time, he was frequently at odds with his contemporaries Isaac Newton and Christiaan Huygens; it is not unlikely that they all independently developed similar notions on, among others, the inverse-square law of gravity.
```{figure} images/portraits/HookeMicrographia.jpg
---
width: 300
---
Drawing of the cell structure of cork by Hooke, from his 1665 book Micrographia<sup>[^3]</sup>. No portraits of Hooke survive.
```
````



(sec:FHooke)=
### Springs: Hooke's law

One very familiar example of a force is the spring force: you need to exert a force on something to compress it, and (in accordance with Newton's third law), if you press on something you'll feel it push back on you. The simplest possible object that you can compress is an ideal spring, for which the force necessary to compress it scales linearly with the compression itself. This relation is known as **Hooke's law**:

$$
\bm{F}_s = - k \bm{x},
$$ (FHooke)

where $\bm{x}$ is now the displacement (from rest) and $k$ is the spring constant, measured in newtons per meter. The value of $k$ depends on the spring in question - stiffer springs having higher spring constants.

Hooke's law gives us another way to *measure* forces. We have already defined the unit of force using Newton's second law of motion, and we can use that to calibrate a spring, i.e., determine its spring constant, by determining the displacement due to a known force. Once we have $k$, we can simply measure forces by measuring displacements - this is exactly what a spring scale does. 

 

 
(sec:Fgrav)=
### Gravity: Newton's law of gravity

A second and probably even more familiar example is force due to gravity, at the local scale, i.e., around you, in the approximation that the Earth is flat. Anything that has mass attracts everything else that has mass, and since the Earth is very massive, it attracts all objects in the space around you, including yourself. Since the force of gravity is weak, you won't feel the pull of your book, but since the Earth is so massive, you do feel its pull. Therefore if you let go of something, it will be accelerated towards the Earth due to its attracting gravitational force. As demonstrated by Galilei (and some guys in spacesuits on a rock we call the moon<sup>[^4]</sup>), the acceleration of any object due to the force of gravity is the same, and thus the force exerted by the Earth on any object equals the mass of that object times this acceleration, which we call $\bm{g}$:

$$
\bm{F}_g = m \bm{g}.
$$ (Fg)

Because the Earth's mass is not exactly uniformly distributed, the magnitude of $\bm{g}$ varies slightly from place to place, but to good approximation equals $9.81\,\mathrm{m}/\mathrm{s}^2$. It always points down.

Although equation&nbsp;{eq}`Fg` for local gravity is handy, its range of application is limited to everyday objects at everyday altitudes - say up to a couple thousand kilograms and a couple kilometers above the surface of the Earth, which is tiny compared to Earth's mass and radius. For larger distances and bodies with larger mass - say the Earth-Moon, or Earth-Sun systems - we need something else, namely **Newton's law of gravitation** between two bodies with masses $m_1$ and $m_2$ and a distance $r$ apart:

$$
\bm{F}_\mathrm{G} = -G \frac{m_1 m_2}{r^2} \bm{\hat{r}},
$$ (FGrav)

where $\bm{\hat{r}}$ is the unit vector pointing along the line connecting the two masses, and the proportionality constant $G = 6.67 \cdot 10^{-11} \; \mathrm{N} \cdot \mathrm{m}^2 / \mathrm{kg}^2$ is known as the gravitational constant (or Newton's constant). The minus sign indicates that the force is attractive. Equation&nbsp;{eq}`FGrav` allows you to actually calculate the gravitational pull that your book exerts on you, and understand why you don't feel it. It also lets you calculate the value of $g$ - simply fill in the mass and radius of the Earth. If you wish to know the value of $g$ on any other celestial body, you can put in its particulars, and compare with Earth. You'll find you'd 'weigh' 3 times less on Mars and 6 times less on the Moon. Most of the time we can safely assume the Earth is flat and use&nbsp;{eq}`Fg`, but in particular for celestial mechanics and when considering satellites we'll need to use&nbsp;{eq}`FGrav`.

````{admonition} Galileo Galilei (1564-1642)
:class: dropdown
**Galileo Galilei** (1564-1642) was an Italian physicist and astronomer, who is widely regarded as one of the founding figures of modern science. Unlike classical philosophers, Galilei championed the use of experiments and observations to validate (or disprove) scientific theories, a practice that is now the cornerstone of the scientific method. He pioneered the use of the telescope (newly invented at the time) for astronomical observations, leading to his discovery of mountains on the moon an the four largest moons of Jupiter (now known as the Galilean moons in his honor). On the theoretical side, Galilei argued that Aristotle's argument that heavy objects fall faster than light ones is incorrect, and that the acceleration due to gravity is equal for all objects (equation&nbsp;{eq}`Fg`). Galilei also strongly advocated the heliocentric worldview introduced by Copernicus in 1543, as opposed to the widely-held geocentric view. Unfortunately, the Inquisition thought otherwise, leading to his conviction for heresy with a sentence of life-long house arrest in 1633, a position that was only recanted by the church in 1995.
```{figure} images/portraits/Galilei.jpg
---
width: 300
---
Portrait of Galileo Galilei by Justus Sustermans (1636)<sup>[^5]</sup>.
```
````
 
(sec:FCoulomb)=
### Electrostatics: Coulomb's law

Like two masses interact due to the gravitational force, two charged objects interact via Coulomb's force. Because charge has two possible signs, Coulomb's force can both be attractive (between opposite charges) and repulsive (between identical charges). Its mathematical form strongly resembles that of Newton's law of gravity:

$$
\bm{F}_\mathrm{C} = k_e \frac{q_1 q_2}{r^2} \bm{\hat{r}},
$$ (FCoulomb)

where $q_1$ and $q_2$ are the signed magnitudes of the charges, $r$ is again the distance between them, and $k_\mathrm{e} = 8.99 \cdot 10^9\;\mathrm{N} \cdot \mathrm{m}^2/\mathrm{C}^{2}$ is Coulomb's constant. For everyday length and force scales, Coulomb's force is much larger than the force of gravity.

(sec:frictiondrag)=
### Friction and drag

Why did it take the genius of Galilei and Newton to uncover Newton's first law of motion? Because everyday experience seems to contradict it: if you don't exert a force, you won't keep moving, but gradually slow down. You know of course why this is: there's *drag* and *friction* acting on a moving body, which is why it's much easier (though not necessarily handier) for a car to keep moving on ice than on a regular tarmac road (less friction on ice), and why walking through water is so much harder than walking through air (more drag in water). The *medium* in which you move can exert a drag force on you, and the *surface* over which you move exerts friction forces. These of course are the forces responsible for slowing you down when you stop exerting force yourself, so the first law doesn't apply, as there are forces acting.

For low speeds, the drag force typically scales linearly with the velocity of the moving object. Drag forces for objects moving through a (fluid) medium moreover depend on the properties of the medium (its viscosity $\eta$) and the cross-sectional area of the moving object. For a sphere of radius $R$ moving at velocity $\bm{v}$, the drag force is given by **Stokes' law**:

$$
\bm{F}_\mathrm{d} = -6 \pi \eta R \bm{v}.
$$ (FStokes)

The more general version for an object of arbitrary shape is $\bm{F}_d = \zeta \bm{v}$, where $\zeta$ is a proportionality constant. Stokes' law breaks down at high velocities, for which the drag force scales quadratically with the speed:

$$
F_\mathrm{d} = \frac12 \rho c_\mathrm{d} A v^2,
$$ (Fdraghighspeed)

where $\rho$ is the density of the fluid, $A$ the cross-sectional area of the object, $v$ it's speed, and $c_\mathrm{d}$ it's dimensionless drag coefficient, which depends on the object's shape and surface properties. Typical values for the drag coefficient are 1.0 for a cyclist, 1.2 for a running person, 0.48 for a Volkswagen Beetle, and 0.19 for a modern aerodynamic car. The direction of the drag force is still opposite that of the motion.

````{admonition} Charles-Augustin de Coulomb (1736-1806)
:class: dropdown
**Charles-Augustin de Coulomb** (1736-1806) was a French physicist and military engineer. For most of his working life, Coulomb served in the French army, for which he supervised many construction projects. As part of this job, Coulomb did research, first in mechanics (leading to his law of kinetic friction, equation&nbsp;{eq}`Coulombfriction`), and later in electricity and magnetism, for which he discovered that the force between charges (and those between magnetic poles) drops off quadratically with their distance (equation&nbsp;{eq}`FCoulomb`). Near the end of his life, Coulomb participated in setting up the SI system of units. 
```{figure} images/portraits/Coulomb.jpg
---
width: 300
---
Portrait of Charles de Coulomb<sup>[^6]</sup>.
```
````



Frictional forces are due to two surfaces sliding past each other. It should come as no surprise that the direction of the frictional force is opposite that of the motion, and its magnitude depends on the properties of the surfaces. Moreover, the magnitude of the frictional force also depends on how strongly the two surfaces are pushed against each other - i.e., on the forces they exert on each other, perpendicular to the surface. These forces are of course equal (by Newton's third law) and are called **normal** forces, because they are normal (that is, perpendicular) to the surface. If you stand on a box, gravity exerts a force on you pulling you down, which you 'transfer' to a force you exert on the top of the box, and causes an equal but opposite normal force exerted by the top of the box on your feet. If the box is tilted, the normal force is still perpendicular to the surface (it remains normal), but is no longer equal in magnitude to the force exerted on you by gravity. Instead, it will be equal to the component of the gravitational force along the direction perpendicular to the surface (see {numref}`fig:tableforcedecomposition`). We denote normal forces as $\bm{F}_n$. Now according to the **Coulomb friction law** (not to be confused with the Coulomb force between two charged particles), the magnitude of the frictional force between two surfaces satisfies

$$
F_f \leq \mu F_n.
$$ (Coulombfriction)

Here $\mu$ is the *coefficient of friction*, which of course depends on the two surfaces, but also on the question whether the two surfaces are moving with respect to each other or not. If they are not moving, i.e., the configuration is static, the appropriate coefficient is called the *coefficient of static friction* and denoted by $\mu_s$. The actual magnitude of the friction force will be such that it balances the other forces (more on that in {numref}`sec:multipleforces`). Equation&nbsp;{eq}`Coulombfriction` tells us that this is only possible if the required magnitude of the friction force is less than $\mu_s F_n$. When things start moving, the static friction coefficient is replaced by the *coefficient of kinetic friction* $\mu_k$, which is usually smaller than $\mu_s$; also in that case the inequality in equation&nbsp;{eq}`Coulombfriction` gets replaced by an equals sign, and we have $F_f = \mu_k F_n$.

```{figure} images/fallingobjects.png
:name: fig:fallingobjects
Dropping under the force of gravity. (a and b) A ball released from rest drops with a constant acceleration, resulting in a constantly increasing velocity. Images in (a) are taken every &nbsp;$0.05\;\mathrm{s}$; distances are multiples of $12\;\mathrm{mm}$. In (b), the trajectory of the ball resulting from repeated bounces is shown with intervals of $0.04\;\mathrm{s}$ [^7], CC BY-SA 3.0. (c) Paragliders need to balance the force of gravity and that of drag to stop accelerating and fall at a continuous speed (known as their terminal velocity) [^8], CC BY-SA 3.0.
```



(sec:eom)=
## Equations of motion

Now that we have set our axioms - Newton's laws of motion and the various force laws - we are ready to start combining them to get useful results, things that we did not put into the axioms in the first place but follow from them. The first thing we can do is write down *equations of motion*: an equation that describes the motion of a particle due to the action of a certain type of force. For example, suppose you take a rock of a certain mass&nbsp;$m$ and let go of it at some height&nbsp;$h$ above the ground, then what will happen? Once you've let go of the rock, there is only one force acting on the rock, namely Earth's gravity, and we are well within the regime where equation&nbsp;{eq}`Fg` applies, so we know the force. We also know that this net force will result in a change of momentum (equation&nbsp;{eq}`N2`), which, because the rock won't loose any mass in the process of falling, can be rewritten a&nbsp;{eq}`N2b`. By equating the forces we arrive at an equation of motion for the rock, which in this case is very simple:

$$
m \bm{g} = m \ddot{\bm{x}}.
$$ (freefalleom)

We immediately see that the mass of the rock doesn't matter (Galilei was right! - though of course he was in our set of axioms, because we arrived at them by assuming he was right...). Less trivially, equation&nbsp;{eq}`freefalleom` is a second-order differential equation for the motion of the rock, which means that in order to find the actual motion, we need two initial conditions - which in our present example are that the rock starts at height&nbsp;$h$ and zero velocity.

Equation&nbsp;{eq}`freefalleom` is essentially one-dimensional - all motion occurs along the vertical line. Solving it is therefore straightforward - you simply integrate over time twice. The general solution is:

$$
\bm{x}(t) = \bm{x}(0) + \bm{v}(0) t + \frac12 \bm{g} t^2,
$$ (generalfreefall)

which with our boundary conditions becomes

$$
\bm{x}(t) = (h - \frac12 g t^2) \bm{\hat{z}},
$$ (freefallspecific)

where $g$ is the magnitude of $\bm{g}$ (which points down, hence the minus sign). Of course equation&nbsp;{eq}`freefallspecific` breaks down when the rock hits the ground at $t = \sqrt{2h/g}$, which is easily understood because at that point gravity is no longer the only force acting on it.

We can also immediately write down the equation of motion for a mass on a spring (no gravity at present), in which the net force is given by Hooke's law. Equating that force to the net force in Newton's second law of motion gives:

$$
- k \bm{x}(t) = m \ddot{\bm{x}}(t).
$$ (springeom)

Of course, we find another second-order differential equation, so we again need the initial position and velocity to specify a solution. The general solution of&nbsp;{eq}`springeom` is a combination of sines and cosines, with a frequency $\omega = \sqrt{k/m}$ (as we already know from the dimensional analysis in <a href="https://interactivetextbooks.tudelft.nl/nb1140/content/mechanicsintroduction.html#sec-dimanalysis">Section 1.2</a>):

$$
\bm{x}(t) = \bm{x}(0) \cos(\omega t) + \frac{\bm{v}(0)}{\omega} \sin(\omega t).
$$ (harmonicoscillator)

We'll study this case in more detail in <a href="https://interactivetextbooks.tudelft.nl/nb1140/content/oscillations.html#sec-oscillation">Section 8.1</a>.

In general, the force in Newton's second law may depend on time and position, as well as on the first derivative of the position, i.e., the velocity. For the special case that it depends on only one of the three variables, we can write down the solution formally, in terms of an integral over the force. These formal solutions are given in {numref}`sec:eomsolutions`. To see how they work in practice, let's consider a slightly more involved problem, that of a stone falling with drag.

### Worked example: falling stone with drag
Suppose we have a spherical stone of radius $a$ that you drop from a height $h$ at $t = 0$. At what time, and with which velocity, will the stone hit the ground? We already solved this problem in the simple case without drag above, but now let's include drag. There are then two forces acting on the stone: gravity (pointing down) with magnitude $mg$, and drag (pointing in the direction opposite the motion, in this case up) with magnitude $6 \pi \eta a v = b v$, as given by Stokes' law (equation&nbsp;{eq}`FStokes`). Our equation of motion is now given by (with $x$ as the height of the particle, and the downward direction as positive):

$$
m \ddot{x} = -b \dot{x} + m g.
$$ (eomfallingstonewithdrag)

We see that our force does not depend on time or position, but only on velocity - so we have case 3 of {numref}`sec:eomsolutions`. We could invoke either equation&nbsp;{eq}`EOMvelocitysolutiontime` or&nbsp;{eq}`EOMvelocitysolutionspace` to write down a formal solution, but there is an easier way, which will allow us to evaluate the relevant integrals without difficulty. Since our equation of motion is linear, we know that the sum of two solutions is again a solution. One of the terms on the right hand side of equation&nbsp;{eq}`eomfallingstonewithdrag` is constant, which means that our equation is not homogeneous (we can rewrite it to $m \ddot{x} + b \dot{x} = m g$ to see this), so a useful thing to do is to split our solution in a homogeneous and a particular part. Rewriting our equation in terms of $v = \dot{x}$ instead of $x$, we get $m \dot{v} + b v = m g$, from which we can immediately get a particular solution: $v_\mathrm{p} = m g / b$, as the time derivative of this constant $v_\mathrm{p}$ vanishes. Subtracting $v_\mathrm{p}$, we are left with a homogeneous equation: $m \dot{v}_\mathrm{h} + b v_\mathrm{h}$, which we now solve by separation of variables. First we write $\dot{v}_\mathrm{h} = \mathrm{d}v_\mathrm{h} / \mathrm{d}t$, then re-arrange so that all factors containing $v_\mathrm{h}$ are on one side and all factors containing $t$ are on the other, which gives $-(m/b) (1/v_\mathrm{h}) \mathrm{d}v_\mathrm{h} = \mathrm{d}t$. We can now integrate to get:

$$
-\frac{m}{b} \int_{v_0}^v \frac{1}{v'} \mathrm{d}v' = -\frac{m}{b} \log\left(\frac{v}{v_0}\right) = t-t_0,
$$ (fallingstonehomsol1)

which is an example of equation&nbsp;{eq}`EOMvelocitysolutiontime`. After rearranging and setting $t_0 = 0$:

$$
v_\mathrm{h}(t) = v_0 \exp\left(-\frac{b}{m}t\right).
$$ (fallingstonehomsol2)

Note that this homogeneous solution fits our intuition: if there is no extra force on the particle, the drag force will slow it down exponentially. Also note that we didn't set $v_0 = 0$, as the homogeneous solution does not equal the total solution. Instead $v_0$ is an integration constant that we'll need to set once we've written down the full solution, which is:

$$
v(t) = v_\mathrm{h}(t) + v_\mathrm{p}(t) = v_0 \exp\left(-\frac{b}{m}t\right) + \frac{mg}{b}.
$$ (fallingstonefullsol1)

Now setting $v(0) = 0$ gives $v_0 = -mg/b$, so

$$
v(t) = \frac{mg}{b} \left[ 1 - \exp\left(-\frac{b}{m}t\right)\right].
$$ (fallingstonefullsol2)

To get $x(t)$, we simply integrate $v(t)$ over time, to get:

$$
x(t) = \frac{mg}{b}\left[ t + \frac{m}{b} \exp\left(-\frac{b}{m}t\right) \right].
$$ (fallingstoneposition)

We can find when the stone hits the ground by setting $x(t) = h$ and solving for $t$; we can find how fast it is going at that point by substituting that value of $t$ back into $v(t)$.

(sec:multipleforces)=
## Multiple forces

In the examples in {numref}`sec:eom` there was only a single force acting on the particle of interest. Usually there will be multiple forces acting at the same time, not necessarily pulling in the same direction. This is where vectors come into play.

Suppose you put a book on a table. The Earth's gravity pulls it down with a force of magnitude $F_g$. Consequently the book exerts a normal force down on the table with the same magnitude, and the table reciprocates with an identical but oppositely directed normal force of magnitude $F_n = F_g$. Now suppose you push against the book from the side with a force of magnitude $F$. As we've seen in {numref}`sec:forcelaws`, there will then be a friction force between the book and the table in the opposite direction, which, as long as it doesn't exceed $\mu_s F_n$, equals the force you push with. However, once $F$ is larger than $\mu_s F_n$, there will be a *net force* acting on the book. It is the net force that we substitute into Newton's second law, and from which the book will get a net acceleration.

In the situation described above, things are still simple - you get the net force by subtracting the kinetic friction $F_f = \mu_f F_n$ from the force $F$ you exert on the book, because these are horizontal and thus perpendicular to the vertical normal and gravitational forces. But what happens if you lift the table on one end, so that it becomes slanted? To help organize our thoughts, we'll draw a *free body diagram*, shown in {numref}`fig:tableforcedecomposition`. Gravity still acts downward, and the mass of the book stays the same, so $\bm{F}_g$ doesn't change. However, the orientation of the contact plane between the book and table does change, so the normal force (remember, normal to the surface) changes as well. Its direction will remain perpendicular to the surface, and as long as you don't push on the book (or push along the surface only), the only other force having a component perpendicular to the surface is gravity, so the magnitude of the normal force better be equal to that (or the book would either spontaneously start to float, or fall through the table). You can find this component by decomposing the gravitational force along the directions perpendicular and parallel to the slanted surface. The remaining component of the gravitational force points downward along the surface of the table, and is comparable to the force you were exerting on the book in the flat case. Up to some point it is balanced by a static frictional force, but once it gets too large (because the slant angle of the table gets too large), friction reaches its maximum and gravity results in a net force on the book, which will start to slide down (as you no doubt guessed already).

```{figure} images/coordinates.svg
:name: fig:tableforcedecomposition
Free body diagram of the forces acting on a book on a slanted table. Gravity always points down, normal forces always perpendicular to the surface, and frictional forces always parallel to the surface. The force of gravity can be decomposed in directions perpendicular and parallel to the surface as well.
```


(sec:statics)=
## Statics

When multiple forces act on a body, the (vector) sum of those forces gives the *net force*, which is the force we substitute in Newton's second law of motion to get the equation of motion of the body. If all forces sum up to zero, there will be no acceleration, and the body retains whatever velocity it had before. *Statics* is the study of objects that are neither currently moving nor experiencing a net force, and thus remain stationary. You might expect that this study is easier than the dynamical case when bodies do experience a net force, but that just depends on context. Imagine, for example, a jar filled with marbles: they aren't moving, but the forces acting on the marbles are certainly not zero, and also not uniformly distributed.

Even if there is no net force, there is no guarantee that an object will exhibit no motion: if the forces are distributed unevenly along an extended object, it may start to rotate. Rotations always happen around a stationary point, known as the *pivot*. Only a force that has a component perpendicular to the line connecting its point of action to the pivot (the arm) can make an object rotate. The corresponding *angular acceleration* due to the force depends on both the magnitude of that perpendicular component and the length of the arm, and is known as the *moment of the force* or the *torque*&nbsp;$\bm{\tau}$. The magnitude of the torque is therefore given by $F r \sin\theta$, where $F$ is the magnitude of the force, $r$ the length of the arm, and $\theta$ the angle between the force and the arm. If we write the arm as a vector&nbsp;$\bm{r}$ pointing from the pivot to the point where the force acts, we find that the magnitude of the torque equals the cross product of $\bm{r}$ and $\bm{F}$:

$$
\bm{\tau} = \bm{r} \times \bm{F}.
$$ (deftorque)

The direction of rotation can be found by the right-hand rule from the direction of the torque: if the thumb of your right hand points along the direction of $\bm{\tau}$, then the direction in which your fingers curve will be the direction in which the object rotates due to the action of the corresponding force&nbsp;$\bm{F}$.

We will study rotations in detail in <a href="https://interactivetextbooks.tudelft.nl/nb1140/content/rotationalmotion.html#ch-rotation">Section 5</a>. For now, we're interested in the case that there is no motion, neither linear nor rotational, which means that the forces and torques acting on our object must satisfy the *stability condition*: for an extended object to be stationary, both the sum of the forces and the sum of the torques acting on it must be zero.

````{prf:example} Suspended sign
:label: sec:examplesuspendedsign
:class: example
A sign of mass&nbsp;$M$ hangs suspended from a rod of mass&nbsp;$m$ and length&nbsp;$L$ in a symmetric way and such that the centers of mass of the sign and rod align nicely ({numref}`fig:suspendedsign`a). One end of the rod is anchored to a wall directly, while the other is supported by a wire with negligible mass that is attached to the same wall a distance&nbsp;$h$ above the anchor. (a) If the maximum tension the wire can support is&nbsp;$T$, find the minimum value of&nbsp;$h$. (b) For the case that the tension in the wire equals the maximum tension, find the force (magnitude and direction) exerted by the anchor on the rod.
```{figure} images/suspendedsign.svg
:name: fig:suspendedsign
A suspended sign (example of a calculation in statics). (a) Problem setting. (b) Free-body diagram.
```
---
**Solution**
1. We first draw a free-body diagram, {numref}`fig:suspendedsign`b. Force balance on the sign tells us that the tensions in the two lower wires add up to the gravitational force on the sign. The rod is stationary, so we know that the sum of the torques on it must vanish. To get torques, we first need a pivot; we pick the point where the rod is anchored to the wall. We then have three forces contributing a clockwise torque, and one contributing a counterclockwise torque. We're not told exactly where the wires are attached to the rod, but we are told that the configuration is symmetric and that the center of mass of the sign aligns with that of the rod. Let the first wire be a distance $\alpha L$ from the wall, and the second a distance $(1-\alpha)L$. The total (clockwise) torque due to the gravitational force on the sign and rod is then given by:
```{math}
\tau_\mathrm{z} = \frac12 m g L + \frac12 M g \alpha L + \frac12 M g (1-\alpha) L = \frac12 (m+M)gL.
```
The counterclockwise torque comes from the tension in the wire, and is given by 
```{math}
\tau_\mathrm{wire} = F_\mathrm{T} \sin\theta L = F_\mathrm{T} (h/\sqrt{h^2+L^2}) L.
```
Equating the two torques allows us to solve for&nbsp;$h$ as a function of $F_\mathrm{T}$, as requested, which gives:
```{math}
h^2 = \left(\frac12 \frac{(m+M)g}{F_\mathrm{T}} \right)^2 (h^2 + L^2) \quad \rightarrow \quad h = \frac{(m+M)gL}{\sqrt{4 F_\mathrm{T}^2 - (m+M)^2 g^2}}.
```
We find the minimum value of $h$ by substituting $F_\mathrm{T} = T_\mathrm{max}$.
1. As the rod is stationary, all forces on it must cancel. In the horizontal direction, we have the horizontal component of the tension, $T_\mathrm{max} \cos\theta$ to the left, which must equal the horizontal component of the force exerted by the wall, $F_\mathrm{w} \cos\phi$. In the vertical direction, we have the gravitational force and the two forces from the wires on which the sign hangs in the downward direction, and the vertical component of the tension in the wire in the upward direction, the sum of which must equal the vertical component of the force exerted by the wall (which may point either up or down). We thus have
```{math}
\begin{align*}
F_\mathrm{w} \cos\phi &= T_\mathrm{max} \cos\theta, \\
F_\mathrm{w} \sin\phi &= (m+M)g + T_\mathrm{max} \sin\theta,
\end{align*}
```
where $\tan\theta = h/L$ and $h$ is given in the answer to (a). We find that
```{math}
\begin{align*}
F_\mathrm{w}^2 &= T_\mathrm{max}^2 + 2 (m+M)g T_\mathrm{max} \sin\theta + (m+M)^2 g^2, \\
\tan \phi &= \frac{T_\mathrm{max} \cos\theta}{(m+M)g + T_\mathrm{max} \sin\theta}.
\end{align*}
```
Note that the above expressions give the complete answer (magnitude and direction). We could eliminate $h$ and $\theta$, but that'd just be algebra, leading to more complicated expressions, and not very useful in itself. If we'd been asked to calculate the height or force for any specific values of $M$, $m$, and $L$, we could get the answers easily by substituting the numbers in the expressions given here.
````

(sec:eomsolutions)=
## Solving the equations of motion in three special cases*

In {numref}`sec:eom` we saw some examples of equations of motion originating from Newton's second law of motion. For the quite common case that the mass of our object of interest is constant, its trajectory will be given as the solution of a second-order ordinary differential equation, with time as our variable. In general, the force in Newton's second law may depend on time and position, as well as on the first derivative of the position, i.e., the velocity. In one dimension, we thus have

$$
m \ddot{x} = F(x, \dot{x}, t).
$$ (generalEOM)

Equation&nbsp;{eq}`generalEOM` can be hard to solve for complicated functions&nbsp;$F$. However, in each of the special cases that the force only depends on one of the three variables, we can write down a general solution - albeit as an integral over the force, which we may or may not be able to calculate explicitly.

### Case 1: $F = F(t)$
If the force only depends on time, we can solve equation&nbsp;{eq}`generalEOM` by direct integration. Using that $v = \dot{x}$, we have $m \dot{v} = F(t)$, which we integrate to find

$$
\int_{t_0}^t F(t') \mathrm{d}t' = m \int_{v_0}^v \mathrm{d}v' = m [v(t) - v_0],
$$ (EOMtimesolution)

where at the initial time $t=t_0$ the object has velocity $v=v_0$. We can now find the position by integrating the velocity:

$$
x(t) = \int_{t_0}^t v(t') \mathrm{d}t'.
$$ (positionvelocityintegral)


### Case 2: $F = F(x)$
If the force depends only on the position in space (as is the case for the harmonic oscillator), we cannot integrate over time, as to do so we would already need to know $x(t)$. Instead, we invoke the chain rule to rewrite our differential equation as an equation in which the position is our variable. We have:

$$
a = \frac{\mathrm{d}v}{\mathrm{d}t} = \frac{\mathrm{d}v}{\mathrm{d}x} \frac{\mathrm{d}x}{\mathrm{d}t} = v \frac{\mathrm{d}v}{\mathrm{d}x},
$$ (accelerationchainrule)

and so our equation of motion becomes

$$
m v \frac{\mathrm{d}v}{\mathrm{d}x} = F(x),
$$ (EOMspace)

which we again solve by direct integration:

$$
\int_{x_0}^x F(x') \mathrm{d}x' = m \int_{v_0}^v v' \mathrm{d}v' = \frac{m}{2} [v^2(x) - v_0^2].
$$ (EOMspacesolution)

To get $x(t)$, we use the relation that $\mathrm{d}x/\mathrm{d}t = v(x)$. Separation of variables gives $\mathrm{d}x / v(x) = \mathrm{d}t$, which we can integrate to get

$$
t-t_0 = \int_{x_0}^x \frac{1}{v(x')} \mathrm{d}x',
$$ (implicitposition)

which gives us $t(x)$. In principle we can invert this expression to give us $x(t)$, although in practice this may not be easy. <!--We could use the method in this case to solve the equation of motion for the harmonic oscillator, but there is an easier way, which we'll use in {numref}`ch:oscillations`.-->

### Case 3: $F = F(v)$
If the force depends only on the velocity, there are two ways we can proceed. We can write the equation of motion as $m \mathrm{d}v / \mathrm{d} t = F(v)$ and use separation of variables to get:

$$
t-t_0 = m \int_{v_0}^v \frac{1}{F(v')} \mathrm{d}v',
$$ (EOMvelocitysolutiontime)

from which we can get $v(t)$ after inverting, and $x(t)$ after integrating $v(t)$ as in equation&nbsp;{eq}`positionvelocityintegral`. Alternatively, we could again rewrite our equation of motion as an equation in space instead of time, and arrive at:

$$
x - x_0 = m \int_{v_0}^v \frac{v'}{F(v')} \mathrm{d}v'.
$$ (EOMvelocitysolutionspace)

From equation&nbsp;{eq}`EOMvelocitysolutionspace` we can get $v(x)$ by inverting, and $x(t)$ from equation&nbsp;{eq}`implicitposition`. Note that equation&nbsp;{eq}`EOMvelocitysolutionspace` does not give us $x(t)$ directly, as $x$ is the variable in that equation.

````{prf:example} velocity of the harmonic oscillator
:label: sec:exampleharmonicoscillatorvelocity
:class: example

It may seem that what we've done so far in this section has hardly helped matters: the 'solutions' we found contain integrals and often need to be inverted to get our desired function $x(t)$ (or, depending on the problem we're studying, $v(t)$ or $v(x)$). To show you how these solutions may be useful, let's consider a specific example: a harmonic oscillator, consisting of a mass on a Hookean spring, with $F = F(x) = -k x$. We already wrote down the equation of motion&nbsp;{eq}`springeom` and its general solution&nbsp;{eq}`harmonicoscillator`. The general solution can be found through the substitution of exponentials, as we'll do in <a href="https://interactivetextbooks.tudelft.nl/nb1140/content/oscillations.html#sec-oscillation">Section 8.1</a>. However, we can also learn something useful from writing the equation of motion in the form&nbsp;{eq}`EOMspace`. Its solution, formally given by equation&nbsp;{eq}`EOMspacesolution`, can be calculated explicitly for our force as
```{math}
:label: EOMharmoscsolution
\frac{m}{2} \left[v^2(x) - v_0^2\right] = \int_{x_0}^x (-k x') \mathrm{d}x' = - \frac{k}{2} \left[x^2 - x_0^2\right],
```
which gives
```{math}
:label: harmoscvelocity
v(x) = \sqrt{v_0^2 - \frac{k}{m} \left(x^2 - x_0^2 \right)}
```
for $v(x)$. Although $x(t)$ and $v(t)$ are more easily obtained from the solution given in equation&nbsp;{eq}`harmonicoscillator`, that solution will not give you $v(x)$, and deriving it is tricky. Here we get it almost for free. Moreover, as you have probably noted, equation&nbsp;{eq}`EOMharmoscsolution` relates the kinetic to the potential energy of the harmonic oscillator - a special case of conservation of energy, which we'll discuss in the next chapter.
````





[^1]: Appendix 1 lists some basic properties of vectors that you may find useful.

[^2]: Portrait of Isaac Newton by Godfrey Kneller, painted in 1689. Picture is a faithful reproduction of a two dimensional public domain work, retrieved from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:GodfreyKneller-IsaacNewton-1689.jpg).

[^3]: Drawing by Robert Hooke of the cell structure of cork from two different angles, as published in his 1665 book Micrographia. Picture is a faithful reproduction of a two dimensional public domain work, retrieved from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:RobertHookeMicrographia1665.jpg).

[^4]: To be precise, astronaut David Scott of the Apollo 15 mission in 1971, who dropped both a hammer and a feather and saw them fall at exactly the same rate, as shown in this [NASA movie](https://moon.nasa.gov/resources/331/the-apollo-15-hammer-feather-drop/).

[^5]: Portrait of Galileo Galilei by Justus Sustermans, painted in 1636, currently located at the National Maritime Museum in London, UK. Picture is a faithful reproduction of a two dimensional public domain work, retrieved from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Justus_Sustermans_-_Portrait_of_Galileo_Galilei,_1636.jpg).

[^6]: Portrait of Charles de Coulomb. Picture is a faithful reproduction of a two dimensional public domain work, retrieved from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Charles_de_coulomb.jpg).

[^7]: Images by Michael Maggs, [Wikimedia commons, falling ball](https://commons.wikimedia.org/wiki/File:Falling_ball.jpg) and [Wikimedia commons, bouncing ball](https://commons.wikimedia.org/wiki/File:Bouncing_ball_strobe_edit.jpg), CC BY-SA 3.0.

[^8]: Image by Amber Turner, [Unsplash](https://unsplash.com/photos/vqj83ATYeoI), public domain.

[^9]: Image by GSenkow, [Wikimedia commons](https://commons.wikimedia.org/w/index.php?curid=22239204), CC BY-SA 3.0.


## Problems
```{exercise} Terminal velocity
:class: dropdown
The *terminal velocity* is the maximum (constant) velocity a dropping object reaches. In this problem, we use equation&nbsp;{eq}`Fdraghighspeed` for the drag force.
1. Use dimensional analysis to relate the terminal velocity of a falling object to the various relevant parameters.
1. Estimate the terminal velocity of a paraglider ({numref}`fig:fallingobjects`c).
1. Use the concept of terminal velocity to predict whether a mouse (without parachute) is likely to survive a fall from a high tower.
```

```{exercise} Sticky rice
:class: dropdown
When you cook rice, some of the dry grains always stick to the measuring cup. A common way to get them out is to turn the measuring cup upside-down and hit the bottom (now on top) with your hand so that the grains come off.
1. Explain why static friction is irrelevant here.
1. Explain why gravity is negligible.
1. Explain why hitting the cup works, and why its success depends on hitting the cup hard enough.
```

```{exercise} Maximum area trajectory
:class: dropdown
A ball is thrown at speed $v$ from zero height on level ground. We want to find the angle&nbsp;$\theta$ at which it should be thrown so that the area under the trajectory is maximized.
1. Sketch of the trajectory of the ball.
1. Use dimensional analysis to relate the area to the initial speed&nbsp;$v$ and the gravitational acceleration&nbsp;$g$.
1. Write down the $x$ and $y$ coordinates of the ball as a function of time.
1. Find the total time the ball is in the air.
1. The area under the trajectory is given by $A = \int y \mathrm{d}x$. Make a variable transformation to express this integral as an integration over time.
1. Evaluate the integral. Your answer should be a function of the initial speed&nbsp;$v$ and angle&nbsp;$\theta$.
1. From your answer at (f), find the angle that maximizes the area, and the value of that maximum area. Check that your answer is consistent with your answer at (b).
```

```{exercise} Double spring
:class: dropdown
If a mass $m$ is attached to a given spring, its period of oscillation is $T$. If two such springs are connected end to end, and the same mass m is attached, find the new period $T'$, in terms of the old period $T$.
```

```{exercise} Two blocks
:class: dropdown
Two blocks, of mass $m$ and $2m$, are connected by a massless string and slide down an inclined plane at angle&nbsp;$\theta$. The coefficient of kinetic friction between the lighter block and the plane is&nbsp;$\mu$, and that between the heavier block and the plane is&nbsp;$2\mu$. The lighter block leads.
1. Find the magnitude of the acceleration of the blocks.
1. Find the tension in the taut string.
```

```{exercise} Decelerating boat
:class: dropdown
A 1000 kg boat is traveling at 100 km/h when its engine is shut off. The magnitude $F_\mathrm{d}$ of the drag force between the boat and the water is proportional to the speed $v$ of the boat, with a drag coefficient $\zeta = 70\;\mathrm{N}\cdot\mathrm{s}/\mathrm{m}$. Find the time it takes the boat to slow to 45 km/h.
```

```{exercise} Attractive forces
:class: dropdown
Two particles on a line are mutually attracted by a force $F = - a r$, where $a$ is a constant and $r$ the distance of separation. At time $t = 0$, particle A of mass $m$ is located at the origin, and particle B of mass $m/4$ is located at $r = 5.0\;\mathrm{cm}$.
1. If the particles are at rest at $t = 0$, at what value of $r$ do they collide?
1. What is the relative velocity of the two particles at the moment the collision occurs?
```

````{exercise} Drag racing
:class: dropdown
In drag racing, specially designed cars maximize the friction with the road to achieve maximum acceleration. Consider a drag racer (or 'dragster') as shown in {numref}`fig:dragster`, for which the center of mass is close to the rear wheels.
```{figure} images/dragracer_small.jpg
:name: fig:dragster
:width: 300
A drag racer or dragster&nbsp;[^9], CC BY-SA 3.0.
```

1. Draw a free-body diagram of the dragster in side view. Draw the wheels as circles, and approximate the shape of the dragster body as a triangle with a horizontal line between the wheels, a vertical line going up from the rear axis, and a diagonal line connecting the top to the front wheels. NB: consider carefully the direction of the friction force!
1. On which of the wheels is the frictional force the largest?
1. The frictional force is maximized if the wheels just don't slip (because, as usual, the coefficient of kinetic friction is smaller than that of static friction). Find the maximal possible frictional force on the rear wheels.
1. Find the maximal possible acceleration of the dragster.
1. For a coefficient of (static) friction of 1.0 (a fairly realistic value for rubber and concrete) and a track of 500&nbsp;m, find the maximal velocity a drag racer can achieve at the end of the track when starting from rest.
````
