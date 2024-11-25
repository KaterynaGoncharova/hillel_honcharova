class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_teamead():
    lead = TeamLead("Brad Pitt", 5000, "IT Department", "Python", 10)

    assert lead.name == "Brad Pitt"
    assert lead.salary == 5000
    assert lead.department == "IT Department"
    assert lead.programming_language == "Python"
    assert lead.team_size == 10

    print('All tests passed')

test_teamead()




