X = pima.copy()
y = X.pop(8)

X = scale(X)

clf = MLP(alpha=0.2, eta=0.02, n_hidden_dim=50)
clf.fit(X, y)

accuracy_score(y, clf.predict(X))
