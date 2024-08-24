<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="card/static/card/img/icon.png" alt="Logo">

<h3 align="center">Django App | Discovering yugioh cards with django app</h3>

  <p align="center">
    <br />
    <a href="https://docs.djangoproject.com/en/5.0/releases/3.2/">View Django Documentation</a>
    <!-- · -->
    <!-- <a href="https://github.com/github_username/repo_name/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#screenshot">Screenshot</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
    <img src="card/static/card/img/Card-Pixel.svg" alt="Logo" width="300" height="300">
</div>

<div align="left">
    <h3>What can this django app do? This app can find yugioh cards. Which is:
    </h3>
    <br/>
    <h4>There are three types of methods to search for cards</h4>
    <ol>
        <li>By random numbers</li>
        <li>By name</li>
        <li>By advance filters</li>
    </ol>
    <br/>
    <p><strong>By random numbers : </strong>can search for as many cards as the number entered</p>
    <p><strong>By name : </strong>can search for the card with the entered name</p>
    <p><strong>By advance filters : </strong>can search for cards with entered filters</p>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

<!-- * [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->
* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![SQLite][SQLite]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

<div align="left">
    <h3>What do you need to run this django app?
    </h3>
    <ol>
        <li>Python 3.8.10</li>
        <li>Django 3.2.25 (included SQLite 3.31.1)</li>
    </ol>
</div>


<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->

### Installation

<!-- 1. <h3><strong>Install mega.py package</strong></h3>
    Run the following command, or run setup from the latest github source.<br/>
    ```sh
    pip install mega.py
    ```

2. <h3><strong>Install humanize package</strong></h3>
    ```sh
    pip install humanize
    ``` -->


1. Install Python 3.8.10 | Setup documentation [Ubuntu](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) / [Windows](https://www.c-sharpcorner.com/article/how-to-install-python-3-8-in-windows/) / [Mac OS](https://www.dataquest.io/blog/installing-python-on-mac/)
2. Install django 3.2.25
   ```sh
   pip install django==3.2.25
   ```
3. Create django project
   ```sh
   django-admin startproject yugioh
   ```
<!-- 4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ``` -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Create django project
```sh 
django-admin startproject yugioh
```
Copy and Paste this ***card*** folder into path of yugioh project, like this
```
  --- yugioh (project folder)
  -------- card (app folder)
  -------- yugioh (app folder)
```
Make & Migration database django
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
Setting URL in directory file ***yugioh(project folder)*** / ***yugioh(app folder)*** / ***urls.py***
```sh
from card import views as card_views

urlpatterns = [
    path('card', include('card.urls')),
    path('card/kartu', card_views.another_page),
    path('card/love', card_views.insert_favorite_to_bucket),
    path('card/trash', card_views.delete_favorite_from_bucket),
]
```
Open Localhost URL in your browser
```sh
http://127.0.0.1:8000/card
```

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Screenshot
<div align="center">
  <img src="card/static/card/img/yugioh-ss-1.png" alt="Image1">
  <img src="card/static/card/img/yugioh-ss-2.png" alt="Image2">
  <img src="card/static/card/img/yugioh-ss-3.png" alt="Image3">
</div>



<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Dewa Firmansyah - firmansyahdewa702@gmail.com
<!-- Dewa Firmansyah - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com -->

Project Link: [https://github.com/dewafirmansyah99](https://github.com/dewafirmansyah99)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python]: https://img.shields.io/badge/Python-3.8.10-3776AB.svg?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Odoo]: https://img.shields.io/badge/Odoo-16.0-714B67.svg?style=for-the-badge&logo=odoo&logoColor=#714b67
[Odoo-url]: https://www.odoo.com
[Mega]: https://img.shields.io/badge/build-api-salmon?style=for-the-badge&logo=mega&logoColor=%23D9272E&label=mega
[Mega-url]: https://github.com/odwyersoftware/mega.py
[Django]: https://img.shields.io/badge/Django-3.2.25-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[SQLite]: https://img.shields.io/badge/sqlite-3.31.1-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
