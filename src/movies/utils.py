def transform_movie_details_to_db_format(movie):
    movie = {k.lower(): v for k, v in movie.items()}
    try:
        movie['imdbvotes'] = int(movie['imdbvotes'].replace(',', ''))
    except ValueError:
        movie['imdbvotes'] = 0
    try:
        movie['imdbrating'] = float(movie['imdbrating'])
    except ValueError:
        movie['imdbrating'] = 0.0
    return movie
