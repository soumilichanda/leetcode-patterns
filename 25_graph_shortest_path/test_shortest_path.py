import pytest
from importlib import import_module

lc743 = import_module("25_graph_shortest_path.0743_network_delay_time").Solution()
lc787 = import_module("25_graph_shortest_path.0787_cheapest_flights_k_stops").Solution()


def test_network_delay_time_cyclic_reachable():
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    assert lc743.networkDelayTime(times, 3, 1) == 3


def test_network_delay_time_unreachable_node():
    times = [[1, 2, 1]]
    assert lc743.networkDelayTime(times, 2, 2) == -1


def test_cheapest_flights_exact_k_stops():
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # With 0 stops, must take direct route (500)
    assert lc787.findCheapestPrice(3, flights, 0, 2, 0) == 500
    # With 1 stop, can take indirect route (200)
    assert lc787.findCheapestPrice(3, flights, 0, 2, 1) == 200


def test_cheapest_flights_no_path():
    flights = [[0, 1, 100]]
    assert lc787.findCheapestPrice(3, flights, 0, 2, 1) == -1
