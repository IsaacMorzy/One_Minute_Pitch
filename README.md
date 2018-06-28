# One_Minute_Pitch
Web app where users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them

## Description
[This](https://python-one-minute-pitch.herokuapp.com) is a web application that allows users to submit a pitch. Also, other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account. <br>

The pitches are organized by categories. Examples of categories: <br> 
- pickup lines
- interview pitches
- product pitches
- promotion pitches

## User Stories
As a user I would like:
* to view the different categories
* to see the pitches other people have posted
* to submit a pitch in any category
* to comment on the different pitches and leave feedback
* to vote on the pitch and give it a downvote or upvote

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : jane@doe.com <br> Username : jane101 <br> Password : doe1 | New user is registered |
| Log in | Your email : jane@doe.com <br> Password : doe1 | Logged in |
| Display pitch categories | N/A | List of various pitch categories |
| See pitches from selected category | **Click** a category | Directed to a page with a list of pitches from the selected category |
| Create a pitch | **Click Create A Pitch** | An authenticated user is directed to a page with a form where the user can create and submit a pitch |
| See a pitch | **Click** on a pitch | A user is directed to a page containing the pitch, its comments and its votes |
| Comment on a pitch | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a pitch |
| Upvote on a pitch | **Click** on upvote glyphicon | The votes on the pitch increases by one |
| Downvote on a pitch | **Click** on downvote glyphicon | The votes on the pitch decreases by one |

## Setup/Installation Requirements

* Click [One Minute Pitch](https://) <br/>
  or <br/>
* Copy [One Minute Pitch](https) and  Paste the link on your prefered browerser

This requires internet connection.

## Known Bugs



## Technologies Used
- Python3.6
- Flask
- Bootstrap
- Postgres Database
- CSS
- HTML

### License

MIT (c) 2017 **[IsaacMorzy](https://github.com/IsaacMorzy)**