# Bauer Media Audio - AI Podcast Intro Generator

A Proof of Concept (PoC) application that generates psychologically tailored podcast intros using OpenAI's GPT model.

## Features

- Simple web interface for inputting podcast themes/genres
- AI-powered generation of 15-20 second podcast intros
- Incorporates psychological hooking techniques:
  - Curiosity hooks
  - Concreteness
  - Urgency
- Responsive design with Bauer Media Audio branding
- Mock responses when no API key is provided

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
   Note: If no API key is provided, the application will use mock responses.

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter a podcast theme/genre (e.g., "true crime", "comedy", "business")
2. Click "Generate Intro"
3. View the AI-generated intro in the result section

## Technical Details

- Backend: Python 3.x with Flask
- Frontend: HTML/CSS
- AI Integration: OpenAI GPT-3.5-turbo
- No database required
- Simple, single-route architecture

## Example Outputs

- True Crime: "Who's the killer? [Podcast Name] dives into chilling cases—tune in now!"
- Comedy: "What's the wildest joke? [Podcast Name] brings gut-busting laughs—don't miss out!"
- Business: "Ready to disrupt? [Podcast Name] reveals game-changing strategies—act fast!" 