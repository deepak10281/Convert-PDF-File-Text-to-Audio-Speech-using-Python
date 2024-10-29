import PyPDF2
from gtts import gTTS
import os

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"  # Add newline for page separation
    return text

# Function to convert text to audio
def text_to_audio(text, audio_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)

# Main function
def main(pdf_path, audio_path):
    # Extract text from PDF
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    
    if not text.strip():
        print("No text found in the PDF.")
        return
    
    # Convert text to audio
    print("Converting text to audio...")
    text_to_audio(text, audio_path)
    
    print(f"Audio saved to {audio_path}")

# Example usage
if __name__ == "__main__":
    pdf_file_path = "Deepak Documents/PROJECTS/MAJOR PROJECT/code explaination.pdf"  # Replace with your PDF file path
    audio_file_path = "output.mp3"  # Output audio file
    main(pdf_file_path, audio_file_path)
