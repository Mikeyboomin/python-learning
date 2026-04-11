def can_watch_movie(age, has_ticket, movie_title, rating):
    if not isinstance(age, (int, float)):
        return 'Age must be a number'
    elif age <= 0:
        return 'Age must be greater than 0'
    elif not isinstance(has_ticket, bool):
        return 'has_ticket must be True or False'
    elif not isinstance(movie_title, str) or not movie_title:
        return 'Movie title is required'
    elif rating not in ['G', 'PG', 'PG-13', 'R']:
        return 'Invalid rating'
    elif rating == 'R' and age < 18:
        return f'You must be 18 or older to watch {movie_title}'
    elif rating == 'PG-13' and age < 13:
        return f'You must be 13 or older to watch {movie_title}'
    elif not has_ticket:
        return f'You need a ticket to watch {movie_title}'
    else:
        return f'Enjoy {movie_title}!'
    
print(can_watch_movie(18, True, 'Jurassic World', 'R'))