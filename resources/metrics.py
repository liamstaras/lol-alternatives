# this file contains functions to compare the training data to outputs

import powerbox as pb
import numpy as np

def power_spectrum_diff(output, target):
    return _power_spectrum_diff(output.cpu(), target.cpu())

def power_spectrum_diff_log(output, target):
    return _power_spectrum_diff(np.exp(output.cpu())-1, np.exp(target.cpu())-1)

def _power_spectrum_diff(output, target):
    output_ps, output_k = pb.get_power(output, 1000)
    target_ps, target_k = pb.get_power(target, 1000)

    diff = (output_ps - target_ps)/target_ps
    rms = np.sqrt(np.mean(diff**2))
    return rms