
# Gary Simons - personal resume website

---

## Overview

This is a website to **promote me as a Full Stack Web Developer**. In the future, I shall be able to use it to send to protential employers as a way of advertising my skills. It has been built using template inheritance which should make it easier to add content as my projects and skills grow. 

The aim of the project is to produce a website using **Flask** and **Python** that allows the use of data stored in a database on **MongoDB**. The site has to demostrate the data storage principles that you should be able to **create, read, update and delete (CRUD)** that data through a user interface. For my project, the user of that interface will be **me** as the site's owner. I have 'hidden' an admin section, which can be accessed from the footer on the **Contact** page. This takes you to the **Admin** page, from which you can read, add, update or delete the data. The data is diplayed to the users in a panel on the **About** page, using easy to diguest text and progress bars to show skills and skill levels attained. 

The site is designed to reflect me as a creative full stack web developer and show my style. The site is clean and stylish, using muted blocks of colour to define areas. I created a simple, complimentary, sophisticated colour scheme that carries through the site. This enables the different pages to have their own feel and identity, while maintaining a holding colour theme that ties them all together, giving an upmarket feel.

I've used the san serif font **Montserrat** in two weights (300 and 500) with some sophisticated letter spacing to add to the airy feel. I like the no-nonsense clean lines of the font, and feel it suits the site perfectly.

I carried the same basic grid throught the pages to add contsiancy and easy of navigation. A lager section header quickly establishes the page you've landed on, and under that, is a panel holding the content for that page.

I created an image of a woodcut style bird carrying a card with the coding symbol on it. It is not only a beautiful image, but symbolizes me delivering coding solutions. I have used this image throughout the site and a visual logo of the site and of me.

---

## UX

Using the Bootstrap framework, the site is fully responsive. Each element on the pages has been designed to work and look visually appealing depending on the viewing device. 

The **Navigation bar** is always visible when you are on the site, allowing for easy navigation to any part, no matter where you first land. 

The home button and logo will take you right back to the landing page where you can get your bearings and start your journey.

The **Home** page opens with strong simple white typography on a plain grey background. It has a larger image of the bird and establishes the tone and feel of the site. A small about me button takes you straight to the **About** page. 

The **About** page shows some of the key information about me. There is a brief introduction to me and the things i stand for. Below that are two panels. One showing my skills with an easy to understand progress bar showing my proficiency level in a graphic way. The other shows my relevant education and qualification. Below them is a panel containing links to my LinkedIn, Twitter, Instagram, GitHub and a downloadable pdf of my CV.

The **Projects** page highlighs some of the work I have been doing. Each project is in a coloured panel with the website showing in a graphic line drawing of a laptop. A view button under each title opens a large modal with larger images of a laptop, tablet and phone. There is a short description of the site, a list of programs and languages used and a link to the live website.

The **Contact** page simply holds an email for for users to fill in and contact me. I kept the wording on the page very inviting and conversational to help the user feel more at ease and give a friendly vibe. At the bottom of this page is the footer, which again holds links to my LinkedIn, Twitter, Instagram, GitHub and a downloadable pdf of my CV. It has a copyright sign off and a link to the 'hidden' **Admin** page.  

The **Admin** page is the interface with the MongoDB database. It shows a panel showing the stored data. Beside each of the listings are two buttons, edit and delete. Below is a add new skill button. The edit button opend a new page where it shows the data that you've clicked on in a form that allows for them to be edited. Below are a save changes button with sends the updated data to MongoDB, and a back to skills button which takes you back to the list of skills on the Admin page. The delete button simply deletes that data from the MongoDB database. The add skills button opens a page with a form that needs to be filled in with a new skill and new proficiency level. The form has placeholder text to prompt the correct way to inpurt the data. There is a add skill button which adds that skill and level to the MongoDB database. Again there is a back to skills button which takes you back to the list of skills on the Admin page. All the buttons on the site share common styles wit two different widths. All the changes made in these panels are reflected in the information on the **About** page.

---

## User story

### User one: me
As the site owner I am using it to promote myself and my work to potential employers. It is my shop front that refects me as a developer and my personality. I can quickly and easily add new skills as I aquire them via the Admin page to keep it up to date. I can also add or modify any projects I do. I can sent this as a link to anyone I want to market myself to.

### User two: recruiter
The users here are looking to find a developer to work with or employ. When trying to decide if they want to work with someone, they can find the site and have all the information at their disposal. Not only is the site itself a showcase, the links to previous projects and relevant social media and work sites will help to give a wider picture of the person's workstyle and personality. The downloadedable CV is there too as some people people will still want that option. This is a quick and simple way to get all the informtion required to decide if they would like to proceed. They can also get in contact to arrange for more inforation or to meet up.

### User three: developers
The users here are other developers looking to see what other people in their field are doing. They want to get ideas, or see who is out there. 

---

## Wireframes

These are my original wireframes for my site. 

---

## Features

### Navigation bar
This holds all the links to the sections of the site: Logo (home button), home, about, projects and contact. This allows the user to navigate quickly to the relevant section. The Navigation bar is always visible when you are on the site, allowing for easy navigation to any part, no matter where you first land.

### Home
This is the first page a user comes to and it has to make a big impact. It has the job of informing the user as to what sort of site this is and to entice them to move further and engage with it. Having a big name announces very quickly who the site is about. The tag line underneath then gives more context and explains what they do. A beautiful illustration on a bird holding a card with </> on it symbolizes delevering code. A tasteful about me link invites them to enter the site andf takes the user straight to the About page where they can learn a bit more.

### About
The About page shows some of the key information about me. There is a brief introduction to me and the things i stand for. Below that are two panels. One showing my skills with an easy to understand progress bar showing my proficiency level in a graphic way. The other shows my relevant education and qualification. Below them is a panel containing links to my LinkedIn, Twitter, Instagram, GitHub and a downloadable pdf of my CV.

### Projects
The Projects page highlighs some of the work I have been doing. Each project is in a coloured panel with the website showing in a graphic line drawing of a laptop. A view button under each title opens a large modal with larger images of a laptop, tablet and phone. There is a short description of the site, a list of programs and languages used and a link to the live website.

### Contact
The Contact page simply holds an email for for users to fill in and contact me. I kept the wording on the page very inviting and conversational to help the user feel more at ease and give a friendly vibe. At the bottom of this page is the footer, which again holds links to my LinkedIn, Twitter, Instagram, GitHub and a downloadable pdf of my CV. It has a copyright sign off and a link to the 'hidden' **Admin** page.  

### Admin
The Admin page is the interface with the MongoDB database. It shows a panel showing the stored data. Beside each of the listings are two buttons, edit and delete. Below is a add new skill button. The edit button opend a new page where it shows the data that you've clicked on in a form that allows for them to be edited. Below are a save changes button with sends the updated data to MongoDB, and a back to skills button which takes you back to the list of skills on the Admin page. The delete button simply deletes that data from the MongoDB database. The add skills button opens a page with a form that needs to be filled in with a new skill and new proficiency level. The form has placeholder text to prompt the correct way to inpurt the data. There is a add skill button which adds that skill and level to the MongoDB database. Again there is a back to skills button which takes you back to the list of skills on the Admin page. All the buttons on the site share common styles wit two different widths. All the changes made in these panels are reflected in the information on the **About** page.

### Favicon
The site has a Favicon to visually show the user where the site is in their open tabs. It uses the GS logo from the Nav Bar on the same grey background to tie it together.

---

## Features left to implement

1.xxxxxxxxxxxx

---

## Technologies used

1. [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
3. [Python](https://www.python.org/)
4. [Flask](https://flask.palletsprojects.com/en/1.1.x/#)
4. [MongoDB](https://account.mongodb.com/account/login)
5. [Heroku](https://www.heroku.com/)
6. [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
7. [Font Awesome](https://fontawesome.com/)
8. [Google Fonts](https://fonts.google.com/)
9. [Balsamiq Wireframes](https://wireframestogo.com/)
10. [TinyPNG](https://tinypng.com/)
10. [Genfavicon](http://www.genfavicon.com/)

---

## Testing
xxxxxxx


---

## Deployment

My site is deployed on Heroku.

1. First log onto Heroku.
2. In the App Name form, create a uniquie app name.
3. In the Choose a Region dropdown, choose Europe as that's our region and delivery will be quicker.
4. Click on Create App.
5. Next, log in to Heroku in the terminal with 'heroku login'. You will need to enter you email and password. This allows the connection from your project to Heroku and allows us to push changes to Heroku using git.
6. If not using GitPod, you will have to create a new Git repository with the command, git innit.
7. Do a 'git add .' to add the files and git commit -m "Intial commit' to commit those files.
8. We need now to associate Heroku as our remote master branch. Back on Heroku you will find the command 'heroku git:remote -a (name of your app)', in the Deploy using Heroku Git section. Paste this into the terminal to set it up.
9. Create a requirements.txt file which will contain a list of all the applications required for Heroku to run the application.To do this type 'sudo pip3 freeze --local > requirements.txt' in the terminal. This will create a txt file with the list in.
10. Add this file, commit it and push it to Heroku with 'git push heroku master'.
11. You now have to create a Procfile which will tell Heroku which file to call to get the application running. To do this, in the terminal write 'echo web: python app.py >Procfile'. Add this to GitHub, and commit. Then 'git push heroku master' to save it to Heroku.
12. Next, we want to get our application running on Heroku. In the terminal, type 'heroku ps:scale web=1'. 
13. On Heroku, go to 'settings', and click on the 'Reveal Config Vars' button. 
14. In here we need to supply a our IP address and our port. The first 'KEY' is 'IP' and it's 'VALUE' is '0.0.0.0'. The second 'KEY' is 'PORT' and it's 'VALUE' is '5000'.
15. Click on the button 'Open app' and it will start the app and show your page.
16. Simen's video about automatically updating xxxx xx xxx xx x xx xx xx xx x xxxxxxx

## Credits

### Thanks

My mentor **Simen Dehlin** for all the advice and pointers. And for always pushing me to go further.

All the **tutors** that helped me along the way on the **Tutor Support**. 

### Images

Bird image was sourced from the [iStock](https://www.istockphoto.com/gb) image library, but adapted by me to hold the </> card in it's mouth. 

### Text

All text written by me.

---

## Acknowledgements

### Corey Schafer
I watched Corey Schafer's YouTube tutorial [Python Flask Tutorial: Full-Featured Web App Part 2 - Templates](https://www.youtube.com/watch?v=QnDWIZuWYW0) to help me understand Template Inheritance better.

### xxxxxxx
xxxxxxxxx.
[xxxxxxxx](https://axxxxx)

