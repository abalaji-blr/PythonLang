from functools import lru_cache
from polygon import RegConvexPolygon

class PolygonSeq:
  '''
  This class implements a custom polygon sequence type.
  
  The following methods are implemented:
  1. init
    Takes a number of vertices of a largest polygon in sequence.
    Takes a common circumradius for all polygons.

  2. max_efficiency - property
    returns the polygon with highest area to perimeter ratio.

  3. The following methods are implemented:
    __repr__ method
    __len__ method
    __getitem__ method
   
  '''
  def __init__(self, num_vertices, common_circumradius):
    self._num_vertices = num_vertices
    self._cmn_circumradius = common_circumradius
    self._ratio = dict()

  @property
  def max_efficiency(self) -> str:
    for i in range(1, self._num_vertices+1):
      if i > 1:
        self._ratio[i] = self.__getitem__(i)

    #get the key of the max value
    key = max(self._ratio, key=self._ratio.get)
    return f'Max ratio is {self._ratio[key]} with {key} vertices.'


  @staticmethod
  @lru_cache(2 ** 10)
  def _area_perimeter_ratio(vertices, circumradius) -> 'float':
    if vertices < 2:
      return 1
    else:
      p = RegConvexPolygon(vertices, circumradius)
      return p.area / p.perimeter

  def __getitem__(self, vertex):
    if isinstance(vertex, int):
      if vertex < 0 or vertex > self._num_vertices:
        print(f'vertex : {vertex}')
        raise IndexError
      else:
        if vertex > 1:
          return PolygonSeq._area_perimeter_ratio(vertex, self._cmn_circumradius)
        else:
          return 'Its not a polygon'
    else:
      raise IndexError
    

  def __repr__(self):
    txt = 'Polygon with {} vertices and {} as circumradius.'.format(self._num_vertices, 
                                                                     self._cmn_circumradius 
                                                                     )
    return(txt)

  def __len__(self):
    return(self._num_vertices)
