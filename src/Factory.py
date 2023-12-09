from CheckInputValues import InputsValidatorRecord, InputsValidatorPriority, InputsValidatorReport, InputsValidatorQuery


class Factory(object):
    def run_inputs_check(self, inputs, database): pass


class RecordFactory(Factory):
    def run_inputs_check(self, inputs, database):
        return InputsValidatorRecord(inputs[1:], database).check_all()


class QueryFactory(Factory):
    def run_inputs_check(self, inputs, database):
        return InputsValidatorQuery(inputs[1:], database).check_all()


class ReportFactory(Factory):
    def run_inputs_check(self, inputs, database):
        return InputsValidatorReport(inputs[1:], database).check_all()


class PriorityFactory(Factory):
    def run_inputs_check(self, inputs, database):
        return InputsValidatorPriority(inputs, database).check_all()
