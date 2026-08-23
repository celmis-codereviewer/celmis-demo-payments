from src.settlement import split_settlement


def test_split_between_two_parties():
    assert split_settlement(100, ["alice", "bob"]) == {"alice": 50, "bob": 50}


def test_split_preserves_the_total():
    """The parts must add up to the whole. Three ways into 100 cents leaves a
    remainder, and the remainder is somebody's money."""
    out = split_settlement(100, ["alice", "bob", "carol"])
    assert sum(out.values()) == 100


def test_split_rejects_no_parties():
    try:
        split_settlement(100, [])
    except ValueError:
        return
    raise AssertionError("expected ValueError")
