<!--![responsive app](static/images/multiple-devices.jpeg)

<h1 align="center">SetGoals</h1>

[View the live project here.](http://set-goals-vl.herokuapp.com)

This is the website built to meet the requirements for milestone 3 of fullstack developer diploma at Code Institute. It is designed to be responsive and accessible on a range of devices, making it easy to navigate for users and visiting users.

I aim to develop and test a platform where the user can plan life goals. Users will be looking to take control of their lives and would have listened talkers or have read books that had encouraged planning and goal setting. Ideas such as “He who fails to plan is planning to fail.” by Winston Churchill or “We become what we think about most of the time” by Earl Nightingale support the need to set goals.  
This platform will enable users to create their goals, store them, edit or delete them from the my goals page. As a future feature, the app would include a forum where different users could post their achievements or discuss hurdles, or points of view to increase users interaction with the app. Another feature that had not been included would be the upload of images into the goal card as create an image board with the collection of images. For this feature I would need to use technology that I have not learned yet, as MongoDB BSON documents are capped at 16 MB.

## User Experience (UX)

- ### User stories

  - #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about setting goals.
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    3. As a First Time Visitor, I want to be able to easily register on website as user and set first goals.

  - #### Returning Visitor Goals

    1. As a Returning Visitor, I want to easily refer back to the main steps of setting smart goals.
    2. As a Returning Visitor, I want to easily log in to my goals page.
    3. As a Returning Visitor, I want to be able to create, update and delete my goals.

  - #### Frequent User Goals
    1. As a Frequent User, I want to explore content in image boards online related to my goals. As images are a powerful tool to help focus in goals.
    2. As a Frequent User, I want to easily access my current goals and costumize them.

- ### Design
  - #### Colour Scheme
    - The two main colours used on the website are inspired by this [photo](https://www.behance.net/gallery/45528461/Selectologie) using [ adobe color ](color.adobe.com) software.  
      ![alt text](static/images/colours.jpeg "generated colour scheme")
  - #### Typograpy
    - The Gruppo font is the font used for the Logo with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Gruppo Font is a display typeface that comes with clean and clear texture.
    - The Noto Sans font in the main font used throughou this project, with Sans Serif as the fallback font.
  - #### Imagery
    - The background hero image is chosen as a path and is divided in two. It is designed to be striking and give the user the ilusion of discovering a path.  
      The svg image used in the middle div in home pageuses the same colour as navbar and footer and is supposed to suggest planning ideas. The same svg is used in my goals card while upload image is not available.

* ### Wireframes

  - [Register page in desktop and tablet view](static/images/wireframes/register_dt.png "wireframe for register page in desktop and tablet view");

  - [Register page in mobile view](static/images/wireframes/register_mobile.png "wireframe for register page in mobile view");

  - [Login page in desktop and tablet view](static/images/wireframes/login_dt.png "wireframe for login page in desktop and tablet view");

  - [Login page in mobile view](static/images/wireframes/login_mobile.png "wireframe for login page in mobile view");

  - [Home page in desktop and tablet view](static/images/wireframes/home_dt.png "wireframe for Home page in desktop and tablet view");

  - [Home page in mobile view](static/images/wireframes/home_mobile.png "wireframe for Home page in mobile view");

  - [New Goal page in desktop and tablet view](static/images/wireframes/newGoal_dt.png "wireframe for My progress page in desktop and tablet view");

  - [New Goal page in mobile view](static/images/wireframes/newGoal_mobile.png "wireframe for New Goal page in mobile view");

  - [Goal page in desktop and tablet view](static/images/wireframes/goalPage_dt.png "wireframe for Goal page in desktop and tablet view")

  - [Goal page in mobile view](static/images/wireframes/goalPage_mobile.png "wireframe for New Goal page in mobile view");

Wireframes had been an excellent starting point to this project however, after having login and my goals page in place I have realised that the project would benefit from having a home page and a SMART page, where a visiting user could fill inspired in using the app.

## Features

- Responsive on multiple device sizes

- Interactive elements
    - Materialize Navigation bar with sidenav for mobile view and small tablets
    - Materialize Footer with links for homepage and social media
    - Materialize parallax feature to add beauty to the app and allude to "seeing the road ahead" - in home page
    - Logo in navbar redirects to home page
    - Links in navbar redirect user to the corresponding pages
    - Materialize pulse button in home page to call attention to the word SMART - once clicked it will redirect to the SMART? page
    - Materialize collapsible cards in SMART page - to add more information
    - Materialize forms with dropdown menu
    - Materialize waves effect when ckicking on a button

- Register and Login
    - Register page with Materialize input form for username, email, password and submit button
    - Login page with Materialize input form for username, password and submit button

- Create, update and delete data
    - Goal cards in My goals page have a edit and delete icons that will enable existing Goals to be deleted and updated
    - New Goal page has a form that allows the user to create a new goal by storing the new date when the form is filled

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python3](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Frameworks, Libraries & Programs Used

1. [Materialize 1.0.0:](https://materializecss.com)
   - Materialize was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import Gruppo and Noto Sans fonts into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used throughout the website to add icons for UX purposes.
4. [jQuery:](https://jquery.com/)
   - jQuery came with Materialize to make the navbar toggle, the collapsible bars, dropdown menu, the parallax effect in home page, the tooltip effect in edit and delete Icons, the card hide/show content, but it was also used for the alert box with function in JavaScript.
5. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
7. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
   - Photoshop was used to resize images for the website.
8. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
9. [Adobe Color:](https://color.adobe.com/create/color-wheel)
   - Adobe Color was used to generate the color scheme.
10. [Flask:](https://pypi.org/project/Flask/)
    - Flask was used in the html templates including a base template.
11. [Jinja2:](<https://en.wikipedia.org/wiki/Jinja_(template_engine)>)
    - Jinja is part of the Flask library. Flask templates for this project used Jinja.
12. [Werkzeug:](https://pypi.org/project/Werkzeug/)
    - Werkzeug is part of the Flask library and was used throughout this project to encrypt data.
13. [PyMongo:](https://pypi.org/project/pymongo/)
    - The pymongo package is a native Python driver for MongoDB. crucial in the communication of python with MongoDB, both used in this project.
14. [MongoDb:](https://www.mongodb.com/)
    - MongoDB is a document database and is used to store the data input from the forms in new goals page. The data stored is created, updated and deleted in mongoDb through the app.  
15. [Heroku:](https://www.heroku.com/)
    - Heroku is a cloud platform as a service (PaaS) and supports python language. Heroku was used to deploy this project, is where the app is hosted.
16. [Responsivedesign.is:](http://ami.responsivedesign.is/)
    - Website used to create responsive image used in readme page (however mobile view is not true to app display in a mobile, as hero section is visible in the actual app)
17. [Undraw:](https://undraw.co/)
    - To obtain SVG illustrations with colour scheme of the project, used in Home, SMART and My Goals pages.

##  Testing

Please refer to [testing.md](testing.md) file to find the report on the testing carried out in this project.

---

##  Deployment

SL arts was developed using Gitpod and GitHub to host the repository.

### Local Deployment
For local deployment, you need to have an IDE such as Gitpod and you need to install the following in your IDE:
- An IDE - for this project was used GitPod
- to create the database was used MongoDB Atlas
- Git, Python3, PIP3
  
#### Directions

##### Cloning repository using command line

1. You can save a copy of this repository:
On GitHub, navigate to the main page of the repository. Above the list of files, click  Code then "Download Zip" button, and after extract the Zip file to your folder.

2. Open Terminal.

3. Change the current working directory to the location where you want the cloned directory.

4. Type git clone, and then paste the URL you copied earlier.

    $ git clone https://github.com/veraleitaodev/setGoals.git
    Press Enter to create your local clone.

5. Now create a Database that you intend to use for this cloned project with MongoDB. 

6. Create a new Database called "setGoals" in [MongoDB Atlas](https://www.mongodb.com/).   
7. In "setGoals" database create the three following collections:
    ##### categories
    ```
    _id: <ObjectId>
    category_name: <String>
    ```
    ##### goals
    ```
    _id: <ObjectId>
    goal_title:  <String>
    category_name: <String>
    goal_description: <String>
    due_date: <String>
    author: <String>
    ```
    ##### Users
    ```
    _id: <ObjectId>
    username: <String>
    password: <String>
    ```

8. Return to the Terminal and enter the following to install all required dependencies:
```
pip3 install -r requirements.txt
```
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*

9. Set up environment variables:
    - Create __.env__ file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
  
10. You will now be able to run the application using the following command `python3 run.py`. 

Find information about deploying a repository [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

##### Heroku Deployment

To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:

1. Create or update __requirement.txt__ file using the following command in the terminal:  
`pip3 freeze > requirements.txt`

2. Create a __Procfile__ using the following command in the terminal:   
`echo web: python run.py > Procfile`
    (__remember__ to use capital P);  
    delete extra line at the bottom in Procfile as it might cause problems;

3. `git add`, `git commit` and `git push` these files to GitHub repository

4. Create a __new app__ in Heroku, assigning a unique name and set a region (for SetGoals i had set Europe)

5. Set up automatic deployment by adding environment variables to settings:
    -   click on the __settings__ and then click on __Reveal Config Vars__ and set the following vars:
        -   __IP__ : 0.0.0.0
        -   __PORT__ : 8080
        -   __MONGO_URI__ : `<link to MongoDB database>`
        -   __SECRET_KEY__ : `<secret key>`
        -   __DEBUG__: __FALSE__  

6. The app will be deployed and ready to run. Click "Open App" to view the app.   
  
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.

---

##  Credits
-   I had great help from my mentor Rohit Sharma.
-   I have written the code for the project with inspiration in the materials learnt at code institute and the use of libraries such as Materialize, as mentioned in this document.
-   Cloning information sourced from [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository);
-   Information in smart.html obtained from [here](https://www.ucop.edu/local-human-resources/_files/performance-appraisal/How%20to%20write%20SMART%20Goals%20v2.pdf);
-   Code obtained from [stackoverflow](https://stackoverflow.com/questions/553402/how-to-fadeout-remove-a-div-in-jquery) to fade out and hide flash message.-->
xxxxx
<!--# Deployment

## Setting up the database and Heroku app

- Go heroku.com, create an account or log in. <i>I already have an account so I just had to log in and validate my account as I had arrived to a maximum of 5 app created.</i> 
- Click on new and then on new app. Give your app a name, it has to be unique. <i>I called my app sandra-lopes-art.</i> Then choose the region closest to you and lastly click on create app button.

- Go to the resources tab, go to the add-ons and search for Heroku Postgres. Use the free plan and click on the submit order form button.

- On your code editor install dj_database_url and psycopg2-binary with the commands
            <i> pip3 install dj_database_url

            pip3 install psycopg2-binary </i>

 for the use of heroku Postgres.

- After that freeze the requirements, <i>pip3 freeze > requirements.txt</i>.

- Go to settings.py and import dj_database_url.  Go to the database settings section and  comment out the the default configuration and add a new database default with a call to dj_database_url.parse(). Go back to Heroku, go to the settings tab and reveal the config vars. Copy the database-url value and past this into the parentheses (). 
<i>DATABASE = {
	'default': dj_database_url.parse('here comes you database-url value')
}</i>

- Because you're using Postgres, you have to run all the migrations again, you can see this when you run python3 manage.py show migrations as the boxes are no longer checked. If you used JSON files to upload your categories an products you have to load them again. If you add them manually then you have again after your app is deployed to Heroku.

- Create a new superuser, <i>python3 manage.py createsuperuser,</i> and follow the steps. Your Heroku app and database are ready to go so remove the new database default and uncomment the original database default. You do this last step to make sure your database URL doesn't end up in version control and people can't use it for them selfs.

-  Then add, commit and push to Github.

## Deploying to Heroku

- In settings.py go back to the database section. You're going to going to set your database default in an if statement, if 'DATABASE_URL' in os.environ:. So that when our app is running on Heroku we connect to Postgres otherwise we connect to your local database. The first part of this if statement is going to be the default database for when connected to Heroku and it will be similar to the default database code you just removed but with your Heroku URL secured

        DATABASE = {
	        'default': dj_database_url.parse(os.environ.get('DATABASE_URL))
        }

Put the original database default in an else statement

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

- To be able to deploy to Heroku you need a couple of other things:
 	- Install gunicor, <i>that will act as a web server,</i> and freeze this in the requirments.txt

	- Create a Procfile, it needs the capital P. To tell Heroku to create a web dyno, <i>which will run gunicorn and serve our Django app</i>. You open a new file and add this to the file. web: gunicorn taste_world_snacks.wsgi:application

- Login to Heroku in the console. To log in, you can use the command Heroku login or Heroku login -i and follow the steps. Then temporarily disable collective static by using the command Heroku config: set DISABLE_COLLECTSTATIC=1 --app taste-world-snacks, <i>so that Heroku won't try to collect static files when we deploy</i>.

- You need to add taste-world-snacks to allowed hosts in settings.py and add the localhost as well, <i>so that you can still work on it. I tidied up secured later so I could test automatic deployment.</i> Then add, commit and push to Github.

- To deploy to Heroku using the commands:
	- heroku git:remove -a taste-world-snacks
	- git push heroku master

- To set up automatic deployment go to the deploy tab on Heroku and click on connect to Github. Search for the correct repository and then click connect, after that go to the Enable Automatic Deploys button and click it.

- Then to add secure, look up a secret key generator and generate a secret key. Copy that and go to the settings tab in Heroku, reveal config vars to make a new key with the name SECRET_KEY and past in your generated secret key in the value field and add it. After that go settings.py to replays the SECRET_KEY value with a call to get it from the environment with an empty string as default, <i>SECRET_KEY = os.environ.get('SECRET_KEY', '').</i>

- Set DEBUG to be true only if there is a variable called development, <i>DEBUG = 'DEVELOPMENT' in os.environ.</i> Lastly add, commit and push to Github. If you go to the activity tab on Heroku, you can see there is a build-in progress and that your automatic deployment is working.

## Store static files and images on AWS

### Setup bucket

- Go to aws.amazon.com there create an account and follow the steps or log in. <i>I already have an account from a previous project so I only had to log in.</i>

- Once logged in search for S3 and open it and create a new bucket and give it a name. to keep it simple I gave it my Heroku app name, taste-world-snacks. Then select the region that is close to you, uncheck block all public access and acknowledge that the bucket will be public. <i><u>It needs to be public to allow public access to our static files.</i></u> Then click create bucket

- The new bucket needs a few basic settings. 
	- To do that select your bucket, go to properties tab, look for static website hosting and click edit and click on enable and host a static website. <i>I used index.html and error.html as index 	and error documents. As this is for educational use so I can go with defaults.</i> 

	- Then go to the permission tab, from there the cors configuration tab and click edit. <i>I pasted 	in the Cors configuration provided by school.</i> <u><i>This is to setup the required access between our Heroku app and this S3 bucket. </i></u>

	- Then under the policy tab in the permission tab select policy generator to create a security policy for the bucket. The policy type is S3 bucket policy, effects will be allow, principal will be *,  action will be get object and the ARN you can find on top of the bucket policy tab. Click add statement, then generate policy. Copy this policy into the bucket policy editor and add a 	/*  on to the end of the resource key to allow all access to all resources in the bucket and finally click save. Leave the policy generate window open for when you will create a user.

	- As the last step go to the access control list tab and select public access to everyone, select list and understand the effects and save.

### Setup user to access bucket

- Go back to the server menu and open I am. Click on groups, create a new group and give it a name. <i>To keep it simple I gave it the name manage-taste-world-snacks.</i> Then click on create group.

- To make a policy to use to access our bucket click on policies and then create policy. Go to the JSON tab, click on import managed policy, search for S3, choose AmazonS3FullAccess and import. As I only want full access to the bucket and everything in it, you will go to the policy generate page that you left open and copy the ARN behind resource. You can paste this in the list behind resource and in a second line past it in again but with /* behind it. Click review policy, give it a name and description and click create policy. <i>I name mine taste-world-snacks and as description, I added to access S3 bucket for taste world snacks static files.</i>

- You will attach the policy to the group you just created. To do so go to groups, click on the group that was just made, click attach policy, search for the policy with the name that you just made, select it and click attach policy.

- Then finally you will create a user to put in the group. Click on users page, click add user and give it a name. <i>I called it taste-world-snacks-staticfiles-user.</i> select programmatic access as access type, click next, select your group, click through till the end and then click create user. Download the CSV file with the user access key and secret key and click close. <u><i>It is very important to download and save this file as it cannot be downloaded or accessed again.</i></u>

## Connect S3 bucket to Django

- In the code editor install bato 3, django-storages and freeze them. Add storages  in settings.py under installed apps. 
	<i>-pip3 install bato 3, pip3 install django-storages, pip3 freeze > requirements.txt</i>

- You need to add the next settings under the media root section of settings.py to tell it with which bucket to communicate with. Add an if statement to check if there is an environment variable called use aws and give it these variables with the corresponding values:

        if 'USE_AWS' in os.environ:
	        AWS_STORAGE_BUCKET_NAME,
	        AWS_S3_REGION_NAME,
   	        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID'),
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY'),
	        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

- Then go to Heroku settings tap and reveal config vars to add:
	- AWS_ACCESS_KEY_ID
	- AWS_SECRET_ACCESS_KEY
	- USE_AWS with value True
- You can find the credentials in the CSV file you downloaded from AWS and remove the DISABLE COLLECTSTATIC variable.

- In your code editor create a file named custom_storages.py to tell Django where to store static files and uploaded product images when you run collect static files. In this file you import settings from django.config and import S3Boto3Storage from storages.backends.s3boto3. Add a class to tell Django where to store static files and another for where to store media files.

	    from django.conf import settings
	    from storages.backends.s3boto3 import S3Boto3Storage


	    class StaticStorage(S3Boto3Storage):
   		    location = settings.STATICFILES_LOCATION


	    class MediaStorage(S3Boto3Storage):
    		    location = settings.MEDIAFILES_LOCATION

- Then go back to settings.py to tell it that for static file storage you want to use the StaticStorage class, for media files you want MediaStorage and what location it should save them.

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
   	    STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

 
- You also need to override and explicitly set the URLs for static and media files using your custom domain and new locations.

	    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

## Adding other files to S3 bucket

- You can add an extra setting to the use aws if statement in settings.py, that will tell the browser that it is okay to cache static files for a long time.

	    AWS_S3_OBJECT_PARAMETERS = {
       		 'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
       		 'CacheControl': 'max-age=94608000',
    	}

- To add media files to your S3 bucket, you need to go back to awsamazon.com, open S3, open your bucket,   click on create folder and give it a name. I called mine media. Open this folder, click upload then click on add files, then select all the images you want to select and click upload.
<i>If you have your images on Github than download them first from there and make sure that you add your images in with the same path as in your local database, example images/image.jpg.</i>

# Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

# Making a local clone

1. Navigate to https://github.com/ceciliabinck/(taste-world-snacks).
2. Click the green 'Clone or Download' button.
3. Copy the URL in the dropdown box.
4. Using your favourite IDE open up your preferred terminal.
5. Navigate to your desired file location.
6. Copy the following code and input it into your terminal to clone Cook with me.
7. git clone https://github.com/ceciliabinck/(taste-world-snacks).git

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```-->
##  Credits
-   Used bootstrap theme [freelancer](https://startbootstrap.com/previews/freelancer) as base template to home page and costumised it for this project
-   Used previous work and as templates to write README page and [taste world snacks](https://github.com/ceciliabinck/taste-world-snacks.git) deployment as guidance to write up my deployment
-   I have copied and pasted small pieces of work from my first attempt at this project, in the repository [sl_art](https://github.com/veraleitaodev/sl_art/).
-  Logo created at [canva.com](https://www.canva.com/)
-  css gradient code from [cssportal.com](https://www.cssportal.com/css-text-gradient-generator/)
- help in understanding how to use django in a carousel https://stackoverflow.com/questions/30119351/how-to-make-an-object-slider-in-django
