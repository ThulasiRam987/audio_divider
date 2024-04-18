from pydub import AudioSegment
def split_audio(input_file, output_prefix, segment_length_ms):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the number of segments
    num_segments = len(audio) // segment_length_ms

    # Split the audio into segments
    for i in range(num_segments):
        start_time = i * segment_length_ms
        end_time = (i + 1) * segment_length_ms
        segment = audio[start_time:end_time]
        segment.export(f"{output_prefix}_{i}.wav", format="wav")

# Example usage:
input_file = "file_name"
output_prefix = "back_name"
segment_length_ms = 4000  # Length of each segment in milliseconds (5 seconds in this example)
split_audio(input_file, output_prefix, segment_length_ms)
