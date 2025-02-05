# AutoClipUpload

A simple app to quickly upload your videos to youtube.

## First-Time Configuration

### 1. Create a Google Cloud Project
You can title the project however you want.

### 2. Enable the YouTube Data API
Search for the YouTube Data API V3, and enable it.

### 3. Create an OAuth2.0 Client
Go to the credentials tab, click "Create Credentials, and select OAuth Client ID"

### 4. Configure Oauth2.0 Client
Add "http://localhost:8080" as an authorized JavaScript origin and redirect URI

### 5. Allow Users
Either publish the OAuth app, or go to the OAuth consent screen tab, and add your desired account to upload videos with as a test user.

### 6. Configure App
Inside the app, copy your Client ID and Client Secret into the configuration tab of the app

## TO-DO
- [ ] Add App Icons
- [ ] Video modifications (trimming)
- [X] Automatically validate credentials before allowing user to upload
- [ ] Back button after video uploads returns to home page
- [ ] Clean codebase