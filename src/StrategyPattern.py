from Factory import RecordFactory, QueryFactory, ReportFactory, PriorityFactory


class Strategy(object):
    def execute(self, user_inputs, database): pass


class RecordStrategy(Strategy):
    def execute(self, user_inputs, database):
        RecordFactory().run_inputs_check(user_inputs, database)


class QueryStrategy(Strategy):
    def execute(self, user_inputs, database):
        QueryFactory().run_inputs_check(user_inputs, database)


class ReportStrategy(Strategy):
    def execute(self, user_inputs, database):
        ReportFactory().run_inputs_check(user_inputs, database)


class PriorityStrategy(Strategy):
    def execute(self, user_inputs, database):
        PriorityFactory().run_inputs_check(user_inputs, database)


class Context(object):
    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_decision(self, user_inputs, database):
        if user_inputs[0].lower() == "record":
            self.set_strategy(RecordStrategy())
        elif user_inputs[0].lower() == "query":
            self.set_strategy(QueryStrategy())
        elif user_inputs[0].lower() == "report":
            self.set_strategy(ReportStrategy())
        elif user_inputs[0].lower() == "priority":
            self.set_strategy(PriorityStrategy())
        self.strategy.execute(user_inputs, database)
