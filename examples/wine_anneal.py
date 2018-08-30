def ss(x):
    return np.sum((x - x.mean())**2).sum()
    
def within_ss(assignment):
    return sum(ss(wine[solution_current==i]) for i in range(3))

tau_start = 10000
# cooling_schedule = [tau_start]*60 + [tau_start/2]*120 + [tau_start/10]*240
cooling_schedule = [tau_start*0.99**i for i in range(1000)]
ss_values = []

solution_current = solution_best = np.random.randint(0, 3, nrows)
ss_best = ss_current = within_ss(solution_current)
ss_values.append(ss_best)

within_ss(solution_current)

for tau in cooling_schedule:
        
    # Random change 1-neighborhood
    change = np.random.randint(0, nrows)
    solution_step = solution_current.copy()
    solution_step[change] = np.random.randint(0, 3)
    ss_current = within_ss(solution_step)
    alpha = min(1, np.exp((ss_values[-1] - ss_current)/tau))
    if ((ss_current < ss_values[-1]) or (np.random.uniform() < alpha)):
        # Accept proposed solution
        ss_values.append(ss_current)
        solution_current = solution_step
        if ss_current < ss_best:
            
            # Replace previous best with this one
            ss_best = ss_current
            solution_best = solution_step.copy()
            
    else:
        ss_values.append(ss_values[-1])
        
plt.plot(ss_values)
plt.xlim(0, len(ss_values))
plt.xlabel('Iteration')
plt.ylabel('SS')
print('Best SS: {0}\nBest solution: {1}\nDiscovered at iteration {2}'.format(ss_best, 
            solution_best,
            np.where(ss_values==ss_best)[0][0]))
plt.plot(np.where(ss_values==ss_best)[0][0], ss_best, 'ro')