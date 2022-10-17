# Matrice hessienne

$$
\nabla^2 f(a) := \begin{pmatrix}
\frac{\partial^2 f}{\partial x_1 x_1}(a) & \frac{\partial^2 f}{\partial x_1 x_2}(a) & \ldots & \frac{\partial^2 f}{\partial x_1 x_n}(a) \\
\frac{\partial^2 f}{\partial x_2 x_1}(a) & \frac{\partial^2 f}{\partial x_2 x_2}(a) & \ldots & \frac{\partial^2 f}{\partial x_2 x_n}(a) \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n x_1}(a) & \frac{\partial^2 f}{\partial x_n x_2}(a) & \ldots & \frac{\partial^2 f}{\partial x_n x_n}(a) \\
\end{pmatrix}
$$
Sert à calculer la [[dérivée seconde au sens de Frechêt]]:

$$
\forall h \in \mathbb{R}^n, \forall h \in \mathbb{R}^n, f''(a)\cdot(h, k) = h{}^T \nabla^2 f(a)\cdot k
$$
