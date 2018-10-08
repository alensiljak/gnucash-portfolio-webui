"""
A few functions that help with file caching
86400 seconds in a day <= should be the default value for day-caching.
"""

class Cache():
    """ 
    The default cache repository.
    File cache is stored in system temp directory.
    """
    _cache = None

    def __init__(self):
        import tempfile
        import diskcache as dc

        tempdir = tempfile.gettempdir()
        self._cache = dc.Cache(tempdir)

    def get(self, key: str):
        return self._cache.get(key)
    
    def set(self, key: str, value: str):
        self._cache.set(key, value)

    def delete(self, key: str):
        """ Removes the file cache with the given name """
        self._cache.delete(key)


class AssetAllocationCache(Cache):
    """
    Cache implementation specific for Asset Allocation.
    """
    def get(self):
        """ retrieves the Asset Allocation cached in a text file """
        key = self.get_key()
        output = super(AssetAllocationCache, self).get(key)
        return output

    def set(self, value: str):
        """ Stores asset allocation into cache """
        key = self.get_key()
        super(AssetAllocationCache, self).set(key, value)

    def get_key(self):
        """ Creates the asset allocation cache key """
        from pydatum import Datum

        today_str = Datum().to_iso_date_string()
        key = f"aa_{today_str}.txt"
        return key

    def delete(self):
        """ Clears the cache """
        key = self.get_key()
        super(AssetAllocationCache, self).delete(key)
