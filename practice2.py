# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:38:49 2020

@author: currysesame
"""
#cost 15mins average

import numpy as np
import copy
nphs = np.hstack


def cost_function(cases):
    costs_each = cases * prices
    return sum(costs_each)

def cost_function_ditem(cases):
    return prices

def item_gain(cases):
    # what could they gain
    gain = np.zeros((12))

    gain[0] = cases[0] + cases[12] 
    gain[1] = cases[1] + cases[12] +3*cases[16]
    gain[2] = cases[2] + cases[12] +4*cases[16]
    
    gain[3] = cases[3] + cases[13]
    gain[4] = cases[4] + cases[13]
    gain[5] = cases[5] + cases[13]
    
    gain[6] = cases[6] + cases[14]
    gain[7] = cases[7] + cases[14] +3*cases[16]
    gain[8] = cases[8] + cases[14]
    
    gain[9] = cases[9] + 2*cases[15] + 4*cases[16]
    gain[10] = cases[10] + cases[15] 
    gain[11] = cases[11] + cases[15] 
    return gain

def item_loss(cases):
    # check the request is enough or not
    loss = np.zeros((17))

    loss[0] = cases[0] + cases[12] - desired_food[0]
    loss[1] = cases[1] + cases[12] + 3*cases[16] - desired_food[1]
    loss[2] = cases[2] + cases[12] + 4*cases[16] - desired_food[2]
    
    loss[3] = cases[3] + cases[13] - desired_food[3]
    loss[4] = cases[4] + cases[13] - desired_food[4]
    loss[5] = cases[5] + cases[13] - desired_food[5]
    
    loss[6] = cases[6] + cases[14] - desired_food[6]
    loss[7] = cases[7] + cases[14] + 3*cases[16] - desired_food[7]
    loss[8] = cases[8] + cases[14] - desired_food[8]
    
    loss[9] = cases[9] + 2*cases[15] + 4*cases[16] - desired_food[9]
    loss[10] = cases[10] + cases[15] - desired_food[10]
    loss[11] = cases[11] + cases[15] - desired_food[11]
    return loss

def negative_count(values):
    # only take the negative part
    for i in range(len(values)):
        if values[i] > 0:
            values[i] = 0
    return values

def total_item_loss(cases):
    loss = item_loss(cases)
    return sum(abs(loss))

def ditem_loss_d_item(cases):
    # diff of the item_loss depend on the item
    i_loss = item_loss(cases)
    i_loss = negative_count(i_loss)
    value = np.zeros((17))
    for i in range(len(value)):
        if i>=0 and i < 12:
            value[i] += 2*i_loss[i]
        if i == 12:
            value[i] += 2*(i_loss[0] + i_loss[1] + i_loss[2])
        if i == 13:
            value[i] += 2*(i_loss[3] + i_loss[4] + i_loss[5])
        if i == 14:
            value[i] += 2*(i_loss[6] + i_loss[7] + i_loss[8])
        if i == 15:
            value[i] += 2*(2*i_loss[9] + i_loss[10] + i_loss[11])
        if i == 16:
            value[i] += 2*(3*i_loss[1] + 4*i_loss[2] + 3*i_loss[7] + 4*i_loss[9])
    return value

def round_off(cases):
    # keep the order is regular
    for i in range(len(cases)):
        if cases[i]<0:
            cases[i] = 0
        if cases[i]>6:
            cases[i] = 6
    return cases
        
def update_one_step(cases):
    #shrink the update step to -1,0 or 1
    d_cost = cost_function_ditem(cases)/200
    print('d',d_cost[2])
    ditem_loss = ditem_loss_d_item(cases)/3.2
    print('d2',ditem_loss[2])
    update_cases = np.floor(d_cost + ditem_loss)
    print('up',update_cases[2])
    for i in range(len(update_cases)):
        if update_cases[i] >0.5:
            update_cases[i] = 1
        elif update_cases[i]< -0.5:
            update_cases[i] = -1
        else:
            update_cases[i] = 0
    return update_cases

def test_enough(cases):
    # test everybody get enough food
    gain = np.int32(item_gain(cases))
    for i in range(len(gain)):
        if gain[i] - desired_food[i] < 0:
            return False
    return True

def test_not_too_much(cases):
    gain = np.int32(item_gain(cases))
    # buy too much is a waste
    main_gain = gain[0] + gain[3] + gain[6] + gain[9] 
    main_desired = desired_food[0] + desired_food[3] + desired_food[6] + desired_food[9]
    if main_gain - main_desired >= 2:
        return False
    sub_gain = gain[1] + gain[4] + gain[7] + gain[10] 
    sub_desired = desired_food[1] + desired_food[4] + desired_food[7] + desired_food[10]
    if sub_gain - sub_desired >= 4:
        return False
    drink_gain = gain[2] + gain[5] + gain[8] + gain[11] 
    drink_desired = desired_food[2] + desired_food[5] + desired_food[8] + desired_food[11]
    if drink_gain - drink_desired >= 3:
        return False
    return True

def test_same_cases(memory, cases):
    for i in range(len(cases)):
        if memory[i] != cases[i]:
            return True
    return False

def shrink_cases(cases):
    gain = np.int32(item_gain(cases))
    for i in range(len(gain)):
        if gain[i] - desired_food[i] > 0:
            if cases[i]>0:
                cases[i] -=  1
    return cases




prices = np.array([120, 55, 30, 100, 60, 30, 110, 45, 25, 60, 50, 25, 150, 130, 140, 150, 200])
desired_food_origin = np.array([1,5,2,0,1,2,1,4,1,3,2,0])

report_sheets = []
# the following for-loops are for just one objective,
# for chosen one specific food which is not descript clear in the question (the requirements).
# so add all the choices be the situation, and analyse these cases.
for main in range(4):
    for humb1 in range(3):
        for humb2 in range(3):
            for sub in range(4):
                for drink in range(4):
                    desired_food = copy.copy(desired_food_origin)
                    desired_food[3*main] += 1
                    desired_food[3*humb1] += 1
                    desired_food[3*humb2] += 1
                    desired_food[3*sub + 1] += 1
                    desired_food[3*drink + 2] += 1
                    
                    good_cases = []
                    # in such a background, chose one random sheet and start training
                    # if no any result is good enough, try it again. until 40 times.
                    # if there exist a good enough result, then jump out for another situation.
                    for x in range(40):
                        # initial random case
                        cases = np.random.randint(2, size=17)
                        # if find the good enough, jump out for another situation.
                        if len(good_cases)>0:
                            break
                        # each case uses 150 iterations.
                        for i in range(150):
                            # avoid infeasible cases, randomly drop one out.
                            if cases[16] == 1 and cases[15] == 1:
                                cases[np.int(15 + np.random.randint(2, size=1))] = 0
                            print('cases initial',cases)
                            update_cases = update_one_step(cases)
                            print('updata       ', update_cases)
                            index = i % 12
                            #update
                            cases[index] = cases[index] - update_cases[index]
                            # avoid explosion
                            cases = round_off(cases)
                            cases = shrink_cases(cases)
                            print('cases new    ',cases)
                            na = np.int32(item_loss(cases))
                            if test_enough(cases):
                                print('Enough!')
                            else:
                                print('Need more!')
                            if test_not_too_much(cases):
                                print('Not too much waste!')
                            else:
                                print('Waste!')
                            print('gain         ', np.int32(item_gain(cases)))
                            print('target       ', desired_food)
                            print('======')
                            print('item diff',total_item_loss(cases))
                            print('price',cost_function(cases))
                            
                            # save the good enough cases
                            if total_item_loss(cases)<=3 and cost_function(cases)<=1500 and test_enough(cases) and test_not_too_much(cases):
                                # for initial
                                if len(good_cases) == 0:
                                    good_cases.append(desired_food)
                                    good_cases.append(cases)
                                    good_cases.append(total_item_loss(cases))
                                    good_cases.append(cost_function(cases))
                                else:
                                    # for not duplicate
                                    if good_cases[-1] != cost_function(cases) or good_cases[-2] != total_item_loss(cases) or test_same_cases(good_cases[-3], cases):
                                        good_cases.append(desired_food)
                                        good_cases.append(cases)
                                        good_cases.append(total_item_loss(cases))
                                        good_cases.append(cost_function(cases))
                    report_sheets.append(good_cases)
