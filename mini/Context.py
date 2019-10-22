################################################################################
## CONTEXT
################################################################################

class Context:
    def __init__(self, a_display_name, a_parent=None, a_parent_entry_position=None):
        self.display_name = a_display_name
        self.parent = a_parent
        self.parent_entry_position = a_parent_entry_position
        self.symbol_table = None
