"""Module defining decoders."""
from onmt.decoders.decoder import DecoderBase, InputFeedRNNDecoder, \
    StdRNNDecoder
from onmt.decoders.transformer import TransformerDecoder


str2dec = {"transformer": TransformerDecoder}

__all__ = ["DecoderBase", "TransformerDecoder"]
