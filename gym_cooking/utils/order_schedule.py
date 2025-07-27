from gym_cooking.utils.core import *
from gym_cooking.utils.config import ORDER_EXPIRE_PUNISH


import numpy as np
import copy

class OrderScheduler:
    def __init__(self, arglist, recipes):
        self.arglist = arglist
        self.recipes = recipes
        all_food = {a.replace('Fresh', ''): 0 for a in FRESH_FOOD}
        for recipe in self.recipes:
            fns = recipe.full_name.split('-')
            for f in fns:
                name = f.removeprefix("Cooked").removeprefix("Grill")
                all_food[name] += 1
        self.used_food =  [f for f, c in all_food.items() if c != 0]

        if len(self.recipes) == 4 :
            weights = np.array([0.27, 0.27, 0.27, 0.19]) 
            while True:
                self.rand_recipe_list = np.random.choice(len(self.recipes), size=100, replace=True, p=weights)
                if len(set(self.rand_recipe_list[:3]))==3:
                    break

        elif len(self.recipes) == 6:
            weights = np.array([0.2, 0.2, 0.2, 0.2,  0.1, 0.1])  
            while True:
                self.rand_recipe_list = np.random.choice(len(self.recipes), size=100, replace=True, p=weights)
                if len(set(self.rand_recipe_list[:3]))==3:
                    break
        
        else: 
            self.rand_recipe_list = [np.random.randint(len(self.recipes)) for _ in range(100)]
        self.rand_recipe_idx = 0

        self.max_num_orders = arglist.max_num_orders

        self.current_orders = []
        for _ in range(self.max_num_orders):
            self.current_orders.append(self.new_order())

        self.reward = 0
        self.successful_orders = 0
        self.failed_orders = 0
        self.order_plus = arglist.order_plus

    def assign_rand_recipe_list(self, rand_recipe_list):
        self.rand_recipe_list = rand_recipe_list
        self.rand_recipe_idx = 0

        self.current_orders = []
        for _ in range(self.max_num_orders):
            self.current_orders.append(self.new_order())

    def __copy__(self):
        new = OrderScheduler(self.arglist, copy.copy(self.recipes))
        new.rand_recipe_list = copy.copy(self.rand_recipe_list)
        new.rand_recipe_idx = self.rand_recipe_idx
        new.current_orders = copy.copy(self.current_orders)
        new.reward = self.reward
        return new

    def new_order(self):
        recipe = self.recipes[self.rand_recipe_list[self.rand_recipe_idx]]
        self.rand_recipe_idx = (self.rand_recipe_idx +
                                1) % len(self.rand_recipe_list)
        goal_obj = copy.deepcopy(recipe.final_task)
        return goal_obj, recipe.length, recipe.length, recipe.bonus

    def update(self, world, passed_time=1.):
        # check completed orders
        current_orders = []
        delivery_list = list(
            filter(lambda o: o.name == 'Delivery', world.get_object_list()))
        for order, restTime, timeLimit, bonus in self.current_orders:
            goal_obj = order
            success = False
            for delivery in delivery_list:
                if delivery.exists(goal_obj.full_name):
                    delivery.pop(goal_obj.full_name)
                    success = True
                    goal_obj.location = delivery.location
                    world.remove(goal_obj)
                    break
            if success:
                self.reward += bonus
                self.successful_orders += 1
            else:
                current_orders.append((order, restTime, timeLimit, bonus))
        self.current_orders = current_orders

        # update order time
        current_orders = []
        for order, restTime, timeLimit, bonus in self.current_orders:
            if restTime - passed_time > 1e-3:
                current_orders.append(
                    (order, restTime - passed_time, timeLimit, bonus))
            else:
                self.failed_orders += 1
                self.reward -= ORDER_EXPIRE_PUNISH
        self.current_orders = current_orders

        while len(self.current_orders) < self.max_num_orders:
            self.current_orders.append(self.new_order())

    def consume_reward(self):
        # temp = self.reward
        # self.reward = 0
        return 0
