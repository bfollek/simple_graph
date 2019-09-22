# This runs from the simple_graph folder

from functools import total_ordering
from data_structures.simple_graph.graph import Digraph, Graph

CITIES = ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York",
          "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"]


def _add_edges(g):
    g.add_edge_by_vertices("Seattle", "Chicago")
    g.add_edge_by_vertices("Seattle", "San Francisco")
    g.add_edge_by_vertices("San Francisco", "Riverside")
    g.add_edge_by_vertices("San Francisco", "Los Angeles")
    g.add_edge_by_vertices("Los Angeles", "Riverside")
    g.add_edge_by_vertices("Los Angeles", "Phoenix")
    g.add_edge_by_vertices("Riverside", "Phoenix")
    g.add_edge_by_vertices("Riverside", "Chicago")
    g.add_edge_by_vertices("Phoenix", "Dallas")
    g.add_edge_by_vertices("Phoenix", "Houston")
    g.add_edge_by_vertices("Dallas", "Chicago")
    g.add_edge_by_vertices("Dallas", "Atlanta")
    g.add_edge_by_vertices("Dallas", "Houston")
    g.add_edge_by_vertices("Houston", "Atlanta")
    g.add_edge_by_vertices("Houston", "Miami")
    g.add_edge_by_vertices("Atlanta", "Chicago")
    g.add_edge_by_vertices("Atlanta", "Washington")
    g.add_edge_by_vertices("Atlanta", "Miami")
    g.add_edge_by_vertices("Miami", "Washington")
    g.add_edge_by_vertices("Chicago", "Detroit")
    g.add_edge_by_vertices("Detroit", "Boston")
    g.add_edge_by_vertices("Detroit", "Washington")
    g.add_edge_by_vertices("Detroit", "New York")
    g.add_edge_by_vertices("Boston", "New York")
    g.add_edge_by_vertices("New York", "Philadelphia")
    g.add_edge_by_vertices("Philadelphia", "Washington")


def _make_graph():
    city_graph = Graph(CITIES)
    _add_edges(city_graph)
    return city_graph


def _make_digraph():
    city_digraph = Digraph(CITIES)
    _add_edges(city_digraph)
    return city_digraph


def test_graph():
    g = _make_graph()
    assert sorted(g.neighbors_for_vertex("Seattle")) == [
        'Chicago', 'San Francisco']
    assert sorted(g.neighbors_for_vertex("San Francisco")) == [
        'Los Angeles', 'Riverside', 'Seattle']
    assert sorted(g.neighbors_for_vertex("Atlanta")) == [
        'Chicago', 'Dallas', 'Houston', 'Miami', 'Washington']
    assert sorted(g.neighbors_for_vertex("Washington")) == [
        'Atlanta', 'Detroit', 'Miami', 'Philadelphia']


def test_empty_graph():
    """Just to make sure the __init__ works when `vertices` isn't passed."""
    g: Graph = Graph()
    assert g


def test_digraph():
    g = _make_digraph()
    assert sorted(g.neighbors_for_vertex("Seattle")) == [
        'Chicago', 'San Francisco']
    assert sorted(g.neighbors_for_vertex("San Francisco")) == [
        'Los Angeles', 'Riverside']
    assert sorted(g.neighbors_for_vertex("Atlanta")) == [
        'Chicago', 'Miami', 'Washington']
    assert sorted(g.neighbors_for_vertex("Washington")) == []

##########################################
# Test with objects that have attributes
##########################################


# https://stackoverflow.com/questions/8796886/is-it-safe-to-just-implement-lt-for-a-class-that-will-be-sorted

@total_ordering
class City():
    def __init__(self, name):
        self._name = name.strip()

    @property
    def name(self):
        return self._name

    def str(self):
        return self.name

    @property
    def _normalized_name(self):
        """For comparisons"""
        return self.name.lower()

    def __eq__(self, other):
        return self._normalized_name == other._normalized_name

    def __lt__(self, other):
        return self._normalized_name < other._normalized_name


SEATTLE = City("Seattle")
SAN_FRANCISCO = City("San Francisco")
LOS_ANGELES = City("Los Angeles")
RIVERSIDE = City("Riverside")
PHOENIX = City("Phoenix")
CHICAGO = City("Chicago")
BOSTON = City("Boston")
NEW_YORK = City("New York")
ATLANTA = City("Atlanta")
MIAMI = City("Miami")
DALLAS = City("Dallas")
HOUSTON = City("Houston")
DETROIT = City("Detroit")
PHILADELPHIA = City("Philadelphia")
WASHINGTON = City("Washington")

CITY_OBJS = [SEATTLE, SAN_FRANCISCO, LOS_ANGELES,
             RIVERSIDE, PHOENIX, CHICAGO, BOSTON, NEW_YORK, ATLANTA, MIAMI, DALLAS, HOUSTON, DETROIT, PHILADELPHIA, WASHINGTON]


def _add_obj_edges(g):
    g.add_edge_by_vertices(SEATTLE, CHICAGO)
    g.add_edge_by_vertices(SEATTLE, SAN_FRANCISCO)
    g.add_edge_by_vertices(SAN_FRANCISCO, RIVERSIDE)
    g.add_edge_by_vertices(SAN_FRANCISCO, LOS_ANGELES)
    g.add_edge_by_vertices(LOS_ANGELES, RIVERSIDE)
    g.add_edge_by_vertices(LOS_ANGELES, PHOENIX)
    g.add_edge_by_vertices(RIVERSIDE, PHOENIX)
    g.add_edge_by_vertices(RIVERSIDE, CHICAGO)
    g.add_edge_by_vertices(PHOENIX, DALLAS)
    g.add_edge_by_vertices(PHOENIX, HOUSTON)
    g.add_edge_by_vertices(DALLAS, CHICAGO)
    g.add_edge_by_vertices(DALLAS, ATLANTA)
    g.add_edge_by_vertices(DALLAS, HOUSTON)
    g.add_edge_by_vertices(HOUSTON, ATLANTA)
    g.add_edge_by_vertices(HOUSTON, MIAMI)
    g.add_edge_by_vertices(ATLANTA, CHICAGO)
    g.add_edge_by_vertices(ATLANTA, WASHINGTON)
    g.add_edge_by_vertices(ATLANTA, MIAMI)
    g.add_edge_by_vertices(MIAMI, WASHINGTON)
    g.add_edge_by_vertices(CHICAGO, DETROIT)
    g.add_edge_by_vertices(DETROIT, BOSTON)
    g.add_edge_by_vertices(DETROIT, WASHINGTON)
    g.add_edge_by_vertices(DETROIT, NEW_YORK)
    g.add_edge_by_vertices(BOSTON, NEW_YORK)
    g.add_edge_by_vertices(NEW_YORK, PHILADELPHIA)
    g.add_edge_by_vertices(PHILADELPHIA, WASHINGTON)


def _make_obj_digraph():
    city_obj_digraph = Digraph(CITY_OBJS)
    _add_obj_edges(city_obj_digraph)
    return city_obj_digraph


def test_obj_digraph():
    g = _make_obj_digraph()
    assert sorted(g.neighbors_for_vertex(SEATTLE)) == [
        CHICAGO, SAN_FRANCISCO]
    assert sorted(g.neighbors_for_vertex(SAN_FRANCISCO)) == [
        LOS_ANGELES, RIVERSIDE]
    assert sorted(g.neighbors_for_vertex(ATLANTA)) == [
        CHICAGO, MIAMI, WASHINGTON]
    assert sorted(g.neighbors_for_vertex(WASHINGTON)) == []
