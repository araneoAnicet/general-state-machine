from random import randint
from time import clock

State = type('State', (object,), {})


class StateTwo(State):
    def execute(self):
        print('State 2')


class StateOne(State):
    def execute(self):
        print('State 1')

# ================================================ #

class Transition:
    def __init__(self, trans_state):
        self.to_state = trans_state

    def execute(self):
        print('Transitioning...')

# ================================================ #

class FSM:
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.current_state = None
        self.transitioning = None

    def set_state(self, state_name):
        self.current_state = self.states[state_name]

    def transition(self, transition_name):
        self.transitioning = self.transitions[transition_name]

    def execute(self):
        if self.transitioning:
            self.transitioning.execute()
            self.set_state(self.transitioning.to_state)
            self.transitioning = None
        self.current_state.execute()

# ================================================ #
class Char(object):
    def __init__(self):
        self.FSM = FSM(self)
        self.state_one = True


if __name__ == '__main__':
    state_result = Char()
    state_result.FSM.states['state condition I'] = StateOne()
    state_result.FSM.states['state condition II'] = StateTwo()
    state_result.FSM.transitions['to I state'] = Transition('I')
    state_result.FSM.transitions['to II state'] = Transition('II')

    state_result.FSM.set_state('state condition I')

    for i in range(20):
        start_time = clock()
        time_interval = 1
        while start_time + time_interval > clock():
            pass
        if randint(0, 2):
            if state_result.state_one:
                state_result.FSM.transition('to II state')
                state_result.state_one = False
            else:
                state_result.FSM.transition('to I state')
                state_result.state_one = True

    state_result.FSM.execute()