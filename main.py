from jarvis_app.core2 import Jarvis

j = Jarvis()
j.load('users.json')
j.get_user("Ali").add_run()
j.save('users.json')
print(j.report())