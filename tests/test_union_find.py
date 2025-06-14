from union_find.dynamic_connectivity import UF
def test_union_find():
    uf = UF(10)
    uf.union(1, 2)
    uf.union(2, 3)
    assert uf.connected(1, 3) == True
    assert uf.connected(1, 4) == False