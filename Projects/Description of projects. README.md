# **Triton Software Engineering Project (Onboarding Repository)**

The onboarding repository is a set of instructions and readings that new TSE members complete before becoming developers. The goal is to build a website where users can input tasks with descriptions. Once a task is submitted, it appears in a list that users can check or uncheck. The site also supports user account handling.

To help members build this, the onboarding repo introduces the typical structure of a TSE app. It walks through the purpose of each file and teaches members how to create:

API client functions in the frontend,

Backend function handlers that process user inputs and interact with the database.

The API functions are triggered when a user clicks a button, sending the task data to the backend via these function handlers.

Members are also guided through using Figma for UI mockups and React to build reusable components and style them with CSS. They create a schema that defines how a User object is stored in the database, allowing the website to handle user accounts.

On the backend, members learn to build routers, routes, and more function handlers to support task storage. The project emphasizes connecting frontend and backend through API functions and involves creating CSS classes to style the UI.

# **3 Project Series 2023 (The files are called Project 1, 2, & 3)**

This folder contains three projects I completed in my Python introductory class.

Project 1: I used the csv library to retrieve data from a file called zonann_temps.

Project 2: I used the PIL library to create four image filtering functions. These functions could access and filter images. I combined them using a function called project() to produce a new image with distinct filters applied to three JPG files.

Project 3: I created a game called "Avoid the X's" using the random module. I implemented eight functions to:

Run the game

Run each of the five levels

Display the instructions

Display the game board

Display the lives and selected numbers

Compare your selected numbers with the computer’s

Display a "GG" or "XX" result on the board

Handle gameplay progression

For further details, please see each individual project file.

# **Computer Chords 2024 (The file is called PlaySound.c)**

This folder contains a personal project that combines my passion for music with my software engineering skills. The project consists of a single file named PlaySound.c.

The code in this file interacts with the computer's audio device to produce sound in the form of chords. It does this using three key functions from the ALSA (Advanced Linux Sound Architecture) framework:

snd_pcm_open

snd_pcm_set_params

snd_pcm_writei

These functions allow the program to configure and send sound data to the audio hardware.

The file also includes one main function and three helper functions:

play_chord: stores information about a chord

save_note: saves note data into an array

play_signal: calls snd_pcm_writei to output the sound signal for a chord

Together, these functions work with the ALSA library to generate and play musical chords through the computer's audio system.
