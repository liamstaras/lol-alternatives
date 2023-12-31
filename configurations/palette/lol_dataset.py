import torch.utils.data as data
import torch
import numpy as np

def lol_loader(dataset,index):
    return LnMbPair(*np.array(dataset[index,:,:,:]))

class LnMbPair:
    def __init__(self,ln_array,mb_array):
        self.lognormal = ln_array
        self.manybody = mb_array

class LOLDataset(data.Dataset):
    def __init__(self, data_path, loader=lol_loader):
        data_dir, data_index = data_path.split(':')
        self.data_file = data_dir+'/data.npy'
        self.index_file = data_dir+'/data-%s.split.npy' % data_index
        self.indices = np.load(self.index_file)
        self.dataset = np.load(self.data_file, mmap_mode='r')
        self.loader = loader

    def __getitem__(self, index):
        ret = {}
        
        pair = self.loader(self.dataset, self.indices[index])

        img = pair.manybody
        cond_image = pair.lognormal

        ret['gt_image'] = torch.tensor(np.expand_dims(img,0), dtype=torch.float32)
        ret['cond_image'] = torch.tensor(np.expand_dims(cond_image,0), dtype=torch.float32)
        ret['path'] = index
        return ret

    def __len__(self):
        return self.indices.size
