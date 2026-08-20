import os
from pypdf import PdfReader
from gtts import gTTS

def pdf_to_audio(pdf_path, audio_output_path):
    """
    Extracts text from a PDF file and converts it into an MP3 audio file.
    """
    print(f"\n🚀 Starting conversion for: {pdf_path}")
    
    # Initialize PDF reader and text variables
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    full_text = ""
    
    # Extract text page by page with a real-time terminal progress indicator
    for page_num, page in enumerate(reader.pages, start=1):
        print(f"📖 Reading page {page_num} of {total_pages}...", end="\r")
        
        text = page.extract_text()
        if text:
            full_text += text + " "
            
    print("\n✅ Text extraction complete!") 
    
    # Guard clause against empty or scanned/image-only PDFs
    if not full_text.strip():
        print("❌ Error: No readable text found in this PDF.")
        return

    print(f"🎙️ Converting {len(full_text):,} characters to speech... Please wait.")
    
    # Generate speech and save the final audio asset
    tts = gTTS(text=full_text, lang='en', slow=False)
    tts.save(audio_output_path)
    print(f"🎉 Success! Audio file saved to: {audio_output_path}")


if __name__ == "__main__":
    print("--- PDF to Speech Converter ---")
    
    # Input validation loop to ensure a clean, existing target file
    while True:
        input_pdf = input("👉 Enter the path to your PDF file: ").strip()
        
        if not input_pdf:
            print("❌ Input cannot be empty. Please type a filename.\n")
            continue
            
        if not os.path.exists(input_pdf):
            print(f"❌ Could not find the file '{input_pdf}'.")
            print("💡 Tip: Double-check the spelling and make sure it's in this same folder.\n")
            continue
            
        if not input_pdf.lower().endswith('.pdf'):
            print("❌ That file is not a PDF. This script only works with .pdf files.\n")
            continue
            
        break

    # Parse the base filename and dynamically generate the output path
    base_name, _ = os.path.splitext(input_pdf)
    output_audio = f"{base_name}.mp3"
    
    # Run core execution pipeline
    pdf_to_audio(input_pdf, output_audio)
