# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id int, 
        start_time bigint, 
        user_id int, 
        level varchar, 
        song_id varchar, 
        artist_id varchar, 
        session_id int, 
        location varchar, 
        user_agent varchar)
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id int, 
        first_name varchar, 
        last_name varchar, 
        gender varchar, 
        level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id varchar, 
        title varchar, 
        artist_id varchar, 
        year int, 
        duration float
    )
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id varchar, 
        name varchar, 
        location varchar, 
        latitude int, 
        longitude int
    )
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time bigint, 
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday int
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT into users VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
    INSERT into songs VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
    INSERT INTO artists VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
    INSERT into time VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, s.artist_id from songs s join artists a on (s.artist_id = a.artist_id) where s.title = %s and a.name = %s and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]