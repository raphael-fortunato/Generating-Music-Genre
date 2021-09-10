import os
from torch.utils.data import Dataset
import torchaudio

class MusicDataset(Dataset, transform=None):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.data = []
        self.labels = []
        self.classes = []
        self.transform = transform
        for path, dir_names, files in os.walk(root):
            if not self.classes:
                self.classes = dir_names
            for f in files:
                full_path = os.path.join(path, f)
                label = self.classes.index(f.split('.')[0])
                self.labels.append(label)
                self.data.append(full_path)


    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        fname = self.data[i]
        audio = torchaudio.load(fname)[0]
        if transform: 
            audio = transform(audio)
        class_idx = self.labels[i]
        return audio, class_idx