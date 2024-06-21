# Blog-with-users
Blog website, with ability to make posts and comments, with an Admin and users that must log in to access.
using SQLite/SQLalchemy for the databases (users, blogposts, comments), werkzeug for security, and various Flask functions/modules (login, bootstrap, ckeditor, gravatar).

![blog-1](https://github.com/HarryPilgrim/Blog-with-users/assets/76102114/2ca9b4da-bf71-4e9f-99a4-ea7a7e813b27)


![blog-2](https://github.com/HarryPilgrim/Blog-with-users/assets/76102114/5e265b51-5650-402b-9d99-ba40dc13644e)

there is an Admin wrapper function, so that only users with admin privileges can create new posts, delete them etc

![blog-3](https://github.com/HarryPilgrim/Blog-with-users/assets/76102114/af776cfa-23e7-4437-9a4b-06467d6e3dfd)


users register on the site with an email, password, and username, after which they can leave comments.
the password is made save with werkzeug.security and hashed/salted.

![blog-4](https://github.com/HarryPilgrim/Blog-with-users/assets/76102114/9094583c-129f-46bf-83a0-8f5e612fc7f4)

there are 3 tables in the database, the user table relating to the others in one-to-many relationships.


# what I'd like to take from this

I am planning on adding this login functionality to other web-apps (if it makes sense to do so).
