import math

class RegConvexPolygon:
  '''
  Class which describes the regular convex polygon.
  Regular Convex polygon follows the below rules:
  1. All sides are equal length.
  2. All interior angles are less than 180 degrees.

  This class implements the following as python properties:
  1. num_vertices (n)
  2. circumradius (R)
  3. interior_angle
  4. edge_length
  5. apothem
  6. area
  7. perimeter
  '''
  def __init__(self, num_vertices, circumradius):
    self._num_vertices = num_vertices
    self._circumradius = circumradius

  @property
  def num_vertices(self):
    return(self._num_vertices)

  @property
  def circumradius(self):
    return(self._circumradius)

  @property
  def interior_angle(self):
    ia = (self._num_vertices - 2) * (180 / self._num_vertices)
    return(ia)

  @property
  def edge_length(self):
    el = 2 * self._circumradius * math.sin(math.pi / self._num_vertices)
    return(el)

  @property
  def apothem(self):
    apo = self._circumradius * math.cos(math.pi / self._num_vertices)
    return(apo)

  @property
  def area(self):
    ar = (1/2) * self._num_vertices * self.edge_length * self.apothem
    return(ar)

  @property
  def perimeter(self):
    peri = self._num_vertices * self.edge_length
    return(peri)

  def __repr__(self):
    return(f'Regular Convex Polygon with {self._num_vertices} vertices and {self._circumradius} circumradius')

  def __eq__(self, other):
    if isinstance(other, RegConvexPolygon) == False:
      raise TypeError('Invalid type of object passed.')

    return(self._num_vertices == other.num_vertices and self._circumradius == other.circumradius)

  def __gt__(self, other):
    if isinstance(other, RegConvexPolygon) == False:
      raise TypeError('Invalid type of object passed.')

    return( self._num_vertices > other.num_vertices)

