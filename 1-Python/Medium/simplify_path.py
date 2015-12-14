# 8/22 - Stack, String
# Given an absolute path for a file (Unix-style), simplify it.
# For example,
#   path = "/home/", => "/home"
#   path = "/a/./b/../../c/", => "/c"
#
class SimplifyPath(object):
    # Test on LeetCode - 56ms
    # Note corner cases
    def simplify_path(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        lst = path.split('/')
        for e in lst:
            if e:  # e is not empty ('')
                if e == '..':  # pop
                    if stack:
                        stack.pop()
                elif e == '.':  # do nothing
                    continue
                else:
                    stack.append(e)
        if not stack:
            return '/'
        result = ''
        for e in stack:
            result += '/' + e
        return result


def main():
    test = SimplifyPath()
    print test.simplify_path("/home/")
    print test.simplify_path("/a/./b/../../c/")
    print test.simplify_path("/../")
    print test.simplify_path("/home//foo/")

if __name__ == "__main__":
    main()