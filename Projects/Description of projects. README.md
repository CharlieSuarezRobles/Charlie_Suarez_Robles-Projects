# **Triton Software Engineering Project (Onboarding Repository)**

  The onboarding repository is a set of instructions and readings that incoming TSE members have to complete prior to becoming TSE developers. The product that comes
from this project is a website where the user can input a task and a description. Once the user clicks a button, the name and description appear inside of a list
of tasks that the user can check and uncheck. Besides this, the website also handles user accounts.
To achieve this product, the onboarding repository talks about the structure that an application built on TSE tends to follow as well as the purpose of each file
within the application. The instructions make the incoming member create API client functions in the frontend and function handlers in the backend. The API functions are only activated when the user clicks on a button after they have typed their task with its description. Once these functions are activated, they call specific backend functions called function handlers which give to the database the given task that the user is trying to enter. Besides this milestone, the
instructions also make the member use Figma to simulate how designers would want a given task to look like in the website. More specifically, the instructions
make the member use React to create new components, reuse others, and create CSS classes to determine the appearance of each task as well as how these will
fit inside of the bigger container that makes up the list of tasks. Finally, the instructions also make the member create a new schema (kind of object) that defines
how a User object should look like in the database. With this schema and more function handlers and API functions, the member can make the website handle user
accounts.

in the backend that involve creating new routers, routes, and function handlers
to make the backend store a set of tasks in the fronten. The incoming member also needs to implement API functions to achieve communication between the frontend and backend. The project also involves creating CSS classes 

# **3 Project Series 2023 (The files are called Project 1, 2, & 3)**

This folder contains three projects I did in my python introductory class. In "Project 1," I used the library "csv" to retrive data from a file called zonann_temps. In "Project 2,"
I used "PIL" to create four filtering functions that could access and filter images; I put all functions together into project() and made them create a new image with distinct filters from the three
jpg. images combined. In "Project 3," I created a game called "Avoid the X's" using the "Random" class; I implemented eight functions, each for: running the game, running each of the five levels,
displaying the instructions, displaying the game board, displaying the lives and the numbers selected in the game board, comparing the numbers you and the computer selected, and displaying
the "GG" or the "XX" result on the board. For further details, please see each project file. 

# **Computer Chords 2024 (The file is called PlaySound.c)**

This folder also contains a personal project I made which combined my passion for music with my software engineering skills. The project consists of one file called PlaySound.c. This code in this file interacts with the computer's audio devices to produce sound in form of chords. It does that by using three special functions called "snd_pcm_open", "snd_pcm_set_params", and "snd_pcm_writei" all which come from a linux software framework called ALSA. The file also uses one main function and three helper functions called "play_chord" (it stores the information about a chord), "save_note" (it saves the information of a note into an array), and "play_signal" (uses the special function called "snd_pcm_writei" to tell the sound card to play a given chord) which with the help of the three ALSA functions play the desired chord.
