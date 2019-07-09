class Error(Exception):
    """Base class for other exceptions"""
    pass

class ItemHasNoPriceError(Error):
    """Raised when an item is added without a price"""
    pass