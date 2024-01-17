# Virtual Dressing Room Project

Welcome to the Virtual Dressing Room project! This repository showcases a virtual dressing room system powered by [Texel.Moda](https://texelmoda.com/), allowing users to try on various outfits using clothing and avatar images. The project integrates with the RapidAPI platform to facilitate the virtual try-on process seamlessly.

## Prerequisites

Before you start, ensure you have the following prerequisites:

 RapidAPI Account: Sign up on the [RapidAPI website](https://rapidapi.com/texel-inc-texel-inc-default/api/texel-virtual-try-on) to obtain an API key.

## Installation

1. Clone this repository to your local machine:

   git clone https://github.com/YourUsername/YourRepository.git

Navigate to the project directory:

cd YourRepository
Install necessary dependencies:


pip install -r requirements.txt

Usage
Obtain your RapidAPI key by signing up on the RapidAPI website.

Open the src/config.py file and replace 'RAPID_API_KEY' with your actual RapidAPI key.

Prepare the clothing item image and avatar image in a compatible format (e.g., JPG, PNG).

Run the virtual dressing room script:

bash
Copy code
python src/main.py
The script will generate an output image (result.jpg) showing the avatar wearing the chosen clothing item
