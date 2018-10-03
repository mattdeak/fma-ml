from pydub import AudioSegment
from scipy.io.wavfile import read as read_wav
import shutil
import tempfile

class MP3Reader:

    def __init__(self):
        self.TMP_DIR = tempfile.mkdtemp()
        self.EXPORT_PATH = self.TMP_DIR + '/export.wav'

    def __del__(self):
        """Removes the temporary directory before cleanup."""
        shutil.rmtree(self.TMP_DIR)

    def read(self, filepath):
        """Reads an mp3 file into a numpy array.
        
        Arguments:
            filepath {str} -- The path to the mp3 file
        """
        # Convert from mp3 to wav
        sound = AudioSegment.from_mp3(filepath)
        sound.export(self.EXPORT_PATH, "wav")

        _, data = read_wav(self.EXPORT_PATH)
        return data

    def make_generator(self, batch_size, mp3_directory):
        """Creates a generator that reads wav data from mp3 files
        in a directory. Assumes that all mp3 files are prepended with `mp3`.
        
        Arguments:
            batch_size {int} -- The number of data samples to extract per batch
            mp3_directory {str} -- The directory containing mp3 files
        """


        