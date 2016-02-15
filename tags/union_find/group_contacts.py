# 2/12 - Union-Find, Hash Table, String
# Given a class Contact which contains a string field name and a list of strings which stores the contact's
# email addresses.
# E.g. Given an array of contacts
#   [
#    John [john@gmail.com]
#    Mary [mary@gmail.com]
#    John [john@yahoo.com]
#    John [john@gmail.com, john@yahoo.com, john@hotmail.com]
#    Bob [bob@gmail.com]
#  ]
# If two contacts have the same email address, they must be the same person. Given the list of contacts, group
# contacts and return List[List[Contact]].
# For example, in the case above, contact 1, 3 and 4 are the same person. However, you cannot group by name since
# two different contacts may have the same name.
#
# Idea:
#   Use Union-Find to partition contacts.
#   1. Group contacts by emails. Basically, create a dictionary of (email, List[Contact]).
#   2. Union-Find on the List[Contact]. This makes sure that contacts that have overlapping emails gets grouped together.
#   3. Traverse the parents values and group contacts.
from union_find import UnionFindRank as UnionFind


class Contact(object):
    def __init__(self, name, emails):
        """
        :param name: String
        :param emails: List[String]
        """
        self.name = name
        self.emails = emails

class Solution(object):
    def group_contacts(self, contacts):
        """
        :param contacts: List[Contact]
        :return: List[List[Contact]]
        """
        email_dict = {}
        # store (email, [contact_index]) in dictionary
        for i in range(len(contacts)):
            contact = contacts[i]
            for email in contact.emails:
                if email not in email_dict:
                    email_dict[email] = []
                email_dict[email].append(i)

        # unionize contacts for each email (contacts are partitioned)
        uf = UnionFind(len(contacts))
        for vals in email_dict.values():
            first_contact = vals[0]
            for i in range(1, len(vals)):
                uf.union(first_contact, vals[i])

        visited_contacts = {}
        for i in range(0, len(contacts)):
            parent = uf.parents[i]
            if parent not in visited_contacts:
                visited_contacts[parent] = []
            visited_contacts[parent].append(i)

        ret = []
        for vals in visited_contacts.values():
            ret.append([])
            for contact_index in vals:
                ret[-1].append(contacts[contact_index])

        return ret

test = Solution()
contacts = [Contact("John", ["john@gmail.com"]),
            Contact("Mary", ["mary@gmail.com"]),
            Contact("John", ["john@yahoo.com"]),
            Contact("John", ["john@gmail.com", "john@yahoo.com", "john@hotmail.com"]),
            Contact("Boc", ["bob@gmail.com"])
           ]
print test.group_contacts(contacts)
