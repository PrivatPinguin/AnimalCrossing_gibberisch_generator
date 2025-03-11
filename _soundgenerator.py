import random
from pydub import AudioSegment

def generate_random_audio(duration_seconds: int, file_count: int):
    """
    Generiert [file_count] Dateien, mit der länge von [duration_seconds]
    """
    files = [f"{chr(i)}.mp3" for i in range(ord('a'), ord('z') + 1) if chr(i) not in ['v', 'y']]
    total_duration_ms = duration_seconds * 1000
    silence = AudioSegment.silent(duration=10)  # 10 ms Stille
    
    for i in range(file_count):
        combined_audio = AudioSegment.silent(duration=0)
        
        while len(combined_audio) < total_duration_ms:
            random_file = random.choice(files)
            try:
                segment = AudioSegment.from_mp3(random_file)
                combined_audio += segment + silence  # 10 ms Delay einfügen
            except Exception as e:
                print(f"Fehler beim Laden von {random_file}: {e}")
        
        combined_audio = combined_audio[:total_duration_ms]
        filename = f"output_t{str(total_duration_ms).zfill(6)}_{str(i).zfill(4)}.mp3"
        combined_audio.export(filename, format="mp3")
        print(f"Datei gespeichert: {filename}")

def generate_audio_from_string(input_string: str):
    """
    Transferiert einen Text in "AnimalCrossing" gibberisch
    """
    input_string = input_string.lower().replace(" ", "_")
    output_file = f"{input_string[:20]}.mp3"
    combined_audio = AudioSegment.silent(duration=0)
    silence = AudioSegment.silent(duration=3)  # ms Stille
    long_silence = AudioSegment.silent(duration=170)  #  ms Stille für "_"
    long_silence_dot = AudioSegment.silent(duration=300)  #  ms Stille für "_"
    
    input_string = input_string.replace('v', 'f').replace('y', 'j')

    for char in input_string:
        if 'a' <= char <= 'z':
            file_name = f"{char}.mp3"
            try:
                segment = AudioSegment.from_mp3(file_name)
                combined_audio += segment + silence
            except Exception as e:
                print(f"Fehler beim Laden von {file_name}: {e}")
        elif char == '_':
            combined_audio += long_silence
        elif char == '.' or char == ',':
            combined_audio += long_silence_dot
        else:
            pass
    
    combined_audio.export(output_file, format="mp3")
    print(f"Datei gespeichert: {output_file}")


# Beispielaufruf
# generate_random_audio(4,3) # generiert 3 dateien mit der länge von 4 sekunden
# generate_audio_from_string("Ratking kann wie animal krossing sprechen, die geile sahnebutterhupfdohle, lol die hat rofl gesagt") # übersetzt das in AnimalCrossing gibberisch
