def transform_movie_details_to_db_format(movie):
    movie = {k.lower(): v for k, v in movie.items()}
    movie['imdbvotes'] = int(movie['imdbvotes'].replace(',', ''))
    movie['imdbrating'] = float(movie['imdbrating'])
    return movie