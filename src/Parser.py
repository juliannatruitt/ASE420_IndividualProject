import argparse


class ParserClass(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser()

    def get_parser(self):
        return self._parser

    def get_array_of_users_input_from_CMD(self):
        self.get_parser().add_argument("get_amount_of_inputs", type=str, nargs='+')
        args = self.get_parser().parse_args()
        return args.get_amount_of_inputs
