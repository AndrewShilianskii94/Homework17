# Homework17#
Movie Search API

This project implements an API for searching movies with information about actors, directors, and genres. The API provides the following endpoints:

- `/movies` — Returns a list of all movies, paginated.
- `/movies/<id>` — Returns detailed information about a movie.
- `/directors` — Returns a list of all directors.
- `/directors/<id>` — Returns detailed information about a director.
- `/genres` — Returns a list of all genres.
- `/genres/<id>` — Returns information about a genre, including a list of movies in that genre.
- `POST /movies` — Adds a movie to the movie database.
- `PUT /movies/<id>` — Updates a movie.
- `DELETE /movies/<id>` — Deletes a movie.

## Requirements

- Python 3.x
- Flask
- Flask-RESTX
- SQLAlchemy

## Installation

1. Clone the repository:

git clone <repository_url>

css
Copy code

2. Navigate to the project directory:

cd movie-search-api

arduino
Copy code

3. Create a virtual environment (optional but recommended):

python -m venv env

r
Copy code

4. Activate the virtual environment:

- For Windows:
  ```
  env\Scripts\activate
  ```

- For macOS/Linux:
  ```
  source env/bin/activate
  ```

5. Install the required dependencies:

pip install -r requirements.txt

markdown
Copy code

## Usage

1. Start the development server:

python app.py

python
Copy code

2. Access the API endpoints using the provided URLs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
