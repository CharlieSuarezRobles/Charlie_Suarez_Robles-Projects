# **Triton Software Engineering Project (Onboarding Repository)**

The onboarding repository is a set of instructions and readings that new TSE members complete before becoming developers. The goal is to build a website where users can input tasks with descriptions. Once a task is submitted, it appears in a list that users can check or uncheck. The site also supports user account handling.

To help members build this, the onboarding repo introduces the typical structure of a TSE app. It walks through the purpose of each file and teaches members how to create:

API client functions in the frontend,

Backend function handlers that process user inputs and interact with the database.

The API functions are triggered when a user clicks a button, sending the task data to the backend via these function handlers.

Members are also guided through using Figma for UI mockups and React to build reusable components and style them with CSS. They create a schema that defines how a User object is stored in the database, allowing the website to handle user accounts.

On the backend, members learn to build routers, routes, and more function handlers to support task storage. The project emphasizes connecting frontend and backend through API functions and involves creating CSS classes to style the UI.

# **3 Project Series 2023 (The files are called Project 1, 2, & 3)**

This folder contains three projects I did in my python introductory class. In "Project 1," I used the library "csv" to retrive data from a file called zonann_temps. In "Project 2,"
I used "PIL" to create four filtering functions that could access and filter images; I put all functions together into project() and made them create a new image with distinct filters from the three
jpg. images combined. In "Project 3," I created a game called "Avoid the X's" using the "Random" class; I implemented eight functions, each for: running the game, running each of the five levels,
displaying the instructions, displaying the game board, displaying the lives and the numbers selected in the game board, comparing the numbers you and the computer selected, and displaying
the "GG" or the "XX" result on the board. For further details, please see each project file. 

# **Computer Chords 2024 (The file is called PlaySound.c)**

This folder also contains a personal project I made which combined my passion for music with my software engineering skills. The project consists of one file called PlaySound.c. This code in this file interacts with the computer's audio devices to produce sound in form of chords. It does that by using three special functions called "snd_pcm_open", "snd_pcm_set_params", and "snd_pcm_writei" all which come from a linux software framework called ALSA. The file also uses one main function and three helper functions called "play_chord" (it stores the information about a chord), "save_note" (it saves the information of a note into an array), and "play_signal" (uses the special function called "snd_pcm_writei" to tell the sound card to play a given chord) which with the help of the three ALSA functions play the desired chord.
