def baseball_anneal(cooling_schedule, tau=10):
    
    aic_values = []
    
    solution_current = solution_best = np.random.binomial(1, 0.5, ncols).astype(bool)
    solution_vars = predictors[predictors.columns[solution_current]]
    g = LinearRegression().fit(X=solution_vars, y=logsalary)
    aic_best = aic(g, solution_vars, logsalary)
    aic_values.append(aic_best)
    
    for tau in cooling_schedule:

        # Random change 1-neighborhood
        flip = np.random.randint(0, ncols)
        solution_current[flip] = not solution_current[flip]
        solution_vars = predictors[predictors.columns[solution_current]]
        g = LinearRegression().fit(X=solution_vars, y=logsalary)
        aic_step = aic(g, solution_vars, logsalary)
        alpha = min(1, np.exp((aic_values[-1] - aic_step)/tau))

        if ((aic_step < aic_values[-1]) or (np.random.uniform() < alpha)):
            # Accept proposed solution
            aic_values.append(aic_step)
            if aic_step < aic_best:
                # Replace previous best with this one
                aic_best = aic_step
                solution_best = solution_current.copy()
        else:
            # Revert solution
            solution_current[flip] = not solution_current[flip]
            aic_values.append(aic_values[-1])
            
    return aic_values

schedule_1 = [tau_start]*60 + [tau_start/2]*120 + [tau_start/10]*240
schedule_2 = [tau_start*0.99**i for i in range(400)]

aic_1 = baseball_anneal(schedule_1)
aic_2 = baseball_anneal(schedule_2)