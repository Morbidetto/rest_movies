# Rest movies

Rest movies is simple Django application implementing basic REST API. It uses Django REST framework to showcase rest flow. Data is saved to PostgreSQL database, which was chosen because of implementation of ArrayField, and HStoreField perfect for storing Python's list and dictionaries.

## Installation

You can run application directly on your system or using prepared Docker compose solution. Please modify those environment variables in your system or in docker-compose.yml:

SECRET_KEY - Django secret key

OMDB_KEY - Key to [omdb API](http://www.omdbapi.com/)

Remember to run:
```bash
python manage.py migrate
```
Configure PostgreSQL database settings if you're not using Docker.

## Usage
​**POST api/movies:**

​Request body should contain movie title.
Based on passed title, other movie details are fetched from [omdbapi](http://www.omdbapi.com/).
Request response includes created movie object, along with data fetched from external API.

**GET api/movies:**

​List of all movies already present in application database.
Can be filtered using 'year', 'director', 'title', 'type' fields.
Can be sorted using 'year', 'metascore', 'imdbrating', 'imdbvotes fields.
Can be searched.

**POST api/comments:**

​Request body contain ID of movie already present in database, and comment text body.
Comment is saved to application database with actual date and returned in request response.

**GET api/comments:**

Fetch list of all comments present in application database.
Can be filtered using 'movie' and 'date' fields.

**GET api/top:**

​Return top movies already present in the database ranking based on a number of comments added to the movie in the specified date range using start_date and end_date in request body. The response include the ID of the movie, position in rank and total number of comments (in the specified date range).
Movies with the same number of comments have the same position in the ranking.
