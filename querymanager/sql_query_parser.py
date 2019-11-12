import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML


def is_subselect(parsed):
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        if item.is_group:
            for x in extract_from_part(item):
                yield x
        if from_seen:
            if is_subselect(item):
                for x in extract_from_part(item):
                    yield x
            elif item.ttype is Keyword and item.value.upper() in ['ORDER', 'GROUP', 'BY', 'HAVING', 'GROUP BY']:
                from_seen = False
                StopIteration
            else:
                yield item
        if item.ttype is Keyword and item.value.upper() == 'FROM':
            from_seen = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                value = identifier.value.replace('"', '').lower()
                yield value
        elif isinstance(item, Identifier):
            value = item.value.replace('"', '').lower()
            yield value


def extract_tables(sql_query):
    # let's handle multiple statements in one sql string
    extracted_tables = []
    statements = list(sqlparse.parse(sql_query))
    for statement in statements:
        if statement.get_type() != 'UNKNOWN':
            stream = extract_from_part(statement)
            extracted_tables.append(
                set(list(extract_table_identifiers(stream))))
    if len(extracted_tables) > 0 and sql_query.find('data'):
        extracted_tables[0] = 'data'

    return extracted_tables[0]


def replace_date_filters(sql_query, date_from):
    split_by_between = sql_query.split('BETWEEN')
    if len(split_by_between) >= 1:
        split_by_and = split_by_between[1].split('AND')
        date_from_in_db = split_by_and[0]
        sql_query = sql_query.replace(date_from_in_db, " '"+date_from+"' ")
    return sql_query


def get_tokens(sql_query):
    parsed = sqlparse.parse(sql_query)
    where = parsed[0][-1]
    sql_tokens = []
    identifier = None
    for i in where.tokens:
        try:
            name = i.get_real_name()
            if name and isinstance(i, sqlparse.sql.Identifier):
                identifier = i
            elif identifier and isinstance(i, sqlparse.sql.Parenthesis):
                sql_tokens.append({
                    'key': str(identifier),
                    'value': token.value
                })
            elif name:
                identifier = None
                # sql_tokens.append("{0} - {1} - {2}".format(str(i), str(name), i.value))
                sql_tokens.append({
                    'key': str(name),
                    'value': u''.join(token.value for token in i.flatten()),
                })
            else:
                get_tokens(i)
        except:
            pass
    return sql_tokens
