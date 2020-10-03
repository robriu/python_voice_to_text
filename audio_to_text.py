import speech_recognition as sr

recognizer = sr.Recognizer()
print('[INFO] This program exactracts scripts from audio file.')

# example filename "data_input.wav"
with sr.AudioFile(input("[INPUT] Enter filename: ")) as data_input:
    print ('[UPDATE] Recognizing an audio file...')
    data_output = recognizer.record(data_input)

try:
    print ('[UPDATE] Extracting a script...')
    script = recognizer.recognize_google(data_output)

    print ('[UPDATE] Creating an output file...')
    output_file = open("audio_output.txt", "w", encoding = 'utf-8')

    output_file.writelines(script + "\n")
    output_file.close()
    print ('[UPDATE] Script Extracted...')

except Exception as e:
    print("[FAILURE]: " + str(e))

print('[SUCCESS] Execution Done.')
print('[INFO] Program Finished.')