# 1/31 - Sort
# For a given string which contains pairs of "food-weight", sort the food by its weight.
# Note:
#   1. if food is after food, use default weight, like the weight of crab in case 1 is 5.
#   2. if number is after number, the second number is actually name of a food, as 2.0 in case 4.
# e.g.
# sort_food("crab hotdog  9.0 chicken 9.2", 5);  =>  chicken hotdog crab
# sort_food("  pizza  1 hotdog 2.0", 5);  => hotdog pizza
# sort_food("pizza 500 hotdog 2.0 ", 5);  => pizza hotdog
# sort_food(" pizza  500 2.0 ", 5);  => pizza 2.0
#
# Note:
#   easy sorting problem, need to pay attention to comparison of doubles, use precision epsilon.
#   determine whether a string is an int, double or ....

class Solution(object):
    def sort_food(self, food_list, def_weight):
        """
        :param food_list: str
        :param def_weight: double
        :return: List[str]
        """
        food_weight_lists = []
        fl = food_list.split()
        last_food = ""
        for i in range(0, len(fl)):
            e = fl[i]
            if not last_food:  # must always start with food
                last_food = e
            else:
                if self.is_number(e):  # weight
                    food_weight_lists.append(FoodWeight(last_food, float(e)))
                    last_food = ""
                else:  # food
                    # use default weight
                    food_weight_lists.append(FoodWeight(last_food, def_weight))
                    last_food = e
        if last_food:
            food_weight_lists.append(FoodWeight(last_food, def_weight))
        sorted_food = sorted(food_weight_lists, key=lambda food_weight_list: food_weight_list.weight)
        return [food_weight.food for food_weight in sorted_food]

    # nice way to check whether a string is a float number
    def is_number(self, s):
        """
        :param s: str
        :return: boolean
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

class FoodWeight(object):
    def __init__(self, food, weight):
        self.food = food
        self.weight = weight


test = Solution()
print test.sort_food("crab hotdog  9.0 chicken 9.2", 5)
print test.sort_food(" pizza  500 2.0 ", 5)