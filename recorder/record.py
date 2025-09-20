import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 5  # Durasi rekaman

print("Mulai merekam...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Tunggu rekaman selesai
namaFile = input("masukkan nama file : ") + ".wav"
write(namaFile, fs, recording)
print(f"Rekaman selesai, disimpan ke {namaFile}")

