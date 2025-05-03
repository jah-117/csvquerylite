import pandas as pd

def query_csv(file_path, query):
    df = pd.read_csv(file_path)

    query = query.strip()
    if not query.lower().startswith("select "):
        raise ValueError("Query must start with SELECT")

    # Lowercase for searching positions
    lower_query = query.lower()

    # Initialize positions
    where_pos = lower_query.find(" where ")
    order_pos = lower_query.find(" order by ")
    limit_pos = lower_query.find(" limit ")

    # Default values
    select_clause = query[7:]
    where_clause = None
    order_by_col = None
    order_by_asc = True
    limit_clause = None

    # Extract WHERE
    if where_pos != -1:
        select_clause = query[7:where_pos].strip()
        if order_pos != -1:
            where_clause = query[where_pos + 7:order_pos].strip()
        elif limit_pos != -1:
            where_clause = query[where_pos + 7:limit_pos].strip()
        else:
            where_clause = query[where_pos + 7:].strip()
    else:
        if order_pos != -1:
            select_clause = query[7:order_pos].strip()
        elif limit_pos != -1:
            select_clause = query[7:limit_pos].strip()
        else:
            select_clause = query[7:].strip()

    # Extract ORDER BY
    if order_pos != -1:
        if limit_pos != -1:
            order_clause = query[order_pos + 9:limit_pos].strip()
        else:
            order_clause = query[order_pos + 9:].strip()

        order_parts = order_clause.split()
        order_by_col = order_parts[0]
        if len(order_parts) > 1 and order_parts[1].lower() == "desc":
            order_by_asc = False

    # Extract LIMIT
    if limit_pos != -1:
        limit_clause = query[limit_pos + 7:].strip()

    # Apply WHERE
    if where_clause:
        df = df.query(where_clause)

    # Apply ORDER BY
    if order_by_col:
        df = df.sort_values(by=order_by_col, ascending=order_by_asc)

    # Apply SELECT
    selected_cols = [col.strip() for col in select_clause.split(",")]
    if selected_cols != ["*"]:
        df = df[selected_cols]

    # Apply LIMIT
    if limit_clause:
        df = df.head(int(limit_clause))

    return df
