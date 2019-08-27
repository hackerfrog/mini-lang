class ParserResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, a_result):
        if isinstance(a_result, ParserResult):
            if a_result.error:
                self.error = a_result.error
            return a_result.node
        return a_result

    def success(self, a_node):
        self.node = a_node
        return self

    def failure(self, a_error):
        self.error = a_error
        return self