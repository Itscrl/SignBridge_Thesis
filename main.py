import os
from src.app import app

# Ensure that the heavily ignored directories exist on your machine
os.makedirs("dataset/raw_videos", exist_ok=True)
os.makedirs("dataset/extracted_landmarks", exist_ok=True)
os.makedirs("saved_models", exist_ok=True)

if __name__ == '__main__':
    print("Starting SignBridge UI Server...")
    print("Go to http://127.0.0.0:5000 in your web browser!")
    
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
