# PROJECT PORTFOLIO 4 - WARCRAFT MOGS - TESTING

👩🏻‍💻 View an example of this section [here](https://github.com/kera-cudmore/Found-In-Translation/blob/main/TESTING.md#found-in-translation----testing-documentation)

Add an image of the finished site here. I like to use [amiresponsive](https://ui.dev/amiresponsive) to get an image of my site on all device sizes, and amiresponsive allows you to click links on the page and scroll, so each device can show a different element of your site.

Add a link to the live site here, for Milestone 1 this will be the GitHub Pages Link from when you deployed the site.

If you want to add optional shields.io badges to your TESTING file, I like to add them to this section (Shields.io have some badges for W3C validation which makes it easy to see at a glance whether the project has passed validation).

---

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Lighthouse](#lighthouse)
  * [WAVE](#wave)

* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

* [BUGS](#bugs)
  * [Known Bugs](#known-bugs)
  * [Solved Bugs](#solved-bugs)

---

## Validators

###  W3C Validator

👩🏻‍💻 View an example of a completed W3C HTML & CSS validation section [here](https://github.com/kera-cudmore/TheQuizArms/blob/main/TESTING.md#W3C-Validator)

The most popular HTML validator is [W3C](https://validator.w3.org/). There are two ways to validate the HTML for your first milestone - you can copy the live link for your site page and paste into the validate by URI field, or you can copy all the code for your page and paste this into the validate by direct input field.

#### **URI Input**

If you validate with your sites URL, you can run the validation and then copy the link from the address bar and insert the link here as your proof of validation.

![W3C URI Validator](documentation/milestone1-testing/w3c-uri-validatation.png)

#### **Direct Input**

If you validate with the code, you will need to screenshot the validation results and then link the image here.

![W3C Direct Input Validator](documentation/milestone1-testing/w3c-directinput-validation.png)

#### **CSS Validation**

CSS Validation can only be done by copying and pasting the CSS file contents into the direct input. Make sure that the checkbox for CSS is selected.

![W3C CSS Validation](documentation/milestone1-testing/w3c-css-validation.png)

### Lighthouse

👩🏻‍💻 View an example of a completed lighthouse testing section [here](https://github.com/kera-cudmore/earth-day-hackathon-2022/blob/main/TESTING.md#Lighthouse)

Lighthouse Testing is part of the Chrome Developer Tools. For more information on how to use this tool, please visit [chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en#:~:text=Lighthouse%20is%20an%20open%2Dsource,how%20well%20the%20page%20did.).

You will need to run the Lighthouse testing on each individual page of your site, for desktop as a minimum. If you have time it would be great to also add in the mobile testing.

![Lighthouse Testing](documentation/milestone1-testing/lighthouse.png)

### WAVE

👩🏻‍💻 View an example of a completed WAVE testing section [here](https://github.com/kera-cudmore/earth-day-hackathon-2022/blob/main/TESTING.md#WAVE)

[WAVE](https://wave.webaim.org/) is an accessibility testing tool. I like to run this on each page of my site and take a screenshot of the results to add here. They have a website for testing and a Chrome extension.

![Wave Desktop](documentation/milestone1-testing/wave-desktop.png)

![Wave Exetension](documentation/milestone1-testing/wqave-extension.png)

## MANUAL TESTING

### Testing User Stories

👩🏻‍💻 View an example of a completed user stories testing section [here](https://github.com/kera-cudmore/BookWorm/blob/main/TESTING.md#Testing-User-Stories)

This is where you will test the user stories you created in the README against your site. I like to use a table for this section - I create a column for the user stories goals, how these have been achieved and I use the third column to add any supporting images.

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
|  |  |  |  |  |
| Home (left) | When clicked the user will be redirected to the home page. | Clicked link | Redirected to the home page | Pass |
| Home (right) | When clicked the user will be redirected to the home page. | Clicked link | Redirected to the home page | Pass |
| About | When clicked the user will be redirected to the About page. | Clicked link | Redirected to the about page | Pass |
| Contact | When clicked the user will be redirected to the Contact page. | Clicked link | Redirected to the contact page | Pass |
| Register | When clicked the user will be redirected to the Register page. | Clicked link | Redirected to the register page | Pass |
| Sign In | When clicked the user will be redirected to the Sign In page. | Clicked link | Redirected to the log in page | Pass |
| Upload Post | When clicked the user will be redirected to the Upload Post page. | Clicked link | Redirected to the upload post page | Pass |
| Sign Out | When clicked the user will be redirected to the Sign Out page. | Clicked link | Redirected to the log out page | Pass |
| `Footer` |
|  |  |  |  |  |
| Instagram link | When clicked the user will be redirected to my Instagram page. | Clicked Logo | Redirected to the Instagram page. | Pass |
| Facebook link | When clicked the user will be redirected to my Facebook page. | Clicked Logo | Redirected to the Facebook page. | Pass |
| Github link | When clicked the user will be redirected to my Github page. | Clicked Logo | Redirected to the Github page. | Pass |
| `Home Page` |
|   |   |   |   |
| Image | When clicked the user will be redirected to Post detail page. |  Clicked image | Redirected to the Post detail page. | Pass |
| Title | When clicked the user will be redirected to Post detail page. |  Clicked title | Redirected to the Post detail page. | Pass |
| Username | When clicked the user will be redirected to the user page | Clicked username | Does not redirect to profile (feature not implemented) | Fail |
| Next | When clicked the user will be redirected to the next page with older posts. | Clicked button | Redirected to the next page. | Pass |
| Previous | When clicked the user will be redirected to the next page with newer posts. | Clicked button | Redirected to the previous page. | Pass |
| Increment Likes Count | Increment the number of likes on post to display the count of likes | Clicked icon | Likes count is incremented by 1 on the index.html page when a user likes a post | Pass |
| Decrease Likes Count | Decrease the number of likes on post to display the count of likes | Clicked icon | Likes count is decreased by 1 on the index.html page when a user unlikes a post | Pass |
| Increment Comment Count | Increment the number of comments displayed on a post when a comment is added | Commented on post | Comment count is incremented by 1 on the index.html page when a user comments on a post | Pass |
| Decrease Comment Count | Decreases the number of comments displayed on a post when a comment is removed | Delete comment | Commen count is decreased by 1 on the index.html page when a user removes their comment on a post | Pass |
| `Post Detail Page` |
| Increment Likes Count | Increment the number of likes on post to display the count of likes | Clicked icon | Likes count is incremented by 1 on the index.html page when a user clicks the heart icon | Pass |
| Decrease Likes Count | Decrease the number of likes on post to display the count of likes | Clicked icon | Likes count is decreased by 1 on the index.html page when a user clicks the heart icon | Pass |
| Liked Icon (Heart) | The heart icon is solid when a user has liked a post | Clicked icon | Heart icon is coloured in (solid) when a user has liked a post | Pass |
| Uniked Icon (Heart) | The heart icon is hollow when a user has not yet liked a post | Clicked icon again (after liking it) | Heart icon is hollow when a user has unliked a post | Pass |
| Edit icon Redirect | When the edit icon is pressed, the user is redirected to the edit_post.html | Clicked edit button | Redirects to edit_post.html |
| Delete icon Redirect | When the delete icon is pressed, the user is redirected to the delete_post.html | Clicked delete button | Redirects to delete_post.html |
| Back Button | When a user clicks the back button, they will be redirected to the home page. | Clicked button | Redirected to the home page | Pass |
| Submit a Comment | When a user writes a comment, the comment will be displayed on the detail_post.html page | Submitted a comment | Comment is displayed in the detail_post.html page | Pass |
| Comment Message Alert | When a user comments on a post, a message is displayed on the top of the page verifying to the user that their comment was successfully added | Submitted a comment | Displays successful comment message | Pass |
| Remove a Comment (X Icon) | When a user writes a comment, the comment will be removed on the detail_post.html page | Deleted a comment | Comment is deleted in the detail_post.html page | Pass |
| Submit Button | When the Submit button is pressed, the comment is successfully added | Clicked Submit button | Successfully submits a comment | Pass |
| Empty Comments Dield | When the textfield for writing a comment is not filled in, an alert should inform the user to fill in this field | Submit comment with empty textarea field | Displays error message to fill in the required field | Pass |
| Increment Comment Count | Increment the number of comments displayed on a post when a comment is added | Commented on post | Comment count is incremented by 1 anytime a user comments on a post | Pass |
| Decrease Comment Count | Decreases the number of comments displayed on a post when a comment is removed | Delete comment | Comment count is decreased by 1 anytime a user removes their comment on a post | Pass |
| Paginate Comments | Paginates the comments to a new page when the comment count number exceeds 4 | Wrote more than 4 comments | A button to go to next page of comments whenever there is more than 4 comments | Pass |
| Paginate Buttons | Each button should take the user to either of these comment pages: the first page, previous page, previous page (number), current page (number), next page (number), next page, last page. | Wrote more than 4 comments | A button to go to next page of comments whenever there is more than 4 comments | Pass |
| Remove comment as not signed in | When a user is attempting to remove a comment without being signed in, the removal icon should not be displayed | Visiting comments section without being logged in | Remove comment icon not displayed | Pass |
| Remove comment signed in as a different user from the comment author | When a user is attempting to remove a comment without being signed in to the user that wrote the comment, the removal icon should not be displayed | Visiting comments section logged in as a different user from the comment author | Remove comment icon not displayed | Pass |
| `About Page` |
|   |   |   |   |  |
| Back Button | When a user clicks the back button, they will be redirected to the home page. | Clicked button | Redirected to the home page | Pass |
| `Contact Page` |
|   |   |   |   |   |
| Required* Name Field | When left empty, user should be informed that this field needs to be filled in | Submit with empty field | Displays error message to fill in the required field | Pass |
| Required* Email Field  | When left empty, user should be informed that this field needs to be filled in | Submit with empty field | Displays error message to fill in the required field | Pass |
| Required* Message Field  | When left empty, user should be informed that this field needs to be filled in | Submit with empty field | Displays error message to fill in the required field | Pass |
| Email Field Validation  | When not using an @ character or . (.se for example), the user should be informed the email is not valid | Field filled in without @ or . | Form fails to submit | Pass |
| Name Field | When filled in, form should be submitting correctly | Field left filled in when submitting the form | Form submits correctly | Pass |
| Email Field | When filled in, form should be submitting correctly | Field left filled in when submitting the form | Form submits correctly | Pass |
| Message Field | When filled in, form should be submitting correctly | Field left filled in when submitting the form | Form submits correctly | Pass |
| Submit Button | When clicked, form should be submitted | Clicked button | Form submits correctly | Pass |
| Submit Redirect | When form has been submitted, user will be redirected to success_contact.html | Clicking submit button with all required filled in correctly | Redirects to success_contact.html successfully | Pass |
| `Register Page` |
| | | | | | |
| Sign in button Redirect | When clicked, user will be redirected to the sign in page | Clicked button | Redirects to sign in page | Pass |
| Empty Username field | When username field not filled in, an alert should inform the user to fill in this field | Submit with empty username field | Displays error message to fill in the required field | Pass |
| Empty Password field | When password field not filled in, an alert should inform the user to fill in this field | Submit with empty password field | Displays error message to fill in the required field | Pass |
| Empty Password (Again) field | When password field not filled in, an alert should inform the user to fill in this field | Submit with empty password field | Displays error message to fill in the required field | Pass |
| Username taken | If username is in use, alert is shown to the user that the name is taken | Register with a username already in use | Error message displaying that a user with that username alerady exists | Pass |
| Empty Password | When left empty, user should be informed that this field needs to be filled in | Submit form with empty password field | Displays error message to fill in the required field | Pass |
| Password less than 8 characters | When password is entered with fewer than 8 characters, an error message should inform user of minimum 8 characters | Submit form with less than 8 chacters in the password field | Error message displaying that the password is too short and must contain at least 8 characters | Pass |
| Not matching Passwords | When entering two different passwords, user should be alerted that the passwords are not matching | Submitting form without matching passwords | Displays error message to user | Pass |
| Submit Button without email  | When clicked, form should be submitted | Clicked button | Form submits correctly | Pass |
| Submit Button with email | When clicked, form should be submitted | Clicked button | Form submits correctly | Pass |
| Submit Redirect | When form has been submitted, user will be redirected to index.html | Clicking submit button with all required filled in correctly | Redirects to index.html successfully | Pass |
| `Log in Page` |
| Empty Username field | When username field not filled in, an alert should inform the user to fill in this field | Sign in with empty username field | Displays error message to fill in the required field | Pass |
| Empty Password field | When password field not filled in, an alert should inform the user to fill in this field | Sign in with empty password field | Displays error message to fill in the required field | Pass |
| Wrong Username & Password | When a user enters the wrong username and password, it should alert the user that the username/password is not correct | Sign in with wrong username and password | Displays error message that the username or password is incorrect | Pass |
| Remember me checkbox | When a user clicks the "Remember me" checkbox, it should remember the username the next time the user wants to login | Checked "Remember me" checkbox | Username is not remembered and already filled in when the user is logging in again | Fail |
| Sign in Button | When the Sign in button is pressed, the user should be logged in to their account | Clicked Sign in button | Successfully logs in a user | Pass |
| Sign in Redirect | When Sign in button is pressed, user will be redirected to index.html | Clicked Sign in button | Redirects to index.html successfully | Pass |
| Sign in Message Alert | When a user signs in, a message is displayed on the top of the page verifying to the user that they are logged in | Logged in | Displays log in message successfully | Pass |
| `Sign out Page` |
|   |   |   |   |  |
| Sign Out Button | When clicked the user will be signed out to the home page. | Clicked button | User signed out | Pass |
| Sign Out Redirect | When Sign out button is pressed, user will be redirected to index.html | Clicked Sign out button | Redirects to index.html successfully | Pass |
| Sign Out Message | When a user signs out, a message is displayed on the top of the page verifying to the user that they are logged out | Logged in | Displays sign out message successfully | Pass |
| `Upload Post Page` |
| Empty Title field | When title field not filled in, an alert should inform the user to fill in this field | Submit with empty title field | Displays error message to fill in the required field  | Pass |
| Empty Content field | When content field not filled in, an alert should inform the user to fill in this field | Submit with empty content field | Displays error message to fill in the required field  | Pass |
| Submit with Title | When submitting the form with a title, the title will successfully be added to the post | Submit form with title | Submits post with the title the user wrote | Pass |
| Submit with Description | When submitting the form with a description, the description will successfully be added to the post | Submit form with description | Submits post with the description the user wrote | Pass |
| Submit with Content | When submitting the form with text content, the content will successfully be added to the post | Submit form with text content | Submits post with the content the user wrote | Pass |
| Select Category | When selecting a category, the selected category will be successfully be added to the post | Submit form with category | Submits post with the category the user selected | Pass |
| Submit with Image | When submitting the form with an image, the image will successfully be added to the post | Submit form with image | Submits post with chosen image | Pass |
| Submit without Image | When submitting the form without an image, the placeholder image will successfully be added to the post | Submit form with image | Submits post with placeholder image | Pass |
| Submit Button | When the Submit button is pressed, the users uploaded post will be saved | Clicked submit button | Saves and uploads the post successfully | Pass |
| Submit Redirect | When form has been submitted, user will be redirected to index.html | Clicking submit button with all required filled in correctly | Redirects to post_detail.html successfully | Pass |
| `Edit Post Page` |
| Pre-populated Title field | When a user edits a post, the original title should be pre-populated in the title field | Clicked edit post button in post_detail.html | Displays the original title text in the title field | Pass |
| Pre-populated Content field | When a user edits a post, the original content should be pre-populated in the content textarea | Clicked edit post button post_detail.html | Displays the original content text in the content area | Pass |
| Pre-populated Category field | When a user edits a post, the original category tag that was selected when uploading the post should be displaying | Clicked edit post button post_detail.html | Displays the original category selected | Pass |
| Pre-populated Image | When a user edits a post, the original image that was selected when uploading the post should be displaying as current image | Clicked edit post button post_detail.html | Displays the original image selected | Pass |
| Save Button | When the Save button is pressed, the users uploaded post will be saved | Clicked submit button | Saves and uploads the post successfully | Pass |
| Save Redirect | When form has been submitted, user will be redirected to the edited post (post_detail.html/slug) | Clicked save button | Redirects to the updated post successfully (post_detail.html/slug) | Pass |
| `Delete Post Page` |
|   |   |   |   |  |
| Delete Button | When the user clicks the delete button, the user will be redirected to the home page. | Clicked button | Redirected to the home page | Pass |
| `Error Page` |
|   |   |   |   |   |
| Accessing the edit page as not signed in | When a user is attempting to access the edit page without being signed in, a 404 error not found page should be shown | Loading up the URL to edit a post without being signed in | Displays a 404 page not found page | Pass |
| Accessing the delete page as not signed in | When a user is attempting to access the delete page without being signed in, a 404 error not found page should be shown | Loading up the URL to delete a post without being signed in | Displays a 404 page not found page | Pass |
| Accessing the edit page as a different user from the post author | When a user is attempting to access the edit page of a post they did not make without being signed in, a 404 error not found page should be shown | Loading up the URL to edit a post without being signed in | Displays a 404 page not found page | Pass |
| Accessing the delete page as a different user from the post author | When a user is attempting to access the delete page of a post they did not make without being signed in, a 404 error not found page should be shown | Loading up the URL to delete a post without being signed in | Displays a 404 page not found page | Pass |

 - - -

## BUGS

### Known Bugs

List (or put in a table) all known bugs on your site here as soon as you find them. This will prevent you from forgetting any at the end. Some (if not all) of these bugs will hopefully make their way over to the next section, solved bugs, as you progress through your project.

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | When I tried to access the /admin site when the server was ran locally, I would receive error messages such as DISALLOWED HOST, which made me unable to access the Admin site. | By adding the Gitpod URL to the ALLOWED_HOSTS in settings.py as well as adding the SITE_ID = 1, the problem was solved. |
| 2 | Everytime a new post was uploaded with an image, the images would appear in different sizes - making the content appear out of alignment. | After a lot of testing back and forth, moving the % for post in post_list % placement to underneath the first div, made the content align neatly. |
| 3 | The main content in the pages had a slight gap from the header | By adding the Bootstrap class mb-0 to the header class in base.html, I was able to remove the margin. |
| 4 | Nothing happening after uploading a post on the website via the upload_post.html. The post does not get sent to admin for approval. | By adding the def form_valid to my UploadPost view, I was able to upload a blog post logged in as admin, to the admin site, and from there I was able to set the blog post to published to display it on the website. The def form_valid sets the author of the post as the current user and sets the post to a 0 (Draft). By calling the super().form_valid(form), the data is then saved to the database. |
| 5 | After solving the first issue with the blog post not being saved and sent to the admin for publishing, I logged in with a different user to test if I was able to upload a blog post. I received an error "UNIQUE constraint failed: blog_post.slug", which indicated that the slug generated on the blog post already exists in the database. | To fix this issue I had to start with importing the get_random_string from the django.utils.crypto as well as the slugify from the django.utils.text module to make it possible to generate a unique slug from the title (if there was already a title existing with the same name). I then had to iterate with a while loop through the database to check if a slug already exists with that title. If the title is not unique, it appends a random string (with the help of the get_random_string) to the slug to make it unique inside the while loop. Lastly, when a unique slug is made, it is saved and set to the post it has been generated for. |
| 6 | When submitting a comment, the comment textarea is not emptied when reloading the page, which results in the same comment being posted again. | Added "return redirect('post_detail', slug=slug)" to the comment_form if statement, to return back to the post when a comment has been successfully submitted. |
| 7 | When deleting a comment, the comment wasn't actually removed from the database, but only removed from the frontend. The comments count function was still displaying the amount of comments although some were deleted. | Added a "DeleteView" inherit to the DeleteComment class, which updates the database correctly. |

### Bug Examples:
- Bug 2

![Error2](/media/images/2.png)

- Bug 3

![Error3](/media/images/3.png)

- Bug 6

![Error6](/media/images/6.png)