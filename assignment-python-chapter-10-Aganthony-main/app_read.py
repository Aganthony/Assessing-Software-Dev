import sqlite3

db_name = sqlite3.connect('chinook_backup.db')
cursor = db_name.cursor()
cursor.execute("SELECT T.Name, T.Composer, T.UnitPrice FROM tracks T INNER JOIN playlist_track PT ON T.TrackId = PT.TrackId WHERE PT.PlaylistId = 12 ")
for row in cursor:
    print(f"Title: {row [0]}. Composer: {row[1]}. Unite Price: {row[2]} ")
