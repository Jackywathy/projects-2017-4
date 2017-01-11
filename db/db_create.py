import sqlite3

with sqlite3.connect('db.db') as conn:
    cur = conn.cursor()

    # Drop tables if they exist
    cur.execute('DROP TABLE IF EXISTS comments')
    cur.execute('DROP TABLE IF EXISTS photos')
    cur.execute('DROP TABLE IF EXISTS posts')
    cur.execute('DROP TABLE IF EXISTS users')

    # Create the `users` table
    cur.execute(
    '''
    CREATE TABLE users
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    nickname TEXT,
    email TEXT NOT NULL,
    gender TEXT,
    dob TEXT,
    bio TEXT,
    picture TEXT,
    creation_date TEXT)
    '''
    )

    # Create the `posts` table
    cur.execute(
    '''
    CREATE TABLE posts
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    description TEXT,
    title TEXT NOT NULL,
    post_date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id))
    '''
    )

    # Create the `photos` table
    cur.execute(
    '''
    CREATE TABLE photos
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL,
    post_id INTEGER NOT NULL,
    photo_date TEXT NOT NULL,
    FOREIGN KEY(post_id) REFERENCES posts(id))
    '''
    )

    # Create the comments table
    cur.execute(
    '''
    CREATE TABLE comments
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    parent_id INTEGER,
    text TEXT NOT NULL,
    date TEXT NOT NULL,
    score INTEGER NOT NULL,
	loc_latitude REAL,
	loc_longitude REAL,
    FOREIGN KEY(parent_id) REFERENCES comments(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(post_id) REFERENCES posts(id))
    '''
    )
    conn.commit()


    # ---- Populate the database with dummy data

    # Create dummy users
    cur.execute(
    '''
    INSERT INTO users VALUES
    (NULL, 'george', 'password', 'G', 'some@email.com', 'Male', '01/01/2000', 'I''m a cool kid.', '', '11/1/2017'),
    (NULL, 'tim', 'password', 'TimmyD', 'some@email.com', 'Male', '01/01/1990', 'Only tutor who knows what a Finite State Automata is :\).', '', '07/1/2017'),
    (NULL, 'will', 'password', '', 'some@email.com', 'Male', '01/01/1993', 'Full Full-stack developer', '', '07/1/2017'),
    (NULL, 'steph',	'password', 'Stiff', 'some@email.com', 'Female', '01/01/2000', 'New Zealand is the best country', '', '08/01/2016'),
    (NULL, 'evan', 'password', 'CompSci', 'some@email.com', 'Male',	'01/01/1995', 'Computer Science is obviously the best subject', '', '08/01/2016'),
    (NULL, 'liam', 'password', '', 'some@email.com', 'Male', '01/01/1995', 'Don''t scare me please :O', '', '08/01/2017'),
    (NULL, 'james', 'password', 'God', 'some@email.com', 'Male', '01/01/1989', 'God to NCSS students. I read stories to children for a living. I lost my hat :\(', '', '08/01/2016'),
    (NULL, 'rachel', 'password', 'Rad Rachel', 'some@email.com', 'Female', '01/01/2000', '¯\\_\(ツ\)_/¯', '', '08/01/2016'),
    (NULL, 'luke', 'password', 'GitOut', 'some@email.com', 'Male', '01/01/1999', 'Git King. Git Kraken. Git Merge without mr merge monkey',	'', '08/01/2016'),
    (NULL, 'lucy', 'password', '', 'some@email.com', 'Female', '01/01/1990', 'Atlassian.', '', '08/01/2016'),
    (NULL, 'julia', 'password', '', 'some@email.com', 'Female', '01/01/1990', ':)', '', '08/01/2016'),
    (NULL, 'robot', 'password', 'Mr Robot', 'some@email.com', '', '01/01/1999', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean non mattis odio. Suspendisse mollis tristique sapien. Proin ac mi ornare nibh tempus luctus. Ut in ex scelerisque felis lacinia hendrerit. Nulla scelerisque ultricies tempus. Vestibulum ullamcorper eros mi, non ultricies erat dapibus sed. Aenean pretium nisi a magna vestibulum varius. Phasellus odio ex, porta quis erat rhoncus, malesuada cursus libero. Nam nec nibh eget felis eleifend vestibulum. Aenean lobortis eleifend dolor vitae elementum. Nullam tincidunt tellus id dolor tempus, laoreet hendrerit lorem commodo.', '', '01/01/1970'),
    (NULL, 'generic', 'password', 'Generico', 'some@email.com', '', '01/01/2017', 'Your Generic User Bio', '', '11/01/2017')
    '''
    )

    # Create dummy posts
    cur.execute(
    '''
    INSERT INTO posts VALUES
    (NULL, 0, 'Where can I find this watch from? It looks sick and I really want it :)', 'What watch is this?', '01/01/2017'),
    (NULL, 0, 'Yeah, they kinda cool ^_^', 'What is this pair of shoes?', '01/01/2017'),
    (NULL, 0, 'Yeah, they kinda cool ^_^', 'What is this pair of shoes?', '01/01/2017'),
    (NULL, 0, 'Yeah, they kinda cool ^_^', 'What is this pair of shoes?', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 1, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 2, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 2, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 4, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 4, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 4, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 7, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 7, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 7, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 7, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 8, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 10, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 10, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 10, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 10, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 10, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 12, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 12, 'Some generic description O_O', 'Generic title', '01/01/2017'),
    (NULL, 12, 'Some generic description O_O', 'Generic title', '01/01/2017')
    '''
    )

    # Create dummy photos
    cur.execute(
    '''
    INSERT INTO photos VALUES
    (NULL, '/images/cats.jpg', 0, '01/01/2017'),
    (NULL, '/images/cats.jpg', 1, '01/01/2017'),
    (NULL, '/images/cats.jpg', 3, '01/01/2017'),
    (NULL, '/images/cats.jpg', 7, '01/01/2017'),
    (NULL, '/images/cats.jpg', 8, '01/01/2017'),
    (NULL, '/images/cats.jpg', 10, '01/01/2017'),
    (NULL, '/images/cats.jpg', 10, '01/01/2017'),
    (NULL, '/images/cats.jpg', 12, '01/01/2017'),
    (NULL, '/images/cats.jpg', 15, '01/01/2017'),
    (NULL, '/images/cats.jpg', 18, '01/01/2017'),
    (NULL, '/images/cats.jpg', 19, '01/01/2017'),
    (NULL, '/images/cats.jpg', 22, '01/01/2017'),
    (NULL, '/images/cats.jpg', 22, '01/01/2017'),
    (NULL, '/images/cats.jpg', 22, '01/01/2017')
    '''
    )

    # Create dummy comments
    cur.execute(
    '''
    INSERT INTO comments VALUES
    (NULL, 0, 0, NULL, 'Nice meme!', '01/01/2017', 1, -33.8883064, 151.1941413),
    (NULL, 1, 0, 1, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 0, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 2, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 4, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 6, 6, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 7, 7, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 9, 8, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 8, 9, 'Nice meme!', '01/01/2017', 1, -33.8883064, 151.1941413),
    (NULL, 4, 8, 9, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 8, 10, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 10, NULL, 'Nice meme!', '01/01/2017', 1, -33.8883064, 151.1941413),
    (NULL, 2, 10, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 11, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 14, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 17, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 6, 17, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 18, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 20, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 12, 20, 19, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 21, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 22, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL)
    '''
    )
	
