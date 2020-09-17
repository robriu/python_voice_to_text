import speech_recognition as sr

recognizer = sr.Recognizer()
print('[INFO] Program initialized.')

with sr.AudioFile("data_input.wav") as data_input:
    print ('[UPDATE] Preparing a sound file...')
    data_output = recognizer.record(data_input)

try:
    print ('[UPDATE] Extracting text...')
    script = recognizer.recognize_google(data_output)

    print ('[UPDATE] Creating an output file...')
    output_file = open("audio_output.txt", "w", encoding='utf-8')

    output_file.writelines(script + "\n")
    output_file.close()
    print ('[UPDATE] Text Extration Done...')

except Exception as e:
    print("[FAILURE]: " + str(e))

print('[SUCCESS] Execution Done.')
print('[INFO] Program Closed.')