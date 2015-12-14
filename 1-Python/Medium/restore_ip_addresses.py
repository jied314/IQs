# 10/21 - Backtracking, String (M)
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example: Given "25525511135",
#             return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# Note:
#   special cases: s too long or too short. if starting with 0, then 01, 001 is invalid; just use 0.
#   10/21 first round failed in checking long s and string with 0.


class RestoreIPAddresses(object):
    def restore_ip_addresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        ret = []
        self.visit_ip_addresses_recursive(s, 0, length, 4, "", ret)
        return ret

    # Test on LeetCode - 64ms
    # Idea:
    #   recursive break up the string, ranging length = 1, 2, 3. check substring value < 256.
    #   string starting with 0, just return 0.
    def visit_ip_addresses_recursive(self, s, start, length, rest_unit_num, prefix, ips):
        rest_length = length - start
        if rest_length == 0 and rest_unit_num == 0:
            ips.append(prefix[1:])
        elif rest_unit_num * 3 >= rest_length >= rest_unit_num:
            if s[start] == "0":
                self.visit_ip_addresses_recursive(s, start + 1, length, rest_unit_num - 1, prefix + "." + "0", ips)
            else:
                max_unit_length = min(rest_length, 3)
                for i in range(1, max_unit_length + 1):
                    str_unit = s[start:start + i]
                    if i != 3 or i == 3 and int(str_unit) < 256:
                        self.visit_ip_addresses_recursive(s, start + i, length, rest_unit_num - 1, prefix + "." + str_unit, ips)

    # Test on LeetCode - 52ms
    # Idea:
    #   similar to recursive approach, faster.
    def restore_ip_addresses_iterative(self, s):
        ips = []
        length = len(s)
        rest_length, rest_unit_num = length, 4
        max_i, max_j, max_k = 3, 3, 3

        # check length constraints
        if not self.is_rest_length_valid(rest_length, rest_unit_num):
            return ips
        # check for special cases when string starts with 0 - only keeps 0
        if s[0] == "0":
            max_i = 1

        for i in range(1, max_i+1):
            index = 0
            if not self.is_rest_length_valid(rest_length - i, rest_unit_num - 1):
                continue
            s1 = s[index:index+i]
            if not self.is_valid_str(s1):
                continue
            max_j = 3
            if s[index+i] == "0":
                max_j = 1
            for j in range(1, max_j+1):
                index = i
                if not self.is_rest_length_valid(rest_length - index - j, rest_unit_num - 2):
                    continue
                s2 = s[index:index+j]
                if not self.is_valid_str(s2):
                    continue
                max_k = 3
                if s[index+j] == "0":
                    max_k = 1
                for k in range(1, max_k+1):
                    index = i + j
                    if not self.is_rest_length_valid(rest_length - index - k , rest_unit_num - 3):
                        continue
                    s3 = s[index:index+k]
                    s4 = s[index+k:length]
                    if self.is_valid_str(s3) and self.is_valid_str(s4):
                        if s4[0] == "0" and len(s4) > 1:
                            continue
                        ips.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
        return ips

    def is_rest_length_valid(self, rest_length, rest_unit_num):
        return rest_unit_num * 3 >= rest_length >= rest_unit_num

    def is_valid_str(self, s):
        return int(s) < 256

def main():
    test = RestoreIPAddresses()
    print test.restore_ip_addresses("252")
    print test.restore_ip_addresses("2525")
    print test.restore_ip_addresses("010010")
    print test.restore_ip_addresses("25525511135")
    print test.restore_ip_addresses_iterative("252")
    print test.restore_ip_addresses_iterative("2525")
    print test.restore_ip_addresses_iterative("010010")
    print test.restore_ip_addresses_iterative("25525511135")

    print test.restore_ip_addresses("101023")
    print test.restore_ip_addresses_iterative("101023")


if __name__ == "__main__":
    main()