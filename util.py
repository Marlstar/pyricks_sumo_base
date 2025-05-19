def clamp(val: int|float, lower: int|float, upper: int|float) -> int|float:
    return max(min(val, upper), lower)
