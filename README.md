# Shopbridge - Inventory API's
ShopBridge is an e-commerce application

## API Documentation URL(Swagger)
```
base_url/api/doc/
```

## Backend Installation

#
**Step 1:**

Create an empty folder
windows: Right click -> gitbash, A terminal window will open, In that window run the following command
linux: Right click -> open terminal, A terminal window will open, In that window run the following command

```
git clone https://github.com/pr4shantS0naw4n3/shopbridge-backend.git
```
This will clone the repository on your local environment
#
**STEP 2:**

Inside the cloned folder open command prompt(cmd) and run
```
virtualenv venv
pip install -r requirements.txt
```
This will install all the dependencies of the project on your local machine
#
**STEP 3:**

**Next Thing is Setting up Database**
If your Mysql and Mysql Workbench is Installed
1. Open MySql workbench and setup the host,port,username and password
2. Open a Connection to it and Create a new Schema(this will be your db name for django database settings)
#
**STEP 4:**

Open IDE and load your project inside it
Now goto ```settings.py``` and search for ```DATABASES```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "your schema name",
        'USER': 'your Username',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
After all this configuration is done
#
**STEP 5:**

goto the terminal(project terminal) and run the following command

```
python manage.py migrate
```
this command will apply initial migrations and models so that all your models is reflected in the database
#
**STEP 6:**

Final command
```
python manage.py runserver
```
With this command your backend server will be up and running
