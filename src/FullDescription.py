class GetFullDescription(object):
    def __init__(self, description):
        self._description = description

    def get_description_input(self):
        total_lines_of_description = ''
        for x in range(0, len(self._description)):
            total_lines_of_description += self._description[x] + ' '
        return total_lines_of_description
