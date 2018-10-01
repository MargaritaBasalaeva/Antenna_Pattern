def antenna_pattern():
    diag = []
    for x in tqdm_notebook(np.linspace(-1.2, 1.2, 83028)):
        if x == 0:
            diag.append(1)
        else:
            diag.append((np.sin(x)/x)**2)