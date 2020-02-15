### 
 
## Gamer Network Technical Challenge Documentation

### Setup

My initial thoughts were to use the Django framework to set up a model template for the challenge. I firstly created a folder in my developer directory called 'Gamer Network' that I could target with my terminal to open up VSCode using the 'code .' command. 

Once the folder was open in the text editor I created a virtual enviroment using a pre installed packege for enviroment management called 'Anaconda'. I used the 'conda create -name < ENVNAME > django' command to create a venv called 'GNENV.

Then I created a main directory with all the main settings and urls called 'gamerNetPro1'. I cd into this directory and then created a singular application called 'gamerNetApp1'. I then initiated git and created my initial commit.

I continued to create a templates folder in which I created a sub directory called 'gamerNetApp1' containing only one HTML file for the app. This was the index.html. Following this I created a static folder in a similar fashion containing a sub directory, again called 'gamerNetApp1' and in this, two more directories for the CSS file and a Javascript file if needed.

The next task was to configure the directory path settings for the templates folder and the static folder. This is the standard code that I placed in the relevent section of settings.py:

    TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
    STATIC_DIR = os.path.join(BASE_DIR, "static")

I then input 'gamerNetApp1' into the INSTALLED_APPS list and 'TEMPLATES_DIR' in the TEMPLATES dictionary under 'DIRS'. The final thing to do in settings.py was it add the STATICFILES_DIRS list containing 'STATIC_DIR' at the bottom of the file.

### First Approach

#### Model

I thought that a good way to approach this task would be to place the data dictionary I was given into a Django admin database. and display the data via template tagging with a for loop in the HTML page.

Firstly I created a model class in models.py that had two feilds, one for the title and one for the column length:

    class Article(models.Model):
        title = models.CharField(max_length=128)
        columns = models.IntegerField()

#### View

Then in views.py I made a fuction to render the html file:

    from django.shortcuts import render
    from gamerNetApp1.models import Article

    def index(request):
        Article_list = Article.objects.order_by('title')
        Article_dict = { 'Articles': Article_list}
        return render(request, 'gamerNetApp1/index.html', context=Article_dict)

#### URLs

I then created an application specific urls.py and inputh the right path settings in this and in the main urls.py file.

#### Admin 

I registered the model in admin.py

#### Migrate

I migrated the models to the Django admin database using the 'python manage.py migrate' command and the 'python manage.py makemigrations' command. This was successful.

#### Create Super User

I created a super user to access the Django admin pannel

#### Data Input

I used the dictionary of data I was given to fill up the database.

#### Develop HTML template

There was no need to make a base.html extension as this application only has one page. In the index.html I started by loading the static files at the very top under the !DOCTYPE html tag using {% load staticfiles %}.

Then I continued by adding a title and the bootstrap CDN (just to make the text look a bit nicer for now). I also added a static filre link to my own stylesheet to create the grid. At the bottom before the closing body tag I placed my Javascript external link incase I needed to use andy Javascript.

Next I needed to create the template tag that targets the database using an if statement 

{% if Articles %} '''{% endfor %}

Inside this I made a for loop that iterate through the articles and interpolates the data from the database to display in the browser. I created a class container and a ID container with a child class of item to use for styling the grid later. 

    {% for col in Articles %}
        <div class="container" id="container">
            <div class="item">{{ col.title }}{{ col.columns}}</div>
        </div>
    {% endfor %}

#### CSS Styling

I looked up the best way to stle grids without bootstrap. I found flexbox css grids, I knew of flexbox but have never used it in the past. Using some documentation I targeted the classes and IDs in the HTML file and implimanted the body, paragraph, container and item elements and styled them with a basic theme using flex box. This created a uniform set of rows with each article taking up one of the three columns.

#### Grouping the different column sizes

I placed the dictionary into the views.py file and began working on grouping the articles into collections of different column length. I found some code that groups dictionaries into collections this can be found at https://www.saltycrane.com/blog/2014/10/example-using-groupby-and-defaultdict-do-same-task/ 

This function collects the articles into these groups:

Articles that take up 2 columns:
[{'title': 'Star Ocean review', 'columns': '2'}, {'title': 'Lego Star Wars review', 'columns': '2'}, {'title': 'Inside review', 'columns': '2'}, {'title': 'Umbrella Corps review', 'columns': '2'}, {'title': 'Edge of Nowhere review', 'columns': '2'}, {'title': 'Sherlock Holmes review', 'columns': '2'}, {'title': 'The Warcraft movie review', 'columns': '2'}, {'title': 'Overwatch Review', 'columns': '2'}, {'title': 'The Witcher 3 review', 'columns': '2'}]


Articles that take up 1 columns:
[{'title': 'Prison Architect review', 'columns': '1'}, {'title': 'Trials of the Dragon review', 'columns': '1'}, {'title': 'Mighty No. 9 review', 'columns': '1'}, {'title': 'Guilty Gear Xrd Revelator review', 'columns': '1'}, {'title': 'Dangerous Golf review', 'columns': '1'}, {'title': 'Teenage Mutant Turtles review', 'columns': '1'}]


Articles that take up 3 columns:
[{'title': "Dino Dini's Kick Off review", 'columns': '3'}, {'title': "Mirror's Edge Catalyst review", 'columns': '3'}, {'title': 'Kirby: Planet Robobot review', 'columns': '3'}]





















