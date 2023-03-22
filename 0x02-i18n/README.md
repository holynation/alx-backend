## Resources

**Read or watch:**

-   [Flask-Babel](https://intranet.alxswe.com/rltoken/fBpGjDt2BFuBFiz-jwublQ "Flask-Babel")
-   [Flask i18n tutorial](https://intranet.alxswe.com/rltoken/RtGz7pI7TKnYqrMMG9rWMg "Flask i18n tutorial")
-   [pytz](https://intranet.alxswe.com/rltoken/7rrCz4pkpqAn4FfRZ2Vsvw "pytz")
## Requirements

-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle style (version 2.5)
-   The first line of all your files should be exactly  `#!/usr/bin/env python3`
-   All your  `*.py`  files should be executable
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   All your functions and coroutines must be type-annotated.

## Tasks

### 0. Basic Flask app

mandatory

Score:  0.0%  (Checks completed: 0.0%)

First you will setup a basic Flask app in  `0-app.py`. Create a single  `/`  route and an  `index.html`  template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `0-app.py, templates/0-index.html`

Done?  Help  Check your code  Ask for a new correction  QA Review

### 1. Basic Babel setup

mandatory

Score:  0.0%  (Checks completed: 0.0%)

Install the Babel Flask extension:

```
$ pip3 install flask_babel

```

Then instantiate the  `Babel`  object in your app. Store it in a module-level variable named  `babel`.

In order to configure available languages in our app, you will create a  `Config`  class that has a  `LANGUAGES`  class attribute equal to  `["en", "fr"]`.

Use  `Config`  to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `1-app.py, templates/1-index.html`

Done?  Help  Check your code  Ask for a new correction  Get a sandbox  QA Review

### 2. Get locale from request

mandatory

Score:  0.0%  (Checks completed: 0.0%)

Create a  `get_locale`  function with the  `babel.localeselector`  decorator. Use  `request.accept_languages`  to determine the best match with our supported languages.

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `2-app.py, templates/2-index.html`

Done?  Help  Check your code  Ask for a new correction  QA Review

### 3. Parametrize templates

mandatory

Score:  0.0%  (Checks completed: 0.0%)

Use the  `_`  or  `gettext`  function to parametrize your templates. Use the message IDs  `home_title`  and  `home_header`.

Create a  `babel.cfg`  file containing

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_

```

Then initialize your translations with

```
$ pybabel extract -F babel.cfg -o messages.pot .

```

and your two dictionaries with

```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr

```

Then edit files  `translations/[en|fr]/LC_MESSAGES/messages.po`  to provide the correct value for each message ID for each language. Use the following translations:

msgid

English

French

`home_title`

`"Welcome to Holberton"`

`"Bienvenue chez Holberton"`

`home_header`

`"Hello world!"`

`"Bonjour monde!"`

Then compile your dictionaries with

```
$ pybabel compile -d translations

```

Reload the home page of your app and make sure that the correct messages show up.

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`

Done?  Help  Check your code  Ask for a new correction  Get a sandbox  QA Review

### 4. Force locale with URL parameter

mandatory

Score:  0.0%  (Checks completed: 0.0%)

In this task, you will implement a way to force a particular locale by passing the  `locale=fr`  parameter to your app’s URLs.

In your  `get_locale`  function, detect if the incoming request contains  `locale`  argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting  `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting  `http://127.0.0.1:5000/?locale=fr`  should display this level 1 heading:**  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230322T172302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=118570ab46ab2a2ed6e9becd8198703088ccfe902f416132f58fc9156cc81c07)

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `4-app.py, templates/4-index.html`

Done?  Help  Check your code  Ask for a new correction  QA Review

### 5. Mock logging in

mandatory

Score:  0.0%  (Checks completed: 0.0%)

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in  `5-app.py`.

```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

```

This will mock a database user table. Logging in will be mocked by passing  `login_as`  URL parameter containing the user ID to log in as.

Define a  `get_user`  function that returns a user dictionary or  `None`  if the ID cannot be found or if  `login_as`  was not passed.

Define a  `before_request`  function and use the  `app.before_request`  decorator to make it be executed before all other functions.  `before_request`  should use  `get_user`  to find a user if any, and set it as a global on  `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid

English

French

`logged_in_as`

`"You are logged in as %(username)s."`

`"Vous êtes connecté en tant que %(username)s."`

`not_logged_in`

`"You are not logged in."`

`"Vous n'êtes pas connecté."`

**Visiting  `http://127.0.0.1:5000/`  in your browser should display this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230322T172302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=494532c3874920e2af7f9c23839b26b2549ac419fbcd293a74213931ad94c1b1)

**Visiting  `http://127.0.0.1:5000/?login_as=2`  in your browser should display this:**  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230322T172302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cc755dc3159edbc1b779cbff83d95dae820bcce3821a4eced8be90b40b3e2a43)

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `5-app.py, templates/5-index.html`

Done?  Help  Check your code  Ask for a new correction  QA Review

### 6. Use user locale

mandatory

Score:  0.0%  (Checks completed: 0.0%)

Change your  `get_locale`  function to use a user’s preferred local if it is supported.

The order of priority should be

1.  Locale from URL parameters
2.  Locale from user settings
3.  Locale from request header
4.  Default locale

Test by logging in as different users

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230322T172302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=85edc60cf0f1267cb488cd8862320930d4e09c4acdaba812fc60ddad56815a25)

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `6-app.py, templates/6-index.html`

Done?  Help  Check your code  Ask for a new correction  QA Review

### 7. Infer appropriate time zone

mandatory

Score:  0.0%  (Checks completed: 0.0%)

Define a  `get_timezone`  function and use the  `babel.timezoneselector`  decorator.

The logic should be the same as  `get_locale`:

1.  Find  `timezone`  parameter in URL parameters
2.  Find time zone from user settings
3.  Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use  `pytz.timezone`  and catch the  `pytz.exceptions.UnknownTimeZoneError`  exception.


**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `7-app.py, templates/7-index.html`
### 8. Display the current time

#advanced

Score:  0.0%  (Checks completed: 0.0%)

Based on the inferred time zone, display the current time on the home page in the default format. For example:

`Jan 21, 2020, 5:55:39 AM`  or  `21 janv. 2020 à 05:56:28`

Use the following translations

msgid

English

French

`current_time_is`

`"The current time is %(current_time)s."`

`"Nous sommes le %(current_time)s."`

**Displaying the time in French looks like this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bba4805d6dca0a46a0f6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230322T172341Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=391f7fd57e06d785fd667d0982a12cb4e54ac73c707e1b540237cc0971ab6050)

**Displaying the time in English looks like this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/54f3be802024dbcf06f4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230322T172341Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=450f8cd63ab14007b72f3009bf450f3b2f653c0477482e88c62b6c9ea7e3687b)

**Repo:**

-   GitHub repository:  `alx-backend`
-   Directory:  `0x02-i18n`
-   File:  `app.py, templates/index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po`

Done?  Help  Get a sandbox  QA Review

Ready for a  new  manual review

Copyright © 2023 ALX, All rights reserved.
