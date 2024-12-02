import sqlite3
import requests



def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    connection = sqlite3.connect('posts.db')
    response = requests.get('https://jsonplaceholder.typicode.com//posts')
    posts = response.json()

    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        title TEXT NOT NULL,
        body TEXT NOT NULL );
        ''')

    choice=input("Wanna downlod posts from server into DB?(y/n): ")
    if choice=='y':
        for post in posts:
            cursor.execute('INSERT INTO posts (id,user_id,  title, body) VALUES (?, ?, ?, ?)',
                           (post['id'],post['userId'], post['title'], post['body']))

    readChoice = input("Wanna see all posts?(y/n): ")
    if readChoice == 'y':
        cursor.execute('SELECT * FROM posts')
        posts = cursor.fetchall()
        for post in posts:
            print(post)

    readUChoice = input("Wanna see specific user posts?(y/n): ")
    if readUChoice == 'y':
        userId=input("input user ID: ")
        cursor.execute('SELECT * FROM posts WHERE user_id=?',(userId,))
        posts = cursor.fetchall()
        for post in posts:
            print(post)
    connection.commit()
    connection.close()