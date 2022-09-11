class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {sc: tc for sc, tc in zip(s, t)}

        # No two characters may map to the same character,
        # but a character may map to itself.
        if len(char_map) > len(set(char_map.values())):
            return False

        # All occurrences of a character must be replaced with
        # another character while preserving the order of characters.
        new_t = ""

        for c in s:
            new_t += char_map[c]

        return new_t == t