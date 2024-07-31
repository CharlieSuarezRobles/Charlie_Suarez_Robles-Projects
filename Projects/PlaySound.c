#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <alsa/asoundlib.h>

#define PCM_DEVICE "default"

int SAMPLE_RATE = 44100;
int SECONDS = 5;
double AMPLITUDE = 0.5;
int NUM_SAMPLES = 5 * 44100;
int MAX_NUMBER_OF_NOTES = 20;

void play_chord(int16_t **signal, char *chord_name, int* index_to_save, int num_of_notes, int inversion, int octave);
void save_note(int16_t **signal, int freq, int index_to_save);
void play_signal(snd_pcm_t *handle);

	

void play_chord(int16_t **signal, char *chord_name, int *index_to_save, int num_of_notes, int inversion, int octave) {

	if (*index_to_save > MAX_NUMBER_OF_NOTES) {
		fprintf(stderr, "you want to add more notes into the signal than it can handle\n");
		EXIT_FAILURE;
	}

	if (num_of_notes > 4) {
		fprintf(stderr, "you want to play more notes inside the chord than what this function can handle\n");
		EXIT_FAILURE;
	}

	int freq_to_add = 0;
	int *note_array = (int *)malloc(4 * sizeof(int));

	if (strcmp(chord_name, "A") == 0) {
		}

	else if (strcmp(chord_name, "A#") == 0 || strcmp(chord_name, "Bb") == 0) {
		freq_to_add = 1;
		}

	else if (strcmp(chord_name, "B") == 0) {
		freq_to_add = 2;
	}

	else if (strcmp(chord_name, "C") == 0) {
		freq_to_add = -9;
	}

	else if (strcmp(chord_name, "C#") == 0 || strcmp(chord_name, "Db") == 0) {
		freq_to_add = -8;
	}
	
	else if (strcmp(chord_name, "D") == 0) {
		freq_to_add = -7;
	}
	
	else if (strcmp(chord_name, "D#") == 0 || strcmp(chord_name, "Eb") == 0) {
		freq_to_add = -6;
	}

	else if (strcmp(chord_name, "E") == 0) {
		freq_to_add = -5;
	}

	else if (strcmp(chord_name, "F") == 0) {
		freq_to_add = -4;
	}

	else if (strcmp(chord_name, "F#") == 0 || strcmp(chord_name, "Gb") == 0) {
		freq_to_add = -3;
	}
	
	else if (strcmp(chord_name, "G") == 0) {
		freq_to_add = -2;
	}
	
	else if (strcmp(chord_name, "G#") == 0 || strcmp(chord_name, "Ab") == 0) {
		freq_to_add = -1;
	}
	
	note_array[0] = 0 + freq_to_add + ((octave - 4) * 12);
        note_array[1] = 4 + freq_to_add + ((octave - 4) * 12);
        note_array[2] = 7 + freq_to_add + ((octave - 4) * 12);
        note_array[3] = 12 + freq_to_add + ((octave - 4) * 12);

	if (inversion == 0) {
	}
	else if (inversion == 1) {
		note_array[1] += 16;
	}
	else if (inversion == 2) {
		note_array[1] += 16;
		note_array[2] += 15;
	}

	for (int i = 0; i < num_of_notes; i++) {
		double freq = (double)440 * pow(2, (double)note_array[i]/12);
		save_note(signal, freq, *index_to_save);
		*index_to_save += 1;
	}
	return;
	}	


void save_note(int16_t **signal, int freq, int index_to_save) {
	if (index_to_save < MAX_NUMBER_OF_NOTES) {
		for (int i = 0; i < NUM_SAMPLES; i++) {
			double t = (double)i / SAMPLE_RATE;
			signal[index_to_save][i] = (int16_t)(AMPLITUDE * 32767.0 * sin(2 * M_PI * freq * t));
		}
		return;
	}
	fprintf(stderr, "index is too high for save_note function\n");
	exit(EXIT_FAILURE);
	}



void play_signal(snd_pcm_t *handle) {
	int index_to_save = 0;
	
	int16_t **signal = (int16_t **)calloc(MAX_NUMBER_OF_NOTES, sizeof(int16_t *));
	if (!signal) {
		fprintf(stderr, "Memory allocation failed\n");
		EXIT_FAILURE;
		}
	for (int i = 0; i < MAX_NUMBER_OF_NOTES; i++) {
		signal[i] = (int16_t *)malloc(NUM_SAMPLES * sizeof(int16_t));
		if (!signal[i]) {
			fprintf(stderr, "Memory allocation failed\n");
			EXIT_FAILURE;
			}
		}

	play_chord(signal, "F", &index_to_save, 4, 0, 5);		

   	 int16_t *buffer = (int16_t *)malloc(NUM_SAMPLES * sizeof(int16_t));
   	 if (!buffer) {
       		 fprintf(stderr, "Memory allocation failed\n");
       		 return;
   	 }

	for (int i = 0; i < NUM_SAMPLES; i++) {
		int32_t mixer = 0;
		for (int j = 0; j < index_to_save; j++) {
			mixer += (int32_t)signal[j][i];
		}
		mixer = mixer / index_to_save; //index_to_save is the equivalent to the number of notes the signal has
		
		if (mixer > INT16_MAX) {
			mixer = INT16_MAX;
		}
		if (mixer < INT16_MIN) {
			mixer = INT16_MIN;
		}
		buffer[i] =(int16_t)mixer;
	}




   	 // Write the buffer to the PCM device
   	 int err = snd_pcm_writei(handle, buffer, NUM_SAMPLES);
   	 if (err < 0) {
     		   fprintf(stderr, "Playback error: %s\n", snd_strerror(err));
   	 }

   	 free(buffer);

        for (int i = 0; i < MAX_NUMBER_OF_NOTES; i++) {
                free(signal[i]);
		signal[i] = NULL;
                }
	free(signal);
	signal = NULL;
	return;

	}

int main() {
    snd_pcm_t *handle;
    int err;

    if ((err = snd_pcm_open(&handle, PCM_DEVICE, SND_PCM_STREAM_PLAYBACK, 0)) < 0) {
        fprintf(stderr, "Cannot open PCM device %s: %s\n", PCM_DEVICE, snd_strerror(err));
        return 1;
    }

    if ((err = snd_pcm_set_params(handle,
                                  SND_PCM_FORMAT_S16_LE,
                                  SND_PCM_ACCESS_RW_INTERLEAVED,
                                  1, // Mono
                                  44100, // Sample rate
                                  0, // No resampling
                                  50000)) < 0) { // 50ms latency
        fprintf(stderr, "Cannot set PCM parameters: %s\n", snd_strerror(err));
        snd_pcm_close(handle);
        return 1;
    }

    play_signal(handle);

    snd_pcm_close(handle);
    return 0;
}
