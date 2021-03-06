import speech_recognition as sr

AIFF = [".aiff", ".aif"]
AIFFC = [".aifc"]
WAV = [".wav", ".wave"]
FLAC = [".flac"]

FORMATS_SUPPORTED = tuple(AIFF + AIFFC + WAV + FLAC)

Language = {
    "EN" : "en-EN",
    "RU" : "ru-RU",
    "CN" : "zh-CN"
}

recognizer = sr.Recognizer()

print('[INFO] This program exactracts scripts from audio files.')
input_filename = input("[INPUT] Enter input filename: ")

if not input_filename.lower().endswith(FORMATS_SUPPORTED):
    print("[FAILURE] Not supported file format.")
    
else:
    try:
        # example input filename "data_input.wav"
        with sr.AudioFile(input_filename) as data_input:
            print ('[UPDATE] Recognizing audio file...')
            data_output = recognizer.record(data_input)

        print ('[UPDATE] Extracting script...')
        print ("[INFO] Languages: EN = English | RU = Русский | CN = 中文")
        script = recognizer.recognize_google(data_output, language = Language[input("[INPUT] Choose language: ")])

        print ('[UPDATE] Creating output file...')
        # example output filename "audio_output.txt"
        output_file = open(input("[INPUT] Enter output filename: "), "w", encoding = 'utf-8')

        output_file.writelines(script + "\n")
        output_file.close()

        print ('[UPDATE] Script Extracted...')
        print('[SUCCESS] Execution Done.')

    except Exception as e:
        print("[FAILURE]: " + str(e).replace("; ", "\r\n\t"))
    
print('[INFO] Program Finished.')