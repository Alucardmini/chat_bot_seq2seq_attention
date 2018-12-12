# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Ops for building neural network seq2seq decoders and losses.

See the @{$python/contrib.seq2seq} guide.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=unused-import,wildcard-import,line-too-long
from seq2seq.attention_wrapper import *
from seq2seq.basic_decoder import *
# from seq2seq.beam_search_decoder import *
# from seq2seq.beam_search_ops import *
from seq2seq.decoder import *
from seq2seq.helper import *
from seq2seq.loss import *
from tensorflow.python.util.all_util import remove_undocumented
# pylint: enable=unused-import,widcard-import,line-too-long

_allowed_symbols = [
    "sequence_loss",
    "Decoder",
    "dynamic_decode",
    "BasicDecoder",
    "BasicDecoderOutput",
    "CopyNetDecoder",
    "BeamSearchDecoder",
    "BeamSearchDecoderOutput",
    "BeamSearchDecoderState",
    "Helper",
    "CustomHelper",
    "CopyNetTrainingHelper",
    "FinalBeamSearchDecoderOutput",
    "gather_tree",
    "GreedyEmbeddingHelper",
    "SampleEmbeddingHelper",
    "ScheduledEmbeddingTrainingHelper",
    "ScheduledOutputTrainingHelper",
    "TrainingHelper",
    "BahdanauAttention",
    "LuongAttention",
    "hardmax",
    "AttentionWrapperState",
    "AttentionWrapper",
    "AttentionMechanism",
    "tile_batch",
    "safe_cumprod",
    "monotonic_attention",
    "monotonic_probability_fn",
    "BahdanauMonotonicAttention",
    "LuongMonotonicAttention",
]


remove_undocumented(__name__, _allowed_symbols)