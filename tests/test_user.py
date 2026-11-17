from jarvis_app.user import User

def test_remember_and_recall():
    u = User("Ali")
    u.remember('city', 'Buxoro')
    assert u.recall('city') == 'Buxoro'

def test_recall_missing():
    new_user = User('Islom')
    assert new_user.recall('age') == "I don't know"

def test_add_run_twice():
    u = User('Vali')
    u.add_run()
    u.add_run()
    assert u.runs == 2

def test_str():
    u = User('Ali')
    u.remember('hobby', 'coding')
    u.add_run()
    u.add_run()
    assert str(u) == "Ali (runs: 2, facts: 1)"