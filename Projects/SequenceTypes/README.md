# EPAi4 Session9 - Sequence Type

### About Sequences:

Sequence is collection of elements in an order.

We can refer the element with an index number. ie., can refer them as first element, second element etc. There is a notion of **positional** ordering.

**In Python, index starts from 0**.

**Built-in** sequence types:

- Mutable
  - list
- Immutalbe
  - string
  - tuples
  - range

---

### About standard Sequence methods / operations:

- x in s
- x not in s
- s1 + s2 - concatenation
- s * n - repetition, n is int.
- len(s)
- min(s)
- max(s)
- s.index(x) - first occurence of x in s
- s.index(x, i) - first occurrence of x in s at or after i.
- s.index(x, i, j) - first occurrence of x in s at or after i but before j.
- s[i] - element at index i
- s[i:j] - slice from index i but excluding index j.
- s[i:j:k] - slice from index i but excluding j, in steps of k.
- range object

---

### About Assignment



* Implement a **Regular Convex Polygon** class.

  ```
  class RegConvexPolygon(builtins.object)
   |  RegConvexPolygon(num_vertices, circumradius)
   |  
   |  Class which describes the regular convex polygon.
   |  Regular Convex polygon follows the below rules:
   |  1. All sides are equal length.
   |  2. All interior angles are less than 180 degrees.
   |  
   |  This class implements the following as python properties:
   |  1. num_vertices (n)
   |  2. circumradius (R)
   |  3. interior_angle
   |  4. edge_length
   |  5. apothem
   |  6. area
   |  7. perimeter
   |  
   |  Methods defined here:
   |  
   |  __eq__(self, other)
   |      Return self==value.
   |  
   |  __gt__(self, other)
   |      Return self>value.
   |  
   |  __init__(self, num_vertices, circumradius)
   |      Initialize self.  See help(type(self)) for accurate signature.
   |  
   |  __repr__(self)
   |      Return repr(self).
   |  
   |  ----------------------------------------------------------------------
   |  Data descriptors defined here:
   |  
   |  __dict__
   |      dictionary for instance variables (if defined)
   |  
   |  __weakref__
   |      list of weak references to the object (if defined)
   |  
   |  apothem
   |  
   |  area
   |  
   |  circumradius
   |  
   |  edge_length
   |  
   |  interior_angle
   |  
   |  num_vertices
   |  
   |  perimeter
   |  
   |  ----------------------------------------------------------------------
   |  Data and other attributes defined here:
   |  
   |  __hash__ = None
  ```

  *  Usage

    ```
    p1 = RegConvexPolygon(4, 2)
    
    print(p1.num_vertices)
    print(p1.circumradius)
    print(p1.edge_length)
    print(p1.interior_angle)
    print(p1.apothem)
    print(p1.area)
    print(p1.perimeter)
    
    4
    2
    2.82842712474619
    90.0
    1.4142135623730951
    8.0
    11.31370849898476
    ```

    

    ```
    p1 = RegConvexPolygon(10, 4)
    p2 = RegConvexPolygon(10, 4)
    p3 = RegConvexPolygon(100, 2)
    p4 = RegConvexPolygon(2, 100)
    p5 = RegConvexPolygon(10, 2)
    
    assert p1 == p2
    assert p1 != p5
    assert p3 > p4
    assert p3 > p2
    ```

    

  

* Implement a **Custom Polygon Sequence**:

  ```
  class PolygonSeq(builtins.object)
   |  PolygonSeq(num_vertices, common_circumradius)
   |  
   |  This class implements a custom polygon sequence type.
   |  
   |  The following methods are implemented:
   |  1. init
   |    Takes a number of vertices of a largest polygon in sequence.
   |    Takes a common circumradius for all polygons.
   |  
   |  2. max_efficiency - property
   |    returns the polygon with highest area to perimeter ratio.
   |  
   |  3. The following methods are implemented:
   |    __repr__ method
   |    __len__ method
   |    __getitem__ method
   |  
   |  Methods defined here:
   |  
   |  __getitem__()
   |  
   |  __init__(self, num_vertices, common_circumradius)
   |      Initialize self.  See help(type(self)) for accurate signature.
   |  
   |  __len__(self)
   |  
   |  __repr__(self)
   |      Return repr(self).
   |  
   |  ----------------------------------------------------------------------
   |  Data descriptors defined here:
   |  
   |  __dict__
   |      dictionary for instance variables (if defined)
   |  
   |  __weakref__
   |      list of weak references to the object (if defined)
   |  
   |  max_efficiency
  ```



---





