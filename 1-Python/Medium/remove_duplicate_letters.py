class RemoveDuplicateLetters(object):
    def remove_duplicate_letters(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s

        ret_backward = self.remove_backward(s)
        ret_forward = self.remove_forward(s)
        return min(ret_backward, ret_forward)

    def remove_backward(self, s):
        ret_backward = ""
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char not in ret_backward:
                ret_backward = char + ret_backward
            else:
                next = ret_backward[0]
                if char < next:  # keep new and remove older
                    prev_pos = ret_backward.index(char)
                    ret_backward = ret_backward[0:prev_pos] + ret_backward[prev_pos+1:]
                    ret_backward = char + ret_backward
        return ret_backward

    def remove_forward(self, s):
        ret_forward = ""
        for i in range(0, len(s)):
            char = s[i]
            if char not in ret_forward:
                ret_forward += char
            else:
                prev_pos = ret_forward.index(char)
                next_char = ret_forward[min(prev_pos + 1, len(ret_forward)-1)]
                if char > next_char:  # keep new and remove older
                    ret_forward = ret_forward[0:prev_pos] + ret_forward[prev_pos+1:]
                    ret_forward += char
        return ret_forward

test = RemoveDuplicateLetters()
print test.remove_duplicate_letters("bcabc")
print test.remove_duplicate_letters("cbacdcbc")
print test.remove_duplicate_letters("ccacbaba")
print test.remove_duplicate_letters("abacb")
print test.remove_duplicate_letters("abcab")
print test.remove_duplicate_letters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")

