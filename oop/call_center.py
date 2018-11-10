"""
Imagine you have a call center with three levels of employees: fresher, technical lead
(TL), product manager (PM). There can be multiple employees, but only one TL or PM.
An incoming telephone call must be allocated to a fresher who is free. If a fresher
can’t handle the call, he or she must escalate the call to technical lead. If the TL is
not free or not able to handle it, then the call should be escalated to PM. Design the
classes and data structures for this problem. Implement a method getCallHandler()
"""


class Employee:
    def __init__(self, name, manager):
        self.name, self.manager, self.call = name, manager, None

    def take_call(self, call):
        pass

    def escalate(self, call):
        pass

    def finish_call(self, call):
        pass


class TechnicalLead(Employee):
    def __init__(self):
        pass