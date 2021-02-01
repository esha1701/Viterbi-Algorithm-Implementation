hidden_states=("Exercise", "Sedentary")
observed_states=("Loss", "No Change", "Gain")
start_prob={"Exercise":0.5, "Sedentary":0.5}
transition_prob={
    "Exercise": {"Exercise": 0.7, "Sedentary": 0.3},
    "Sedentary": {"Exercise": 0.2, "Sedentary": 0.8},
}
    
emission_prob={
    "Exercise": {"Loss": 0.5, "No Change": 0.4, "Gain": 0.1},
    "Sedentary": {"Loss": 0.1, "No Change": 0.3, "Gain": 0.6},
}



def trellis(obs, obs_states, start_p, trans_p, emission_p):
    T = [{}]
    #Starting probabilities
    for i in obs_states:
        T[0][i] = {"prob": start_p[i] * emission_p[i][obs[0]], "prev": None}
        
    for iter_ in range(1, len(obs)):
        T.append({})
        for i in obs_states:
            max_prob = T[iter_ - 1][obs_states[0]]["prob"] * trans_p[obs_states[0]][i] * emission_p[i][obs[iter_]]
            prev_st_selected = obs_states[0]
            for prev_st in obs_states[1:]:
                tr_prob = T[iter_ - 1][prev_st]["prob"] * trans_p[prev_st][i] * emission_p[i][obs[iter_]]
                if tr_prob > max_prob:
                    max_prob = tr_prob
                    prev_st_selected = prev_st

            
            T[iter_][i] = {"prob": max_prob, "prev": prev_st_selected}
    return T


def backtrack(T):           
    hidden_seq = []
    iterations=len(T)
    
    #Checking last iteration for highest probability
    max_prob = 0
    chosen_state = None
    for key in T[iterations-1]:
    
        if T[iterations-1][key]["prob"]>max_prob:
            max_prob = T[iterations-1][key]["prob"]
            chosen_state  = key 
   
    hidden_seq.append(chosen_state)
    previous_state = chosen_state
        

    for i in range(len(T) - 2, -1, -1):
        hidden_seq.insert(0, T[i + 1][previous_state]["prev"])
        previous_state = T[i + 1][previous_state]["prev"]
    print (hidden_seq)

    
      
            





            
