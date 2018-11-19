from golem.browser import elements, element


new_column_button = ('css', "a[onclick='dataTable.addColumnToDataTable();']")
new_row_button = ('css', "a[onclick='dataTable.addRowToDataTable();']")


def fill_in_header_by_index(index, value):
    header_input = elements('#dataTable>thead input')[index]
    header_input.send_keys(value)


def empty_column_values_by_index(index):
    datatable_rows = elements('#dataTable tbody tr')
    for row in datatable_rows:
        row.find_all('input')[index].clear()


def fill_in_column_values_by_index(col_index, values):
    """Fill in a column with values by index.
    Add any extra necessary rows.
    """
    empty_column_values_by_index(col_index)
    row_index = 0
    for value in values:
        rows = elements('#dataTable tbody tr')
        if row_index >= len(rows):
            # add a row
            element(new_row_button).click()
        rows = elements('#dataTable tbody tr')
        rows[row_index].find_all('input')[col_index].send_keys(value)
        row_index += 1


def add_variable_to_datatable(var_name, var_values=None):
    """Add a variable to the datatable to the first empty column.
    Add a new column if there is no empty column.
    Optional, add values to the column
    """
    headers = elements('#dataTable thead tr th')
    # first is numbering column, remove
    del(headers[0])
    # find first empty header
    empty_col_index = None
    for i, header in enumerate(headers):
        header_input = header.find('input')
        if header_input.value == '':
            empty_col_index = i
            break
    if empty_col_index is None:
        # add a new column
        element(new_column_button).click()
        empty_col_index = i + 1
    fill_in_header_by_index(empty_col_index, var_name)
    if var_values:
        fill_in_column_values_by_index(empty_col_index, var_values)


def assert_variable_in_datatable(column_name):
    header_inputs = elements('#dataTable>thead input')
    msg = '{} header was not found in datatable'.format(column_name)
    assert any(x.value == column_name for x in header_inputs), msg