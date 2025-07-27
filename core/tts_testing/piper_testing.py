import subprocess
import os

voice_path = "core/tts_testing/piper/voices/en_US-amy-low.onnx"
piper_exe = "core/tts_testing/piper/piper.exe"
text = "Hello! I'm your blind assistant, ready to describe your surroundings."
output_path = r"D:\blind-assistant\core\tts_testing\output.wav"
command = f"{piper_exe} --model {model_path} --text \"{text}\" --output_file {output_path}"



print("Running Piper command:")
print(" ".join(command))

result = subprocess.run(
    command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    timeout=30  # kill after 30s if it hangs
)


# Show Piper output
print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)

# Try to play the file (only if it was created)
if os.path.exists("output.wav"):
    os.system("start output.wav")
else:
    print("❌ output.wav not created!")
