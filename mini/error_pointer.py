def error_pointer(a_text, a_position_start, a_position_end):
    result = ''

    index_start = max(a_text.rfind('\n', 0, a_position_start.index), 0)
    index_end = a_text.find('\n', index_start + 1)
    
    if index_end < 0:
        index_end = len(a_text)
    
    line_count = a_position_end.line - a_position_start.line + 1
    for itr in range(line_count):
        line = a_text[index_start:index_end]
        if itr == 0:
            column_start = a_position_start.column
        else:
            column_start = 0
        if itr == line_count - 1:
            column_end = a_position_end.column
        else:
            column_end = len(line) - 1
        
        result += line + '\n'
        result += '~' * column_start + '^'

        index_start = index_end
        index_end = a_text.find('\n', index_start + 1)
        if index_end < 0:
            index_end = len(a_text)

    return result.replace('\t', '')