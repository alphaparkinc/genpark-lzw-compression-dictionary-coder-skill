"""Lempel-Ziv-Welch (LZW) Lossless Compression Engine.
100% Python Standard Library.
"""

class LZWCoder:
    """LZW dictionary encoder and decoder."""

    @staticmethod
    def compress(uncompressed: str) -> list:
        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}
        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = c
        if w:
            result.append(dictionary[w])
        return result

    @staticmethod
    def decompress(compressed: list) -> str:
        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}
        if not compressed:
            return ""
        w = chr(compressed[0])
        result = [w]
        for k in compressed[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError(f"Corrupt LZW code token: {k}")
            result.append(entry)
            dictionary[dict_size] = w + entry[0]
            dict_size += 1
            w = entry
        return "".join(result)
