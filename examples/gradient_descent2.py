def gradient_descent2(init_loc, f, f_prime, atol=1e-10, step=None):
    
    x_i, y_i = init_loc
    gd_output = []
    converged = False

    while not converged:
        fxy = (f([x_i, y_i]))
        gd_output.append([x_i, y_i, fxy])
        dx_i, dy_i = f_prime(np.asarray([x_i, y_i]))
        if step is None:
            # Compute a step size using a line_search
            step = optimize.line_search(f, f_prime,
                                np.r_[x_i, y_i], -np.r_[dx_i, dy_i],
                                np.r_[dx_i, dy_i], c2=.05)
            step = step[0]
            
        x_i += -step*dx_i
        y_i += -step*dy_i
        
        if fxy < atol:
            converged = True
        
    return gd_output