vlbw = pd.read_csv("../data/vlbw.csv", index_col=0)

y = vlbw.pop('ivh')

brier = lambda mod, X, y: ((mod.fit(X,y).predict_proba(X) - y)**2).mean()

C = np.linspace(0, 10, 20)

scores = np.empty(len(C))
scores_std = np.empty(len(C))


for i,c in enumerate(C):
    lr = linear_model.LogisticRegression(C=c)
    s = cross_validation.cross_val_score(lr, vlbw, y, scoring=brier, n_jobs=-1)
    scores[i] = s.mean()
    scores_std[i] = s.std()

plt.semilogx(alphas, scores)
plt.semilogx(alphas, np.array(scores) + np.array(scores_std)/20, 'b--')
plt.semilogx(alphas, np.array(scores) - np.array(scores_std)/20, 'b--')
plt.yticks(())
plt.ylabel('Brier score')
plt.xlabel('alpha')
plt.axhline(np.max(scores), linestyle='--', color='.5')
plt.text(5e-2, np.max(scores)+1e-4, str(np.max(scores).round(3)))