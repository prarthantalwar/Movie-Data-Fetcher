# MovieDataFetcher

MovieDataFetcher is a Python project that utilizes the TMDB (The Movie Database) API to retrieve comprehensive movie information. It provides various features to explore and access movie data, such as certifications, genres, now playing movies, upcoming releases, trending movies, search functionality, watch providers, similar movies, recommendations, user reviews, release dates, keywords, and translations.

## Features

- **Movie Certifications**: Get an up-to-date list of the officially supported movie certifications on TMDB.

- **Genre List**: Retrieve the list of official genres for movies.

- **Now Playing**: Access a list of movies that are currently in theaters, filtered by country.

- **Upcoming**: Explore movies that are being released soon, filtered by country.

- **Trending Movies**: Discover the movies that are currently trending on TMDB.

- **Movie Search**: Search for movies by their title, returning relevant matches along with details.

- **Watch Providers**: Retrieve a list of watch providers for a specific movie, filtered by country.

- **Similar Movies**: Find movies similar to a given movie based on keywords and genres.

- **Recommendations**: Access recommended movies based on a given movie.

- **User Reviews**: Get user reviews for a particular movie.

- **Release Dates**: Retrieve release dates for a movie in different country zones.

- **Keywords**: Explore keywords associated with a specific movie.

- **Translations**: Access translations for a movie in different languages.

## Getting Started

1. Clone the repository:

`git clone https://github.com/prarthantalwar/Movie-Data-Fetcher.git`

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Obtain a TMDB API key by creating an account on the TMDB website (https://www.themoviedb.org/).

4. Replace the placeholder API key in the `main.py` file with your own TMDB API key.

5. Run the project:
`python main.py`


## Usage

The project provides a command-line interface (CLI) to interact with different functionalities. Simply run the project as mentioned in the "Getting Started" section, and follow the prompts and instructions provided in the CLI.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request. 


## Acknowledgements

- This project utilizes the TMDB API ([https://www.themoviedb.org/documentation/api](https://developer.themoviedb.org/reference/intro/getting-started)) to retrieve movie data.

- The project relies on the pycountry library (https://pypi.org/project/pycountry/) for country code to country name conversions.


## Disclaimer

Please refer to TMDB's terms of service and usage guidelines when accessing and utilizing their API.



