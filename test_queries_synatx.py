def test_queries_synatx():
    engine = create_engine('<connection string>')
    with engine.connect() as con:
        queries_list = glob.glob('**/*.sql',recursive=True)
        for query_file in queries_list:
            with open(query_file) as f:
                query = f.read()
                test_query = f"Explain {query}"
                con.execute(test_query)