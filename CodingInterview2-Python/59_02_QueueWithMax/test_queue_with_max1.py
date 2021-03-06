from queue_with_max import QueueMax

qm = QueueMax()

# {4}
def test1():
    qm.push_back(4)
    assert qm.max == 4


# {4, 3}
def test2():
    qm.push_back(3)
    assert qm.max == 4


# {4, 3, 2}
def test3():
    qm.push_back(2)
    assert qm.max == 4


# {4, 3, 2, 8}
def test4():
    qm.push_back(8)
    assert qm.max == 8


# {3, 2, 8}
def test5():
    qm.pop_front()
    assert qm.max == 8


# {2, 8}
def test6():
    qm.pop_front()
    assert qm.max == 8


# {8}
def test7():
    qm.pop_front()
    assert qm.max == 8


# {8, 6}
def test8():
    qm.push_back(6)
    assert qm.max == 8


# {8, 6, 2}
def test9():
    qm.push_back(2)
    assert qm.max == 8


# {8, 6, 2, 5}
def test10():
    qm.push_back(5)
    assert qm.max == 8


# {6, 2, 5}
def test11():
    qm.pop_front()
    assert qm.max == 6


# {2, 5}
def test12():
    qm.pop_front()
    assert qm.max == 5


# {5}
def test13():
    qm.pop_front()
    assert qm.max == 5


# {5, 1}
def test14():
    qm.push_back(1)
    assert qm.max == 5
