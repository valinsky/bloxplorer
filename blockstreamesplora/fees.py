from blockstreamesplora.utils import get_from_path


def get():
    """
    Get an object where the key is the confirmation target (in number of blocks)
    and the value is the estimated feerate (in sat/vB).
    The available confirmation targets are 2, 3, 4, 6, 10, 20, 144, 504 and 1008 blocks.
    """
    return get_from_path('fee-estimates')
