# Music App

## Overview
This project is a music application built using Flask. It provides various functionalities such as user registration, OTP verification, song retrieval, and playlist management. The application is designed to work with MongoDB for data storage and utilizes JWT for authentication.

## Project Structure
```
music-app
├── api
│   └── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd music-app
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Set up your MongoDB URI and JWT secret key in your environment variables or directly in the `app.py` file (not recommended for production).

5. **Run the Application**
   ```bash
   python api/app.py
   ```

## Usage
- The API provides the following endpoints:
  - `GET /`: Welcome message and available endpoints.
  - `POST /register`: Register a new user.
  - `POST /send-otp`: Send an OTP to the user's email.
  - `POST /verify-otp`: Verify the OTP sent to the user's email.
  - `GET /songs`: Search for songs.
  - `POST /playlists`: Create a new playlist.
  - `GET /playlists`: Retrieve user playlists.
  - `POST /playlists/add-song`: Add a song to a playlist.
  - `GET /playlists/<playlist_id>/songs`: Get songs from a specific playlist.
  - `DELETE /playlists/<playlist_id>`: Delete a specific playlist.
  - `POST /playlists/<playlist_id>/remove-song`: Remove a song from a playlist.

## Deployment
This application is designed to be deployed on Vercel. Ensure that the `app.py` file includes a handler function compatible with Vercel's serverless architecture.

## Additional Notes
- Make sure to handle sensitive information such as API keys and database credentials securely.
- Consider implementing password hashing for user passwords in production.
- The application is currently set to run in debug mode; disable this in production environments.