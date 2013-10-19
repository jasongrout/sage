.. role:: latex(raw)
   :format: latex

.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN
.. |ellipsis| unicode:: U+02026 .. HORIZONTAL ELLIPSIS
.. |Latex| replace:: :latex:`\LaTeX{}`


.. _linear_programming:

**************
Linear Algebra
**************


This tutorial on linear algebra is licensed under the Creative Commons Attribution 3.0
United States License (see
http://creativecommons.org/licenses/by/3.0/us/deed.en_US for a copy of
the license).  You are free to copy, distribute, transmit, and adapt this
copyrighted work, including for commercial purposes, but only if you
give credit as follows.  The authors are Robert Beezer, Robert
Bradshaw, Jason Grout, and William Stein. This is a version of Chapter
91 from *The Handbook of Linear Algebra, 2nd edition*, copyright
|copy| Taylor and Francis Group, LLC.

.. An updated and expanded version of this chapter is available in the
   Sage documentation as a thematic tutorial on linear algebra.

Introduction
============

Sage is generally recognized as the leading comprehensive open source
mathematics software system.  Development began in 2005 by William
Stein and progressed rapidly due to the incorporation of many mature
open source packages for various areas of mathematics. The main
website for Sage is http://sagemath.org.  Free downloads of Sage, free
public servers, and many other resources are located at the website.

Sage is distributed with an open-source license (GPL version 3), which
provides several advantages over commercial offerings.

-  There is no cost to obtain or upgrade Sage.  Collaborators
   and students have a platform that does not depend on institutional
   licenses and remains accessible in the future.

-  *All* source code can be freely examined, modified, and
   redistributed.  Algorithms can be traced and examined, bugs can be
   located, and improvements and bugfixes can be made and distributed
   freely.  Often, bugs and improvements are made by experts in the
   field and frequent updates make these available rapidly.

-  Every copy includes the web server software to run Sage
   as a multi-user server, so workgroups and educational institutions
   can provide computational services over the internet at no additional cost.

-  Many routines in Sage leverage highly specialized packages
   included in Sage that are written and vetted by experts.
   Many of these packages have been developed over decades and
   are reliable and fast.

Users may interact with Sage via a command-line interface or via a web
interface known as the Sage Notebook.  The Sage Notebook is a web
application that runs in a web browser and serves as a front end for a
Sage server, which may run on a remote computer or on the local
computer.  The online notebook is the easiest way to begin working
with Sage since it works in any modern web browser (including on
mobile devices) and requires no extra installation.  A free public
Sage server is accessible from http://sagemath.org.

Sage understands mathematical objects like rings, fields, vector
spaces, matrices over different fields, etc.  Each vector and matrix
knows the ring in which its entries live, such as integers, rationals,
elements of a finite field, floating-point double-precision reals (or
complexes), high-precision reals (or complexes), or more exotic
objects such as multivariate polynomials or algebraic numbers.
Different routines or libraries will be transparently used depending
on the type of entries.  Sage includes many linear algebra
libraries which it uses to do computations, including LAPACK, LinBox,
IML, M4RI, etc.  Support for floating-point double-precision matrices
is provided by the included SciPy and NumPy scientific computation
packages, which ultimately rely on LAPACK and other standard packages.


.. ::
   For example, many computations for matrices
   of rational numbers are internally converted to equivalent
   computations for matrices of integers, which are then delegated to the
   Integer Matrix Library (IML).

Extensive help and additional resources can be obtained freely through
the Sage website at http://sagemath.org.  Context-sensitive help can
be easily obtained by evaluating a function or method name followed by
a question mark.  Functions and methods can be discovered using
tab-completion (see below).

In this chapter, example lines that start with ``sage:`` are input
lines, and everything on an input line following the ``sage:`` prompt
should be typed into Sage.  Evaluate input by pressing the enter key
(in the command line) or by clicking evaluate or pressing shift-enter
(in the notebook).  In the examples below, the Sage output immediately
follows the input on separate lines without ``sage:`` prompts.  An
ellipsis ``...`` indicates output that has been deleted for brevity.

Working with Sage
=================

.. ::

   This section contains both general and specific advice on using
   Sage for linear algebra.  On a first reading, it can be safely
   skimmed or skipped.

Facts
-----

#. You can use Sage in a web browser by accessing the Sage Notebook,
   which can be served from your own computer or a remote computer
   (such as a public server accessible from http://sagemath.org).  You
   can also run Sage in command-line mode on your own computer
   (``exit`` or ``quit`` will stop Sage).  If you are running Sage in
   command-line mode, you can start the online notebook server for
   only your own computer by typing ``notebook()`` at the ``sage:``
   prompt; stop the notebook with Control-C.  You can also download an
   Apple OS X Sage application that lets you start a local Sage
   notebook or command-line environment by double-clicking.

#. Users use the general-purpose, popular, and easy-to-learn Python
   programming language to interact with Sage.  Python is used in many
   scientific and other disciplines, so learning Python has many
   applications beyond Sage.  Sage also includes many libraries that
   are compiled C, C++, Fortran, or other languages, but the "glue"
   tying everything together, as well as a substantial mathematical
   library, is also implemented in Python.

#. Mathematical objects in Sage belong to "parents," an idea pioneered
   by the Magma computer algebra system.  Allowable operations,
   available methods, implemented algorithms and documentation are all
   sensitive to an object's parent.

   .. ::

   ..  sage: (5).parent()
   ..  Integer Ring
   ..  sage: (3/2).parent()
   ..  Rational Field
   ..  sage: v = vector([2, sin(4.3), -6]); v.parent()
   ..  Vector space of dimension 3 over Real Field with 53 bits of precision
   ..  sage: a,b,c = var('a b c')
   ..  sage: A = matrix([[a,b], [b,c]]); A.parent()
   ..  Full MatrixSpace of 2 by 2 dense matrices over Symbolic Ring

#. What Sage prints (the text representation), and what Sage knows,
   are two different things, and often what is printed is not the full
   story.  The ``parent()`` method is helpful in understanding an
   object. 

   .. ::

   .. sage: a = 5; a
   .. 5
   .. sage: b = 5/1; b
   .. 5
   .. sage: a.parent()
   .. Integer Ring
   .. sage: b.parent()
   .. Rational Field

   .. It's even possible for the result itself depends on the parent.  For example,
      a polynomial by default factors over its basering::

       sage: f = QQ['x'](x^4 - 4); f
       x^4 - 4
       sage: f.parent()
       Univariate Polynomial Ring in x over Rational Field
       sage: f.factor()
       (x^2 - 2) * (x^2 + 2)
       sage: g = f.change_ring(RR); g.parent()
       Univariate Polynomial Ring in x over Real Field with 53 bits of precision
       sage: g.factor()
       (x - 1.41421356237310) * (x + 1.41421356237310) * (x^2 + 2.00000000000000)
       sage: h = f.change_ring(CC); h.factor()
       (x - 1.41421356237310) * (x - 1.41421356237310*I) * (x + 1.41421356237310*I) * (x + 1.41421356237310)
       sage: f.change_ring(QQ[sqrt(2),I]).factor()
       (x + I*sqrt2) * (x - I*sqrt2) * (x + sqrt2) * (x - sqrt2)

#. Much of Sage is object-oriented, and vectors, matrices, and vector
   spaces are considered objects.  If an object is assigned a name,
   then typing the name, then a period, and then a method name
   followed by parentheses will have Sage call the method to return a
   result.  For example, if ``A`` is a matrix, then ``A.det()`` will
   calculate the determinant of ``A`` using the
   :meth:`det` method.  Typing the name, appending a period, and then
   pressing the ``Tab`` key will bring up a full list of the methods
   available for that object (e.g., if ``A`` is a matrix, try
   ``A.<tab>``, or ``A.a<tab>`` to see all methods beginning with an
   "a").  Many computations are also available as top-level commands
   (you can use either ``det(A)`` or ``A.det()`` to calculate the
   determinant).  Appending a question mark to a command or method
   name, such as ``A.det?``, and evaluating gives the documentation
   for the function or method (and the method documentation is context
   sensitive, depending on the object).  Appending two question marks
   will display the source code for the command, method, or object.

   Documentation of commands and methods contain short informative
   examples that are tested for accuracy.  The possible methods and
   documentation for vectors and matrices may depend on greatly on the
   types of entries it contains.  A quick way to learn about the
   capabilities of Sage is to build the revelant object (for example,
   a matrix) and explore methods and their documentation using tab
   completion and question marks.

#. Sage implements a variety of rings and fields that can be used as
   entries of vectors or matrices.  Some common fields are listed
   below.  The ``RDF``, ``CDF``, ``RR``, and ``CC`` fields have 53-bit
   precision (see :ref:`Numerical Linear Algebra`). 
   ``RealField``, ``ComplexField``, ``RealIntervalField``, and
   ``ComplexIntervalField`` support arbitrary precision.  All other
   fields listed are exact with no round off error.

   .. csv-table::
      :header: "Field", "Name", "Notes"
      :delim: &

      Symbolic   & ``SR`` & used with symbolic variables
      Rationals  & ``QQ`` & 
      Mod `p`    & ``Integers(p)`` or ``GF(p)`` &  `p` prime, `p=2` highly optimized
      Finite Field & ``GF(p^n, 'a')`` & `p` prime
      Q[sqrt(d)]  & ``QuadraticField(d, 'a')`` & generator ``a``
      Cyclotomic Fields & ``CyclotomicField(n)`` & rationals with `n`\ th roots of unity
      Number Fields & ``NumberField(poly, 'a')`` & irreducible ``poly``, generator ``a``
      Algebraic Numbers & ``QQbar`` & Algebraic closure of ``QQ``
      Algebraic Reals & ``AA`` & real numbers in ``QQbar``
      Machine Reals & ``RDF`` &  best for numerical linear algebra
      Machine Complexes & ``CDF`` &  best for numerical linear algebra
      Reals & ``RealField(prec)``  & ``prec`` = precison in bits
      Complexes & ``ComplexField(prec)``  & ``prec`` = precison in bits
      Reals & ``RR`` & same as ``RealField(53)``
      Complexes & ``CC`` & same as ``ComplexField(53)``
      Real Interval & ``RealIntervalField(prec)``  & ``prec`` = precision in bits
      Complex Interval & ``ComplexIntervalField(prec)``  & ``prec`` = precision in bits

   .. .. csv-table:: Fields in Sage
      :header: "Field", "Name", "Precision", "Notes"
      :delim: &

      Symbolic   & ``SR`` & Exact & used with symbolic variables
      Rationals  & ``QQ`` & Exact &
      Mod `p`    & ``Integers(p)`` & Exact & `p` prime
      Mod 2        & ``GF(2)`` & Exact & optimized for `p=2`
      Finite Field & ``GF(p^n, 'a')`` & Exact & `p` prime
      Q[sqrt(d)]  & ``QuadraticField(d, 'a')`` & Exact & generator ``a``
      Cyclotomic Fields & ``CyclotomicField(n)`` & Exact & rationals with nth roots of unity
      Number Fields & ``NumberField(poly, 'a')`` & Exact & irreducible ``poly``, generator ``a``
      Algebraic Reals & ``AA`` & Exact &
      Algebraic Numbers & ``QQbar`` & Exact &
      Double Precision  Reals & ``RDF`` & 53 bit & best for numerical linear algebra
      Double Precision Complexes & ``CDF`` & 53 bit & best for numerical linear algebra
      High Precision Reals & ``RealField(prec)`` & Arbitrary & ``prec`` = precison in bits
      High Precision Complexes & ``ComplexField(prec)`` & Arbitrary & ``prec`` = precison in bits
      Double Precision Real Interval & ``RIF`` & 53 bit &
      Double Precision Complex Interval & ``CIF`` & 53 bit &
      High Precision Real Interval & ``RealIntervalField`` & Arbitrary & ``prec`` = precision in bits
      High Precision Complex Interval & ``ComplexIntervalField`` & Arbitrary & ``prec`` = precision in bits


#. Create symbolic variables with ``var()``.  Note that ``x`` is
   predefined at startup to be a symbolic variable (you will need to
   create any other symbolic variables).

   .. ::

   ..  sage: var('w, y, zeta')
   ..  (w, y, zeta)
   ..  sage: x*y+w*zeta^2
   ..  w*zeta^2 + x*y

#. Indices of vectors, matrix rows, matrix columns, lists and tuples
   all begin at 0.  For example, the third row of a matrix is accessed
   with the index 2.  While perhaps uncomfortable at first, this makes
   programming easier, and makes vectors and matrices consistent with
   similar Python constructs.

#. Large matrices (at least 20 rows or 50 columns) do not print
   all their entries by default.  To print the entries, do ``print A.str()``.
   You can adjust the cutoff for this behavior using 
   ``sage.matrix.matrix0.set_max_rows`` and ``sage.matrix.matrix0.set_max_cols``.

#. We can save vectors and matrices (and most objects in Sage) to a
   file with the :meth:`save` method.  Given a filename, the
   :func:`load` function returns the saved object.  This lets us save
   the results of a computation and then resume it later or on another
   computer.

#. Vectors and matrices may be immutable, which means that they cannot
   be changed.  For example, the reduced row-echelon form of a matrix
   is typically cached (and hence made immutable) so that another
   computation for the same matrix will not need to repeat the
   reduction to echelon form.  We can make a matrix ``A`` immutable
   using ``A.set_immutable()``.  We can use the ``copy()`` function to
   make a mutable copy.

   .. ::

   ..  sage: A = matrix(QQ, 3, 4, range(12))
   ..  sage: A.is_mutable()
   ..  True
   ..  sage: B = A.echelon_form()
   ..  sage: B.is_immutable()
   ..  True
   ..  sage: C = copy(B)
   ..  sage: C.is_mutable()
   ..  True

#. Place comments in your code by prefixing each comment with ``#``.
   Comments extend from ``#`` to the end of the line.

#. Place several commands on a single line by separating them with a
   semi-colon: ``a = 4; a + 7``.  Several quantities can be output in one tuple by
   creating a single command with values separated by commas: ``2+3, 8-7``.  

   .. ::

   .. sage: a = 4; a + 7
   .. 11
   .. sage: 2 + 3, 8 - 7
   .. (5, 1)

#. In the notebook, only the value of the last expression is printed.
   An assignment of a value to a variable will not produce any output.
   A common idiom for assigning ``v`` to the result of a command and
   then displaying ``v`` is ``v = some_command(); v``.

#. Lists in Sage are delimited by brackets ``[,]``.  Entries may be
   added, removed and sorted.  Duplicates are allowed.  Sage also has
   a ``set`` data type, for which duplicates are removed, and
   determining membership is very fast. Tuples are very similar to
   lists, but are immutable, and are delimited by parentheses ``(,)``.
   Be careful not to confuse tuples with vectors, since vectors also
   print using parentheses.  Lists, tuples, and sets are part of the
   Python language.  The official Python tutorial in the Python
   documentation has an excellent discussion of lists, tuples and
   sets.

   .. ::

   ..  sage: zoo = ["dog", "baboon", "alligator"]
   ..  sage: zoo.append("cat"); zoo
   ..  ['dog', 'baboon', 'alligator', 'cat']
   ..  sage: manifest = sorted(zoo); manifest # sort a copy of zoo
   ..  ['alligator', 'baboon', 'cat', 'dog']
   ..  sage: zoo.sort(); zoo # sort zoo in-place
   ..  ['alligator', 'baboon', 'cat', 'dog']
   ..  sage: a_tuple = (9, -2, 4); a_tuple
   ..  (9, -2, 4)
   ..  sage: a_vector = vector([9, -2, 4]); a_vector
   ..  (9, -2, 4)
   ..  sage: a_tuple == a_vector
   ..  False

#. Python has a very convenient way to build lists using list
   comprehensions, which is similar to set-builder notation. 

   .. ::

   ..  sage: v = vector([-2, 3, 4, -6, 5])
   ..  sage: [x^2 for x in v]
   ..  [4, 9, 16, 36, 25]
   ..  sage: [x^2 for x in v if x > 0]
   ..  [9, 16, 25]

#. ``lambda`` is a reserved word in Python, so it cannot be used as a
   variable name!  ``lambda`` is used to create short unnamed
   functions (i.e., "anonymous" functions).

   .. ::

   ..  sage: hilbert = matrix(QQ, 3, 3, lambda x,y: 1/(x+y+1)); hilbert
   ..  [  1 1/2 1/3]
   ..  [1/2 1/3 1/4]
   ..  [1/3 1/4 1/5]

#. By default, ``I`` and ``i`` are both predefined as the complex
   number `i=\sqrt{-1}`.

#. Occasionally, you may want to overwrite a variable that Sage
   predefines with your own value, like using ``i`` as an index or
   setting ``I`` to be an identity matrix.  To access Sage's
   predefined variable, prepend ``sage.all.`` to the variable (e.g.,
   ``sage.all.I`` is the square root of `-1`, even if you've redefined
   ``I``).  Use the :func:`~sage.all.reset` function to reset variables
   to Sage defaults (e.g., ``reset('I')`` resets ``I`` to `\sqrt{-1}`,
   and ``reset()`` will reset all variables to Sage's default values).



Examples
--------

#. The parent of an object helps distinguish between objects that may
   print the same. ::

     sage: 5, parent(5) # this "5" is an integer
     (5, Integer Ring)
     sage: 5/1, parent(5/1) # this "5" is a rational
     (5, Rational Field)

   .. sage: vector([2, sin(4.3), -6]).parent()
   .. Vector space of dimension 3 over Real Field with 53 bits of precision

   .. sage: a,b,c = var('a b c')
   .. sage: matrix([[a,b], [b,c]]).parent()
   .. Full MatrixSpace of 2 by 2 dense matrices over Symbolic Ring


   ..   #. Symbolic variables and expressions

   .. ::

       sage: var('w, y, zeta')
       (w, y, zeta)
       sage: x*y+w*zeta^2
       w*zeta^2 + x*y

#. Mutable and immutable matrices::

     sage: A = matrix(QQ, 3, 4, range(12)); A.is_mutable()  # can change A
     True
     sage: B = A.rref(); B.is_immutable()  # can't change B
     True
     sage: C = copy(B); C.is_mutable()  # can change C
     True
     sage: C[0,0] = 100  # change the upper-left element of C

   .. #. Lists versus tuples

   .. ::

       sage: zoo = ["dog", "baboon", "alligator"]
       sage: zoo.append("cat"); zoo
       ['dog', 'baboon', 'alligator', 'cat']
       sage: manifest = sorted(zoo); manifest # sort a copy of zoo
       ['alligator', 'baboon', 'cat', 'dog']
       sage: zoo.sort(); zoo # sort zoo in-place
       ['alligator', 'baboon', 'cat', 'dog']
       sage: a_tuple = (9, -2, 4); a_tuple
       (9, -2, 4)
       sage: a_vector = vector([9, -2, 4]); a_vector
       (9, -2, 4)
       sage: a_tuple == a_vector  # these are different kinds of objects
       False

#. List comprehensions provide an easy way to map functions or
   filter. ::

    sage: v = vector([-2, 3, 4, -6, 5])
    sage: [i^2 for i in v], [i^2 for i in v if i > 0]
    ([4, 9, 16, 36, 25], [9, 16, 25])





Vectors
=======

Commands
--------


#. **Constructors**: Sage has a number of ways to construct vectors.


   #. Construct vectors over a specific ring with ``vector(ring, entries)``.

      .. ::

      ..  sage: vector(QQ, [1,2,3])
      ..  (1, 2, 3)
      ..  sage: vector(RDF, [1,2,3])
      ..  (1.0, 2.0, 3.0)
      ..  sage: x,y = var('x,y'); vector(SR, [x, y, x*sin(y)])
      ..  (x, y, x*sin(y))
      ..  sage: vector(QQ, [i^2 for i in [1..10]])
      ..  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

   #. The ring is optional; if not provided, Sage will infer the ring
      from the entries.  The :meth:`base_ring` method gives the ring of
      the entries.  We can construct a new vector over a different base
      ring by using the :meth:`change_ring` method.

      .. ::

      ..  sage: v = vector([1,2,3]); v.base_ring()
      ..  Integer Ring
      ..  sage: w = v.change_ring(RDF); w
      ..  (1.0, 2.0, 3.0)

   #. Create vector-valued symbolic functions with ``f(inputs) = [outputs]`` syntax.

      .. ::

      ..  sage: f(x,y) = [x, y, x*sin(y)]; f
      ..  (x, y) |--> (x, y, x*sin(y))
      ..  sage: f(1,2)
      ..  (1, 2, sin(2))



   #. The :func:`zero_vector` and :func:`random_vector` commands
      construct zero and random vectors.  The options to
      :func:`random_vector` depend on the ring; see the
      :meth:`random_element` function documentation for the ring for
      details (for example, ``QQ.random_element?``). 

      .. ::

      ..  sage: zero_vector(QQ, 3)
      ..  (0, 0, 0)
      ..  sage: random_vector(QQ, 10, num_bound=15, den_bound=5)  # random
      ..  (-2, -5/2, 15/4, 1, -11/4, 1, -13/4, 10, -3, 1)

   ..    sage: random_vector(10)  # random
   ..    (-2, 1, 1, -1, -1, 0, 1, 1, -1, 1)
   ..    sage: random_vector(ZZ, 20, x=-20, y=100)   # random
   ..    (95, 2, -14, 78, 26, 22, 42, 35, 43, 20, 40, 32, 31, -8, 29, 9, 61, 25, 43, 24)
   ..    sage: random_vector(ZZ, 20, distribution="1/n")   # random
   ..    (1, -1, -20, 1, -1, 1, 30, 1, 4, 3, -1, -1, 1, 1, 1, -5, 3, 1, 0, 1)


#. **Properties**


   #. In Sage, vectors don't have a column or row orientation.  Instead,
      Sage interprets the vector as either row or column as the situation
      demands.  In order to explicitly get a row or column vector (i.e.,
      a single-row or single-column matrix), use the :meth:`row` or
      :meth:`column` methods. 

      .. ::

      ..   sage: v = vector(QQ, [1,2,3])
      ..   sage: v.column()
      ..   sage: v.row()

   #. Use square brackets to access an element of the vector.  Remember
      that the indices start at zero.

      .. ::

      ..   sage: v = vector(QQ, [3,6,4])
      ..   sage: v[0]
      ..   3

   #. To get the number of elements in a vector, use the :func:`len`
      command.

      .. ::

      ..   sage: len(vector(QQ, [1,0,3]))
      ..   3

      ..  or the :meth:`degree` method

   #. The :meth:`norm` method gives the vector `2`-norm.  We can specify a
      `p` to compute a `p`-norm for any `p\geq 1` (including
      ``Infinity``).

      .. ::

      ..   sage: v = vector(QQ, [4,3,-1])
      ..   sage: v.norm(), v.norm(1), v.norm(2), v.norm(5), v.norm(Infinity)
      ..   (sqrt(26), 8, sqrt(26), 1268^(1/5), 4)
      ..   sage: p = var('p'); v.norm(p)
      ..   (3^p + 4^p + 1)^(1/p)

   #. The :meth:`n` method gives a numerical approximation.  We can
      specify a precision or number of digits.

      .. ::

      ..   sage: v = vector(SR, [pi, e, 3/7])
      ..   sage: v.n()
      ..   (3.14159265358979, 2.71828182845905, 0.428571428571429)
      ..   sage: v.n(digits=3)
      ..   (3.14, 2.72, 0.429)

      .. You can also explicitly convert the vector to a numeric vector by
      .. changing the base ring::

      ..   sage: vector(SR, [pi, e, 3/7]).change_ring(RDF)
      ..   (3.14159265359, 2.71828182846, 0.428571428571)


   .. todo: : ``u.N()`` works if http://trac.sagemath.org/sage_trac/ticket/12195 is applied.  Needs review!

#. **Manipulations**


   #. Linear combinations use standard notation, like ``2*u + 3*v``.

      .. ::

      ..  sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [4, 3, -1])
      ..  sage: 2*u + 3*v
      ..  (14, 13, 3)


   #. The default product ``u*v`` of two vectors is the dot product.  We
      can also use the :meth:`dot_product` method.  The
      :meth:`hermitian_inner_product` method conjugates the first vector
      before taking the dot product.  There are also
      :meth:`outer_product` and :meth:`cross_product` methods (cross
      product works for 3- and 7-dimensional vectors).

      .. ::

      ..  sage: u = vector(QQ, [1,2,3]); v = vector(QQ, [4,3,-1]); w = vector(SR, [4,2+I,3])
      ..  sage: u*v, u.dot_product(v)
      ..  (7, 7)
      ..  sage: w.hermitian_inner_product(u)
      ..  -2*I + 17

      .. #. The :meth:`outer_product` method computes the outer product.

      .. ::

      ..  sage: u = vector(QQ, [1,2,3]); v = vector(QQ, [4,3,-1])
      ..  sage: u.outer_product(v)
      ..  [ 4  3 -1]
      ..  [ 8  6 -2]
      ..  [12  9 -3]
      ..  sage: u.column()*v.row()
      ..  [ 4  3 -1]
      ..  [ 8  6 -2]
      ..  [12  9 -3]


      .. #. The :meth:`cross_product` method computes the cross product of 3-
      ..    or 7-dimensional vectors.

      .. ::

      ..  sage: u = vector(QQ, [1,2,3]); v = vector(QQ, [4,3,-1])
      ..  sage: u.cross_product(v)
      ..  (-11, 13, -5)

      .. sage: u = vector(QQ, [1,2,4/3,3,0,1,5]); v = vector(QQ, [0,-1,2,-4,2/3,5,-3])
      .. sage: u.cross_product(v)
      .. (-59/3, -208/9, 62/3, -9, -32/3, -29/3, 15)


   #. The :meth:`apply_map` method will apply a function to each element
      of the vector.  Equivalently, you could also explicitly construct a
      new vector using a list comprehension.


      .. ::

      ..   sage: u = vector(QQ, [1,2,3])
      ..   sage: v = u.apply_map(lambda x: x^2); v
      ..   (1, 4, 9)
      ..   sage: f(x) = x^3
      ..   sage: w = u.apply_map(f); w
      ..   (1, 8, 27)


      .. ::

      ..   sage: u = vector(QQ, [1,2,3])
      ..   sage: v = vector(QQ, [i^2 for i in u]); v
      ..   (1, 4, 9)




Examples
--------

#. Construct vectors::

     sage: v = vector(QQ, [1,2,3]); v
     (1, 2, 3)
     sage: v.change_ring(RDF)
     (1.0, 2.0, 3.0)
     sage: v.apply_map(lambda x: x^2)  # also f(x) = x^2; v.apply_map(f)
     (1, 4, 9)
     sage: random_vector(QQ, 10, num_bound=15, den_bound=5)  # random
     (-2, -5/2, 15/4, 1, -11/4, 1, -13/4, 10, -3, 1)

     sage: x,y = var('x,y'); vector(SR, [x, y, x*sin(y)])
     (x, y, x*sin(y))
     sage: f(x,y) = [x, y, x*sin(y)]; f  # vector-valued function
     (x, y) |--> (x, y, x*sin(y))
     sage: f(1,2)
     (1, 2, sin(2))

   .. #. Row and column methods::

   ..      sage: v = vector(QQ, [1,2,3])
   ..      sage: v.column()
   ..      sage: v.row()

#. Properties of a vector.  ``w.n(20)`` gives `\textbf w` with 20 bits
   of precision; use ``w.n(digits=20)`` for 20 digits. ::

     sage: v = vector(QQ, [21,-3,-1,2]); v[0], len(v)
     (21, 4)
     sage: v.norm(), v.norm(1), v.norm(2), v.norm(5), v.norm(Infinity), v.norm(x)
     (sqrt(455), 27, sqrt(455), 4084377^(1/5), 21, (2^x + 3^x + 21^x + 1)^(1/x))
     sage: w = vector(SR, [pi, e, 3/7]); w.n(), w.n(digits=2)
     ((3.14159265358979, 2.71828182845905, 0.428571428571429), (3.1, 2.7, 0.43))

#. Vector arithmetic::

    sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [4, 3, -1])
    sage: 2*u + 3*v, u.cross_product(v)
    ((14, 13, 3), (-11, 13, -5))
    sage: u*v, u.dot_product(v), vector(SR, [4,2+I,3]).hermitian_inner_product(u)
    (7, 7, -2*I + 17)
    sage: u.outer_product(v)  # same as: u.column() * v.row()
    [ 4  3 -1]
    [ 8  6 -2]
    [12  9 -3]




.. _matrices:

Matrices
========

Commands
--------

#. **Constructors**


   #. The ``matrix(ring, entries)`` command constructs a matrix over a
      specific ring of a specific size.  The entries can be given as a
      list of rows, or the numbers of rows and columns can be given with
      a list of entries.  Also, a list of vectors can be given, or a
      function which takes in the indices of an entry (zero-based) and
      returns the entry.  A base ring will be inferred if not specified.

      .. ::

      ..   sage: matrix(QQ, [[1,0,1],[2,0,-1]])
      ..   [ 1  0  1]
      ..   [ 2  0 -1]
      ..   sage: matrix(QQ, 2, 3, [1,0,1,2,0,-1])
      ..   [ 1  0  1]
      ..   [ 2  0 -1]
      ..   sage: u = vector(QQ, [1,0,1]); v = vector(QQ, [2,0,-1])
      ..   sage: matrix([u,v])
      ..   [ 1  0  1]
      ..   [ 2  0 -1]

   #. The :func:`column_matrix` command takes a list of columns instead
      of a list of rows. 

      .. ::

      ..   sage: column_matrix(QQ, [[3,4],[5,0],[2,-1]])
      ..   [ 3  5  2]
      ..   [ 4  0 -1]
      ..   sage: u = vector(QQ, [2,3]); v = vector(QQ, [5,0]); w = vector(QQ, [-1,2])
      ..   sage: column_matrix([u,v,w])
      ..   [ 2  5 -1]
      ..   [ 3  0  2]

   #. A variety of functions construct special types of matrices.

      .. .. csv-table:: Matrix constructors
         :header: "Command", "Description", "Example"
         :delim: &

         :func:`diagonal_matrix` & "Diagonal matrix" & ``diagonal_matrix(QQ, [1,2,3])``
         :func:`identity_matrix` & "Identity matrix" & ``identity_matrix(3)``
         :func:`zero_matrix` & "Zero matrix" & ``zero_matrix(3,4)``
         :func:`ones_matrix` & "All-ones matrix" & ``ones_matrix(3,4)``
         :func:`elementary_matrix` & "Elementary matrix" & ``elementary_matrix(QQ, 4, row1=3, scale=-2)``
         :func:`random_matrix` & "Random matrix" & ``random_matrix(RDF, 3,4)``
         :func:`hadamard_matrix` & "Hadamard matrix" & ``hadamard_matrix(4)``
         :func:`companion_matrix` & "Polynomial companion matrix" & ``companion_matrix(x^2-2*x+1).polynomial(QQ))``

      .. csv-table:: Matrix constructors
         :header: "Description", "Example"
         :delim: &

         "Diagonal matrix" & ``diagonal_matrix(QQ, [1,2,3])``
         "Identity matrix" & ``identity_matrix(3)``
         "Zero matrix" & ``zero_matrix(3,4)``
         "All-ones matrix" & ``ones_matrix(3,4)``
         "Elementary matrix" & ``elementary_matrix(QQ, 4, row1=3, scale=-2)``
         "Random matrix" & ``random_matrix(RDF, 3,4)``
         "Hadamard matrix" & ``hadamard_matrix(4)``
         "Polynomial companion matrix" & ``companion_matrix((x^2-2*x+1).polynomial(QQ))``



      The :func:`zero_matrix`, :func:`ones_matrix`, and
      :func:`random_matrix` functions also can take a single number to
      construct a square matrix.  For more options to give to the
      :func:`random_matrix` function, see the :meth:`random_element`
      method for the ring of entries (e.g., ``RDF.random_element?``).
      The :func:`random_matrix` constructor also takes an
      ``algorithm`` keyword that can be used to create small example
      matrices with integer entries that are "nice" to work
      with. Values of this keyword can be ``echelonizable``,
      ``unimodular``, ``subspaces``, or ``diagonalizable`` and will
      create matrices (respectively) with a "nice" echelon form; with
      determinant one; with simultaneously "nice" bases for the row
      space, column space, right kernel and left kernel; or similar to
      a diagonal matrix.


      ..  sage: diagonal_matrix(QQ, [1,2]), identity_matrix(2), zero_matrix(2,3), ones_matrix(2,3)
          (
          [1 0]  [1 0]  [0 0 0]  [1 1 1]
          [0 2], [0 1], [0 0 0], [1 1 1]
          )

       .. sage: random_matrix(RDF,2,3)
       .. [-0.948579082178  0.245922947925  -0.91994959224]
       .. [ -0.57833972373  0.998060473217 -0.846990627305]

      .. todo: :
         companion_matrix should take a symbolic expression and try
         to make it into a single-variable polynomial, like this::

           sage: p = (x^3 - 2*x^2 + 3*x + 1).polynomial(QQ)
           sage: companion_matrix(p)
           [ 0  0 -1]
           [ 1  0 -3]
           [ 0  1  2]



      .. #. Other matrices are easy to construct from their definitions.  In
      ..    particular, using a function which takes the indices of an entry
      ..    (with 0-based indexing) and returns the entry value can be
      ..    convenient.

      .. ::

      ..   sage: def vandermonde(R, v): return matrix(R, len(v), lambda i,j: v[i]^j)
      ..   sage: vandermonde(QQ, [2,3,4])
      ..   [ 1  2  4]
      ..   [ 1  3  9]
      ..   [ 1  4 16]

      ..   sage: def hilbert(R,n): return matrix(R, n, lambda i,j: 1/(i+j+1))
      ..   sage: hilbert(QQ, 3)
      ..   [  1 1/2 1/3]
      ..   [1/2 1/3 1/4]
      ..   [1/3 1/4 1/5]

      ..     sage: def toeplitz(R,c,r): return matrix(R, len(c), len(r), lambda i,j: c[i-j] if i>=j else r[j-i])
      ..     sage: toeplitz(QQ, [2,3,4], [5,6,7])
      ..     [2 6 7]
      ..     [3 2 6]
      ..     [4 3 2]
      ..
      ..     sage: def hankel(R,c,r): entries=c+r[1:]; return matrix(R, len(c), len(r), lambda i,j: entries[i+j])
      ..     sage: hankel(QQ, [1,2,3], [7,8,9,10])
      ..     [ 1  2  3  8]
      ..     [ 2  3  8  9]
      ..     [ 3  8  9 10]
      ..
      ..     sage: def circulant(R,E): return hankel(R, E, E[-1:]+E[:-1])
      ..     sage: circulant(QQ, [1,2,3])
      ..     [1 2 3]
      ..     [2 3 1]
      ..     [3 1 2]


   #. The included SciPy linear algebra package has a number of matrices as well,
      including the above and Hankel, Leslie, Pascal, Toeplitz matrices
      and more [Sci12]_.

      .. ::

      ..   sage: from scipy.linalg import toeplitz
      ..   sage: matrix(QQ,toeplitz([1,2,3],[1,4,5,6]))
      ..   [1 4 5 6]
      ..   [2 1 4 5]
      ..   [3 2 1 4]

   #. You can construct the space of all matrices ``M`` with a given
      base ring and size and use this space to construct
      matrices. There are also other methods of matrix spaces; see the
      Sage reference manual.

      .. ::

      ..   sage: A=matrix(QQ, 2, 3, [1,2,3,4,5,6])
      ..   sage: M = A.matrix_space(); M
      ..   Full MatrixSpace of 2 by 3 dense matrices over Rational Field
      ..   sage: M([1,0,4,3,2,1])
      ..   [1 0 4]
      ..   [3 2 1]

#. **Block Matrix Constructors**

   #. The :func:`block_matrix` and :func:`block_diagonal_matrix`
      commands create block matrices (see the block matrices example below).  Blocks may
      be rectangular, integer arguments are converted to blocks with
      diagonal entries equal to the integer, and the result carries
      the natural subdivisions by default.  See the
      :func:`block_matrix` documentation for many more features.

      .. ::

      ..   sage: A = jordan_block(-1,2); B = matrix(QQ, [[1,-1/2]])
      ..   sage: block_matrix(QQ, [[A,1],[0,B]])
      ..   [  -1    1|   1    0]
      ..   [   0   -1|   0    1]
      ..   [---------+---------]
      ..   [   0    0|   1 -1/2]
      ..   sage: block_diagonal_matrix([A,B], subdivide=False)
      ..   [  -1    1    0    0]
      ..   [   0   -1    0    0]
      ..   [   0    0    1 -1/2]

   #. The matrix methods :meth:`~sage.matrix.matrix1.Matrix.block_sum`
      (for block diagonal results),
      :meth:`~sage.matrix.matrix1.Matrix.augment` (concatenate
      horizontally), and :meth:`~sage.matrix.matrix1.Matrix.stack`
      (concatenate vertically) provide alternative ways to combine two
      matrices or a matrix and a vector. 

      .. ::

      ..   sage: A = matrix(QQ, [[-1,1],[0,-1]]); B = matrix(QQ, [[1,-1/2]])
      ..   sage: A.augment(vector(QQ, [1,-1/2]), subdivide=True)
      ..   [  -1    1|   1]
      ..   [   0   -1|-1/2]
      ..   sage: A.stack(B)
      ..   [  -1    1]
      ..   [   0   -1]
      ..   [   1 -1/2]

   #. Sage matrices can be subdivided into blocks (i.e., partitioned
      into submatrices).  Blocks are created with the
      :meth:`subdivide` method (specify row and column indices
      before each subdivision point), while the :meth:`subdivisions`
      method returns this subdivision.  The :meth:`subdivision` method
      retrieves a specified block, and the :meth:`subdivision_entry`
      returns a specified entry of a specified block. If arithmetic is
      done between matrices with compatible subdivisions, the result
      also has the natural subdivision.  See the block matrices
      example below.

      .. todo: : deprecate :meth:`get_subdivisions`

#. **Properties**

   #. The :attr:`I`, :attr:`C`, :attr:`T`, and :attr:`H` attributes
      give the inverse, conjugate, transpose, and conjugate transpose
      (Hermitian transpose) of the matrix.  Do not use parentheses
      when using these (e.g., ``A.I``).  The :attr:`I`, :attr:`C`,
      :attr:`T`, and :attr:`H` attributes are shortcuts for the
      :meth:`inverse`, :meth:`conjugate`, :meth:`transpose`, and
      :meth:`conjugate_transpose` methods, respectively.  The inverse
      of a matrix is also ``A^-1`` and ``~A``.


      .. ::

      ..   sage: A = matrix(QQ, 2, [0,-1,2,-2]); A
      ..   [ 0 -1]
      ..   [ 2 -2]
      ..   sage: A.I
      ..   [ -1 1/2]
      ..   [ -1   0]
      ..   sage: A.T
      ..   [ 0  2]
      ..   [-1 -2]


   #. Matrices have a number of methods for standard computations (e.g., ``A.det()``).

      .. csv-table:: Information about matrix
        :header: Method, Description
        :delim: &

        :meth:`density` & density of nonzero entries
        :meth:`det` & determinant
        ``minors(k)`` & list of all `k` by `k` minors, in lexicographic order
        :meth:`ncols` & number of columns
        ``norm(p)`` & norm, ``p`` can be 1, 2, ``Infinity``, or ``'frob'`` (Frobenius)
        :meth:`nrows` & number of rows
        :meth:`permanent` & permanent
        ``permanental_minor(k)`` & sum of permanents of all possible `k` by `k` submatrices
        :meth:`rank` & rank
        :meth:`trace` &  trace

      .. ::

         sage: A = matrix(QQ, 2, [1,2,3,4])
         sage: A.norm('frob') # Frobenius norm
         5.47722557505

         sage: A = matrix(QQ, 2, 3, [1,2,3,4,5,6])
         sage: A.permanental_minor(2)
         58

      .. The :meth:`minors` method returns the minors in lexicographic
         order.  For example, if `A` is a `3` by `3` matrix, then
         ``A.minors(2)`` returns the list of determinants for these
         rows/columns, in order: ``[0,1]x[0,1], [0,1]x[0,2], [0,1]x[1,2],
         [0,2]x[0,1], [0,2]x[0,2], [0,2]x[1,2], [1,2]x[0,1], [1,2]x[0,2],
         [1,2]x[1,2]``.

      .. ::

        sage: A = matrix(QQ, 3, 3, range(9)); A
        [0 1 2]
        [3 4 5]
        [6 7 8]
        sage: A.minors(2)
        [-3, -6, -3, -6, -12, -6, -3, -6, -3]

   #. There are also several other commands to return various matrices.

      .. csv-table:: Matrix constructors
         :header: "Description", "Example"
         :delim: &

         Adjoint & ``A.adjoint()``
         Antitranspose & ``A.antitranspose()``
         Commutator (`AB-BA`) & ``A.commutator(B)``
         Matrix exponential,  `\sum_{k=0}^{\infty} \frac{A^k}{k!}` & ``A.exp()`` (Use ``RDF`` or ``CDF`` matrices)
         Elements satisfying given condition & ``A.find(lambda x: x<0)``
         Numerical approximation & ``A.n()``, ``A.n(digits=4)``, ``A.n(10)`` (10 bits)

      The :meth:`find` method makes a matrix with ones where the
      original matrix entries satisfied the given condition and zeros
      elsewhere. The ``indices=True`` option returns instead a
      dictionary of indices and elements satisfying the condition.

      .. ::

      ..   sage: A = matrix(QQ, 2, [-1,2,1,-3]); A
      ..   [-1  2]
      ..   [ 1 -3]
      ..   sage: A.find(lambda x: x<0)
      ..   [1 0]
      ..   [0 1]
      ..   sage: A.find(lambda x: x>0, indices=True)
      ..   {(0, 1): 2, (1, 0): 1}

      .. todo: : This should work, to filter out the entries that are
          negative: ``A.elementwise_product(A.find(lambda x:x<0))``.
          However, it doesn't work since :meth:`find` returns a ``GF(2)`` matrix.

      .. ::
      .. For example, to calculate the matrix exponential numerically, do::

      ..   sage: A = matrix(QQ,2,[1,2,3,4])
      ..   sage: A.change_ring(RDF).exp()
      ..   [51.9689561987  74.736564567]
      ..   [112.104846851 164.073803049]


   #. The ``A.iterates(v, n, rows=...)`` method takes a vector `\textbf v` and a number
      `n`, and returns the vectors `\textbf v, A\textbf v, A^2\textbf v, \ldots,
      A^{n-1}\textbf v` as rows (if ``rows=True``, which is default) or
      columns (if ``rows=False``) of a matrix.

      .. ::

        sage: A = matrix(QQ, 2, [1,2,3,4]); v = vector([1,2])
        sage: A.iterates(v, 4, rows=False)
        [  1   5  27 145]
        [  2  11  59 317]

   #. The :meth:`charpoly` and :meth:`minpoly` methods return the
      characteristic and minimal polynomial, respectively.  Each
      function optionally takes a variable name.
      
      .. ::

        sage: A = diagonal_matrix([2,2,5])
        sage: A.charpoly()
        x^3 - 9*x^2 + 24*x - 20
        sage: A.minpoly()
        x^2 - 7*x + 10

   #. The :meth:`nonzero_positions`, :meth:`nonzero_positions_in_row`,
      and :meth:`nonzero_positions_in_column` methods give the indices of
      various nonzero elements of a matrix, row, or column.  Remember
      that indices start at zero.

   #. ``A.column_space()``, ``A.row_space()``, ``A.right_kernel``, and
      ``A.left_kernel()`` construct the corresponding vector spaces.
      *Warning*: Default versions of these commands are generally the
      left versions, so ``A.kernel()`` is the left kernel and ``A.image()``
      is the row space, consistent with the `\textbf x\mapsto\textbf xA`
      transformation, where the vector is on the left in the product.

      .. ::

        sage: A = matrix(QQ, 3, range(9)); A
        [0 1 2]
        [3 4 5]
        [6 7 8]
        sage: A.column_space()
        Vector space of degree 3 and dimension 2 over Rational Field
        Basis matrix:
        [ 1  0 -1]
        [ 0  1  2]
        sage: A.right_kernel()
        Vector space of degree 3 and dimension 1 over Rational Field
        Basis matrix:
        [ 1 -2  1]

      .. William says act_on_polynomial is useful in number theory.  
      .. That's outside the scope here, but would be good for the expanded version
      .. . The :meth:`act_on_polynomial` method, on an `n` by `n` matrix `A`,
      ..   takes a polynomial `p` in variables `\textbf v=\left<
      ..   x_1,x_2,\cdots,x_n\right>` returns the polynomial `f(A\textbf v)`::

      ..     sage: R.<x,y> = QQ[] # construct a polynomial ring with variables
      ..     sage: A = matrix(QQ, 2, [1,2,3,4])
      ..     sage: A.act_on_polynomial(x^2 - y^2)
      ..     -8*x^2 - 20*x*y - 12*y^2

   #. Matrices have numerous predicates that start with ``is_``, for
      example, ``A.is_invertible()``.  The :meth:`is_similar` method
      can optionally return a transformation matrix.

      .. _Matrix predicates:
      .. csv-table:: Matrix predicates
        :header: Method, True if |ellipsis|

        :meth:`is_bistochastic`, each row and column sums to 1
        :meth:`is_dense`, matrix is stored in a dense data structure
        :meth:`is_diagonalizable`, matrix is similar to a diagonal matrix
        :meth:`is_hermitian`, matrix is equal to its conjugate transpose
        :meth:`is_idempotent`, matrix is equal to its square
        :meth:`is_immutable`, matrix entries cannot be changed
        :meth:`is_invertible`, matrix is invertible over its base ring
        :meth:`is_mutable`, matrix entries can be changed
        :meth:`is_one`, matrix is identity matrix
        :meth:`is_scalar`, matrix is a multiple of the identity matrix
        :meth:`is_similar`, matrix is similar to another given matrix
        :meth:`is_singular`, matrix is not invertible
        :meth:`is_skew_symmetric`, matrix is equal to its negative transpose
        :meth:`is_sparse`, matrix is stored in a sparse data structure
        :meth:`is_square`, matrix has the same number of rows and columns
        :meth:`is_symmetric`, matrix is equal to its transpose
        :meth:`is_unitary`, columns form an orthonormal basis
        :meth:`is_zero`, every entry is zero

      ..  :meth:`is_nilpotent`, NotImplementedError
      ..  :meth:`is_unit`, NotImplementedError

      .. todo: : :meth:`is_mutable` and :meth:`is_immutable` is redundant [but no more so than dense/sparse, and we naturally used both above]



#. **General manipulations**

   #. Arithmetic with matrices uses standard notation, like ``2*A - A*B + A^3 - A^-1``.

      .. ::

        sage: A = matrix(QQ, 2, [1,2,3,4]); B = matrix(QQ, 2, [-1,2,0,3])
        sage: 2*A - 4*B
        [ 6 -4]
        [ 6 -4]
        sage: A*B
        [-1  8]
        [-3 18]
        sage: A^3
        [ 37  54]
        [ 81 118]

   #. Recall that Sage vectors do not have an implicit row or column
      orientation.  If `A` is a matrix and `\textbf v` is a vector,
      then ``A*v`` views `\textbf v` as a column vector and ``v*A``
      views `\textbf v` as a row vector.  In order to get a specific
      orientation for `\textbf v`, convert it to a single-row or
      single-column matrix using ``v.row()`` or ``v.column()``. 

      .. ::

        sage: A = matrix(QQ, 2, [1,2,3,4]); v = vector(QQ, [3,-1])
        sage: A*v
        (1, 5)
        sage: v*A
        (0, 2)

   #. ``A.elementwise_product(B)`` computes the Hadamard product of
      `A` and `B`, while ``A.tensor_product(B)`` computes the tensor
      product.  Subdivisions are automatically added for tensor
      products; do ``A.tensor_product(B, subdivide=False)`` to not
      have the result subdivided. ``A.trace_of_product(B)`` method
      computes the trace of `AB` without actually computing `AB`.

      .. ::

        sage: a = matrix(QQ, 2, [1,2,3,4]); b = matrix(QQ, 2, [-1,2,0,3])
        sage: a.elementwise_product(b)
        [-1  4]
        [ 0 12]
        sage: a.tensor_product(b)
        [-1  2|-2  4]
        [ 0  3| 0  6]
        [-----+-----]
        [-3  6|-4  8]
        [ 0  9| 0 12]

      .. ::

        sage: A = matrix(QQ, 2, 3, [1,2,3,4,5,6]); B = matrix(QQ, 3, 2, [1,0,-1,2,5,-3])
        sage: A.trace_of_product(B)
        6

   #. ``A.apply_map(function)`` will return a new matrix resulting
      from applying the function to each element of `A`, like ``f(x) =
      x^2; A.apply_map(f)`` or simply ``A.apply_map(lambda x: x^2)``.

      .. ::

        sage: A = matrix(QQ, 2, [1,2,3,4])
        sage: A.apply_map(lambda x: x^2)
        [ 1  4]
        [ 9 16]
        sage: f(x) = x^2
        sage: A.apply_map(f)
        [ 1  4]
        [ 9 16]

      .. Equivalently, you could also explicitly construct a new matrix
         using a list comprehension::

           sage: A = matrix(QQ, 2, [1,2,3,4])
           sage: matrix(QQ, 2, [i^2 for i in A.list()])
           [ 1  4]
           [ 9 16]

      .. ``apply_morphism``


#. **RREF**: There are several ways to compute reduced row
   echelon form (e.g., ``A.rref()``).

   .. csv-table:: Row Reduction Commands
      :header: Method, "Description"

      :meth:`rref`, "Calculate RREF (over fraction field)"
      :meth:`echelon_form`, "Calculate RREF (over base ring)"
      :meth:`echelonize`, "Modify the matrix to echelon form (over base ring)"
      :meth:`extended_echelon_form`, "Augment with identity matrix before reducing"


   .. #. Use :meth:`rref` to calculate the reduced row echelon form of a
       matrix::

         sage: A = matrix(QQ, 3, [1,2,3,4,5,6,7,8,9])
         sage: A.rref()
         [ 1  0 -1]
         [ 0  1  2]
         [ 0  0  0]


   .. #. Like many computer algebra systems, row-reducing a symbolic matrix
      using the :meth:`rref` method assumes that we are working over a
      field (i.e., that if ``b`` is any nonzero element of the base ring,
      then ``1/b`` is also in the base ring).  Since Sage can also work
      with matrices over general rings (which may not be fields), we can
      ask Sage to do operations without assuming that we can divide.  For
      example, if a matrix has entries in a polynomial ring, we can ask
      for the :meth:`echelon_form` of the matrix, which only uses
      operations in the polynomial ring (e.g., Sage won't divide except
      by constants).  We can use the :meth:`matrix_over_field`
      method to get a copy of a matrix over the fraction field of its
      base ring. ::

        sage: R.<b1,b2,b3> = QQ[] # construct a polynomial ring with 3 variables
        sage: A = matrix([[1,1,2,b1], [1,0,1,b2], [2,1,3,b3]]); A
        [ 1  1  2 b1]
        [ 1  0  1 b2]
        [ 2  1  3 b3]
        sage: A.rref() # works over fraction field of R, so 1/b1 exists, etc.
        [1 0 1 0]
        [0 1 1 0]
        [0 0 0 1]
        sage: A.echelon_form() # uses only operations in the polynomial ring R
        [            1             0             1            b2]
        [            0             1             1       b1 - b2]
        [            0             0             0 -b1 - b2 + b3]
        sage: B = A.matrix_over_field(); B.base_ring()
        Fraction Field of Multivariate Polynomial Ring in b1, b2, b3 over Rational Field
        sage: B.echelon_form() == A.rref()
        True

   #. There are a number of commands to perform elementary operations on
      a matrix. Each command also has a variant that returns a new matrix
      instead of modifying the matrix---these variants have the same
      name, but in past tense and prefixed by ``with_``.  For example,
      ``A.rescale_row(0,2)`` rescales row 0 of `A` by a factor of 2,
      while ``A.with_rescaled_row(0,2)`` does not modify `A`, but
      returns a new matrix that is equal to `A`, except row 0 is scaled
      by 2. Remember again that row and column indexing starts at zero.

      .. .. csv-table:: Elementary Operations
         :header: "Modify matrix", "Example operation", "Example command"
         :delim: &

         :meth:`add_multiple_of_column` &        `C_2 \leftarrow C_2 -4C_1` & ``A.add_multiple_of_column(2,1,-4)``
         :meth:`add_multiple_of_row` &           `R_2 \leftarrow R_2 -4R_1` & ``A.add_multiple_of_row(2,1,-4)``
         :meth:`rescale_col` &                   `C_0 \leftarrow 3C_0` & ``A.rescale_col(0, 3)``
         :meth:`rescale_row` &                   `R_0 \leftarrow 3R_0` & ``A.rescale_row(0, 3)``
         :meth:`set_col_to_multiple_of_col` &    `C_0 \leftarrow 3C_2` & ``A.set_col_to_multiple_of_col(0,2,3)``
         :meth:`set_row_to_multiple_of_row` &    `R_0 \leftarrow 3R_2` & ``A.set_row_to_multiple_of_col(0,2,3)``
         :meth:`swap_columns` &                  `C_0 \leftrightarrow C_2` & ``A.swap_columns(0,2)``
         :meth:`swap_rows` &                     `R_0 \leftrightarrow R_2` & ``A.swap_rows(0,2)``

      .. csv-table:: Elementary Operations
         :header: "Row operation", "Example"
         :delim: &

         `C_2 \leftarrow C_2 -4C_1` & ``A.add_multiple_of_column(2,1,-4)``
         `R_2 \leftarrow R_2 -4R_1` & ``A.add_multiple_of_row(2,1,-4)``
         `C_0 \leftarrow 3C_0` & ``A.rescale_col(0, 3)``
         `R_0 \leftarrow 3R_0` & ``A.rescale_row(0, 3)``
         `C_0 \leftarrow 3C_2` & ``A.set_col_to_multiple_of_col(0,2,3)``
         `R_0 \leftarrow 3R_2` & ``A.set_row_to_multiple_of_col(0,2,3)``
         `C_0 \leftrightarrow C_2` & ``A.swap_columns(0,2)``
         `R_0 \leftrightarrow R_2` & ``A.swap_rows(0,2)``


   #. The :meth:`pivots` method returns the indices of the pivot
      columns and :meth:`nonpivots` returns the indices of the
      nonpivot columns. The :meth:`pivot_rows` method returns the
      indices of a topmost subset of the rows that span the row space
      and are linearly independent.

      ..  ::

        sage: A = matrix(QQ, [[0,0,0,0],[1,2,3,4],[2,4,6,8],[3,5,4,3]]); A.rref()
        [  1   0  -7 -14]
        [  0   1   5   9]
        [  0   0   0   0]
        [  0   0   0   0]
        sage: A.pivots(), A.nonpivots(), A.pivot_rows()
        ((0, 1), (2, 3), (1, 3))
        sage: A[:,A.pivots()] # get the pivot columns
        [0 0]
        [1 2]
        [2 4]
        [3 5]
        sage: A[A.pivot_rows(),:] # get the pivot rows
        [1 2 3 4]
        [3 5 4 3]



#. **Solving systems**: Sage has specialized methods for solving
   systems of linear equations over a variety of rings, which can be
   significantly more efficient and stable than inverting a matrix.
   To solve a system of linear equations of the form `A\textbf x =
   \textbf b` or `AX = B` (`X` and `B` matrices), use the matrix
   :meth:`solve_right` method or the synonymous backslash syntax ``A \
   b``. The :meth:`solve_left` method solves equations of the form
   `\textbf xA = \textbf b` or `XA = B`.

   .. ::
   .. sage: A * X
   .. [5 1 0]
   .. [6 0 1]

   .. #. Use the :meth:`solve_left` method to solve a system of equations of
      the form `\textbf xA = b` or `XA = B`. ::

       sage: A = matrix(QQ, 2, [1,2,3,4]); b = vector(QQ, [5,6])
       sage: x = A.solve_left(b); x * A == b
       True

#. **Left vs. Right**: Sage can do many calculations dealing with
   right (`A\textbf x`) or left (`\textbf xA`) matrix-vector products.
   The right or left tells which side the vector is on.  Typically,
   "right" computations return vectors of interest as columns, while
   "left" computations return vectors of interest as rows.  *Warning*:
   Sage typically defaults to left versions of commands (e.g.,
   ``A.kernel()`` is ``A.left_kernel()``).  Use the right or left
   versions of commands below to be explicit.

   .. .. _Right vs. Left:
   .. csv-table::
      :header: Right: `A \\textbf x=\\textbf b`, Left: `\\textbf x A=\\textbf b`

       :meth:`right_eigenmatrix`,   :meth:`left_eigenmatrix`
       :meth:`right_eigenspaces`,   :meth:`left_eigenspaces`
       :meth:`right_eigenvectors`,  :meth:`left_eigenvectors`
       :meth:`right_kernel`,       :meth:`left_kernel`
       :meth:`right_nullity`,      :meth:`left_nullity`
       :meth:`solve_right`,        :meth:`solve_left`

#. **Indexing**: Sage supports very flexible ways of getting and
   setting elements of matrices.  ``A[i,j]`` returns the entry in row
   `i` and column `j` (indices start at zero).  The table below gives
   some general patterns for the index syntax, which is similar to
   NumPy or MATLAB syntax.  If an index is negative, it counts
   backwards from the last index (e.g., ``A[-1,:]`` is the last row),
   and if a step size is negative, it indicates a count down (e.g.,
   ``A[::-1,:]`` gives a new matrix with the rows reversed). See the
   Sage reference manual on matrix indexing,
   http://www.sagemath.org/doc/reference/sage/matrix/docs.html#indexing.

   .. _index notation: 
   .. csv-table:: Index notation 
      :header: Index, Description 
      :delim: &

      ``i`` & index `i`
      ``:`` & all indices
      ``i:`` & indices from `i` to the end
      ``:j`` & indices up to, but not including, `j`
      ``i:j`` & indices from `i` up to, but not including, `j`
      ``i:j:s`` & every `s` th index from `i` up to, but not including, `j`
      negative  & count backwards from the last index
      list & explicit list of indices, possibly with repeats and reorderings

   .. .. todo: :
     vectors do not have the same fancy indexing as matrices

   .. .. note:: it would be fantastic if we supported other fancy indexing
    like numpy, something like indexing by boolean vectors, etc.

   .. .. todo: : should I have i's and j's in the table below, or should the examples really just be numbers?

   .. full table for sage documentation
   .. .. csv-table:: Retrieving parts of a matrix
     :header: Method, Description, Use, Equivalent indexing, Notes
     :delim: &

     :meth:`matrix_from_columns` & construct a matrix with specified columns & ``A.matrix_from_columns([2,3])`` & ``A[:,[2,3]]`` & columns can repeated, reordered, etc.
     :meth:`matrix_from_rows` & construct a matrix with specified rows & ``A.matrix_from_rows([2,3])`` & ``A[[2,3],:]`` & rows can be repeated, reordered, etc.
     :meth:`matrix_from_rows_and_columns` & construct a matrix with specified rows and columns & ``A.matrix_from_rows_and_columns([2,3],[3,4])`` & ``A[[2,3],[3,4]]`` & rows and columns can be repeated, reordered, etc.
     :meth:`submatrix` & construct a submatrix & ``A.submatrix(i,j,nrows,ncols)`` & ``A[i:i+nrows, j:j+ncols]``
     :meth:`column` & return a column as a vector & ``A.column(i)`` & ``A[:,i]`` & indexing returns the column as a single-column matrix
     :meth:`columns` & return specified columns as a list of vectors & ``A.columns([2,3])`` & ``A[:[2,3]]`` & indexing returns a matrix with the specified columns
     :meth:`row` & return a row as a vector & ``A.row(i)`` & ``A[i,:]`` & indexing returns the row as a single-row matrix
     :meth:`rows` & return specified rows as a list of vectors & ``A.rows([2,3])`` & ``A[[2,3],:]`` & indexing returns a matrix with the specified rows


   In the methods below, rows and column lists can contain repeated or
   reordered indices.  The rows and columns methods at the end of the
   table below return vectors or lists of vectors, while the
   equivalent index notation returns submatrices.  The second table
   below indicates how to change submatrices using methods or indexing
   notation.

   .. abbreviated table for HLA
   .. csv-table:: Retrieving parts of a matrix
     :header: Method, Equivalent indexing
     :delim: &

     ``A.diagonal()`` & None
     ``A.matrix_from_columns([2,3])`` & ``A[:,[2,3]]``
     ``A.matrix_from_rows([2,3])`` & ``A[[2,3],:]`` 
     ``A.matrix_from_rows_and_columns([2,3],[3,4])`` & ``A[[2,3],[3,4]]``
     ``A.submatrix(i,j,nrows,ncols)`` & ``A[i:i+nrows, j:j+ncols]``
     ``A.column(i)`` & ``A[:,i]``
     ``A.columns([2,3])`` & ``A[:[2,3]]`` 
     ``A.row(i)`` & ``A[i,:]`` 
     ``A.rows([2,3])`` & ``A[[2,3],:]`` 

   .. Full table for Sage documentation
   .. .. csv-table:: Changing parts of a matrix
     :header: Method, Description, Use, Equivalent indexing
     :delim: &

     :meth:`set_block` & change a submatrix to a given matrix ``B`` & ``A.set_block(i,j,B)`` & ``A[i:i+B.nrows(), j:j+B.ncols()]=B``
     :meth:`set_column` & set a column to given entries & ``A.set_column(i, [2,1,3])`` & ``A[:,i]=vector([2,1,3])`` or ``A[:,i]=[[2],[1],[3]]``
     :meth:`set_row` & set a row to given entries & ``A.set_row(i, [2,1,3])`` & ``A[i,:]=vector([2,1,3])`` or ``A[i,:]=[[2,1,3]]``

   .. abbreviated table for HLA
   .. csv-table:: Changing parts of a matrix
     :header: Method, Equivalent indexing
     :delim: &

     ``A.set_block(i,j,B)`` & ``A[i:i+B.nrows(), j:j+B.ncols()]=B`` (`B` a matrix)
     ``A.set_column(i, [2,1,3])`` & ``A[:,i]=vector([2,1,3])`` or ``A[:,i]=[[2],[1],[3]]``
     ``A.set_row(i, [2,1,3])`` & ``A[i,:]=vector([2,1,3])`` or ``A[i,:]=[[2,1,3]]``

#. **Sparse Matrices**: In order to handle large sparse matrices, Sage
   can store any matrix in a compressed way so that only the nonzero
   entries are stored.  Create a sparse matrix by specifying
   ``sparse=True`` when the matrix is created.  Matrices initialized
   from a Python dictionary defaults to sparse.  The
   included SciPy Python package also has many resources for dealing
   with sparse matrices.

   .. ::

       sage: A = random_matrix(QQ, 1000, density=0.01, sparse=True)  # create 1000 by 1000 matrix
       sage: A.density().n()  # ratio of nonzero entries to size of A
       0.009940...
       sage: len(A.nonzero_positions()) # number of entries actually stored
       9940


#. **Decompositions**: A variety of matrix decompositions are
   available in Sage, and many are available with algorithms for both
   exact and numerical matrices.  Typically the return value is a
   tuple of matrices that can be used to reconstruct the matrix
   (except Jordan form, which requires explicitly asking for the
   transformation matrix).

   Some exact algorithms require the base ring of the matrix to have
   certain properties, such as containing square roots.  In other
   cases, the matrix must have certain properties, such as having a
   characteristic polynomial that factors.  These conditions are
   listed in the "Base ring must contain" column.

   Sage implements the algebraically-closed field of algebraic
   numbers, ``QQbar``, so some decompositions applied to matrices of
   rational numbers will automatically return matrices with entries
   from ``QQbar`` as necessary (e.g., Cholesky).  On the other
   hand, ``jordan_form`` will simply fail if there are eigenvalues
   outside the base ring.

   .. warning ``schur`` does not work for QQ.  Are there decompositions
      that don't work nicely for some reason?  Also, it would be great
      to show how to get the exact value (with square roots, for
      example) from QQbar if, for example, you had a root of a
      quadratic.

   Matrices over ``RDF`` and ``CDF`` use specialized numerical
   algorithms for the LU, QR, SVD, Schur, and Cholesky factorizations;
   see :ref:`Numerical Linear Algebra`.

   .. csv-table:: Matrix decompositions
      :header: "Name", "Method", "Base ring must contain"
      :delim: &

      LU, Triangular  &  :meth:`LU`  &  Fraction
      QR, Gram-Schmidt  &  :meth:`QR`  &  Fraction, Square Roots
      SVD, Singular Value  &  :meth:`SVD`  &
      Schur  &  :meth:`schur`  &
      Cholesky, Square Root &  :meth:`cholesky`  &  Square Roots
      Jordan Form &  :meth:`jordan_form`  &  Eigenvalues
      Rational Canonical Form (Invariant Factors) &  :meth:`rational_form`  &  Field
      Smith Form  &  :meth:`smith_form`  &  Principal Ideal Domain
      Symplectic Form  &  :meth:`symplectic_form`  &  Field
      Subspace Decomposition  &  :meth:`decomposition`  &  Factored characteristic polynomial

   .. .. csv-table:: Matrix decompositions
      :header: "Name", "Method", "Exact", "Numerical"
      :delim: &

      LU, Triangular  &  :meth:`LU`  &  Fraction  &  X
      QR, Gram-Schmidt  &  :meth:`QR`  &  Fraction, Square Roots  &  X
      SVD, Singular Value  &  :meth:`SVD`  &   &  X
      Schur, Orthonormal Diagonalization  &  :meth:`schur`  &  &  X
      Cholesky, Square Root &  :meth:`cholesky_decomposition`  &  Square Roots  &  X
      Jordan Form &  :meth:`jordan`  &  Eigenvalues  &
      Rational, Frobenius Form &  :meth:`rational_form`  &  Field  &
      Smith Form  &  :meth:`smith_form`  &  Principal Ideal Domain  &
      Symplectic Form  &  :meth:`symplectic_form`  &  Field  &
      Subspace Decomposition  &  :meth:`decomposition`  &  Factored characteristic polynomial  &





Examples
--------


#. Constructing matrices. ::

     sage: matrix(QQ, [[1,0,1],[2,0,-1]])  # also matrix(QQ, 2, 3, [1,0,1,2,0,-1])
     [ 1  0  1]
     [ 2  0 -1]
     sage: u = vector(QQ, [2,3]); v = vector(QQ, [5,0]); w = vector(QQ, [-1,2])
     sage: column_matrix([u,v,w])
     [ 2  5 -1]
     [ 3  0  2]
     sage: def vandermonde(R, v): return matrix(R, len(v), lambda i,j: v[i]^j)
     sage: vandermonde(QQ, [2,3,4])
     [ 1  2  4]
     [ 1  3  9]
     [ 1  4 16]
     sage: def hilbert(R,n): return matrix(R, n, lambda i,j: 1/(i+j+1))
     sage: hilbert(QQ, 3)
     [  1 1/2 1/3]
     [1/2 1/3 1/4]
     [1/3 1/4 1/5]

   .. ::

     sage: from scipy.linalg import toeplitz
     sage: matrix(QQ,toeplitz([1,2,3],[1,4,5,6]))
     [1 4 5 6]
     [2 1 4 5]
     [3 2 1 4]

     sage: A=matrix(QQ, 2, 3, [1,2,3,4,5,6])
     sage: M = A.matrix_space(); M
     Full MatrixSpace of 2 by 3 dense matrices over Rational Field
     sage: M([1,0,4,3,2,1])
     [1 0 4]
     [3 2 1]


#.  Constructing block matrices. ::

     sage: A = matrix(QQ, [[-1,1],[0,-1]]);  B = matrix(QQ, [[1,-1/2]])
     sage: block_matrix(QQ, [[A,1],[0,B]])
     [  -1    1|   1    0]
     [   0   -1|   0    1]
     [---------+---------]
     [   0    0|   1 -1/2]
     sage: block_diagonal_matrix([A,B], subdivide=False)
     [  -1    1    0    0]
     [   0   -1    0    0]
     [   0    0    1 -1/2]
     sage: A.augment(vector(QQ, [1,-1/2]), subdivide=True)
     [  -1    1|   1]
     [   0   -1|-1/2]
     sage: A.stack(B)
     [  -1    1]
     [   0   -1]
     [   1 -1/2]

    We can subdivide an existing matrix to get a block matrix.  Here, we
    subdivide just before row 2 and just before columns 1 and 3 (remember
    indices start at 0).  ::

     sage: C = matrix(QQ, 3, 5, range(15))
     sage: C.subdivide([2],[1,3]); C
     [ 0| 1  2| 3  4]
     [ 5| 6  7| 8  9]
     [--+-----+-----]
     [10|11 12|13 14]
     sage: C.subdivision(0,2) # block (0,2)
     [3 4]
     [8 9]
     sage: C.subdivision_entry(0,2,0,1) # entry (0,1) in block (0,2)
     4
     sage: C * C.transpose() # arithmetic preserves block structure if possible
     [ 30  80|130]
     [ 80 255|430]
     [-------+---]
     [130 430|730]

#. Properties of a matrix. ::

     sage: A = matrix(QQ, 2, [0,-1,2,-2]); A, A.I, A.T, A.find(lambda x: x<0)
     (
     [ 0 -1]  [ -1 1/2]  [ 0  2]  [0 1]
     [ 2 -2], [ -1   0], [-1 -2], [0 1]
     )
     sage: A.find(lambda x: x<0, indices=True)
     {(0, 1): -1, (1, 1): -2}
     sage: A.change_ring(RDF).exp() # use RDF for numeric calculations
     [    0.508325986 -0.309559875653]
     [ 0.619119751306 -0.110793765307]
     sage: A.norm(), A.norm(1), A.norm(Infinity), A.norm('frob')
     (2.92080962648, 3.0, 4.0, 3.0)

   .. ::

     sage: A = matrix(QQ, 2, [0,-1,2,-2]); A.iterates(vector([1,2]), 4, rows=False)  # v, A * v, A^2 * v, ...
     [ 1 -2  2  0]
     [ 2 -2  0  4]


   ::

     sage: A = diagonal_matrix([2,2,5])
     sage: A.charpoly(), A.minpoly()
     (x^3 - 9*x^2 + 24*x - 20, x^2 - 7*x + 10)
     sage: A.minors(2)
     [4, 0, 0, 0, 10, 0, 0, 0, 10]
     sage: A.det(), A.rank(), A.trace(), A.permanent(), A.permanental_minor(2)
     (20, 3, 9, 20, 24)

#. Like many computer algebra systems, row-reducing a symbolic matrix
   using the :meth:`rref` method assumes that we are working over a
   field (i.e., that if ``c`` is any nonzero element of the base ring,
   then ``1/c`` is also in the base ring).  Since Sage can also work
   with matrices over general rings (which may not be fields), we can
   ask Sage to do operations without assuming that we can divide.  For
   example, if a matrix has entries in a polynomial ring, we can ask
   for the :meth:`echelon_form` of the matrix, which only uses
   operations in the polynomial ring (e.g., Sage won't divide except
   by constants).  We can use the :meth:`matrix_over_field`
   method to get a copy of a matrix over the fraction field of its
   base ring. ::

     sage: R.<c1,c2,c3> = QQ[] # construct a polynomial ring with 3 variables
     sage: A = matrix([[1,1,2,c1], [1,0,1,c2], [2,1,3,c3]]); A
     [ 1  1  2 c1]
     [ 1  0  1 c2]
     [ 2  1  3 c3]
     sage: A.rref() # works over fraction field of R, so 1/c1 exists, etc.
     [1 0 1 0]
     [0 1 1 0]
     [0 0 0 1]
     sage: A.echelon_form() # uses only operations in the polynomial ring R
     [            1             0             1            c2]
     [            0             1             1       c1 - c2]
     [            0             0             0 -c1 - c2 + c3]
     sage: B = A.matrix_over_field(); B.base_ring()
     Fraction Field of Multivariate Polynomial Ring in c1, c2, c3 over Rational Field
     sage: B.echelon_form() == A.rref()
     True

#. We can easily get pivot columns. ::

        sage: A = matrix(QQ, [[1,2,3,4],[2,4,6,8],[3,5,4,3]]); A.rref()
        [  1   0  -7 -14]
        [  0   1   5   9]
        [  0   0   0   0]
        sage: A.pivots(), A.nonpivots(), A.pivot_rows()
        ((0, 1), (2, 3), (0, 2))
        sage: A[:,A.pivots()]  # get the pivot columns
        [1 2]
        [2 4]
        [3 5]
        sage: A[A.pivot_rows(),:]  # get the pivot rows
        [1 2 3 4]
        [3 5 4 3]

#. The :meth:`extended_echelon_form` method first augments an `m` by
   `n` matrix with an `m` by `m` identity matrix before computing the
   rref.  The result can also be subdivided by specifying
   ``subdivide=True``.  The four relations in the last two lines of
   this example are true in general. ::

     sage: A = matrix(QQ, 3, 3, [2,3,4,-1,2,4,1,5,8])
     sage: B = A.extended_echelon_form(subdivide=True); B
     [   1    0 -4/7|   0 -5/7  2/7]
     [   0    1 12/7|   0  1/7  1/7]
     [--------------+--------------]
     [   0    0    0|   1    1   -1]
     sage: C = B.subdivision(0, 0); C  # C is upper-left submatrix
     [   1    0 -4/7]
     [   0    1 12/7]
     sage: L = B.subdivision(1, 1); L  # L is lower-right submatrix
     [ 1  1 -1]
     sage: A.right_kernel() == C.right_kernel(), A.row_space() == C.row_space()
     (True, True)
     sage: A.column_space() == L.right_kernel(), A.left_kernel() == L.row_space()
     (True, True)

#. We solve systems of equations using ``solve_right`` or backslash
   notation. ::

     sage: A = matrix(QQ, 2, [1,2,3,4]); b = vector(QQ, [5,6])
     sage: x = A.solve_right(b); x  # also x = A \ b
     (-4, 9/2)
     sage: A * x == b
     True
     sage: B = matrix(QQ, 2, 3, [5,1,0,6,0,1])
     sage: X = A \ B; A * X == B  # also X = A.solve_right(B)
     True


#. To be able to compute an exact QR decomposition, we need a field
   that contains square roots, so we create a matrix with entries from
   ``QQbar``.  Sage uses specialized numerical algorithms if the
   matrix is over ``RDF``.

   .. ::

     sage: A = matrix(QQbar, 3, 3, [0..8])  # [0..8] is [0, 1, 2, ..., 8]
     sage: Q, R = A.QR()
     sage: Q
     [                   0   0.912870929175277?  0.4082482904638630?]
     [ 0.4472135954999580?  0.3651483716701108? -0.8164965809277260?]
     [ 0.8944271909999159? -0.1825741858350554?  0.4082482904638630?]
     sage: R
     [6.708203932499369?  8.04984471899925?  9.39148550549912?]
     [                 0 1.095445115010333? 2.190890230020665?]
     [                 0                  0                  0]
     sage: A == Q*R and Q.is_unitary()  # True if both conditions are True
     True

   ::

     sage: A = matrix(QQbar, 3, 3, [0..8])  # [0..8] is [0, 1, 2, ..., 8]
     sage: Q, R = A.QR(); A == Q*R and Q.is_unitary()  # True if both conditions are True
     True
     sage: B = matrix(RDF, 3, 3, [0..8])
     sage: Q, R = B.QR(); (A - Q*R).norm() < 10^-10 and Q.is_unitary()
     True

   .. We can compute the same decomposition using specialized numerical
      algorithms by using matrices over ``RDF``. ::


   .. :: 
     .. sage: Q.zero_at(10^-10).round(4)  # change small numbers to 0, round to 4 digits
     .. [    0.0  0.9129  0.4082]
     .. [-0.4472  0.3651 -0.8165]
     .. [-0.8944 -0.1826  0.4082]
     .. sage: R.zero_at(10^-10).round(4)
     .. [-6.7082 -8.0498 -9.3915]
     .. [    0.0  1.0954  2.1909]
     .. [    0.0     0.0     0.0]
     
   .. todo: : ``jordan_block`` does not take a ring, so we can't play
       with it very nicely (like stack it with a QQ matrix)





Eigenvalues and Eigenvectors
============================


Sage will compute exact eigenvalues, eigenvectors and eigenspaces
for matrices with entries from exact rings, and will compute
approximate eigenvalues and eigenvectors for matrices with
floating-point entries.  Both right and left variants of the
eigenvector methods are available; we will only discuss the right
variants.


Commands
--------

#. The :meth:`eigenvalues` method computes the eigenvalues.  If a
   matrix over ``QQ`` does not have rational eigenvalues, then the
   eigenvalues may be returned as algebraic numbers in ``QQbar`` (the
   algebraic completion of ``QQ``) and printed as numeric
   approximations followed by question marks.  The question mark
   indicates that the number is contained in the interval found by
   taking the last digit of the printed representation plus or minus
   one (e.g., ``3.25?`` represents an exact root in the interval
   `[3.24, 3.26]`).  We emphasize that a ``QQbar`` element is an exact
   root of a polynomial and the printed approximation indicates an
   interval containing the value, and so may be slower to work with
   than computing the eigenvalues numerically using an ``RDF`` or
   ``CDF`` matrix.
  
#. The :meth:`eigenvectors_right` method returns a list, each element
   of the form ``(eigenvalue, list of eigenvectors, algebraic
   multiplicity)``.  The :meth:`eigenspaces_right` method returns a
   list, each element of the form ``(eigenvalue, eigenspace)``, where
   the eigenspace is a Sage vector space.

#. The :meth:`eigenmatrix_right` method of a matrix `A` returns two
   matrices `D` and `P` such that `AP=PD`.  The eigenvalues are the
   diagonal of `D` and the corresponding eigenvectors are the columns
   of `P`.  Columns of zeros in `P` indicate that the geometric
   multiplicity of the eigenvalue is not equal to the algebraic
   multiplicity.



Examples
--------


#. We calculate various eigenvalues, eigenvectors, and eigenspaces.
   Numerical matrices always claim eigenvalues have multiplicity one
   since numerical error can easily fool multiplicity calculations
   (see :ref:`Numerical Linear Algebra`). ::

     sage: entries = [-8,21,74,-48,24,-7,-78,72,-12,6,44,-36,-4,-3,2,-4]
     sage: A = matrix(QQ, 4, 4, entries); A.eigenvalues()
     [5, 4, 8, 8]
     sage: A.eigenvectors_right()
     [(5, [ (1, -5/7, 2/7, -1/7) ], 1),
      (4, [ (1, -3/2, 3/4, 1/4) ], 1),
      (8, [ (1, 0, 0, -1/3), (0, 1, -1/2, -1/3) ], 2)]
     sage: A.eigenspaces_right()
     [
     (5, Vector space of degree 4 and dimension 1 over Rational Field ...),
     (4, Vector space of degree 4 and dimension 1 over Rational Field ...),
     (8, Vector space of degree 4 and dimension 2 over Rational Field ...)
     ]

#. The :meth:`eigenmatrix_right` method provides a very easy way to
   get corresponding lists of eigenvalues and eigenvectors using the
   :meth:`diagonal` and :meth:`columns` methods of matrices. ::

     sage: entries = [-8,21,74,-48,24,-7,-78,72,-12,6,44,-36,-4,-3,2,-4]
     sage: A = matrix(QQ, 4, 4, entries)
     sage: D, P = A.eigenmatrix_right(); D, P, A * P == P * D
     (
     [5 0 0 0]  [   1    1    1    0]
     [0 4 0 0]  [-5/7 -3/2    0    1]
     [0 0 8 0]  [ 2/7  3/4    0 -1/2]
     [0 0 0 8], [-1/7  1/4 -1/3 -1/3], True
     )
     sage: evals = D.diagonal(); evecs = P.columns()
     sage: A*evecs[0] == evals[0] * evecs[0]  # check first eigenvalue/eigenvector
     True

#. For matrices with rational entries, we can optionally ask that
   eigenspaces be reported just once per irreducible factor of the
   characteristic polynomial since the eigenspaces for each
   irreducible factor are related in a natural way. ::

    sage: A = matrix(QQ, 3, 3, [-7, 2, -22, 10, -3, 33, 3, -1, 10]); A.charpoly()
    x^3 + 1
    sage: A.eigenspaces_right(format='galois')
    [
    (-1, Vector space of degree 3 and dimension 1 over Rational Field ...),
    (a1, Vector space of degree 3 and dimension 1 over
    Number Field in a1 with defining polynomial x^2 - x + 1
    User basis matrix:
    [         1 1/2*a1 - 2       -1/2])
    ]

#. Even if Sage does not directly compute eigenvalues for matrices
   over some exotic ring, other tools may provide information you
   desire.  For example, the :meth:`fcp` method, which returns the
   factored characteristic polynomial, is often useful. ::

    sage: F.<a> = FiniteField(3^2); 
    sage: A = matrix(F, 3, 3, [2*a, a, 2*a, 0, 2, a + 2, 2, a, 2*a]); A.fcp()
    (x + a + 1) * (x^2 + a*x + 2)
    sage: (A - (-a-1)*identity_matrix(3)).right_kernel()  # an eigenspace
    Vector space of degree 3 and dimension 1 over Finite Field in a of size 3^2 ...





Vector Spaces
=============

You can use ``VectorSpace`` objects to work directly with vector
spaces.  

Definitions
-----------

#. The **basis matrix** of a vector space has the basis vectors of the
   vector space as its rows.  By default, Sage will store and use a
   canonical **echelonized** basis for a vector space (i.e., the basis
   matrix will be a matrix in reduced row echelon form).  A **user
   basis** can also be explicitly used (see below for examples).

#. Vectors in a vector space `V` over a field `F` also live in some
   **ambient vector space** `F^n`.  The degree of `V` is `n`.  The
   **dimension** or **rank** of `V` is the size of the basis.  A
   vector space is **full** if its degree equals its dimension.



Commands
--------
   

#. **Constructors**

   #. The simplest way to create a vector space is to raise a field to a
      power (in general, raising a ring to a power will construct a free
      module).  We can also use :class:`VectorSpace` directly by providing
      a field and a dimension.  
      
      .. ::

      .. sage: QQ^3
      .. Vector space of dimension 3 over Rational Field
      .. sage: ZZ^4  # ZZ is the ring of integers
      .. Ambient free module of rank 4 over the principal ideal domain Integer Ring
      .. sage: VectorSpace(RDF, 3)
      .. Vector space of dimension 3 over Real Double Field

   #. The :meth:`parent` method of a vector returns the vector space
      containing the vector.  
      
      .. ::

      .. sage: v = vector(QQ, [1,2,3])
      .. sage: V = v.parent(); V
      .. Vector space of dimension 3 over Rational Field

   #. The :func:`span` command constructs the vector space spanned by
      a list of vectors.  
      
      .. ::

      .. sage: v = vector(QQ, [1,2,3]); w = vector(QQ, [2,0,1])
      .. sage: V = span([v,w]); V
      .. Vector space of degree 3 and dimension 2 over Rational Field
      .. Basis matrix:
      .. [  1   0 1/2]
      .. [  0   1 5/4]

   #. Use the :meth:`subspace` method to construct subspaces.  The
      :meth:`~sage.modules.free_module.FreeModule_generic_field.subspace_with_basis`
      method allows specifying a "user basis".
      
      .. ::

      .. sage: v = vector(QQ, [1,2,3]); w = vector(QQ, [2,0,1])
      .. sage: S = span([v,w])
      .. sage: v+w
      .. (3, 2, 4)
      .. sage: T = S.subspace([v+w]); T  # the basis matrix is canonical
      .. Vector space of degree 3 and dimension 1 over Rational Field
      .. Basis matrix:
      .. [  1 2/3 4/3]
      .. sage: U = S.subspace_with_basis([v+w]); U
      .. Vector space of degree 3 and dimension 1 over Rational Field
      ..     User basis matrix:
      .. [3 2 4]

   .. todo: : make the subspace method take a basis argument, instead of
      having a subspace_with_basis function


#. **Properties**

      
      .. ::

      .. sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
      .. sage: W = span([u,v]); W
      .. Vector space of degree 3 and dimension 2 over Rational Field
      .. Basis matrix:
      .. [ 1  0 -1]
      .. [ 0  1  2]
      .. sage: V = W.ambient_vector_space(); V
      .. Vector space of dimension 3 over Rational Field
      .. sage: W.degree(), W.dimension(), W.rank()
      .. (3, 2, 2)
      .. sage: W.is_full(), V.is_full()
      .. (False, True)

   #. ``v in V`` tests if the vector `\textbf v` is in the vector
      space `V`.
   
   .. ::

      .. sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
      .. sage: W = span([u,v])
      .. sage: 2*u + 3*v in W
      .. True
      .. sage: vector(QQ, [3, 7, 195]) in W
      .. False

   #. Check if two vector spaces `V` and `W` are equal with ``V ==
      W``.  Check if `V` is a subspace of `W` using
      ``V.is_subspace(W)``.
      
      .. ::

      .. sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
      .. sage: x = vector(QQ, [2, 3, 4]); y = vector(QQ, [3, 4, 5])
      .. sage: W = span([u,v]); Z = span([x,y])
      .. sage: W == Z
      .. True
      .. sage: Y = W.subspace_with_basis([vector(QQ, [5, 6, 7])])
      .. sage: Y.is_subspace(Z)
      .. True

   #. The basis (canonical basis) of a vector space is returned by the
      :meth:`basis` (:meth:`echelonized_basis`) method.  The
      corresponding :meth:`basis_matrix` and
      :meth:`echelonized_basis_matrix` methods return matrices in
      which the basis vectors are the rows.
      
      .. ::

      .. sage: v = vector(QQ, [1,2,3]); w = vector(QQ, [2,0,1])
      .. sage: V = (QQ^3).subspace_with_basis([v,w])
      .. sage: V.basis()  # as a sequence of vectors
      .. [
      .. (1, 2, 3),
      .. (2, 0, 1)
      .. ]
      .. sage: V.basis_matrix()  # as a matrix (rows are basis vectors)
      .. [1 2 3]
      .. [2 0 1]

   #. An element of a vector space can be expressed as a linear
      combination of the basis vectors (which are canonical by
      default).  The scalars (i.e., coordinates) can be returned as a
      list (using the :meth:`coordinates` method) or as a vector
      (using the :meth:`coordinate_vector` method).
      
      .. ::

      .. sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1]); x = 3*u - 7*v
      .. sage: W = span([u,v]); W
      .. Vector space of degree 3 and dimension 2 over Rational Field
      .. Basis matrix:
      .. [ 1  0 -1]
      .. [ 0  1  2]
      .. sage: W.coordinates(x)  # relative to the canonical basis
      .. [10, 6]
      .. sage: W.coordinate_vector(x)
      .. (10, 6)
      .. sage: X = (QQ^3).subspace_with_basis([u, v]); X
      .. Vector space of degree 3 and dimension 2 over Rational Field
      .. User basis matrix:
      .. [ 1  2  3]
      .. [-1  0  1]
      .. sage: X.coordinate_vector(x)  # relative to the user basis
      .. (3, -7)
       sage: W.linear_dependence([3*u + v, u - v]) == []
       True
       sage: W.linear_dependence([10*u + 20*v, u + 2*v])
       [
       (1, -10)
       ]
       sage: 1*(10*u + 20*v) - 10*(u + 2*v)
       (0, 0, 0)

      .. #. Conversely, we can compute a linear combination of a basis. 
   
      .. ::

      .. sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
      .. sage: x = 3*u - 7*v
      .. sage: W = span([u,v])
      .. sage: W.linear_combination_of_basis([10, 6])
      .. (10, 6, 2)
      .. sage: X = (QQ^3).subspace_with_basis([u, v])
      .. sage: X.linear_combination_of_basis([3, -7])
      .. (10, 6, 2)

   #. The :meth:`linear_dependence` method takes a list of vectors and
      returns the coefficients of a nontrivial linear combination that
      equals zero.  An empty sequence is returned if the vectors are
      linearly independent.  
      
      .. ::

      .. sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
      .. sage: W = span([u,v])
      .. sage: W.linear_dependence([3*u + v, u - v]) == []
      .. True
      .. sage: W.linear_dependence([10*u + 20*v, u + 2*v])
      .. [
      .. (1, -10)
      .. ]
      .. sage: 1*(10*u + 20*v) - 10*(u + 2*v)
      .. (0, 0, 0)

   .. todo: : make inner products work well with things. What needs to be done?


#. We can intersect two vector spaces (``U.intersection(V)``), add
   them (``U + V``), form their direct sum (``U.direct_sum(V)``), and
   take their quotient (``U / V``).
      
      .. ::

      .. sage: u = vector(QQ, [1, 2, 2]); v = vector(QQ, [-1, 0, 4]); w = vector(QQ, [2, 1, 5])
      .. sage: U = span([u + v, u - 3*v]); W = span([v + w, 5*v - 6*w])
      .. sage: U.intersection(W)
      .. Vector space of degree 3 and dimension 1 over Rational Field
      .. Basis matrix:
      .. [ 1  0 -4]
      .. sage: U + W
      .. Vector space of degree 3 and dimension 3 over Rational Field
      .. Basis matrix:
      .. [1 0 0]
      .. [0 1 0]
      .. [0 0 1]
      .. sage: U.direct_sum(W)
      .. Vector space of degree 6 and dimension 4 over Rational Field
      .. Basis matrix:
      .. [  1   0  -4   0   0   0]
      .. [  0   1   3   0   0   0]
      .. [  0   0   0   1   0  -4]
      .. [  0   0   0   0   1  13]

   .. #. We can also quotient a vector space by a subspace using the division operator ``/``. 
   
      .. ::

      .. sage: u = vector(QQ, [1, 2, 2, 5, 3]); v = vector(QQ, [-1, 0, 4, 3, 1])
      .. sage: U = span([u, v])
      .. sage: Q = (QQ^5).quotient(U); Q.dimension()
      .. 3
      .. sage: phi = Q.quotient_map(); phi
      .. Vector space morphism represented by the matrix:
      .. [   1    0    0]
      .. [   0    1    0]
      .. [   0    0    1]
      .. [   1  1/2 -5/2]
      .. [  -2 -3/2  7/2]
      .. Domain: Vector space of dimension 5 over Rational Field
      .. Codomain: Vector space quotient V/W of dimension 3 over Rational Field where
      .. V: Vector space of dimension 5 over Rational Field
      .. W: Vector space of degree 5 and dimension 2 over Rational Field
      .. Basis matrix:
      .. [ 1  0 -4 -3 -1]
      .. [ 0  1  3  4  2]
      .. sage: phi.kernel() == U
      .. True

   


Examples
--------
   
#. Create a vector space, or more generally, a free module like ``ZZ^3``. ::

    sage: QQ^3
    Vector space of dimension 3 over Rational Field
    sage: VectorSpace(RDF, 3)
    Vector space of dimension 3 over Real Double Field
    
   .. ::

    sage: v = vector(RDF, [1,2,3]); v.parent()  # the vector space v is in
    Vector space of dimension 3 over Real Double Field
    sage: ZZ^4  # ZZ is the ring of integers
    Ambient free module of rank 4 over the principal ideal domain Integer Ring

#. Construct subspaces. ::

    sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-3, 0, 3])
    sage: S = span([u,v]); S  # basis echelonized, not (u,v)
    Vector space of degree 3 and dimension 2 over Rational Field
    Basis matrix:
    [ 1  0 -1]
    [ 0  1  2]
    sage: T = S.subspace([u + v]); T  # the basis matrix is canonical
    Vector space of degree 3 and dimension 1 over Rational Field
    Basis matrix:
    [ 1 -1 -3]
    sage: U = S.subspace_with_basis([u + v]); U  # basis not echelonized
    Vector space of degree 3 and dimension 1 over Rational Field
    User basis matrix:
    [-2 2 6]

#. Properties of vector spaces. ::

     sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
     sage: W = span([u,v]); V = W.ambient_vector_space()
     sage: W.degree(), W.dimension(), W.rank(), W.is_full(), V.is_full(), V == QQ^3
     (3, 2, 2, False, True, True)
     sage: S = span([v]); S.is_subspace(W), S == span([-v])
     (True, True)

   .. #. Relationships between vector spaces. ::

     sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1])
     sage: x = vector(QQ, [2, 3, 4]); y = vector(QQ, [3, 4, 5])
     sage: W = span([u,v]); Z = span([x,y])
     sage: W == Z
     True
     sage: Y = span([u + x])
     sage: Y.is_subspace(Z)
     True

#. Vectors as elements of vector spaces.  The :meth:`coordinates`
   method below returns a Python list, while the
   :meth:`coordinate_vector` method returns an actual vector. ::

     sage: u = vector(QQ, [1, 2, 3]); v = vector(QQ, [-1, 0, 1]); x = 3*u - 7*v
     sage: W = span([u,v]); W
     Vector space of degree 3 and dimension 2 over Rational Field ...
     sage: x in W, vector(QQ, [3, 7, 195]) in W
     (True, False)
     sage: W.coordinates(x), W.coordinate_vector(x)  # relative to the canonical basis
     ([10, 6], (10, 6))
     sage: X = (QQ^3).subspace_with_basis([u, v]); X
     Vector space of degree 3 and dimension 2 over Rational Field
     User basis matrix:
     [ 1  2  3]
     [-1  0  1]
     sage: X.coordinate_vector(x)  # relative to the user basis
     (3, -7)
     sage: X.linear_combination_of_basis([3, -7])
     (10, 6, 2)

#. Vector space arithmetic. ::

     sage: u = vector(QQ, [1,2,2]); v = vector(QQ, [-1,0,4]); w = vector(QQ, [2,1,5])
     sage: U = span([u + v, u - 3*v]); W = span([v + w, 5*v - 6*w])
     sage: U.intersection(W)
     Vector space of degree 3 and dimension 1 over Rational Field ...
     sage: U + W
     Vector space of degree 3 and dimension 3 over Rational Field ...
     sage: U.direct_sum(W)
     Vector space of degree 6 and dimension 4 over Rational Field ...

   ::

     sage: u = vector(QQ, [1,2,2,5,3]); v = vector(QQ, [-1,0,4,3,1])
     sage: U = span([u, v]); Q = (QQ^5).quotient(U); Q.dimension()
     3
     sage: phi = Q.quotient_map(); phi
     Vector space morphism ...
     sage: phi.kernel() == U
     True
       




Linear Transformations
======================

Commands
--------

#. If `A` is a matrix, ``linear_transformation(A)`` constructs the
   transformation `\textbf x \mapsto \textbf xA`.  *Warning*: Notice
   again the preference for a product with the vector on the left.  The 
   domain and codomain are inferred from the base ring and matrix
   dimensions. Create the linear transformation `\textbf x \mapsto
   \textbf A\textbf x` by ``linear_transformation(A, side='right')``,
   which just transposes `A` to create a left-sided version; the
   matrix stored and printed by the linear transformation is
   understood as the left version.
      
   .. ::

   .. sage: A = matrix(QQ, 2, 3, range(6)); A
   .. [0 1 2]
   .. [3 4 5]
   .. sage: T = linear_transformation(A); T
   .. Vector space morphism represented by the matrix:
   .. [0 1 2]
   .. [3 4 5]
   .. Domain: Vector space of dimension 2 over Rational Field
   .. Codomain: Vector space of dimension 3 over Rational Field
   .. sage: U = linear_transformation(A, side='right'); U
   .. Vector space morphism represented by the matrix:
   .. [0 3]
   .. [1 4]
   .. [2 5]
   .. Domain: Vector space of dimension 3 over Rational Field
   .. Codomain: Vector space of dimension 2 over Rational Field
   .. sage: v = vector(QQ, [2,3,1])
   .. sage: U(v) == A * v
   .. True

   ..   #. We can give the domain and codomain explicitly, which may have
   ..      explicit user bases.  The matrix is interpreted (and printed) as
   ..      the representation relative to the bases of the domain and
   ..      codomain.
   ..
   ..       sage: V = (QQ^2).subspace_with_basis([vector(QQ, [-1, 1])])
   ..       sage: W = (QQ^3).subspace_with_basis([vector(QQ, [0,1,0]), vector(QQ, [0,0,1])])
   ..       sage: A = matrix(QQ, [[2,5]])
   ..       sage: T = linear_transformation(V, W, A); T
   ..       Vector space morphism represented by the matrix:
   ..       [2 5]
   ..       Domain: Vector space of degree 2 and dimension 1 over Rational Field
   ..       User basis matrix:
   ..       [-1  1]
   ..       Codomain: Vector space of degree 3 and dimension 2 over Rational Field
   ..       User basis matrix:
   ..       [0 1 0]
   ..       [0 0 1]
   ..       sage: v = vector(QQ, [-4, 4])  # a vector in the domain V
   ..       sage: T(v)
   ..       (0, 8, 20)
   ..       sage: V.coordinate_vector(v)*T.matrix()*W.basis_matrix()  # more conventionally
   ..       (0, 8, 20)

#. We can specify the rule for a linear transformation using a lambda
   function, a Python function defined with the ``def`` keyword, a
   symbolic function, or by a list of images for the elements of the
   domain's basis in place of the matrix `A`.  
      
   .. We illustrate the first and last.

   .. sage: f = lambda x: vector(QQ, [2*x[0] + x[2], 5*x[1] - 6*x[2]])
   .. sage: T = linear_transformation(QQ^3, QQ^2, f); T
   .. Vector space morphism represented by the matrix:
   .. [ 2  0]
   .. [ 0  5]
   .. [ 1 -6]
   .. Domain: Vector space of dimension 3 over Rational Field
   .. Codomain: Vector space of dimension 2 over Rational Field

   .. sage: images = [vector(QQ, [1,2]), vector(QQ, [-2,4])]
   .. sage: T = linear_transformation(QQ^2, QQ^2, images); T
   .. Vector space morphism represented by the matrix:
   .. [ 1  2]
   .. [-2  4]
   .. Domain: Vector space of dimension 2 over Rational Field
   .. Codomain: Vector space of dimension 2 over Rational Field

   ..   #. We can use any base field, e.g., here we use a finite field of order 125. ::
   ..
   ..       sage: F.<a> = FiniteField(5^3)
   ..       sage: f = lambda x: a^2*x
   ..       sage: T = linear_transformation(F^2, F^2, f); T
   ..       Vector space morphism represented by the matrix:
   ..       [a^2   0]
   ..       [  0 a^2]
   ..       Domain: Vector space of dimension 2 over Finite Field in a of size 5^3
   ..       Codomain: Vector space of dimension 2 over Finite Field in a of size 5^3

#. If `T` is a linear transformation and `\textbf v` is a vector,
   ``T(v)`` computes the image of `\textbf v`.

   .. :: 

      .. sage: A = matrix(QQ, 2, 3, range(6))
      .. sage: T = linear_transformation(A)
      .. sage: T(vector(QQ, [-2, 3]))
      .. (9, 10, 11)
       
#. ``T.is_surjective()`` and ``T.is_injective()`` query properties of a transformation `T`.

#. ``T.image()``, ``T.kernel()``, and ``T.inverse_image(V)`` construct
   related vector spaces.

   .. The image and kernel of the linear transformation, and
   .. pre-images of subspaces, are returned as vector spaces.

   .. ::
   .. sage: A = matrix(QQ, 2, 3, range(6))
   .. sage: T = linear_transformation(A)
   .. sage: T.image()
   .. Vector space of degree 3 and dimension 2 over Rational Field
   .. Basis matrix:
   .. [ 1  0 -1]
   .. [ 0  1  2]

   .. sage: T.kernel()
   .. Vector space of degree 2 and dimension 0 over Rational Field
   .. Basis matrix:
   .. []

   .. sage: W = (QQ^3).subspace([vector(QQ, [2,3,4])])
   .. sage: T.inverse_image(W)
   .. Vector space of degree 2 and dimension 1 over Rational Field
   .. Basis matrix:
   .. [1 2]

#. Compose linear transformations by multiplying them together.

#. ``T.restrict_domain()`` and ``T.restrict_codomain()`` construct new transformations.   

      .. by restricting
      .. the domain or restricting the codomain.  
      .. Notice that the
      .. matrix representations of the restrictions are with respect
      .. to the echelonized bases of the new subspaces.  ::

      .. sage: A = matrix(QQ, [[2, 4, 2], [3, 6, 3]])
      .. sage: T = linear_transformation(A)
      .. sage: T(vector(QQ, [10, -15]))
      .. (-25, -50, -25)

      .. sage: new_domain = (QQ^2).subspace([vector(QQ, [2,-3])])
      .. sage: S = T.restrict_domain(new_domain); S
      .. Vector space morphism represented by the matrix:
      .. [-5/2   -5 -5/2]
      .. Domain: Vector space of degree 2 and dimension 1 over Rational Field
      .. Basis matrix:
      .. [   1 -3/2]
      .. Codomain: Vector space of dimension 3 over Rational Field
      .. sage: S(vector(QQ, [10, -15]))
      .. (-25, -50, -25)

      .. sage: new_codomain = (QQ^3).subspace([vector(QQ, [5,10,5])])
      .. sage: R = T.restrict_codomain(new_codomain); R
      .. Vector space morphism represented by the matrix:
      .. [2]
      .. [3]
      .. Domain: Vector space of dimension 2 over Rational Field
      .. Codomain: Vector space of degree 3 and dimension 1 over Rational Field
      .. Basis matrix:
      .. [1 2 1]
      .. sage: R(vector(QQ, [10, -15]))
      .. (-25, -50, -25)

..   #. By restricting both the domain and codomain with vector spaces
..      having specified bases, one can create new matrix representations. ::

..       sage: A = matrix(QQ, [[3,1,-2],[4,2,0]])
..       sage: T = linear_transformation(A)
..       sage: T(vector(QQ, [2,-4]))
..       (-10, -6, -4)

..       sage: BD = [vector(QQ, [-1,2]), vector(QQ, [-2,3])]
..       sage: D = (QQ^2).subspace_with_basis(BD)
..       sage: BC = [vector(QQ, [-1,0,2]), vector(QQ, [-1,1,3]), vector(QQ, [1,-4,-7])]
..       sage: C = (QQ^3).subspace_with_basis(BC)
..       sage: S = T.restrict_domain(D).restrict_codomain(C)
..       sage: S.matrix()
..       [ 19 -33  -9]
..       [ 26 -44 -12]
..       sage: S(vector(QQ, [2,-4]))
..       (-10, -6, -4)
..       sage: D.basis_matrix()*T.matrix()*C.basis_matrix().I  # more conventional way to get S.matrix()
..       [ 19 -33  -9]
..       [ 26 -44 -12]


   .. #. An alternative approach uses the :meth:`restrict_domain` and
   ..    :meth:`restrict_codomain` methods of a matrix.  If a matrix
   ..    describes a linear transformation `\textbf x \mapsto \textbf xA`, then
   ..    the matrix representing the transformation restricted to a subspace
   ..    `V` of the domain, relative to the basis of `V` in the domain, is
   ..    given by the matrix :meth:`restrict_domain` method. ::

   ..     sage: b0 = vector(QQ, [1,2,0]); b1 = vector(QQ, [0,1,0])
   ..     sage: V = (QQ^3).subspace_with_basis([b0,b1]); V
   ..     Vector space of degree 3 and dimension 2 over Rational Field
   ..     User basis matrix:
   ..     [1 2 0]
   ..     [0 1 0]
   ..     sage: A = matrix(QQ, 3, [1,2,0,3,4,0,0,0,0])
   ..     sage: B = A.restrict_domain(V); B
   ..     [ 7 10  0]
   ..     [ 3  4  0]
   ..     sage: (3*b0-b1)*A
   ..     (18, 26, 0)
   ..     sage: vector(QQ, [3,-1])*B
   ..     (18, 26, 0)

   ..    Similarly, if the image of the linear transformation is in a
   ..    subspace `V` of the codomain, the matrix representing the
   ..    transformation restricted to `V`, relative to the basis of `V` in
   ..    the codomain, is given by the matrix :meth:`restrict_codomain`
   ..    method. ::

   ..     sage: b0 = vector(QQ, [1,2,0]); b1 = vector(QQ, [0,1,0])
   ..     sage: V = (QQ^3).subspace_with_basis([b0,b1])
   ..     sage: A = matrix(QQ, 3, [1,2,0,3,4,0,0,0,0])
   ..     sage: B = A.restrict_codomain(V); B
   ..     [ 1  0]
   ..     [ 3 -2]
   ..     [ 0  0]
   ..     sage: v = vector([2,3,1])
   ..     sage: v*A
   ..     (11, 16, 0)
   ..     sage: v*B
   ..     (11, -6)
   ..     sage: 11*b0-6*b1
   ..     (11, 16, 0)

   ..    If a subspace `V` is invariant under linear transformation,
   ..    then the matrix representing the transformation restricted to `V`,
   ..    relative to the basis of `V`, is given by the matrix
   ..    :meth:`restrict` method. ::

   ..     sage: b0 = vector(QQ, [1,2,0]); b1 = vector(QQ, [0,1,0])
   ..     sage: V = (QQ^3).subspace_with_basis([b0,b1])
   ..     sage: A = matrix(QQ, 3, [1,2,0,3,4,0,0,0,0])
   ..     sage: B = A.restrict(V); B
   ..     [ 7 -4]
   ..     [ 3 -2]
   ..     sage: v = 3*b0-b1
   ..     sage: vector(QQ, [3,-1])*B
   ..     (18, -10)
   ..     sage: 18*b0-10*b1
   ..     (18, 26, 0)
   ..     sage: v*A
   ..     (18, 26, 0)

   ..    This provides an easy (and conceptual!) way to obtain a matrix for
   ..    a linear transformation relative to a given basis.  ::

   ..     sage: A = matrix(QQ, 3, [1,2,0,3,4,0,0,0,0])
   ..     sage: V = (QQ^3).subspace_with_basis([[1,2,1],[4,5,0],[0,2,1]])
   ..     sage: A.restrict(V)
   ..     [   -1     2     1]
   ..     [-17/5  28/5  17/5]
   ..     [ -2/5   8/5   2/5]
   ..     sage: V.basis_matrix()*A*(V.basis_matrix().I) # more conventional approach
   ..     [   -1     2     1]
   ..     [-17/5  28/5  17/5]
   ..     [ -2/5   8/5   2/5]


Examples
--------

   
#. Construct some linear transformations. ::

     sage: A = matrix(QQ, 2, 3, range(6)); A
     [0 1 2]
     [3 4 5]
     sage: T = linear_transformation(A); T
     Vector space morphism represented by the matrix:
     [0 1 2]
     [3 4 5]
     Domain: Vector space of dimension 2 over Rational Field
     Codomain: Vector space of dimension 3 over Rational Field
     sage: U = linear_transformation(A, side='right'); U
     Vector space morphism represented by the matrix:
     [0 3]
     [1 4]
     [2 5]
     Domain: Vector space of dimension 3 over Rational Field
     Codomain: Vector space of dimension 2 over Rational Field
     sage: v = vector(QQ, [2,3,1]); U(v) == A * v
     True

   We can give the domain and codomain explicitly.  The matrix is
   interpreted (and printed) as the representation relative to the
   bases of the domain and codomain. ::

     sage: V = (QQ^2).subspace_with_basis([vector(QQ, [-1, 1])])
     sage: W = (QQ^3).subspace_with_basis([vector(QQ, [0,1,0]), vector(QQ, [0,0,1])])
     sage: A = matrix(QQ, [[2,5]]); T = linear_transformation(V, W, A); T
     Vector space morphism represented by the matrix:
     [2 5]
     Domain: Vector space of degree 2 and dimension 1 over Rational Field ...
     Codomain: Vector space of degree 3 and dimension 2 over Rational Field
     User basis matrix:
     [0 1 0]
     [0 0 1]
     sage: v = vector(QQ, [-4, 4]); T(v)
     (0, 8, 20)
     sage: V.coordinate_vector(v) * T.matrix() * W.basis_matrix()  # check
     (0, 8, 20)

   The third argument may be a function or list of images instead of a matrix. ::

     sage: f = lambda x: vector(QQ, [2*x[0] + x[2], 5*x[1] - 6*x[2]])
     sage: T = linear_transformation(QQ^3, QQ^2, f); T
     Vector space morphism represented by the matrix:
     [ 2  0]
     [ 0  5]
     [ 1 -6]
     Domain: Vector space of dimension 3 over Rational Field
     Codomain: Vector space of dimension 2 over Rational Field

   ::

     sage: images = [vector(QQ, [1,2]), vector(QQ, [-2,4])]
     sage: T = linear_transformation(QQ^2, QQ^2, images); T
     Vector space morphism represented by the matrix:
     [ 1  2]
     [-2  4]
     Domain: Vector space of dimension 2 over Rational Field
     Codomain: Vector space of dimension 2 over Rational Field

#. Query properties of a linear transformation. ::

     sage: A = matrix(QQ, 2, 3, range(6))
     sage: T = linear_transformation(A)
     sage: T.is_surjective(), T.is_injective(), T.image() == T(QQ^2)
     (False, True, True)
     sage: T.image()
     Vector space of degree 3 and dimension 2 over Rational Field ...
     sage: T.kernel()
     Vector space of degree 2 and dimension 0 over Rational Field ...
     sage: W = (QQ^3).subspace([vector(QQ, [2,3,4])]); T.inverse_image(W)
     Vector space of degree 2 and dimension 1 over Rational Field ...

#. Composing and restricting linear transformations. ::

     sage: A = matrix(QQ, [[2, 4, 2], [3, 6, 3]])
     sage: T = linear_transformation(A); v = vector(QQ, [10, -15])
     sage: T(v)
     (-25, -50, -25)
     sage: U = linear_transformation(diagonal_matrix([1, 1/2, 1/5]))
     sage: (U * T)(v)
     (-25, -25, -5)

   ::

     sage: new_domain = (QQ^2).subspace([vector(QQ, [2,-3])])
     sage: S = T.restrict_domain(new_domain); S
     Vector space morphism represented by the matrix:
     [-5/2   -5 -5/2]
     Domain: Vector space of degree 2 and dimension 1 over Rational Field ...
     Codomain: Vector space of dimension 3 over Rational Field
     sage: S(vector(QQ, [10, -15]))
     (-25, -50, -25)

   Note that the matrix representations of the restrictions are with
   respect to the echelonized bases of the new subspaces.




Graphics
========

Sage has extensive capabilities for drawing 2D and 3D pictures and
graphs.  We demonstrate just a few of these capabilities here; see the
Sage documentation for many more plotting capabilities.

Examples
--------

#. **Vectors**: ``v.plot(start=u)`` plots a vector `\textbf v`
   starting at `\textbf u`.  Adding graphics objects superimposes
   them. Use :func:`show` to show a plot or use the :meth:`save`
   method of a graphics object to save the plot to a file.  We can
   save plots in a variety of formats (e.g., png, jpg, pdf, eps, svg,
   etc.).  See :ref:`vectorplot`. ::

     sage: u = vector(QQ, [1,2]); v = vector(QQ, [1,-1])
     sage: p = v.plot() + u.plot(start=v) + (u+v).plot(linestyle='dashed')
     sage: show(p) # show picture
     sage: p.save('vectorplot.pdf') # save as a pdf file

   .. Sage commands to generate figure in black and white. ::

        sage: u = vector(QQ, [1,2]); v = vector(QQ, [1,-1]); offset = vector([0.1,0])
        sage: p = v.plot(color='black')+u.plot(start=v,color='black')+(u+v).plot(linestyle='dashed',color='black')
        sage: for e in ('png', 'pdf'): p.save('vectorplot.'+e, fig_tight=False, figsize=2.6, fontsize=8)

   .. ::

        .. sage: p = point(v,pointsize=20,color='black')+point(u+v, pointsize=20,color='black')
        .. sage: p += text('$\\textbf v$', v/2-offset*2,color='black')
        .. sage: p += text('$\\textbf u$', v+u/3+offset,color='black')
        .. sage: p += text('$\\textbf v + \\textbf u$', (u+v)/2+offset*3,color='black')


   .. _vectorplot:
   .. figure:: media/vectorplot.*
      :alt: vector plot example

      Plotting vectors



#. **Matrices**: Sage plots matrices as rectangulars array by mapping
   entry values to colors.  A user-specified color map (rules for how
   values map to colors) can be given and a legend-like color bar can
   be added. In the example below (see :ref:`matrixplot`), we plot a Toeplitz matrix; you can
   clearly see the banded structure. ::

     sage: from scipy.linalg import toeplitz
     sage: A = matrix(QQ,toeplitz([cos(i) for i in range(10)]))
     sage: A.plot(colorbar=True)

   .. _matrixplot:
   .. figure:: media/matrixplot.*
      :alt: matrix plot example

      Plotting dense matrices

   ..  sage: A = random_matrix(QQ,30)
   ..  sage: A.plot(colorbar=True)

   .. Sage commands to generate figure::

        .. sage: p = A.plot(colorbar=True)
        .. sage: for ext in ('png','pdf'): p.save('matrixplot.%s'%ext, fig_tight=False,figsize=2.6, fontsize=8)

   .. Need to apply the following patch to Sage to handle the colorbar fontsize


      diff --git a/sage/plot/graphics.py b/sage/plot/graphics.py
      --- a/sage/plot/graphics.py
      +++ b/sage/plot/graphics.py
      @@ -2237,6 +2236,11 @@
                           SageObject.save(self, filename)

               figure = self.matplotlib(**options)
      +        if options.get('fontsize',False):
      +            for ax in figure.axes:
      +                for t in ax.get_yticklabels():
      +                    t.set_fontsize(options['fontsize'])
      +
               # You can output in PNG, PS, EPS, PDF, or SVG format, depending on the file extension. 
               # matplotlib looks at the file extension to see what the renderer should be.
               # The default is FigureCanvasAgg for PNG's because this is by far the most

   .. .. _dense matrix plot:
   .. .. figure:: media/matrixplot.*
      :alt: matrix plot example

      Plotting matrices

   Sparse matrices plot their nonzero values.  Here we construct the
   adjacency matrix of the Buckyball graph and plot its structure
   (see :ref:`matrixsparseplot`). ::

       sage: A = graphs.BuckyBall().adjacency_matrix(sparse=True)
       sage: A.plot()

   .. Sage commands to generate figure::

        .. sage: p = A.plot(color='black') # will complain
        .. sage: for ext in ('png', 'pdf'): p.save('matrixsparseplot.'+ext, fig_tight=False, figsize=2.6,fontsize=8)
        .. sage: p.save('matrixsparseplot.png', fig_tight=False, figsize=2.6)

   .. _matrixsparseplot:
   .. figure:: media/matrixsparseplot.*
      :alt: matrix plot example

      Plotting sparse matrices


   .. .. _sparse matrix plot:
   .. .. figure:: media/matrixsparseplot.*
      :alt: matrix plot example

      Plotting sparse matrices


   .. todo: : I think it would make a lot of sense to switch the order of
    arguments in the vector's plot command, so you could do something
    like::

       sage: u = vector([1,2]); v = vector([3,4])
       sage: u.plot(start=v) # translate by v

   .. todo: : change visualize_structure to plot_structure? visualize_structure isn't very discoverable



Conversion to other forms
=========================

Examples
--------

#. Sage can convert a vector or matrix to a Python dictionary
   (``v.dict()``; returns indices and entries), a Python list
   (``v.list()``), or a NumPy array (``v.numpy()``). ::

     sage: v = vector(QQ, [1,2,3]); v.dict()
     {0: 1, 1: 2, 2: 3}
     sage: A = matrix(QQ, [[1,2],[3,4]]); A.list()
     [1, 2, 3, 4]

   .. todo: : make ``v.numpy()`` work for all vectors; see #13081

#. The LaTeX code for a vector or matrix can be generated using the
   :func:`latex` method::

     sage: latex(vector(QQ, [1,2,3]))
     \left(1,\,2,\,3\right)
     sage: latex(matrix(QQ, 2, [1,2,3,4/7]))
     \left(\begin{array}{rr}
     1 & 2 \\
     3 & \frac{4}{7}
     \end{array}\right)

#. You can change LaTeX delimiters using the
   :func:`latex.vector_delimiters` or :func:`latex.matrix_delimiters`
   functions.  If you use a delimiter that has a backslash, use two
   backslashes when specifying it, like ``'\\langle'``, or prefix the
   string with ``r``, like ``r'\langle'``. ::

     sage: latex.vector_delimiters('\\langle', r'\rangle')
     sage: latex(vector(QQ, [1,2,3/7]))
     \left\langle1,\,2,\,\frac{3}{7}\right\rangle

   .. ::

     sage: latex.matrix_delimiters('[',']'); latex(matrix(QQ, 2, [1,2,3,4]))
     \left[\begin{array}{rr}
     1 & 2 \\
     3 & 4
     \end{array}\right]



General Rings
=============

As mentioned earlier, every matrix and vector knows what ring in which
its entries live, and this determines how a matrix prints, algorithms
and libraries used to do the computations, methods available, etc.
Sage also supports many more rings and fields than we've mentioned,
including cyclotomic fields, number fields, and univariate and
multivariate polynomial rings.

Examples
--------


#. The following matrix is invertible over the rationals, but not over
   the integers::

     sage: A = matrix(QQ,2,[1,2,3,4])
     sage: A.is_invertible(), A.change_ring(ZZ).is_invertible()
     (True, False)

#. Sometimes matrices over certain fields support additional methods.
   For example, a symbolic matrix has a :meth:`subs` method to
   substitute values in for variables::

     sage: x,y,z = var('x,y,z'); A = matrix(SR, [[x,x-3*y,z],[x*z,0,y-x]])
     sage: A.subs(x=3, y=2)
     [  3  -3   z]
     [3*z   0  -1]

#. **Finite fields**:

   #. Use the ``FiniteField`` command or its shorthand ``GF`` ("Galois
      Field") to construct a finite field, specifying a name for the
      (multiplicative) generator if needed. ::

        sage: FiniteField(37), GF(next_prime(10^5))
        (Finite Field of size 37, Finite Field of size 100003)
        sage: F = GF(3^2, 'a'); F.list()
        [0, 2*a, a + 1, a + 2, 2, a, 2*a + 2, 2*a + 1, 1]
        sage: F.<a> = GF(2^9); a^101
        a^7 + a^6 + a^4 + a^3 + 1

   #. Linear algebra can be done over these finite fields just like any
      other ring.  Special implementations take advantage of different
      field characteristics to efficiently implement these.  Linear
      algebra over ``GF(2)`` is particularly optimized. ::

       sage: A = matrix(GF(5), 2, [1,2,3,14]); A.charpoly()
       x^2 + 3
       sage: A + A, A^-1, A^-1 * A
       (
       [2 4]  [3 1]  [1 0]
       [1 3], [4 2], [0 1]
       )
       sage: B = matrix(GF(37), 3, [1,2,3,4,5,6,7,8,10]); b = vector([1,2,3])
       sage: B * b, B \ b
       ((14, 32, 16), (12, 13, 0))

   #. Matrices over finite fields also support extra methods.
      Comparing a matrix to 1 compares it to the identity matrix.  ::

       sage: A = matrix(GF(37), 3, [1..8,10])
       sage: A.multiplicative_order(), A^684 == 1
       (684, True)

      .. mention mod and lift methods (change_ring probably sufficient)

      .. #. Matrices over ``GF(2)`` are particularly optimized::

      ..     sage: A = random_matrix(GF(2), 1000) 
      ..     sage: A.rank()  # random
      ..     1000
      ..     sage: A[0:10] = 0
      ..     sage: A.rank()  # random
      ..     990




.. _Numerical Linear Algebra:

Numerical Linear Algebra
========================

.. Numerical vectors and matrices (i.e., over ``RDF`` or ``CDF``) are
   constructed in the same manner as those with exact entries, but may
   have specialized methods to handle numerical issues.

Facts
-----

#. The fields ``RDF`` and ``CDF`` are fast machine-level
   double-precision floating point reals and complexes (respectively).
   Many of the algorithms for matrices over ``RDF`` and ``CDF`` are
   provided by SciPy/NumPy and use industry-standard libraries like
   LAPACK.

   .. ::

    sage: A = matrix(RDF, [[1, sqrt(2), 4], [5.67, 1/3, 9.0]]); A
    [           1.0  1.41421356237            4.0]
    [          5.67 0.333333333333            9.0]
    sage: B = matrix(CDF, [[5.62, 3 - 4*I], [1/(3*I), (-4)^(1/2)]]); B
    [             5.62       3.0 - 4.0*I]
    [-0.333333333333*I             2.0*I]

#. The fields ``RealField(prec)`` and ``ComplexField(prec)`` provide
   reals and complexes to any fixed precision (``prec`` is the number
   of bits used for the mantissa), e.g., ``RealField(20)`` has 20 bits
   of precision.  In Sage, ``RR`` is ``RealField(53)`` and ``CC`` is
   ``ComplexField(53)``.  A floating point number is in ``RR`` or
   ``CC`` by default, so a matrix or vector with floating point
   entries is over ``RR`` or ``CC`` unless another ring is specified.

   .. ::

    sage: R = RealField(20)
    sage: v = vector(R, [5, 1/3, sqrt(2)]); v
    (5.0000, 0.33333, 1.4142)

#. We emphasize that ``RR`` and ``CC`` are *not* exactly the same as
   ``RDF`` and ``CDF`` since ``RR`` and ``CC`` are not implemented
   with machine-level floating point numbers.  The ``RealField`` and
   ``ComplexField`` fields (like ``RR`` and ``CC``) are instead
   implemented with rigorous and portable semantics, and thus are
   usually slower.  More importantly, algorithms for matrices over
   ``RealField``, and ``ComplexField`` are not specialized for
   numerical work, so they may return misleading results because of
   numerical error.

#. Since the ``v.n()`` and ``A.n()`` numerical approximation methods
   return objects over ``RR`` or ``CC``, if you are doing numerical
   computations, it is preferable to convert your objects to ``RDF`` or
   ``CDF`` using the :meth:`change_ring` method, e.g.,
   ``v.change_ring(RDF)``.

#. ``RDF`` and ``CDF`` matrices used specialized algorithms for
   computing eigenvalues, eigenvectors, and popular matrix
   decompositions (see the relevant sections of :ref:`matrices` for specific methods).  Eigenvectors (and
   eigenspaces) are reported with multiplicity one, for consistency with
   the format of results for exact matrices.

   .. ::

     .. sage: A = matrix(RDF, 3, 3, range(9)); A.eigenvectors_right()
     .. [7.0, 4.0, 5.0]
     .. sage: A.eigenvectors_right()
     .. [(7.0, [(-0.4364..., -0.8728..., 0.2182...)], 1),
     .. (4.0, [(0.2357..., 0.9428..., -0.2357...)], 1),
     .. (5.0, [(-0.5345..., -0.8017..., 0.2672...)], 1)]

     .. sage: A.eigenmatrix_right()
     .. (
     .. [7.0 0.0  0.0]  [ 0.4364... -0.2357... -0.5345...]
     .. [0.0 4.0  0.0]  [ 0.8728... -0.9428... -0.8017...]
     .. [0.0 0.0  5.0], [-0.2182...  0.2357...  0.2672...]
     .. )

   .. #. Popular matrix decompositions are supported for numerical matrices,
      using algorithms designed specifically for floating-point entries.
      See the description of matrix decompositions in the :ref:`Matrices`
      section.

       sage: entries = [-2, 5, 1, -2, 2, -1, -8, 5, -3, 6, 4, -4]
       sage: A = matrix(RDF, 3, 4, entries); A
       [-2.0  5.0  1.0 -2.0]
       [ 2.0 -1.0 -8.0  5.0]
       [-3.0  6.0  4.0 -4.0]
       sage: A.SVD()
       (
       [ 0.3611... -0.5823... -0.7283...]
       [-0.6714... -0.7043...  0.2302...]
       [ 0.6470... -0.4059...  0.6453...],
       [  13.0460...        0.0        0.0  0.0]
       [         0.0  5.8990...        0.0  0.0]
       [         0.0        0.0  0.0343...  0.0],
       [-0.3071...  0.1650... -0.5540... -0.7559...]
       [ 0.4874... -0.7870...  0.0110... -0.3779...]
       [ 0.6378...  0.5813...  0.3352... -0.3779...]
       [-0.5111... -0.1243...  0.7618... -0.3779...]
       )

#. ``RDF`` and ``CDF`` matrices use specialized algorithms to compute
   properties like the condition number of a matrix
   (``A.condition()``), norms of vectors and matrices, matrix
   exponentials, and checks for properties like unitary or Hermitian
   matrices.
.. #. Round small entries less than ``eps`` in absolute value to zero in ``RDF``
   and ``CDF`` matrices using ``A.zero_at(eps)``.

   .. ::

     sage: hilbert = matrix(RDF, 10, lambda x,y: 1/(x+y+1))
     sage: hilbert.condition()
     1.63346888329e+13




Applications of Linear Algebra
==============================

Sage can do many computations related to linear algebra.  For example:

#. **Graphs**: Sage has a comprehensive graph theory
   and combinatorics library.  See "Graph Theory" and "Combinatorics"
   in the Sage reference manual.

#. **Coding Theory**: Sage includes a number of codes and
   functionality related to coding theory.  See the "Coding Theory"
   section of the reference manual.

#. **Linear Programming**: Sage comes with powerful
   linear programming, integer programming, and semidefinite
   programming tools, and also interfaces seamlessly with several
   industry solutions, such as CPLEX.  See the "Numerical Tools" and
   "Numerical Optimization" sections of the reference manual.

#. **Minimum rank, zero forcing**: A Sage library that
   calculates minimum rank and zero forcing is at
   https://github.com/jasongrout/minimum_rank.


For More Information
====================

#. **Websites**: The main website for Sage is
   http://sagemath.org.  The main public Sage notebook server
   is http://sagenb.org.

#. **Sage help**: Access Sage documentation by clicking "Help" in the
   Sage Notebook or at http://sagemath.org/doc.  Questions
   about how to use Sage should be addressed to either the
   sage-support mailing list,
   http://groups.google.com/group/sage-support/, or to
   the http://ask.sagemath.org website.  Discussion about Sage
   in education also happens on the sage-edu mailing list,
   http://groups.google.com/group/sage-edu/.

#. **Interacts**: Sage makes it very easy to create interactive
   demonstrations that utilize sliders, checkboxes, buttons, etc.,
   allowing a user to easily adjust the inputs to a computation.  See
   a number of examples at
   http://wiki.sagemath.org/interact/ or the
   documentation for :func:`interact` (i.e., ``interact?``) in the Sage
   notebook.

#. **Embedding Sage in a webpage**: Sage computations can easily be
   embedded in any webpage outside of the Sage notebook.  A user can
   modify the Sage code, drag sliders, etc.  See
   https://sagemath.github.com/sagecell/.

#. **SageTeX**: Sage has a very easy way to embed Sage input and
   output directly into a LaTeX file.  This allows an author to type
   Sage code directly into their LaTeX file, run the latex program
   (which generates a sage code file), run sage on the resulting sage
   code file (which generates the outputs, graphics, etc.), and then
   run latex again on their source file (which incorporates output and
   graphics back into the resulting pdf document).  For example, to
   embed a Sage plot, merely type ``\sageplot{plot(x^2, (x,0,4))}`` in
   the LaTeX document, then run latex, sage, then latex again to
   embed the plot in the pdf file.  See the documentation
   for SageTeX in the Sage tutorial.

#. **Fortran support**: It is easy to compile and run FORTRAN code
   from within the Sage notebook.  For examples, see *Numerical Sage*
   in the Sage documentation.


The following resources may also be helpful.

#. *Linear Algebra Quick Reference* by Robert Beezer.  A two-page summary
   of many linear algebra commnds and constructions.
   http://wiki.sagemath.org/quickref.

#. *Linear Algebra with Sage* by Robert Beezer. An extensive tutorial on
   linear algebra, designed as a supplement to the textbook *A First
   Course in Linear
   Algebra*. http://linear.ups.edu/sage-fcla.html.

#. Many numerical calculations and plots can be done using the
   included Python packages SciPy and NumPy
   (http://www.scipy.org/) and Matplotlib
   (http://matplotlib.sourceforge.net/).

#. *Python Scientific Lecture Notes*.
   http://scipy-lectures.github.com/.

#. *NumPy for Matlab Users*. Helps in translating between MATLAB and
   the Python NumPy package.
   http://www.scipy.org/NumPy_for_Matlab_Users.  See
   also
   http://mathesaurus.sourceforge.net/matlab-numpy.html
   for another reference.

#. *Python documentation*.  The official documentation is quite
   comprehensive and contains tutorials and reference material.
   http://docs.python.org/.

#. *Python for Non-Programmers*.  A collection of resources
   introducing Python.
   http://wiki.python.org/moin/BeginnersGuide/NonProgrammers.

#. *Dive into Python* by Mark Pilgrim.  A free comprehensive book
   introducing Python.  http://www.diveintopython.net/.

.. [Sci12]_ See http://docs.scipy.org/doc/scipy/reference/linalg.html for details. 

.. Matrix commands which may not be generally interesting.  We didn't
   include these in the article, but they may be interesting to add later.

   :meth:`wiedemann`
   :meth:`kernel_on`
   :meth:`integer_kernel`
   :meth:`right_kernel_matrix` (RAB: this is the computational heart of the refactored kernel routines.  It is only valuable if you just want a matrix and know what to do with it, and you want to skip the overhead of making a vector space as the kernel.  Probably not interesting.)
   :meth:`height`
   :meth:`hadamard_bound`
   :meth:`rook_vector`
   :meth:`reset_name`
   :meth:`maxspin`
   :meth:`weak_popov_form`
   :meth:`prod_of_row_sums`
   :meth:`A.fcp`
   :meth:`randomize`

   :meth:`set_immutable`

   Instead of the following, just multiply by a vector on the left or right...

   :meth:`linear_combination_of_columns`
   :meth:`linear_combination_of_rows`

   should we mention the :meth:`mod` and :meth:`lift` methods for
   matrices? if so, this section is a good place for it; but we're
   already running short on space, so maybe not.
