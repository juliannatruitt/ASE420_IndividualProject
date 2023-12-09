from src.Parser import ParserClass
from src.StrategyPattern import Context
from src.Connection import CreateConnection


if __name__ == "__main__":
    parser = ParserClass()
    user_inputs = parser.get_array_of_users_input_from_CMD()
    connection = CreateConnection().get_instance()

    Context().make_decision(user_inputs, connection)
