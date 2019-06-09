from graph import Digraph, Graph

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


def test_digraph():
    g = _make_digraph()
    assert sorted(g.neighbors_for_vertex("Seattle")) == [
        'Chicago', 'San Francisco']
    assert sorted(g.neighbors_for_vertex("San Francisco")) == [
        'Los Angeles', 'Riverside']
    assert sorted(g.neighbors_for_vertex("Atlanta")) == [
        'Chicago', 'Miami', 'Washington']
    assert sorted(g.neighbors_for_vertex("Washington")) == []
