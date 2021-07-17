#!/usr/bin/env python3

# Copyright      2021  Xiaomi Corporation (authors: Fangjun Kuang)

from pathlib import Path

import torch
from utils import read_ark_txt, read_wave

import kaldifeat

cur_dir = Path(__file__).resolve().parent


def test_mfcc_default():
    opts = kaldifeat.MfccOptions()
    opts.frame_opts.dither = 0
    mfcc = kaldifeat.Mfcc(opts)
    filename = cur_dir / "test_data/test.wav"
    wave = read_wave(filename)

    features = mfcc(wave)
    gt = read_ark_txt(cur_dir / "test_data/test-mfcc.txt")
    assert torch.allclose(features, gt, rtol=1e-1)


def test_mfcc_no_snip_edges():
    opts = kaldifeat.MfccOptions()
    opts.frame_opts.dither = 0
    opts.frame_opts.snip_edges = False

    mfcc = kaldifeat.Mfcc(opts)
    filename = cur_dir / "test_data/test.wav"
    wave = read_wave(filename)

    features = mfcc(wave)
    gt = read_ark_txt(cur_dir / "test_data/test-mfcc-no-snip-edges.txt")
    assert torch.allclose(features, gt, rtol=1e-1)


if __name__ == "__main__":
    test_mfcc_default()
    test_mfcc_no_snip_edges()
