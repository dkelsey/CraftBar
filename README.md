# CraftBar
Sample REST API
Written in Django 2.0.7, djangorestframework 3.8.2, python 3.5.2

#### REST Endpoints
```json
{
    "users": "http://192.168.101.11:5000/users/",
    "groups": "http://192.168.101.11:5000/groups/",
    "beers": "http://192.168.101.11:5000/beers/"
}
```

#### Example Beer
```json
{
    "url": "http://192.168.101.11:5000/beers/5/",
    "name": "hot-dog-water",
    "brewery": "the sink",
    "beer_style": "gross",
    "price": "1.99",
    "description": "tastes like soup"
}
```

An employee (`is_staff == True`) can do all **CRUD**<br>
All other users have **Read** access.

The current implementation:
* Lists beers,
* Creates, reads, updates, and deletes beers.

# Installation

I created a repeatable deployable development environment using Vagrant/VirtualBox..

### Requirements:
* Vagrant,
* VirtualBox,
* 16GB of RAM.

### Installation steps

```
git clone https://github.com/dkelsey/CraftBar.git

cd CraftBar
vagrant up
```
After this completes ssh to the craftbar guest os
```
vagrant ssh craftbar

...
...
$ cd CraftBar/
CraftBar$ python3 manage.py runserver 0.0.0.0:5000
```

Navigate to http://192.169.101.11:5000

### User accounts:

Admin/employee<br>
`admin/s3cr3t123`

non-employee login<br>
`buddy/buddy123`

# QA/Testing

See [Testing Notes](https://github.com/dkelsey/CraftBar/wiki/Testing-Notes) and [Test Cases](https://github.com/dkelsey/CraftBar/wiki/Testing-Notes#test-cases) on the wiki
