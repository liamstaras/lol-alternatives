# this file contains functions to compare the training data to outputs

import powerbox as pb
import numpy as np

def power_spectrum_diff(output, target):
    
    output_ps, output_k = pb.get_power(output.cpu(), 1000)
    target_ps, target_k = pb.get_power(target.cpu(), 1000)

    diff = (output_ps - target_ps)/target_ps
    rms = np.sqrt(np.mean(diff**2))
    return rms