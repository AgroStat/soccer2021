import random

def teamset():

    list_1 = ['Sowgat', 'Hasnat']
    list_2 = ['Rakib', 'Apurba']
    list_3 = ['Asif','Rashed']
    list_4 = ['Himel', 'Emon']
    list_5 = ['Shahriar R', 'Remon']
    list_6 = ['Shahriar H', 'Riyad']
    list_7 = ['Saif', 'Mostafiz']
    list_8 = ['Priom', 'Nazmul']
    list_9 = ['Anupam', 'Mortuza']
    list_10 = ['Ehsan', 'Sharif']
    list_11 = ['Badhon', 'Huzzatul']


    v_list = random.sample(list_5, 1)
    w_list = random.sample(list_1, 2)
    x_list = random.sample(list_2, 1)
    y_list = random.sample(list_3, 1)
    z_list = random.sample(list_4, 1)

    master = list_1 + list_2 + list_3 + list_4 + list_5 + \
                list_6 + list_7 + list_8 + list_9 + list_10 + list_11

    new_list = (random.sample(list_1, 1) + random.sample(list_2, 1)) + \
                random.sample(list_3, 1) + random.sample(list_4, 1) + \
                random.sample(list_5, 1) + random.sample(list_6, 1) + \
                random.sample(list_7, 1) + random.sample(list_8, 1) + \
                random.sample(list_9, 1) + random.sample(list_10, 1) + \
                random.sample(list_11, 1)  

    pop_list = (list(set(master) - set(new_list)))


    # u = set(['Asif', 'Nazmul', 'Himel'])
    # v = set(['Ehsan', 'Mortuza', 'Priom'])
    w = set(['Apurba', 'Sowgat', 'Rakib'])
    x = set(['Apurba', 'Hasnat', 'Sowgat'])
    y= set(['Anupam', 'Mortuza', 'Ehsan'])
    z= set(['Priom', 'Ehsan', 'Mortuza'])

    
    con = {
        'TeamA':random.sample(new_list, 11),
        'TeamB':random.sample(pop_list, 11),
    }

    A = con['TeamA']
    B = con['TeamB']

    if w.issubset(A) or w.issubset(B) or x.issubset(A) or x.issubset(B) or \
        y.issubset(A) or y.issubset(B) or z.issubset(A) or z.issubset(B):
        context = {}
    else:
        context = con

    return context