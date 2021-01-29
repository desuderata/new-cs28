<p align="center">
    <a href="http://teamentropycs28.pythonanywhere.com/">
        <img class="logo"
             src="/cs28_project/static/icons/UoG_colour_edited.svg"
             alt="uog_logo" /
             height="64">
    </a>
</p>

# CS28 Project

A bespoke and flexible database for the School of Chemistry (SoC) tailored for the calculation of Degree Classification as part of the Team Project module.

##### Table of Contents

[Prerequisites](#prerequisites)  
[Installation / Setup](#installation-setup)  
[Superuser Account](#superuser-account)  
[Usage](#usage)  
[Contributing](#contributing)  
[Authors and Contact](#authors-and-contact)  
[Team Coach](#team-coach)  
[Acknowledgements](#acknowledgements)  

## Prerequisites

This web app is built on:
- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [Django 3.1.3](https://docs.djangoproject.com/en/3.1/releases/3.1.3/)
- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)


## Installation / Setup

1. Create a virtual environment:

```bash
conda create -n cs28 python
conda activate cs28
```

2. Clone the repository:
```bash
git clone https://stgit.dcs.gla.ac.uk/tp3-2020-CS28/cs28-main.git
```

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages through the requirements.txt file:
```bash
pip install -r requirements.txt
```

4. Migrate database models:
```bash
cd cs28_project
python manage.py makemigrations cs28
python manage.py migrate
```

5. Run the server
```bash
python manage.py runserver
```

### Superuser Account

**To create a superuser account:**

```bash
python manage.py createsuperuser
```

You will be prompted to enter your username, email and password.

## Usage

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and Contact
Alana Grant - [2390384G@student.gla.ac.uk](2390384G@student.gla.ac.uk)

Ekaterina Terzieva - [2403606T@student.gla.ac.uk](2403606T@student.gla.ac.uk)

Hieu Nguyen - [2471707N@student.gla.ac.uk](2471707N@student.gla.ac.uk)

Kien Welch - [2371692W@student.gla.ac.uk](2371692W@student.gla.ac.uk)

Yee Hou Teoh - [2471020T@student.gla.ac.uk](2471020T@student.gla.ac.uk)

## Team Coach

Robert Pringle - [2304777P@student.gla.ac.uk](2304777P@student.gla.ac.uk)

## Acknowledgements
[Make a README](https://www.makeareadme.com/)

[Font Awesome](https://fontawesome.com/)


