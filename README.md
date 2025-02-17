# ICEBATH
  Ice Bath is a online community page aimed at the Open cold water/Ice bath at home community, the aim is to bring users togeather from all over the UK & Ireland to share their experiences, adventures, favourite spots they've visited and any benefits/ advice they want to share with new users.

  ![am-I-responsive](https://github.com/user-attachments/assets/3e4db4da-5f13-41a5-9429-4d49c45c8142)

## Features

### Existing Features

* Navigation bar
  
  When a user is logged in the navbar will show Home, share and logout
  these 3 links are present because the user is logged in and has access to share with the community
  
  ![Image](https://github.com/user-attachments/assets/005e64e4-23bd-4e09-b09b-11ad3ea30943)

  When a user is not registered/logged in the navbar will have the following links
  Home, register and login. There is no share link because a user needs to be logged in to share posts to the community.

  ![Image](https://github.com/user-attachments/assets/2970aacd-3ab5-4b92-a078-5843cbf908ec)

* Home page
 
  The homepage has a welcome message to the user informing them of the purpose of the page and how they can post on the website. Below the welcome message are where all the posts are displayed with the title, author and created on displayed. There also next and prev buttons to move through all the posts.

  ![Image](https://github.com/user-attachments/assets/8664671a-7b58-4b61-92b8-48dd37247001)

  ![Image](https://github.com/user-attachments/assets/2ef86365-177d-469e-835b-281e4dd86439)

* Post
  
  When selected post is clicked on the posts content is displayed 

  ![Image](https://github.com/user-attachments/assets/bdd84a87-01f9-47c5-8ec2-126d94c785cc)

* Comment section
   
   Below the post there is a comment section were the user can comment on posts, edit/delete their own comments. Users can only comment on posts when logged in, users can only edit/delete their own comments.

   ![Image](https://github.com/user-attachments/assets/22da9a21-25d7-4d29-a945-91479cc382e4)
   ![Image](https://github.com/user-attachments/assets/ea26b3b4-0c75-4edb-bab9-1a807f2a95e4)

* Share post
  
  When the user decides they want to share a post with the community they will press the share link, and fill in the form followed by the submit button. User has to fill in all 3 fields to submit.

  ![Image](https://github.com/user-attachments/assets/134b1861-d231-4d7c-873d-34663602fb5f)
  ![Image](https://github.com/user-attachments/assets/9588afdc-a0b1-41e7-9499-a54928267406)
* logout
  
  When the user decides to signout, once the logout link has been clicked a message will appear to confirm they want to log out.
  ![Image](https://github.com/user-attachments/assets/a0279147-d17f-4412-b8ad-b02743990f79)

* Register
  
  When the user goes to register to be able to post and comment on the website the following page will be displayed. The email address is optional but all other fields must be filled.
  ![Image](https://github.com/user-attachments/assets/41397019-8172-4789-b2d0-4563d8302dae)

* Sign in

  When the user visits the page and already registered the sign in link will display a page asking the user to sign in to be able to post and comment on the website.
  ![Image](https://github.com/user-attachments/assets/0d71ab67-2c06-4041-b97e-999b5469455f)

### Features Left to Implement
 * Reset passoword if user forgets login details

## Testing 

### Validator Testing 
  
  For testing my project I created 2 test files, 1 for views and other for my forms 
  (test_views.py/test_forms.py), Within thoses files I Created functions to test all features of the website.

### Unfixed Bugs

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site 

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate 
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.


## Credits 

### Content 
- For adding some of my css to this project I used the [Bootstrap](https://getbootstrap.com/) framework.
- Instructions on how to implement form validation on the Sign Up page was taken from the 
  guidance from code institute
- [W3 Schools](https://www.w3schools.com/) was very helpful for keeping me right when 
  working with Django and creating models.

### Media
- [Pexels](https://www.pexels.com/) was used for my images.
- [Fontawesome](https://fontawesome.com/) was used to add icons to webpage.