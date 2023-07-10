import pycountry
import requests
import json

# Common headers for all requests
headers = {
    "accept": "application/json",
    "Authorization": "Bearer <Your API Key/Authorisation token>"
}


# Get http response and return it in a dictionary or list
def get_response_dict(url):
    response = requests.get(url, headers=headers)
    response_dict = json.loads(response.text)  # Parse response text into a dictionary or corresponding type
    return response_dict


# Convert country code to country name
def get_country_name(country_code):
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        if country:
            return country.name
        else:
            return country_code
    except LookupError:
        return country_code



'''
Movie Certifications
'''
# Get an up to date list of the officially supported movie certifications on TMDB.
def get_movie_certifications():
    url = "https://api.themoviedb.org/3/certification/movie/list"
    response_dict = get_response_dict(url)
    print_country_from_response(response_dict)


# Print list of countries from country code from the response dict
def print_country_from_response(response):
    country=response['certifications'].keys()
    print("\n\nFollowing is the list of countries with their codes\n")
    for i in country:
        print(i,"-",get_country_name(i))        
    print_country_restrictions(response)


# Print the restrictions of corresponding country
def print_country_restrictions(response):
    while True:
        cc=input("\nPlease enter the country code of the country you are looking for: ")
        try:
            restrictions=response['certifications'][cc.upper()]
            break
        except:
            print("\nPlease enter correct input and try again\n")
            continue
    print("\n\n\n\nThe following are the different certifications:\n\n")
    for restriction in restrictions:
        print("Certification:", restriction['certification'])
        print("Meaning:", restriction['meaning'])
        print()
    print("\n\n")



'''
Genre List
'''
# Get the list of official genres for movies.
def genre_list():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    response_dict = get_response_dict(url)
    print_genre_list(response_dict)


# Print genre from the response dict
def print_genre_list(response_dict):
    print("\n\n\nThe following is the list of genres:\n\n")
    for i in response_dict['genres']:
        print("ID:", i['id'])
        print("Name:", i['name'])
        print()
    print("\n\n")



'''
Timezones
'''
# Get the list of timezones used throughout TMDB.
def country_codes():
    url = "https://api.themoviedb.org/3/configuration/timezones"
    response_list = get_response_dict(url)
    print_country_codes(response_list)


def print_country_codes(response_list):
    print("\n\n\nThe codes and corresponding zones:\n\n")
    for i in response_list:
        print("Code:", i['iso_3166_1'])
        print("Zones:")
        for j in i['zones']:
            print("     ",j)
        print()
    print("\n\n")
    


'''
Now Playing
'''
# Get a list of movies that are currently in theatres.
def now_playing():
    ch = input("\n\n\nEnter 'Y' if you want to display all the zones and their corresponding code, else anything else: ")
    if ch=='Y':
        country_codes()
    cc=input("\n\n\n\nPlease enter your country code to view the movies currently playing in the theatres: ")
    url = f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1&region={cc.upper()}"
    response_dict = get_response_dict(url)
    print_now_playing(response_dict)
    

# Print all now playing movies    
def print_now_playing(response_dict):
    print(f"\n\n\nThe following are movies playing between {response_dict['dates']['minimum']} and {response_dict['dates']['maximum']}:\n\n\n")
    for i in response_dict['results']:
        print("Title:", i['title'])
        print("Language:", i['original_language'])
        print("Release date:", i['release_date'])
        print("ID:", i['id'])
        print("Genre IDs:")
        for j in i['genre_ids']:
            print("         ",j)   
        print("\n\n\n")
    print("\n\n\n")
    
    

'''
Languages
'''
# Get the list of languages (ISO 639-1 tags) used throughout TMDB.
def languages():
    url = "https://api.themoviedb.org/3/configuration/languages"
    response_list = get_response_dict(url)
    print_languages(response_list)


# Print all the languages
def print_languages(response_list):
    for i in response_list:
        print("ID:", i['iso_639_1'])
        print("Name:", i['english_name'])
        print()
    print("\n\n")
    


'''
Upcoming
'''
# Get a list of movies that are being released soon.
def released_soon():
    ch = input("\n\n\nEnter 'Y' if you want to display all the zones and their corresponding code, else anything else: ")
    if ch=='Y':
        country_codes()
    cc=input("\n\n\n\nPlease enter your country code to view the movies that are being released soon: ")
    url = f"https://api.themoviedb.org/3/movie/upcoming?page=1&region={cc.upper()}"
    response_dict = get_response_dict(url)
    print_released_soon(response_dict)


# Print released soon movies
def print_released_soon(response_dict):
    print(f"\n\n\nThe following are movies released between {response_dict['dates']['minimum']} and {response_dict['dates']['maximum']}:\n\n\n")
    for i in response_dict['results']:
        print("Title:", i['title'])
        print("Language:", i['original_language'])
        print("Release date:", i['release_date'])
        print("ID:", i['id'])
        print("Genre IDs:")
        for j in i['genre_ids']:
            print("         ",j)   
        print("\n\n\n")
    print("\n\n\n")



'''
Trending Movies
'''
# Get the trending movies on TMDB.
def trending_movies():
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"
    response_dict = get_response_dict(url)
    print_trending_movies(response_dict)


# Print trending movies
def print_trending_movies(response_dict):
    print("\n\n\nThe following are the movies trending right now\n\n")
    for i in response_dict['results']:
        print("Title:", i['title'])
        print("Language:", i['original_language'])
        print("Release date:", i['release_date'])
        print("ID:", i['id'])
        print("Genre IDs:")
        for j in i['genre_ids']:
            print("         ",j)   
        print("\n\n\n")
    print("\n\n\n")



'''
Movie search
'''
# Search for movies by their original, translated and alternative titles.
def movie_search():
    name=input("\n\n\nPlease enter the name of the movie you are searching for: ")
    url = f"https://api.themoviedb.org/3/search/movie?query={name}&include_adult=false&language=en-US&page=1"
    response_dict = get_response_dict(url)
    print_movie_search(response_dict)


# Print the movies from the search
def print_movie_search(response_dict):
    movie_ids=[]
    print("\n\n\nThe following are the keyword matches for the movie you entered:\n\n")
    for i in response_dict['results']:
        print("Title:", i['title'])
        print("Language:", i['original_language'])
        print("Release date:", i['release_date'])
        print("ID:", i['id'])
        movie_ids.append(i['id'])
        print("Genre IDs:")
        for j in i['genre_ids']:
            print("         ",j)   
        print("\n\n\n")
    print("\n\n\n")
    print("Please note the movie ID if you wish to find more details related to a movie")
    ch=input("\n\n\nDo you want to find details related to the movie ? If yes, enter 'Y', else anything: ")
    if ch.upper()=='Y':
        ch2 = input("\n\n\nPlease enter the movie ID: ")
        movie_details_choice(movie_ids,ch2)


# Choice for movie details
def movie_details_choice(movie_ids,ch2):
    if int(ch2) in movie_ids:
        movie_menu()
        movie_details(int(ch2))
        while True:
            ch=input("\n\nDo you want to explore other details for the same movie ? If yes, enter 'Y', else anything else: ")
            if ch.upper()=='Y':
                movie_menu()
                movie_details(int(ch2))
            else:
                print("\n\nThanks")
                break
    else:
        print("\n\nWrong ID, please try again")
        movie_details_choice(movie_ids,ch2)
        


'''
Watch providers
'''
# List watch providers for a movie
def watch_providers(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/watch/providers"
    response_dict = get_response_dict(url)
    print_watch_providers(response_dict)


# Print watch providers for the movie
def print_watch_providers(response_dict):
    country_code = input("Enter the country code: ")
    # Check if the country code exists in the dictionary
    if country_code in response_dict["results"]:
        country_data = response_dict["results"][country_code]
        link = country_data["link"]
        providers = {
            "buy": [],
            "flatrate": [],
            "rent": []
        }
        if "buy" in country_data:
            providers["buy"] = country_data["buy"]
        if "flatrate" in country_data:
            providers["flatrate"] = country_data["flatrate"]
        if "rent" in country_data:
            providers["rent"] = country_data["rent"]

        # Print link and providers
        print(f"\n\nFor the selected country, {country_code}\n")
        print("\nLink:", link)
        print("\nProviders:\n")
        for provider_type, provider_list in providers.items():
            if provider_list:
                print(f"{provider_type.capitalize()}:")
                for provider in provider_list:
                    provider_name = provider["provider_name"]
                    print("- ", provider_name)
            print()

    elif response_dict["results"]:
        for country_code, country_data in response_dict["results"].items():
            link = country_data.get("link", "")
            providers = {
                "buy": country_data.get("buy", []),
                "flatrate": country_data.get("flatrate", []),
                "rent": country_data.get("rent", [])
            }

            print("\n\n\nCountry Code:", country_code)
            print("\nLink:", link)
            print("\n\nProviders:")
            for provider_type, provider_list in providers.items():
                if provider_list:
                    print(f"{provider_type.capitalize()}:")
                    for provider in provider_list:
                        provider_name = provider["provider_name"]
                        print("- ", provider_name)
            print()
    
    else:
        print("\n\nSorry we currently don't have any details about the providers, come back later\n")

'''
Similar movies
'''
# Print movies similar to the movie entered based on keywords and genres
def similar_movies(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/similar"
    response_dict = get_response_dict(url)
    print_similar_movies(response_dict)


# Print similar movies
def print_similar_movies(response_dict):
    print("\n\n\nThe following are the movies similar to the movie entered based on keywords and genres:\n\n")
    for i in response_dict['results']:
        print("Title:", i['title'])
        print("Language:", i['original_language'])
        print("Release date:", i['release_date'])
        print("ID:", i['id'])
        print("Genre IDs:")
        for j in i['genre_ids']:
            print("         ",j)   
        print("\n\n\n")
    print("\n\n\n")



'''
Recommendations for the movie
'''
# Print movie recommendations for the movie entered
def recommendations(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/recommendations?language=en-US&page=1"
    response_dict = get_response_dict(url)
    print_recommendations(response_dict)


# Print recommended movies
def print_recommendations(response_dict):
    print("\n\n\nThe following are the recommendations for the movie: \n\n")
    for i in response_dict['results']:
        print("Title:", i['title'])
        print("Language:", i['original_language'])
        print("Release date:", i['release_date'])
        print("ID:", i['id'])
        print("Genre IDs:")
        for j in i['genre_ids']:
            print("         ",j)   
        print("\n\n\n")
    print("\n\n\n")



'''
User reviews
'''
# Get the user reviews for the movie
def user_reviews(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/reviews"
    response_dict = get_response_dict(url)
    print_user_reviews(response_dict)


# Print user reviews
def print_user_reviews(response_dict):
    print("\n\n\nThe following are the reviews for the movie: \n\n")
    for i in response_dict['results']:
        print("\n\nAuthor: ",i['author'])
        print("\nAuthor details:\n")
        j = i['author_details']
        print("Name: ",j['name'])
        print("User name: ",j['username'])
        print("Rating: ",j['rating'])
        print("\n")
        print("Review: ",i['content'])
    print("\n\n\n")
    


'''
Release dates
'''
# Get the release dates for the movie
def release_dates(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/release_dates"
    response_dict = get_response_dict(url)
    print_release_dates(response_dict)


# Print release dates
def print_release_dates(response_dict):
    print("\n\n\nThe following are the release dates in different country zones: \n\n")
    for i in response_dict['results']:
        print("Country zone:", i['iso_3166_1'])
        for j in i['release_dates']:
            print("Language:", j['iso_639_1'])
            print("Release date:", j['release_date'])
        print("\n\n\n")



'''
Keywords
'''
# Get the keywords for the movie
def keywords(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/keywords"
    response_dict = get_response_dict(url)
    print_keywords(response_dict)


# Print keywords
def print_keywords(response_dict):
    print("\n\n\nThe following are the keywords for the movie: \n\n")
    for i in response_dict['keywords']:
        print(i['name'])
    print("\n\n\n")    



'''
Translations
'''
# Get the translations for the movie
def translations(mov_id):
    url = f"https://api.themoviedb.org/3/movie/{mov_id}/translations"
    response_dict = get_response_dict(url)
    print_translations(response_dict)


# Print translations
def print_translations(response_dict):
    print("\n\n\nThe following are the translations for the movie: \n\n")
    for i in response_dict['translations']:
        print("Country code:", i['iso_3166_1'])
        print("Language:", i['iso_639_1'])
        print("Name:", i['name'])
        print("English name:", i['english_name'])
        print("\n\n\n")
    print("\n\n\n")    






# Movie menu
def movie_menu():
    print("""\n\n\nWe have the following services for a movie:
1. Watch providers for the movie
2. Movies similar to the movie based on keywords and genres
3. Recommendations related to it
4. User reviews
5. Release dates
6. Keywords
7. Translations
9. Exit\n\n""")


# Movie details
def movie_details(mov_id):
    ch= input("Please enter your choice of service: ")
    if int(ch)==1:
        watch_providers(mov_id)
    elif int(ch)==2:
        similar_movies(mov_id)
    elif int(ch)==3:
        recommendations(mov_id)
    elif int(ch)==4:
        user_reviews(mov_id)
    elif int(ch)==5:
        release_dates(mov_id)
    elif int(ch)==6:
        keywords(mov_id)
    elif int(ch)==7:
        translations(mov_id)
    elif int(ch)==9:
        print("\n\nThank you.")
    else:
        print("\n\nWrong input, please try again.")
        movie_details(mov_id)
        

# Choice to continue or not
def continue_use():
    print("\n\nDo you want to explore our services again ?")
    ch=input("\nEnter 'Y' if you wish to explore again, else enter anything else: ")
    return ch.upper()


# Menu for the user
def menu():
    print("\n\n\nFollwoing are the service codes:\n\n")
    print("1. Get movie certifications for a country")
    print("2. List all the genres and thier IDs")
    print("3. List all movies currently playing in the theatre")
    print("4. Movies that will be released soon")
    print("5. List all the trending movies")
    print("6. Search for a movie and corresponding details")
    print("9. Exit")
    ch=input("\n\nPlease enter your choice: ")
    choice(ch)


# Choice function
def choice(ch):
    if int(ch)==1:
        get_movie_certifications()
    elif int(ch)==2:
        genre_list()
    elif int(ch)==3:
        now_playing()
    elif int(ch)==4:
        released_soon()
    elif int(ch)==5:
        trending_movies()
    elif int(ch)==6:
        movie_search()
    elif int(ch)==9:
        print("\n\nThank you.")
    else:
        print("\n\nWrong input, please try again.")
        choice()


# MAIN
print("\n\n\nWelcome to the Movie Database\n\n\n")
menu()
while True:
    ch = continue_use()
    if ch.upper()=='Y':
        menu()
    else:
        print("\n\nWe hope you liked our service.\n\n\n\nThank you for using our service.\n\n")
        break
