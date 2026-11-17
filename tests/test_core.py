from jarvis_app.core2 import Jarvis

def test_get_user_same_object():
    j = Jarvis()
    first = j.get_user('Ali')
    second = j.get_user('Ali')
    assert first is second

def test_two_users():
    j = Jarvis()
    Ali = j.get_user('Ali')
    Vali = j.get_user('Vali')
    assert len(j.users) == 2

def test_report():
    j = Jarvis()
    Ali = j.get_user('Ali')
    Vali = j.get_user('Vali')

    Ali.remember('city', 'Buxoro')
    Ali.add_run()

    Vali.add_run()
    assert j.report() == ['Ali (runs: 1, facts: 1)', 'Vali (runs: 1, facts: 0)']
