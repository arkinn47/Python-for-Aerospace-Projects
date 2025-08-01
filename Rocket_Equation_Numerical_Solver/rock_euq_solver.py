import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy import stats

v_e = 3000
m_initial = 100
delta_m = 0.1

t_span = (0, 10)

def rocket_eq_ode(v, mi, d, t):
    delt = mi - d*t
    d_v = v*stats.log(mi/delt)
    return d_v

solution = solve_ivp(rocket_eq_ode, t_span, [0], dense_output=True)
t_eval = np.linspace(0,10, 1000)
v = solution.sol(t_eval)

plt.figure(figsize=(10,6))
plt.plot(t_eval, v[0], label = 'Rocket Veloecity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Rocket Velocity over Time')
plt.grid(True)
plt.show()