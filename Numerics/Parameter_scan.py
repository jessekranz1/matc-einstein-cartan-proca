import numpy as np
import matplotlib.pyplot as plt

alphas = np.linspace(0.0, 0.3, 50)
masses = np.logspace(-5, -1, 50)

results = np.zeros((50, 50))

for i, alpha in enumerate(alphas):
    for j, MA in enumerate(masses):

        # Placeholder success metric
        if 0.03 < alpha < 0.15:
            results[j, i] = 1
        else:
            results[j, i] = 0

plt.imshow(
    results,
    aspect='auto',
    origin='lower',
    extent=[alphas.min(), alphas.max(), masses.min(), masses.max()]
)

plt.xlabel('alpha')
plt.ylabel('M_A')
plt.title('MATC Stability Island')
plt.colorbar(label='successful evolution')

plt.show()
